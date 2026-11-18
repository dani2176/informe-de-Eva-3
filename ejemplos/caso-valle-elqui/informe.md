# Verificación del SLA del enlace dedicado

Agrícola Valle de Elqui SpA

Evaluación 3 · Septiembre de 2026

INTEGRANTE: Daniel Videla

CARRERA: Ingeniería en Telecomunicaciones, Conectividad y Redes

ASIGNATURA: Infraestructura de Telecomunicaciones Avanzada

PROFESOR: Daniel Ruz

SEDE: La Serena

FECHA: 16 de noviembre de 2026

REPOSITORIO: https://github.com/dani2176/informe-de-Eva-3 · Versión requerida v1.1

Informe técnico de cumplimiento y determinación del crédito de servicio

## 01 Identificación

Se evalúa el enlace dedicado de Agrícola Valle de Elqui SpA para determinar qué obligaciones del SLA se cumplieron durante septiembre de 2026 y qué crédito puede respaldarse con los antecedentes del caso. El servicio sostiene el ERP, la trazabilidad de exportación y la telefonía IP de la planta en Vicuña. La revisión permite separar las interrupciones imputables al proveedor de las exclusiones contractuales y de las limitaciones de la medición.

| Antecedente | Identificación |
| --- | --- |
| Cliente | Agrícola Valle de Elqui SpA |
| Proveedor | NorteNet Telecomunicaciones |
| Servicio | Internet dedicado simétrico de 200 Mbps, cláusula 2.1 |
| Demarcación | Puerto LAN del CPE de la planta Vicuña, cláusula 2.2 |
| Período | 01 al 30 de septiembre de 2026, mes calendario completo |
| Duración | 30 días × 24 h/día × 60 min/h = 43.200 min |
| Cargo mensual | \$1.200.000 netos, cláusula 8.4 |
| Equipo evaluador | Integrantes identificados en la portada |
| Carpeta del caso | ejemplos/caso-valle-elqui/ |

## 02 Resumen ejecutivo

El servicio no cumple el SLA: la disponibilidad alcanza 99,62963 %, inferior al 99,9 %, y el ticket INC-2672 registra 66 min de respuesta frente a 60 min permitidos. Corresponde un crédito de 15 %, equivalente a \$180.000 netos. Latencia, throughput y restauración cumplen; el jitter calculado cumple con una reserva de trazabilidad. La pérdida mensual tiene evidencia insuficiente y no justifica crédito adicional.

## 03 Alcance y referencias

Se revisan disponibilidad, latencia, jitter, pérdida de paquetes, throughput, respuesta y restauración conforme a las cláusulas 3.1 a 3.5 y 4.1 a 4.2. La validez se rige por 5.1; las exclusiones, por 6.1 y 6.2; la energía del CPE, por 7.2; y los créditos, por 8.1 a 8.4. Se utiliza el caso EVA 3 como fuente de cifras. El caso Clínica Limarí sirve únicamente como referencia de estructura; sus valores no se trasladan a este análisis.

Las referencias técnicas son ITU-T Y.1540, sobre parámetros de transferencia y disponibilidad IP; RFC 3393, sobre variación del retardo; RFC 5357, sobre TWAMP; y RFC 6349, sobre pruebas de throughput TCP. Estas referencias describen conceptos y métodos: los umbrales y los créditos aplicables son los del contrato del caso. Las fuentes completas se presentan en el anexo final.

## 04 Metodología

### 4.1 Criterios de evaluación

Para cada indicador se compara el valor medido con el umbral, después de revisar punto, método, estadístico y cobertura. Se conservan los valores sin redondear para decidir el cumplimiento; el redondeo se usa solo en la presentación. Una diferencia en puntos porcentuales se identifica como pp y no como porcentaje relativo.

Tabla 1. Variables y reglas de evaluación durante septiembre de 2026

| Métrica | Operador y umbral | Período y estadístico | Cláusula |
| --- | --- | --- | --- |
| Disponibilidad | ≥ 99,9 % | Mes completo; minutos disponibles / 43.200 min | 3.1 |
| Latencia RTT | ≤ 30 ms | Promedio mensual; ICMP cada 60 s | 3.2 |
| Jitter | ≤ 10 ms | Promedio mensual ponderado por muestras válidas | 3.3 |
| Pérdida | ≤ 0,5 % | Proporción mensual de paquetes perdidos | 3.4 |
| Throughput | ≥ 180 Mbps | Promedio de al menos cuatro pruebas mensuales | 3.5 |
| Respuesta | ≤ 60 min | Cada incidente; cumplimiento exigido en el 100 % | 4.1 |
| Restauración | ≤ 240 min | Cada incidente atribuible al proveedor | 4.2 |

Tabla 2. Punto de observación y herramienta

| Métrica | Punto y método | Fuente |
| --- | --- | --- |
| Disponibilidad | Servicio en planta; NMS y contraste con tickets | Anexos 1 y 2 |
| Latencia | CPE ↔ servidor del proveedor en La Serena; Zabbix ICMP | Anexo 3 |
| Jitter | Desde puerto LAN del CPE; TWAMP, referencia RFC 3393 | Anexo 4 |
| Pérdida | Desde puerto LAN del CPE; TWAMP | Anexo 5 |
| Throughput | Puerto LAN del CPE; iperf3 TCP, cuatro flujos, 60 s | Anexo 6 |
| Respuesta | Apertura y primera respuesta del ticket | Anexo 2 |
| Restauración | Inicio y fin de caída del NMS; diagnóstico del ticket | Anexos 1 y 2 |

El requisito de 90 % se aplica a las series mensuales. Para throughput se aplica la regla específica de cuatro pruebas del mes; 4 de 4 pruebas válidas no significa monitoreo continuo durante el 100 % del mes. En respuesta se revisan los cuatro tickets de incidentes. El aviso de mantención MNT-0903 no es un ticket de falla que requiera primera respuesta.

### 4.2 Cobertura y suficiencia

El mínimo de cobertura mensual equivale a 0,90 × 43.200 = 38.880 intervalos de un minuto, o 27 días de observación. No se sustituyen datos faltantes por ceros ni por resultados medidos fuera de la demarcación.

| Evidencia | Cálculo o alcance | Decisión |
| --- | --- | --- |
| Latencia del cliente | 42.725 / 43.200 × 100 = 98,90 % | Aceptada; supera 90 % |
| Jitter del cliente | (9.870 + 10.025 + 9.900 + 12.930) / 43.200 × 100 = 98,90 % | Aceptación condicionada a frecuencia y trazabilidad |
| Pérdida del cliente | 18 / 30 × 100 = 60,00 % como máximo | Insuficiente para el mes |
| Throughput | Cuatro pruebas válidas / cuatro mínimas = 100 % de la cuota | Aceptada para promedio pactado |
| Respuesta | Cuatro tickets de incidente revisados / cuatro disponibles | Se evalúan los cuatro |
| Restauración | Tres eventos atribuibles / tres identificados | Se evalúan los tres |
| Registro NMS | Cinco eventos del mes; sin bitácora de continuidad | Base del caso; cobertura no verificable independientemente |

En jitter, 42.725 muestras no prueban por sí solas una cobertura temporal de 98,90 %. El contrato no indica la frecuencia TWAMP. El porcentaje se obtiene bajo el supuesto de un registro esperado por minuto, consistente con el volumen del anexo. Se requiere la configuración del sondeo para confirmar ese denominador.

Además, el anexo 5 indica que el colector TWAMP se detuvo el 19 de septiembre y no se recuperó. El anexo 4, en cambio, contiene muestras de jitter hasta el 30. Se calcula el jitter con los datos expresamente suministrados para esa métrica, pero su veredicto debe confirmarse mediante el origen de las series. Si ambas dependían del mismo colector sin respaldo, el jitter mensual quedaría con evidencia insuficiente. Esto no genera automáticamente un incumplimiento ni un crédito.

Las 475 muestras ICMP faltantes coinciden numéricamente con los 475 min de caídas registradas. Esta igualdad no permite asegurar que se trate de los mismos intervalos: la correspondencia requiere marcas de tiempo. Tampoco se usa esa coincidencia para certificar la continuidad del NMS.

### 4.3 Evidencia descartada para el veredicto

Los 22,1 ms de latencia y el 0,18 % de pérdida informados por NorteNet corresponden al tramo PE–core. No incluyen el acceso y el CPE del cliente, por lo que no acreditan las cláusulas 3.2 y 3.4. Pueden orientar el diagnóstico interno del proveedor, pero no reemplazan la medición contractual.

El Speedtest de 95 Mbps se realizó por Wi-Fi desde el notebook del gerente. Difiere en herramienta, punto y medio respecto de la prueba iperf3 TCP pactada. Se conserva como antecedente de experiencia del usuario, sin incorporarlo al promedio contractual.

### 4.4 Información pendiente de respaldo

Tabla 3. Datos necesarios para cerrar las limitaciones de evidencia

| Dato requerido | Métrica afectada | Utilidad de la verificación |
| --- | --- | --- |
| Logs TWAMP completos, frecuencia, origen y marcas de tiempo | Jitter | Confirmar cobertura y explicar registros posteriores al 19-sep |
| Registros válidos del 19 al 30-sep y contadores enviados/perdidos | Pérdida | Alcanzar al menos 27 días y recalcular el porcentaje mensual |
| Bitácora de continuidad y sincronización del NMS | Disponibilidad | Verificar que no existan períodos sin observación |
| Declaración que invoque fuerza mayor para E2, si existe | Disponibilidad | Revisar la eventual aplicación de 6.1b |
| Logs iperf3, extremos, dirección y condiciones de cada prueba | Throughput | Auditar las cifras y confirmar ambos sentidos del servicio simétrico |
| Evidencia de rutas, energía y equipos compartidos con el radioenlace | Viabilidad | Validar independencia y capacidad de respaldo |

La ausencia de una declaración de fuerza mayor mantiene E2 como atribuible para esta evaluación. No se concluye que todo daño por terceros sea jurídicamente imposible de excluir: se concluye que la exclusión del contrato no está acreditada en los antecedentes disponibles.

## 05 Resultados

### 5.1 Clasificación de las interrupciones

Tabla 4. Eventos del NMS y aplicación de exclusiones

| Evento y fecha | Duración | Clasificación | Fundamento contractual |
| --- | --- | --- | --- |
| E1 · 03-sep 02:00–05:30 | 210 min | Excluido | Aviso 29-ago 10:00: 112 h antes. Cumple ≥ 72 h y 3,5 h ≤ 4 h/mes; 6.1a |
| E2 · 09-sep 14:12–15:07 | 55 min | Atribuible | Corte de fibra en obras viales. Sin fuerza mayor declarada en el caso; no se acredita 6.1b |
| E3 · 15-sep 10:40–12:25 | 105 min | Excluido | Corte eléctrico de planta y CPE sin UPS. Responsabilidad del cliente; 6.1c y 7.2 |
| E4 · 21-sep 22:05–23:20 | 75 min | Atribuible | Falla de tarjeta de línea del PE del proveedor; no concurre exclusión 6.1 |
| E5 · 27-sep 08:30–09:00 | 30 min | Atribuible | Aviso 26-sep 18:00: 14,5 h antes, inferior a 72 h; no cumple 6.1a |

E1 y E5 suman 4 h de mantención, pero ello no vuelve excluible a E5. El límite mensual y la anticipación son requisitos acumulativos. La denominación “emergencia” no crea una exclusión adicional. Conforme a 6.2, los 315 min excluidos se consideran disponibles y el denominador permanece en 43.200 min.

### 5.2 Disponibilidad mensual

Tabla 4A. Conciliación del tiempo de servicio

| Concepto | Cálculo | Resultado |
| --- | --- | --- |
| Período mensual | 30 × 24 × 60 | 43.200 min |
| Interrupciones físicas | 210 + 55 + 105 + 75 + 30 | 475 min |
| Tiempo excluido | E1 + E3 = 210 + 105 | 315 min |
| Caída atribuible | E2 + E4 + E5 = 55 + 75 + 30 | 160 min |
| Tiempo disponible contractual | 43.200 − 160 | 43.040 min |

Disponibilidad mensual, conservando el período completo como denominador:

```math
A = \frac{T_{total}-T_{caida}}{T_{total}}\times 100
```

```math
A = \frac{43\,200-160}{43\,200}\times 100 = 99,62963\,\%
```

| Comprobación | Sustitución | Resultado |
| --- | --- | --- |
| Caída permitida | 43.200 × (1 − 0,999) | 43,20 min |
| Exceso de caída | 160 − 43,20 | 116,80 min |
| Desviación de disponibilidad | 99,62963 − 99,9 | −0,27037 pp |
| Disponibilidad física sin exclusiones | (43.200 − 475) / 43.200 × 100 | 98,90046 % |

No cumple la cláusula 3.1. El valor contractual queda entre 99,5 % y menos de 99,9 %, por lo que corresponde 10 % de crédito según 8.1. La disponibilidad física se muestra solo como contraste: no sirve para calcular el crédito, porque desconoce 6.2. Los tiempos excluidos se consideran disponibles y no se retiran del denominador. Los eventos no se superponen.

### 5.3 Latencia RTT

La cláusula 3.2 exige el promedio mensual. Se utiliza el RTT promedio de 27,4 ms informado por Zabbix desde el punto pactado, con 42.725 muestras válidas. Promedio = suma de RTT válidos / número de muestras válidas = 27,4 ms, según el agregado del anexo 3. No se dispone de la suma ni de los registros individuales para recalcular ese agregado desde cero.

Comparación = 27,4 ms ≤ 30 ms. Desviación = 27,4 − 30 = −2,6 ms. Cumple. El p95 de 41,2 ms y el máximo de 118 ms justifican investigar episodios de demora, pero no sustituyen el promedio que fija el SLA. Tampoco demuestran que todo el mes haya operado a 118 ms.

### 5.4 Jitter mensual ponderado

Se pondera cada promedio por las muestras válidas del grupo. El promedio simple de los cuatro valores no respeta la distinta cantidad de observaciones; tampoco corresponde ponderar solo por días cuando se conocen los recuentos efectivos.

Tabla 5A. Ponderación del jitter a partir del anexo 4

| Grupo | Muestras válidas n | Jitter medio j | Producto n × j |
| --- | --- | --- | --- |
| 01–07 sep | 9.870 | 9,0 ms | 88.830 ms |
| 08–14 sep | 10.025 | 10,5 ms | 105.262,5 ms |
| 15–21 sep | 9.900 | 13,8 ms | 136.620 ms |
| 22–30 sep | 12.930 | 7,2 ms | 93.096 ms |
| Total | 42.725 | — | 423.808,5 ms |

Promedio ponderado mensual:

```math
J = \frac{\sum n_i j_i}{\sum n_i}
```

```math
J = \frac{423\,808{,}5}{42\,725} = 9,91945\,\mathrm{ms}
```

La desviación es 9,91945 − 10 = −0,08055 ms. El agregado cumple el umbral mensual, aunque dos grupos lo superan. Se conserva la reserva de trazabilidad de 4.2: el cálculo no acredita por sí solo que el registro continuo haya sido auditado.

### 5.5 Pérdida de paquetes

La fórmula contractual es pérdida mensual = paquetes perdidos / paquetes enviados × 100. El 0,31 % del anexo 5 cubre solo del 01 al 18 de septiembre; no se entregan los contadores necesarios para reconstruirlo. La cobertura temporal máxima es 18 × 1.440 / 43.200 × 100 = 60 %, inferior a 90 %.

Faltan al menos 27 − 18 = 9 días para alcanzar el mínimo de cobertura, aunque lo preferible es recuperar los 12 días ausentes. No se puede promediar el 0,31 % con el 0,18 % del proveedor: las rutas, los períodos y los denominadores no son equivalentes. El veredicto mensual es evidencia insuficiente. No se asigna cumplimiento, incumplimiento ni crédito por esta métrica.

### 5.6 Throughput

Umbral = 200 Mbps × 0,90 = 180 Mbps. El anexo 6 contiene cuatro pruebas válidas con iperf3 TCP desde el puerto LAN del CPE.

Tabla 5. Pruebas incorporadas al promedio mensual

| Fecha | Resultado | Diferencia frente a 180 Mbps |
| --- | --- | --- |
| 05-sep | 186 Mbps | +6 Mbps |
| 12-sep | 182 Mbps | +2 Mbps |
| 19-sep | 171 Mbps | −9 Mbps |
| 26-sep | 184 Mbps | +4 Mbps |

Promedio de las cuatro pruebas válidas:

```math
\overline{V}=\frac{186+182+171+184}{4}=180{,}75\,\mathrm{Mbps}
```

```math
P=\frac{180{,}75}{200}\times 100=90{,}375\,\%
```

Desviación = 180,75 − 180 = +0,75 Mbps. Cumple la cláusula 3.5. La prueba de 171 Mbps merece revisión técnica, pero el contrato exige promedio mensual, no cumplimiento individual de cada prueba. El resultado se refiere al conjunto de pruebas suministrado; los anexos no desglosan subida y bajada.

### 5.7 Respuesta y restauración

El plazo de respuesta y el tiempo de restauración se evalúan por separado. Para restauración se utiliza el intervalo completo sin servicio, desde el inicio hasta el fin de la caída.

| Indicador | Inicio del cómputo | Fin del cómputo | Regla contractual |
| --- | --- | --- | --- |
| Primera respuesta | Apertura del ticket | Primera respuesta del proveedor | ≤ 60 min en todos los incidentes |
| Restauración | Inicio de la caída | Restitución del servicio | ≤ 240 min por incidente atribuible |

En INC-2648 también se evalúa la respuesta: la cláusula 4.1 exige atención del 100 % de los incidentes. La exclusión por causa del cliente afecta la disponibilidad y la restauración exigible, sin eliminar por sí sola el compromiso de atención. Aunque MTTR suele designar una media, se aplica el límite individual definido por 4.2.

Tabla 6. Verificación individual de tickets

| Ticket | Cálculo de respuesta | Veredicto ≤ 60 min | Restauración desde caída |
| --- | --- | --- | --- |
| INC-2611 | 14:41 − 14:18 = 23 min | Cumple | 15:07 − 14:12 = 55 min; cumple |
| INC-2648 | 11:20 − 10:47 = 33 min | Cumple | 105 min; 4.2 no aplica por causa del cliente |
| INC-2672 | 23:15 − 22:09 = 66 min | No cumple; exceso de 6 min | 23:20 − 22:05 = 75 min; cumple |
| INC-2690 | 08:40 − 08:33 = 7 min | Cumple | 09:00 − 08:30 = 30 min; cumple |

Cumplimiento de respuesta = 3 / 4 × 100 = 75 %, inferior al 100 % exigido. Máximo = 66 min. Corresponde 5 % de crédito por la métrica de respuesta, según 8.2. No se agrega 5 % por cada minuto de exceso ni se multiplica el crédito por los tickets atendidos.

En restauración, 55, 75 y 30 min son menores que 240 min. Los márgenes respectivos son 185, 165 y 210 min. Como dato complementario, la media de restauración es (55 + 75 + 30) / 3 = 53,33 min; el veredicto se obtuvo verificando cada incidente. Incluso usando apertura a restitución, los intervalos serían 49, 71 y 27 min y el resultado no cambiaría.

### 5.8 Síntesis del cumplimiento

Tabla 7. Resultados contractuales y créditos

| Métrica y objetivo | Medido y desviación | Fuente | Veredicto | Crédito |
| --- | --- | --- | --- | --- |
| Disponibilidad ≥ 99,9 % | 99,62963 %; −0,27037 pp | A1 y A2; 3.1 y 6.2 | No cumple | 10 % |
| RTT ≤ 30 ms | 27,4 ms; −2,6 ms | A3; 3.2 | Cumple | 0 % |
| Jitter ≤ 10 ms | 9,91945 ms; −0,08055 ms | A4; 3.3 | Cumple con reserva de trazabilidad | 0 % |
| Pérdida ≤ 0,5 % | 0,31 % parcial; desviación mensual no determinable | A5; 3.4 y 5.1 | Evidencia insuficiente | No acreditado |
| Throughput ≥ 180 Mbps | 180,75 Mbps; +0,75 Mbps | A6; 3.5 | Cumple | 0 % |
| Respuesta ≤ 60 min en todos | Máx. 66 min; +6 min; 75 % de tickets | A2; 4.1 | No cumple | 5 % |
| Restauración ≤ 240 min | Máx. 75 min; −165 min | A1 y A2; 4.2 | Cumple | Sin crédito específico en 8.2 |

A1 a A7 identifican los anexos del caso EVA 3. La desviación es medido menos objetivo. El veredicto global es no cumple: basta la existencia de las dos obligaciones incumplidas acreditadas, sin convertir la falta de evidencia de otra métrica en una infracción adicional.

## 06 Análisis de incumplimientos

### 6.1 Disponibilidad inferior al compromiso mensual

Los eventos E2, E4 y E5 acumulan 160 min imputables a NorteNet, equivalentes a 2 h 40 min. El presupuesto mensual de caída era de 43,20 min. El corte de fibra del 09-sep, por sí solo, consumió 55 min y ya superó ese presupuesto. La falla del PE del 21-sep y la intervención del 27-sep ampliaron el exceso hasta 116,80 min.

Las causas documentadas son un corte de fibra por obras viales, una falla de tarjeta de línea y una mantención de emergencia cuyo aviso no cumplió la anticipación pactada. El primer evento no dispone de declaración de fuerza mayor en el caso; el segundo afecta un equipo del proveedor; el tercero no satisface 6.1a. Por ello, sus tiempos se incluyen en el cálculo contractual.

La pérdida de conectividad pudo interrumpir las funciones del ERP y de trazabilidad que requieren el enlace, además de afectar la telefonía IP. Se trata de consecuencias operativas previsibles por la dependencia descrita en el caso. No se entregaron registros de transacciones, llamadas ni embarques afectados: no corresponde afirmar que existió una pérdida monetaria específica, retraso de exportación determinado o pérdida de datos comprobada.

### 6.2 Respuesta tardía al incidente del PE

INC-2672 se abrió el 21-sep a las 22:09 y recibió primera respuesta a las 23:15. El plazo fue 66 min, excediendo en 6 min la cláusula 4.1. La reparación concluyó a las 23:20, pero la restauración dentro de cuatro horas no compensa el incumplimiento de atención: son compromisos distintos.

El diagnóstico explica la avería de tarjeta, pero no el motivo de la demora de respuesta. Sin registros de asignación, escalamiento y turnos no puede atribuirse la tardanza a falta de personal, negligencia o saturación de la mesa de ayuda. El efecto verificable es que el cliente no obtuvo la primera respuesta dentro del tiempo acordado, lo que dificultó disponer oportunamente de información de recuperación.

### 6.3 Hallazgos que no generan crédito adicional

El corte eléctrico de E3 produjo 105 min de interrupción, pero el CPE carecía de UPS y 7.2 asigna ese respaldo al cliente. El evento se excluye de disponibilidad y exige una acción interna de continuidad. E1, de 210 min, también se excluye, por cumplir aviso y duración permitida.

La detención del colector de pérdida constituye una falla de observabilidad del cliente y reduce la capacidad de demostrar el nivel de servicio. Los valores altos de jitter de ciertos grupos, el máximo RTT y la prueba de 171 Mbps son señales para diagnóstico; no representan incumplimientos mensuales adicionales bajo los estadísticos pactados.

## 07 Conclusiones técnicas

### 7.1 Crédito de servicio procedente

El servicio no cumple disponibilidad ni respuesta. La latencia y el throughput cumplen con los agregados válidos del caso. La restauración cumple en los tres incidentes atribuibles. El jitter ponderado queda bajo el umbral, con la reserva de origen y continuidad de la serie. La pérdida mensual no puede resolverse por cobertura insuficiente.

Tabla 8. Aplicación de tramos y tope

| Concepto | Regla | Crédito |
| --- | --- | --- |
| Disponibilidad | 99,5 % ≤ 99,62963 % < 99,9 %; cláusula 8.1 | 10 % |
| Respuesta | 66 min > 60 min; cláusula 8.2 | 5 % |
| Latencia, jitter y throughput | Sin incumplimiento mensual acreditado | 0 % |
| Pérdida | Evidencia insuficiente; no se presume incumplimiento | 0 % reconocido |
| Suma previa al tope | 10 % + 5 % | 15 % |
| Tope contractual | Cláusula 8.3 | 50 % |
| Crédito aplicable | mínimo entre 15 % y 50 % | 15 % |

Monto neto del crédito, expresado en pesos chilenos:

```math
M=C_{mensual}\times c=1\,200\,000\times 0{,}15=180\,000\,\mathrm{CLP}
```

Cargo neto remanente, si el crédito se aplica a ese mismo cargo = \$1.200.000 − \$180.000 = \$1.020.000. No se agregan impuestos ni compensaciones no previstas en el extracto. El 50 % constituye un límite, no un beneficio automático por existir varias caídas.

### 7.2 Viabilidad de la infraestructura en serie

Se adopta un modelo simplificado de independencia y disponibilidad estacionaria. Los componentes de la ruta única deben funcionar simultáneamente.

| Componente en serie | Disponibilidad anual | Fracción utilizada |
| --- | --- | --- |
| CPE | 99,95 % | 0,9995 |
| Fibra de acceso | 99,80 % | 0,9980 |
| PE La Serena | 99,99 % | 0,9999 |
| Backbone | 99,99 % | 0,9999 |

```math
A_{serie}=A_{CPE}\times A_{fibra}\times A_{PE}\times A_{backbone}
```

```math
A_{serie}=0{,}9995\times 0{,}9980\times 0{,}9999\times 0{,}9999
```

| Resultado del modelo | Cálculo o valor | Comparación |
| --- | --- | --- |
| Disponibilidad total | 99,73015 % | Inferior a 99,9 % |
| Caída equivalente en 30 días | (1 − 0,997301509775) × 43.200 = 116,57 min | Superior a 43,20 min |

La ruta única no respalda la meta en este modelo; incluso la fibra aislada se encuentra bajo 99,9 %. Las disponibilidades anuales permiten comparar diseños, pero no garantizan un resultado en cada mes ni reemplazan la medición de septiembre. Deben verificarse las fallas comunes, la independencia y el comportamiento de conmutación.

### 7.3 Acceso de respaldo en paralelo

El radioenlace se modela como respaldo de la fibra de acceso. CPE, PE y backbone permanecen en serie. No se supone un segundo servicio completo e independiente, porque el caso solo ofrece respaldo de acceso.

Tabla 8A. Parámetros de la opción de respaldo

| Elemento | Disponibilidad | Papel en el modelo |
| --- | --- | --- |
| Fibra de acceso | 99,80 % | Acceso principal |
| Radioenlace | 99,50 % | Acceso alternativo, en paralelo con la fibra |
| CPE, PE y backbone | 99,95 %; 99,99 %; 99,99 % | Elementos comunes que siguen en serie |

Disponibilidad del acceso con dos alternativas independientes:

```math
A_{acceso}=1-(1-A_{fibra})(1-A_{radio})
```

```math
A_{acceso}=1-(0{,}0020\times 0{,}0050)=0{,}999990
```

```math
A_{total}=0{,}9995\times 0{,}999990\times 0{,}9999\times 0{,}9999
```

Tabla 8B. Comparación de diseños y objetivo mensual

| Escenario | Disponibilidad | Caída equivalente en 30 días | Evaluación |
| --- | --- | --- | --- |
| Fibra de ruta única | 99,73015 % | 116,57 min | Bajo 99,9 % |
| Fibra y radio en paralelo | 99,92901 % | 30,67 min | Viable bajo supuestos |
| Objetivo contractual | 99,9 % | 43,20 min | Referencia mensual |

| Comprobación del respaldo | Sustitución | Resultado |
| --- | --- | --- |
| Caída equivalente | (1 − 0,999290116994) × 43.200 | 30,67 min/mes |
| Margen disponible | 43,20 − 30,67 | 12,53 min/mes |

El diseño supera 99,9 % si existe independencia efectiva y conmutación suficientemente rápida. No evita fallas del CPE, del PE compartido ni de la energía de planta. El caso tampoco informa si el radio soporta 200 Mbps o los límites de latencia y jitter; estos atributos deben comprobarse antes de contratarlo.

### 7.4 Respuesta fundada al gerente

| Afirmación del correo | Evaluación y fundamento |
| --- | --- |
| “Septiembre fue un desastre” | Es una valoración. Técnicamente se acreditan dos métricas incumplidas; no existen antecedentes para cuantificar el daño económico. |
| “Se cayó varias veces” | Se sostiene: cinco eventos y 475 min físicos. Para el SLA son tres eventos y 160 min atribuibles; E1 y E3 se excluyen. |
| “Speedtest dio 95 Mbps cuando pagamos 200” | El resultado figura en el caso, pero no demuestra incumplimiento contractual por su método y punto. iperf3 promedia 180,75 Mbps, sobre el mínimo de 180 Mbps. |
| “En Zabbix vi peaks de 118 ms” | Se sostiene como máximo registrado. El contrato evalúa promedio y este es 27,4 ms, menor que 30 ms. |
| “Exijamos el máximo de 50 %” | No se sostiene con la evidencia actual. Corresponde 15 %, es decir, \$180.000 netos; el 50 % es un tope. |

## 08 Recomendaciones

Tabla 9. Acciones derivadas de los hallazgos

| Hallazgo | Recomendación y responsable propuesto | Mejora y verificación | Prioridad |
| --- | --- | --- | --- |
| Disponibilidad de 99,62963 % y 160 min atribuibles | Solicitar a NorteNet reconocimiento del crédito y plan correctivo para E2, E4 y E5 | Respuesta documentada y crédito de \$180.000 netos | Alta |
| Serie actual bajo 99,9 % | Evaluar fibra más radio con rutas y energía independientes; TI y proveedor | Prueba de conmutación, capacidad y QoS; comprobar supuestos | Alta |
| CPE sin UPS en E3 | Dimensionar UPS y probar autonomía según carga real; TI del cliente | Evitar desconexión del CPE ante cortes de energía | Alta |
| INC-2672 respondió en 66 min | Establecer alertas antes de 60 min y escalamiento de guardia; proveedor | Cumplimiento de atención en el 100 % de tickets | Alta |
| Colector lleno y solo 60 % de cobertura de pérdida | Alertar disco, aplicar retención y respaldo del monitoreo; TI | Cobertura ≥ 90 %, preferentemente continua, y exportación mensual | Alta |
| Contradicción entre anexos TWAMP | Conciliar series, reloj, origen y frecuencia del colector; TI y proveedor | Jitter y pérdida trazables con logs separados | Alta |
| Aviso E5 con 14,5 h | Acordar tratamiento documentado de intervenciones urgentes; proveedor y cliente | Evitar exclusiones sin cumplir 72 h; no modificar retroactivamente el SLA | Media |
| Throughput con margen de 0,75 Mbps | Mantener pruebas conjuntas y conservar logs bidireccionales; TI y proveedor | Detectar degradación persistente y validar simetría | Media |
| Pico RTT de 118 ms y jitter variable | Correlacionar horarios con carga, colas y tráfico; proveedor | Explicar episodios de degradación sin confundirlos con promedios | Media |
| Speedtest por Wi-Fi usado como prueba | Documentar medición cableada en el CPE con iperf3; TI | Evidencia repetible y comparable con 3.5 | Baja |

La prioridad alta corresponde a continuidad, atención o pérdida de evidencia necesaria para reclamar. Las acciones de diagnóstico no deben presentarse como causas ya demostradas. La aceptación del respaldo debe incluir pruebas bajo carga, recuperación del enlace principal y verificación de que la falla eléctrica del cliente no inutilice ambos accesos a la vez.

## 09 Automatización del proceso

### 9.1 Flujo reproducible

Se entrega un paquete local con la carpeta ejemplos/caso-valle-elqui, datos de entrada, calculadora, plantilla de redacción y generador. La carga desde los anexos y la interpretación de exclusiones se realizan manualmente, porque requieren contrastar diagnósticos con las cláusulas. Los cálculos, la tabla de salida y la sustitución de cifras principales se ejecutan con Python. El PDF y el Word se construyen desde la misma fuente estructurada; el Word conserva los elementos gráficos de la plantilla INACAP. La versión informe.md para GitHub emplea tablas Markdown y bloques matemáticos LaTeX, sin saltos de página de impresión.

El archivo objetivos.yaml utiliza sintaxis JSON, que es compatible con YAML 1.2. Esto permite leerlo sin una biblioteca adicional de YAML. mediciones.csv contiene únicamente valores admitidos para el cálculo principal; la pérdida parcial y el Speedtest no se mezclan con las mediciones válidas. Los registros auxiliares conservan muestras de jitter, cobertura y clasificaciones para permitir su revisión.

### 9.2 Comandos de reproducción

Ejecutar desde la carpeta raíz del paquete, con Python 3 y las dependencias de requirements.txt instaladas:

```text
python -m pip install -r requirements.txt
python herramientas/regenerar.py
```

El segundo comando ejecuta calc_sla.py, actualiza salida_calc.txt y resultados.json, completa la plantilla y genera informe.md, informe.docx e informe.pdf en ejemplos/caso-valle-elqui/. La portada del repositorio enlaza las tres versiones y los datos fuente. La calculadora también puede ejecutarse por separado:

```text
python herramientas/calc_sla.py -o ejemplos/caso-valle-elqui/objetivos.yaml -m ejemplos/caso-valle-elqui/mediciones.csv
```

La regeneración actualiza los campos enlazados a resultados. La interpretación contractual, el análisis de causas y los párrafos que mencionan valores fijos requieren revisión humana si cambia el caso; no se presenta el generador como un redactor automático de cualquier escenario. Los archivos incluyen controles para los resultados esperados de este caso.

### 9.3 Declaración de asistencia y revisión

Se utilizó ChatGPT de OpenAI para apoyar la lectura de los documentos, la redacción, la preparación de scripts y la organización del informe. El contexto fue el caso EVA 3, las especificaciones, el ejemplo Clínica Limarí y la plantilla Word INACAP. Las cifras se contrastaron con la calculadora y con las fórmulas expuestas. No se atribuyen al grupo revisiones, correcciones ni commits que todavía no haya realizado; corresponde registrar esas acciones reales antes de la entrega académica.

### 9.4 Versionado y publicación

El paquete local no acredita publicación en un repositorio remoto. La portada identifica el repositorio informado por Daniel Videla. Debe comprobarse que contenga la versión v1.1 después de integrar el trabajo. El historial de commits no se inventa: se adjunta una guía para crear la rama del caso, registrar avances, integrar a main y etiquetar la versión. Cada integrante debe aportar con su identidad real. El anexo de historial debe actualizarse desde ese repositorio antes de entregar.

## Anexo A Datos y objetivos utilizados

El siguiente contenido corresponde al archivo objetivos.yaml. Los porcentajes de crédito se almacenan como fracciones y los objetivos de disponibilidad y pérdida como porcentajes. Los indicadores de tiempo se expresan en minutos.

```text
{
  "servicio": "Internet dedicado simetrico 200 Mbps",
  "periodo": "2026-09",
  "minutos_periodo": 43200,
  "cobertura_minima": 0.9,
  "cargo_mensual": 1200000,
  "tope_credito": 0.5,
  "metricas": {
    "disponibilidad": {"operador": ">=", "objetivo": 99.9, "unidad": "%"},
    "latencia": {"operador": "<=", "objetivo": 30, "unidad": "ms", "estadistico": "promedio"},
    "jitter": {"operador": "<=", "objetivo": 10, "unidad": "ms", "estadistico": "promedio_ponderado"},
    "perdida": {"operador": "<=", "objetivo": 0.5, "unidad": "%"},
    "throughput": {"operador": ">=", "objetivo": 180, "unidad": "Mbps", "estadistico": "promedio"},
    "respuesta": {"operador": "<=", "objetivo": 60, "unidad": "min"},
    "restauracion": {"operador": "<=", "objetivo": 240, "unidad": "min"}},
  "minimo_pruebas": 4,
  "creditos_disponibilidad": [[99.5, 99.9, 0.1], [99.0, 99.5, 0.25], [0, 99.0, 0.5]],
  "credito_otras": 0.05
}
```

## Anexo B Mediciones y salida de la calculadora

Contenido completo de mediciones.csv. El jitter se calcula desde sus grupos en evidencia.json y se conserva sin redondear en la entrada. El programa verifica que coincida con la ponderación antes de evaluar el umbral.

```text
fecha,metrica,valor,unidad
2026-09-09,caida_atribuible,55,min
2026-09-21,caida_atribuible,75,min
2026-09-27,caida_atribuible,30,min
2026-09-30,latencia,27.4,ms
2026-09-30,jitter,9.919449970743125,ms
2026-09-05,throughput,186,Mbps
2026-09-12,throughput,182,Mbps
2026-09-19,throughput,171,Mbps
2026-09-26,throughput,184,Mbps
2026-09-09,respuesta,23,min
2026-09-15,respuesta,33,min
2026-09-21,respuesta,66,min
2026-09-27,respuesta,7,min
2026-09-09,restauracion,55,min
2026-09-21,restauracion,75,min
2026-09-27,restauracion,30,min
```

Salida completa de calc_sla.py para las entradas entregadas:

```text
CALCULADORA SLA | Valle de Elqui | 2026-09
Periodo: 43200 min | Exclusiones consideradas disponibles
disponibilidad: 99.62963 %
  Objetivo >= 99.9 % | NO CUMPLE
latencia: 27.40000 ms
  Objetivo <= 30 ms | CUMPLE
jitter: 9.91945 ms
  Objetivo <= 10 ms | CUMPLE (reserva trazabilidad)
perdida: sin valor mensual valido
  Objetivo <= 0.5 % | EVIDENCIA INSUFICIENTE
throughput: 180.75000 Mbps
  Objetivo >= 180 Mbps | CUMPLE
respuesta: 66.00000 min
  Objetivo <= 60 min | NO CUMPLE
restauracion: 75.00000 min
  Objetivo <= 240 min | CUMPLE
Caida atribuible: 160.00 min
Caida permitida: 43.20 min | Exceso: 116.80 min
Cobertura ICMP: 98.90046 %
Cobertura perdida: 60.00 % (insuficiente)
Respuesta: 23, 33, 66, 7 min | Cumplen 3/4 (75 %)
Credito: 15.00 % | Monto neto: $180000
Serie: 99.73015098 % | 116.57478 min
Con radio: 99.92901170 % | 30.66695 min
Reserva: verificar origen y frecuencia de series TWAMP.
```

## Anexo C Comprobaciones complementarias

### C.1 Anticipación de avisos y conciliación de tiempos

E1: desde 29-ago 10:00 hasta 03-sep 02:00 transcurren 4 días y 16 h = 112 h. La duración es 3 h 30 min = 210 min. Se cumplen las 72 h de anticipación y el límite de 240 min de mantención.

E5: desde 26-sep 18:00 hasta 27-sep 08:30 transcurren 14 h 30 min = 14,5 h. Faltan 72 − 14,5 = 57,5 h de anticipación. Aunque E1 + E5 = 240 min, E5 no cumple el aviso mínimo.

Conciliación: 475 min físicos = 315 min excluidos + 160 min atribuibles. En el cálculo del SLA, 43.200 − 160 = 43.040 min se consideran disponibles. Se revisa esta identidad para evitar contar dos veces un evento o retirar una exclusión del denominador.

### C.2 Sensibilidad a la fuerza mayor de E2

Si se acreditara y aceptara contractualmente la exclusión de E2, el tiempo atribuible sería 75 + 30 = 105 min. A = (43.200 − 105) / 43.200 × 100 = 99,75694 %. Seguiría bajo 99,9 % y en el tramo de 10 %. Con el 5 % por respuesta, el crédito seguiría en 15 %. Este escenario no modifica la clasificación base: muestra el efecto que tendría un antecedente nuevo.

### C.3 Sensibilidad a la inconsistencia TWAMP

Si no se pudiera demostrar que el jitter dispone de registros válidos posteriores al 19-sep, su veredicto cambiaría de cumplimiento condicionado a evidencia insuficiente. No se puede recalcular un jitter mensual alternativo con los grupos publicados, porque el grupo 15–21 mezcla días anteriores y posteriores a la detención. El crédito acreditado permanecería en 15 %; una falta de datos no habilita el 5 % adicional.

### C.4 Registro de cambios y mejoras pendientes

CHANGELOG.md registra la incorporación local de datos, calculadora, informe y generación de documentos. Las mejoras pendientes son importar logs crudos de ICMP/TWAMP e iperf3, validar automáticamente continuidad y dirección de las pruebas, y revisar clasificaciones con evidencia documental. El programa calcula la ponderación y los tiempos por ticket; la decisión de exclusión sigue siendo una revisión contractual manual.

Extracto del historial: pendiente de generación en el repositorio real del grupo. Para obtenerlo sin inventar contribuciones, ejecutar git log --oneline --decorate y copiar la salida al anexo de la versión final. La guía README.md incluye los comandos de rama, commits, merge y tag v1.1. No se acredita que estas operaciones ya hayan ocurrido.

## Anexo D Referencias y trazabilidad

### D.1 Documentos del encargo

EVA 3 CASO DE ESTUDIO.pdf. Contexto y correo del gerente, p. 1; contrato, p. 2; eventos, tickets, latencia y jitter, p. 3; pérdida, throughput e infraestructura, p. 4; tareas y entregable, p. 5; escala de apreciación, p. 6.

Especificaciones_Informe_SLA.pdf. Propósito y formato, p. 1; estructura, pp. 2–3; automatización y contenido del repositorio, pp. 4–5; uso de IA y versionado, p. 6; verificación y entrega, p. 7.

Caso_Clinica_Limari.pdf. Referencia de organización y presentación de cálculos. No constituye evidencia del servicio de Agrícola Valle de Elqui.

Carta-1-vert (3).docx. Plantilla institucional INACAP utilizada como referencia de formato, encabezado, pie y tipografía.

### D.2 Referencias técnicas

ITU-T. Y.1540. Internet protocol data communication service — IP packet transfer and availability performance parameters. https://www.itu.int/rec/T-REC-Y.1540

Demichelis, C. y Chimento, P. (2002). RFC 3393. IP Packet Delay Variation Metric for IP Performance Metrics. https://www.rfc-editor.org/rfc/rfc3393

Hedayat, K. y otros (2008). RFC 5357. A Two-Way Active Measurement Protocol. https://www.rfc-editor.org/rfc/rfc5357

Constantine, B. y otros (2011). RFC 6349. Framework for TCP Throughput Testing. https://www.rfc-editor.org/rfc/rfc6349

### D.3 Correspondencia con la evaluación

| Indicadores de la pauta | Evidencia en el informe |
| --- | --- |
| 1 y 2 · Variables, métodos y puntos | Sección 04, tablas 1 y 2 |
| 3 · Clasificación de eventos | Sección 05, tabla 4 y anexo C |
| 4 y 5 · Validez e información faltante | Sección 04, cobertura y tabla 3 |
| 6 y 7 · Cálculos de servicio | Sección 05, apartados 5.2 a 5.6 |
| 8 · Respuesta y restauración | Sección 05, tabla 6 |
| 9 y 10 · Veredictos y créditos | Tabla 7 y sección 07 |
| 11 · Viabilidad y recomendaciones | Apartados 7.2 y 7.3 y sección 08 |
| 12 · Presentación técnica | Nueve secciones, tablas y anexos |
| 13 · Toolkit y publicación | Sección 09 y paquete local; publicación y aportes del grupo pendientes |
