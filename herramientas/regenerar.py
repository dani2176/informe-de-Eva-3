from pathlib import Path
import sys,json,re,io,copy,html
from zipfile import ZipFile,ZIP_DEFLATED
from lxml import etree
from docx import Document
from docx.shared import Pt,Cm,RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak,Table,TableStyle,Preformatted,KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from calc_sla import calcular
from formulas import parse_math,omml,Equation

ROOT=Path(__file__).resolve().parents[1]; CASE=ROOT/'ejemplos/caso-valle-elqui'
def fmt(v,n=5): return f'{v:.{n}f}'.replace('.',',')
result,out=calcular(CASE/'objetivos.yaml',CASE/'mediciones.csv')
(CASE/'salida_calc.txt').write_text(out,encoding='utf-8')
(CASE/'resultados.json').write_text(json.dumps(result,indent=2,ensure_ascii=False),encoding='utf-8')
o=json.loads((CASE/'objetivos.yaml').read_text(encoding='utf-8'))
# JSON is also YAML 1.2. Compact complete objects keep the appendix readable.
objlines=['{']
for i,(k,v) in enumerate(o.items()): objlines.append('  '+json.dumps(k)+': '+json.dumps(v,ensure_ascii=False)+(',' if i<len(o)-1 else ''))
objlines.append('}')
# Keep each metric on its own line, while preserving valid JSON/YAML.
objtext='\n'.join(objlines)
objtext=objtext.replace('"metricas": {','"metricas": {\n    ').replace('}, "','},\n    "')
(CASE/'objetivos.yaml').write_text(objtext+'\n',encoding='utf-8')
values={'disponibilidad':fmt(result['disponibilidad']),'jitter':fmt(result['jitter']),'serie_factor':fmt(result['serie'],12),'serie_pct':fmt(result['serie']*100),'serie_caida':fmt(result['serie_caida'],2),'paralelo_factor':fmt(result['paralelo'],12),'paralelo_pct':fmt(result['paralelo']*100),'paralelo_caida':fmt(result['paralelo_caida'],2),'margen':fmt(43.2-result['paralelo_caida'],2),'objetivos':objtext,'mediciones':(CASE/'mediciones.csv').read_text(encoding='utf-8').strip(),'salida':out.strip()}
md=(ROOT/'plantillas/informe_base.md').read_text(encoding='utf-8')
for k,v in values.items(): md=md.replace('{{'+k+'}}',v)
assert '{{' not in md
# The print source retains page boundaries; GitHub output is written below.

def parse(text):
 lines=text.splitlines();i=0
 while i<len(lines):
  s=lines[i].strip()
  if not s:i+=1;continue
  if s.startswith('<!-- page'):yield 'break','';i+=1;continue
  if s.startswith('```'):
   language=s[3:].strip();buf=[];i+=1
   while i<len(lines) and not lines[i].startswith('```'):buf.append(lines[i]);i+=1
   yield ('math' if language=='math' else 'code'),'\n'.join(buf);i+=1;continue
  if s.startswith('|'):
   rows=[]
   while i<len(lines) and lines[i].strip().startswith('|'):
    cells=[c.strip() for c in lines[i].strip().strip('|').split('|')]
    if not all(re.fullmatch('[-: ]+',c) for c in cells):rows.append(cells)
    i+=1
   yield 'table',rows;continue
  if s.startswith('## '):yield 'h2',s[3:]
  elif s.startswith('# '):yield 'h1',s[2:]
  else:yield 'p',s
  i+=1
blocks=list(parse(md))
# Dedicated GitHub rendition: one title, linked contents, no print breaks.
github=[]
for idx,(kind,value) in enumerate(blocks):
 if kind=='break': continue
 if kind=='h1': github.append(('# ' if idx==0 else '## ')+value)
 elif kind=='h2': github.append('### '+value)
 elif kind=='math': github.append('```math\n'+value+'\n```')
 elif kind=='code': github.append('```text\n'+value+'\n```')
 elif kind=='table':
  def esc(t): return t.replace('$',r'\$')
  rows=['| '+' | '.join(esc(x) for x in value[0])+' |','| '+' | '.join(['---']*len(value[0]))+' |']
  rows += ['| '+' | '.join(esc(x) for x in r)+' |' for r in value[1:]]
  github.append('\n'.join(rows))
 else: github.append(value.replace('$',r'\$'))
gh='\n\n'.join(github)+'\n'
(CASE/'informe.md').write_text(gh,encoding='utf-8')


template=ROOT/'plantillas/formato_inacap.docx'
d=Document(template)
body=d._element.body
for el in list(body):
 if el.tag!=qn('w:sectPr'):body.remove(el)
s=d.sections[0];s.top_margin=Pt(130);s.bottom_margin=Pt(43)
page=1;next_page=False
def font(run,size=11,bold=False):
 run.font.name='Tahoma';run.font.size=Pt(size);run.font.bold=bold;run.font.color.rgb=RGBColor(0,0,0)
def para(text,size=10,bold=False):
 p=d.add_paragraph();font(p.add_run(text),size,bold);p.paragraph_format.space_after=Pt(6);p.paragraph_format.line_spacing=Pt(12.5);p.paragraph_format.widow_control=True
 return p
for kind,value in blocks:
 if kind=='break':next_page=True;page+=1;continue
 if kind=='math':
  p=d.add_paragraph();p._p.append(omml(parse_math(value)));p.paragraph_format.space_before=Pt(7);p.paragraph_format.space_after=Pt(9);p.paragraph_format.keep_together=True;continue
 if kind=='table':
  t=d.add_table(rows=0,cols=len(value[0]));t.autofit=False
  widths={2:[6,12.5],3:[5.2,6.5,6.8],4:[3.7,3,5.3,6.5],5:[4.1,5.4,2.4,4.1,2.5]}.get(len(value[0]))
  if value[0][-1]=='Prioridad': widths=[4.25,6.48,5.92,1.85]
  if len(value[0])==4 and value[0][0]=='Indicador': widths=[3.5,4.5,4.5,6.0]
  if value[0][0]=='Evento y fecha': widths=[4.25,2.22,2.96,9.07]
  for col,w in zip(t.columns,widths):col.width=Cm(w)
  for ri,row in enumerate(value):
   cells=t.add_row().cells
   for ci,txt in enumerate(row):
    cells[ci].width=Cm(widths[ci]);p=cells[ci].paragraphs[0];font(p.add_run(txt),8.6,ri==0);p.paragraph_format.space_after=Pt(2);p.paragraph_format.space_before=Pt(2);p.paragraph_format.line_spacing=Pt(10.5);p.paragraph_format.keep_with_next=(ri<len(value)-1);p.paragraph_format.widow_control=True
    pr=cells[ci]._tc.get_or_add_tcPr();b=OxmlElement('w:tcBorders')
    for edge in ['top','left','bottom','right']:
     x=OxmlElement('w:'+edge);x.set(qn('w:val'),'single');x.set(qn('w:sz'),'4');x.set(qn('w:color'),'D9D9D9');b.append(x)
    pr.append(b)
    if ri==0:
     sh=OxmlElement('w:shd');sh.set(qn('w:fill'),'E6E6E6');pr.append(sh)
   t.rows[-1]._tr.get_or_add_trPr().append(OxmlElement('w:cantSplit'))
   if ri==0:t.rows[0]._tr.get_or_add_trPr().append(OxmlElement('w:tblHeader'))
  sp=para('',3);sp.paragraph_format.line_spacing=Pt(3);sp.paragraph_format.space_after=Pt(3);continue
 if kind=='code':
  for line in value.splitlines():
   p=para(line,8);p.paragraph_format.space_after=Pt(0);p.paragraph_format.line_spacing=1
  continue
 p=para(value,16 if kind=='h1' else 12 if kind=='h2' else 10,kind in ['h1','h2'])
 if next_page:p.paragraph_format.page_break_before=True;next_page=False
 if value.startswith('Tabla '):p.paragraph_format.keep_with_next=True
 if kind in ['h1','h2']:p.paragraph_format.line_spacing=Pt(20 if kind=='h1' else 16)
 if kind in ['h1','h2']:p.paragraph_format.keep_with_next=True
 if page==1:
  p.alignment=WD_ALIGN_PARAGRAPH.CENTER;p.paragraph_format.space_after=Pt(16)
  if kind=='h1':p.style=d.styles['Title']
d.core_properties.author='Daniel Videla'
d.core_properties.last_modified_by='Daniel Videla'
d.core_properties.title='Verificación del SLA de Agrícola Valle de Elqui'
buffer=io.BytesIO();d.save(buffer)
# Only replace the body part; preserve all original styles, graphics and relationships byte for byte.
generated=ZipFile(buffer)
newxml=generated.read('word/document.xml')
with ZipFile(template) as src,ZipFile(CASE/'informe.docx','w',ZIP_DEFLATED) as dest:
 for entry in src.infolist():dest.writestr(entry,generated.read(entry.filename) if entry.filename in ['word/document.xml','docProps/core.xml'] else src.read(entry.filename))

# Build PDF directly from the generated Markdown, using the template's graphics.
fontdir=Path('C:/Windows/Fonts')
if (fontdir/'tahoma.ttf').exists():
 pdfmetrics.registerFont(TTFont('Body',str(fontdir/'tahoma.ttf')));pdfmetrics.registerFont(TTFont('Bold',str(fontdir/'tahomabd.ttf')))
else:
 from reportlab.pdfbase.pdfmetrics import Font
 pdfmetrics.registerFont(Font('Body','Helvetica','WinAnsiEncoding'));pdfmetrics.registerFont(Font('Bold','Helvetica-Bold','WinAnsiEncoding'))
styles={
 'p':ParagraphStyle('p',fontName='Body',fontSize=10,leading=12.5,spaceAfter=6),
 'h1':ParagraphStyle('h1',fontName='Bold',fontSize=16,leading=20,spaceAfter=11,keepWithNext=True),
 'h2':ParagraphStyle('h2',fontName='Bold',fontSize=12,leading=16,spaceBefore=6,spaceAfter=7,keepWithNext=True),
 'cell':ParagraphStyle('cell',fontName='Body',fontSize=8.1,leading=10),
 'th':ParagraphStyle('th',fontName='Bold',fontSize=8.1,leading=10),
 'cover':ParagraphStyle('cover',fontName='Body',fontSize=11,leading=16,spaceAfter=17,alignment=1),
 'ctitle':ParagraphStyle('ctitle',fontName='Bold',fontSize=23,leading=29,spaceAfter=25,alignment=1),
 'code':ParagraphStyle('code',fontName='Courier',fontSize=7.3,leading=9.4,spaceAfter=5)}
z=ZipFile(template);header=ImageReader(io.BytesIO(z.read('word/media/image2.png')));footer=ImageReader(io.BytesIO(z.read('word/media/image3.jpg')))
def furniture(c,doc):
 c.drawImage(header,0,792-114.5,width=612,height=114.5,mask='auto')
 c.drawImage(footer,0,0,width=612,height=6)
 c.setFont('Body',8);c.setFillColor(colors.HexColor('#555555'));c.drawString(43,24,'Agrícola Valle de Elqui · Verificación SLA · Septiembre 2026');c.drawRightString(569,24,str(doc.page))
story=[];page=1
for kind,v in blocks:
 if kind=='break':story.append(PageBreak());page+=1;continue
 if kind=='table':
  data=[[Paragraph(html.escape(x),styles['th' if i==0 else 'cell']) for x in row] for i,row in enumerate(v)]
  proportions={2:[0.30,0.70],3:[0.28,0.39,0.33],4:[0.20,0.19,0.29,0.32],5:[0.22,0.27,0.13,0.24,0.14]}[len(v[0])]
  if v[0][-1]=='Prioridad': proportions=[0.23,0.35,0.32,0.10]
  if v[0][0]=='Evento y fecha': proportions=[0.23,0.12,0.16,0.49]
  t=Table(data,colWidths=[526*x for x in proportions],repeatRows=1,hAlign='LEFT')
  t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#E6E6E6')),('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#D9D9D9')),('VALIGN',(0,0),(-1,-1),'MIDDLE'),('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),4),('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4)]));story.extend([t,Spacer(1,9)]);continue
 if kind=='math':story.append(Equation(v));continue
 if kind=='code':
  import textwrap
  wrapped='\n'.join('\n'.join(textwrap.wrap(line,105,replace_whitespace=False,drop_whitespace=False)) or ' ' for line in v.splitlines())
  story.append(Preformatted(wrapped,styles['code']));continue
 style=styles['ctitle' if kind=='h1' else 'cover'] if page==1 else styles[kind]
 paragraph=Paragraph(html.escape(v),style)
 if v.startswith('Tabla '):paragraph.keepWithNext=True
 story.append(paragraph)
SimpleDocTemplate(str(CASE/'informe.pdf'),pagesize=(612,792),leftMargin=43,rightMargin=43,topMargin=130,bottomMargin=43,title='Verificación del SLA de Agrícola Valle de Elqui',author='Daniel Videla').build(story,onFirstPage=furniture,onLaterPages=furniture)
assert abs(result['credito']-0.15)<1e-10 and result['monto']==180000
print('Generados informe.md, informe.docx, informe.pdf y resultados de calculo.')
