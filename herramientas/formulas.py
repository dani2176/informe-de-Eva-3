"""Small shared equation tree: LaTeX subset to editable Word math and PDF vectors.

Supports only the operators explicitly used in this report. Unknown commands fail.
"""
import re
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from reportlab.platypus import Flowable
from reportlab.pdfbase import pdfmetrics

def parse_math(s):
 tokens=re.findall(r'\\[a-zA-Z]+|\\.|[{}_^]|[^\\{}_^]',s);i=0
 def atom():
  nonlocal i
  t=tokens[i];i+=1
  if t=='{':return seq(True)
  if t==r'\frac':return ('frac',atom(),atom())
  if t==r'\overline':return ('bar',atom())
  if t in [r'\mathrm',r'\text']:return atom()
  symbols={r'\times':' × ',r'\sum':'Σ',r'\,':' ',r'\%':'%',r'\leq':'≤',r'\geq':'≥',r'\cdot':' · '}
  if t.startswith('\\'):
   if t not in symbols:raise ValueError('Unsupported math command '+t)
   t=symbols[t]
  return ('text',t)
 def seq(group=False):
  nonlocal i
  out=[]
  while i<len(tokens):
   if tokens[i]=='}':
    assert group;i+=1;break
   if tokens[i] in ['_','^']:
    op=tokens[i];i+=1;out[-1]=('sub' if op=='_' else 'sup',out[-1],atom())
   else:out.append(atom())
  # Merge text to preserve consistent font spacing.
  merged=[]
  for n in out:
   if n[0]=='text' and merged and merged[-1][0]=='text':merged[-1]=('text',merged[-1][1]+n[1])
   else:merged.append(n)
  return ('seq',merged)
 return seq()

def omml(tree):
 def make(tag):return OxmlElement('m:'+tag)
 def add(parent,n):
  k=n[0]
  if k=='seq':
   for c in n[1]:add(parent,c)
  elif k=='text':
   r=make('r');prop=make('rPr');sty=make('sty');sty.set(qn('m:val'),'p');prop.append(sty);r.append(prop)
   t=make('t');t.set('{http://www.w3.org/XML/1998/namespace}space','preserve');t.text=n[1];r.append(t);parent.append(r)
  elif k=='frac':
   f=make('f');a=make('num');b=make('den');add(a,n[1]);add(b,n[2]);f.extend([a,b]);parent.append(f)
  elif k in ['sub','sup']:
   f=make('sSub' if k=='sub' else 'sSup');a=make('e');b=make(k);add(a,n[1]);add(b,n[2]);f.extend([a,b]);parent.append(f)
  elif k=='bar':
   f=make('bar');pr=make('barPr');pos=make('pos');pos.set(qn('m:val'),'top');pr.append(pos);f.append(pr);a=make('e');add(a,n[1]);f.append(a);parent.append(f)
 root=make('oMathPara');props=make('oMathParaPr');jc=make('jc');jc.set(qn('m:val'),'center');props.append(jc);root.append(props)
 math=make('oMath');add(math,tree);root.append(math);return root

class Equation(Flowable):
 def __init__(self,latex):
  super().__init__();self.tree=parse_math(latex);self.size=12;self.spaceBefore=7;self.spaceAfter=9;self.hAlign='CENTER'
 def measure(self,n,size):
  k=n[0]
  if k=='text':return pdfmetrics.stringWidth(n[1],'Body',size),size*.85,size*.23
  if k=='seq':
   dims=[self.measure(x,size) for x in n[1]]
   return sum(x[0] for x in dims),max([x[1] for x in dims]+[0]),max([x[2] for x in dims]+[0])
  if k=='frac':
   a=self.measure(n[1],size*.92);b=self.measure(n[2],size*.92)
   return max(a[0],b[0])+8,a[1]+a[2]+size*.35,b[1]+b[2]+size*.18
  if k in ['sub','sup']:
   a=self.measure(n[1],size);b=self.measure(n[2],size*.7)
   return a[0]+b[0],max(a[1],b[1]+size*.45) if k=='sup' else a[1],max(a[2],b[2]+size*.3) if k=='sub' else a[2]
  if k=='bar':
   w,a,b=self.measure(n[1],size);return w,a+3,b
 def wrap(self,availWidth,availHeight):
  w,a,b=self.measure(self.tree,self.size)
  if w>availWidth:self.size*=availWidth/w;w,a,b=self.measure(self.tree,self.size)
  self.width=w;self.height=a+b+4;self.base=b+2
  return self.width,self.height
 def paint(self,n,x,y,size):
  c=self.canv;k=n[0]
  if k=='text':c.setFont('Body',size);c.drawString(x,y,n[1]);return
  if k=='seq':
   for child in n[1]:self.paint(child,x,y,size);x+=self.measure(child,size)[0]
  elif k=='frac':
   w,a,b=self.measure(n,size);num=self.measure(n[1],size*.92);den=self.measure(n[2],size*.92)
   c.setLineWidth(.65);c.line(x,y+size*.12,x+w,y+size*.12)
   self.paint(n[1],x+(w-num[0])/2,y+size*.35+num[2],size*.92)
   self.paint(n[2],x+(w-den[0])/2,y-size*.18-den[1],size*.92)
  elif k in ['sub','sup']:
   self.paint(n[1],x,y,size);self.paint(n[2],x+self.measure(n[1],size)[0],y+(-size*.3 if k=='sub' else size*.45),size*.7)
  elif k=='bar':
   w,a,b=self.measure(n[1],size);self.paint(n[1],x,y,size);c.setLineWidth(.65);c.line(x,y+a+1,x+w,y+a+1)
 def draw(self):self.canv.setFillColorRGB(0,0,0);self.paint(self.tree,0,self.base,self.size)
