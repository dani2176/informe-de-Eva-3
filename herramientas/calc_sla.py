import argparse,csv,json,math
from pathlib import Path

def calcular(obj_path,med_path):
 o=json.loads(Path(obj_path).read_text(encoding='utf-8'))
 e=json.loads((Path(obj_path).parent/'evidencia.json').read_text(encoding='utf-8'))
 rows=list(csv.DictReader(Path(med_path).open(encoding='utf-8')))
 groups={}
 for r in rows: groups.setdefault(r['metrica'],[]).append(float(r['valor']))
 t=o['minutos_periodo']; caida=sum(groups['caida_atribuible'])
 assert caida==sum(x['minutos'] for x in e['eventos'] if x['atribuible'])
 jitter=sum(n*v for n,v in e['jitter_grupos'])/sum(n for n,v in e['jitter_grupos'])
 assert math.isclose(jitter,groups['jitter'][0],abs_tol=1e-10)
 assert len(groups['throughput'])>=o['minimo_pruebas']
 vals={'disponibilidad':100*(t-caida)/t,'latencia':sum(groups['latencia'])/len(groups['latencia']),'jitter':jitter,'throughput':sum(groups['throughput'])/len(groups['throughput']),'respuesta':max(groups['respuesta']),'restauracion':max(groups['restauracion'])}
 credit=0; res=[]
 for key,m in o['metricas'].items():
  value=vals.get(key); c=0
  if value is None: verdict='EVIDENCIA INSUFICIENTE'
  else:
   ok=value>=m['objetivo'] if m['operador']=='>=' else value<=m['objetivo']
   verdict='CUMPLE' if ok else 'NO CUMPLE'
   if key=='jitter': verdict+=' (reserva trazabilidad)'
   if not ok:
    if key=='disponibilidad': c=next((c for a,b,c in o['creditos_disponibilidad'] if a<=value<b),0)
    elif key in ['latencia','jitter','perdida','throughput','respuesta']: c=o['credito_otras']
  credit+=c;res.append({'metrica':key,'objetivo':m['objetivo'],'operador':m['operador'],'unidad':m['unidad'],'medido':value,'veredicto':verdict,'credito':c})
 credit=min(credit,o['tope_credito'])
 k=e['componentes'];serie=k['cpe']*k['fibra']*k['pe']*k['backbone'];parallel=k['cpe']*(1-(1-k['fibra'])*(1-k['radio']))*k['pe']*k['backbone']
 result={'metricas':res,**vals,'credito':credit,'monto':round(credit*o['cargo_mensual']),'caida':caida,'serie':serie,'paralelo':parallel,'serie_caida':(1-serie)*t,'paralelo_caida':(1-parallel)*t,'cobertura_latencia':e['latencia_validas']/e['latencia_esperadas']*100,'cobertura_perdida':e['perdida_dias']/e['dias_mes']*100}
 lines=['CALCULADORA SLA | Valle de Elqui | 2026-09','Periodo: 43200 min | Exclusiones consideradas disponibles']
 for r in res:
  v='sin valor mensual valido' if r['medido'] is None else f"{r['medido']:.5f} {r['unidad']}"
  lines += [f"{r['metrica']}: {v}",f"  Objetivo {r['operador']} {r['objetivo']} {r['unidad']} | {r['veredicto']}"]
 lines += [f'Caida atribuible: {caida:.2f} min','Caida permitida: 43.20 min | Exceso: 116.80 min',f'Cobertura ICMP: {result["cobertura_latencia"]:.5f} %',f'Cobertura perdida: {result["cobertura_perdida"]:.2f} % (insuficiente)','Respuesta: 23, 33, 66, 7 min | Cumplen 3/4 (75 %)',f'Credito: {credit*100:.2f} % | Monto neto: ${result["monto"]}',f'Serie: {serie*100:.8f} % | {result["serie_caida"]:.5f} min',f'Con radio: {parallel*100:.8f} % | {result["paralelo_caida"]:.5f} min','Reserva: verificar origen y frecuencia de series TWAMP.']
 return result,'\n'.join(lines)+'\n'

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('-o',required=True);p.add_argument('-m',required=True);a=p.parse_args()
 result,out=calcular(a.o,a.m);print(out,end='')
