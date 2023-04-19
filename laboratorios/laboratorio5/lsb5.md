# **LABORATORIO 5: – Uso de Ultracortex y BiTalino para EEG**``
Realizado el 19 de abril de 2023
<p align="center">
     <img width="500" height="300" src="https://images.squarespace-cdn.com/content/v1/5f7b55a801226812a44f7180/1609441748072-S5NU5R5YSQF4LYBO7KZT/OpenBCI-WebXR-EEG.gif">
     <img width="500" height="300" src="https://user-images.githubusercontent.com/17307/31218894-586281e4-a9c4-11e7-81d8-bd6f3dfd4267.gif">
</p>

# **Tabla de contenidos**
1. [Introducción](#id0)
2. [Objetivos](#id1)
3. [Materiales y equipos](#id2)
4. [Procedimiento](#id3)
5. [Resultados con BiTalino](#id4)\
     4.1 [Conexión usada](#id5)\
     4.2 [Video de la señal](#id6)\
     4.3 [Ploteo de la señal en OpenSignal](#id7)\{{100
     4.4 [Archivos](#id8)\
     4.5 [Ploteo de la señal en Python](#id9)

6. [Resultados con Ultracortex](#id10)\
     4.1 [Conexión usada](#id11)\
     4.2 [Video de la señal](#id12)\
     4.3 [Ploteo de la señal en OpenBCI](#id13)\
     4.4 [Archivos](#id14)\
     4.5 [Ploteo de la señal en Python](#id15)
7. [Conclusiones](#id16)
8. [Referencias](#id17)

## **Introducción al laboratorio** <a name="id0"></a>
---
<p align="justify">
El encefalograma (EEG) es un estudio que evalúa la actividad eléctrica realizada por el cerebro por medio de electrodos colocados sobre el cuero cabelludo. [1] Puede detectar alteraciones de todo el cerebro o de algunas áreas, tales como:
</p>

- Tumores
- Hemorragias
- Encefalitis
- Traumatismos [2]
<p align="center">
     <img width="500" height="300" src="https://user-images.githubusercontent.com/89707896/233177884-5f650a21-90bc-4509-9312-a1920c89cd09.png">
</p>
<p align="center">
Figura 1. EEG de una convulsión generalizada [3]
</p>

<p align="justify">
Los nombres de los sitios de los electrodos utilizan abreviaturas alfabéticas que identifican el lóbulo o el área del cerebro de la que cada electrodo registra:
</p>

- F: Frontal
- FP: Frontal anterrior
- T: Temporal
- C: Central
- P: Parietal
- O: Occipital
- A: Oreja o apófisis mastoides
- Z: Línea media
- <p align="justify"> TEXTO </p>

<p align="center">
     <img width="600" height="400" src="LINK IMAGEN">
</p>
<p align="center">
Figura 2. Onda ECG con sus características generales [4]
</p>

<p align="justify">
Para poder realizar estas mediciones, en el presente laboratorio, se empleó la placa de desarrollo BiTalino y el Ultracortex EEG Headset, los cuales son herramientas que permiten registrar y analizar la actividad eléctrica de diversas zonas del cuerpo, entre ellas la del cerebro, sin la necesidad de ser invasiva y permitiendo obtener resultados en tiempo real.
</p>

### ¿Cómo se interpreta el EEG?
<p align="justify">
Para ello evaluamos las ondas respecto a lo categorizado como normal:
</p>
- Verificación de onda P
     - La deflección negativa es normalmente < 1mm
     - La duración de la onda P debe ser menor o igual a 0.12 segundos
     - La amplitud de la onda P debe ser < 0.25 mm en las derivaciones de las extremidades
 <p align="center">
     <img width="700" height="200" src="https://user-images.githubusercontent.com/89707896/231650199-b6f9eb24-ebb6-47c8-a5f1-4e44d4d1b342.png">
</p>
<p align="center">
Figura 3. Onda P [4]
</p>

- Verificación del intervalo PR
     - Intervalo normal: 0.12 a 0.22 segundos; el límite superior de referencia es de 0.20 segundos en adultos jóvenes
     - Un intervalo prolongado (>0.22s) es compatible con un bloqueo AV de priemr grado
     - Un intervalo acortado (<0.12s) indica presencia de una vía accesoria
 <p align="center">
     <img width="600" height="400" src="https://user-images.githubusercontent.com/89707896/231649284-d539ff9c-454f-40f7-8e34-6ebe87892adb.png">
</p>
<p align="center">
Figura 4. Intervalo PR [4]
</p>

- Complejo QRS
     - La prolongación del complejo implica que la despolarización ventricular es más lenta de lo normal (<0.12s),  por el contrario, si es mayor se considera un complejo anormalmente ancho, relacionado con enfermedades como:
          - Bloqueo de rama del haz
          - Hiperpotasemia
          - Medicamentos (arrítmicos de clase I, antidepresivos tricíclicos, etc)
          - Ritmo ventricular, ectopia ventricular y marcapasos con estimulación ventricular
          - Preexcitación (síndrome de Wolf-Parkinson-White)
          - Conducción ventricular aberrante
 <p align="center">
     <img width="600" height="400" src="https://user-images.githubusercontent.com/89707896/231650744-66bb11c3-ed7a-44ff-b08c-89250f45e1fc.png">
</p>
<p align="center">
Figura 5. Complejo QRS [4]
</p>

## **Objetivos** <a name="id1"></a>
---
Los objetivos del laboratorio son:
* Adquirir señales biomédicas de ECG.
* Hacer una correcta configuración de BiTalino.
* Extraer la información de las señales ECG del software OpenSignals (r)evolution 


## **Materiales y equipos** <a name="id2"></a>

---
<div align="center">

|  **Imagen**  | **Producto** | **Cantidad** |
|:------------:|:---------------:|:------------:|
| <img width="200" height="150" src="https://i.postimg.cc/VvLXqb8P/14022-01a.jpg"> |   Kit BITalino  |       1      |
| <img width="200" height="150" src="https://i.postimg.cc/XNmdLX3Z/equipos.png"> |      Laptop     |       1      |
| <img width="200" height="150" src="https://user-images.githubusercontent.com/89707896/233160701-4bf7cd35-220c-4483-8847-bb7abb28feb1.png"> |   Ultracortex   |       1      |

</div>



## **Procedimiento** <a name="id3"></a>
-Para la conexión electrodos al cuerpo utilizamos la guía proporcionada por el propio Bitalino de nombre: "BITalino HOME-GUIDE #2 ELECTROCARDIOGRAPHY (ECG) Exploring Cardiac Signals at the Skin Surface".

-Registro de la señal ECG: Se grabó la señal en 3 momentos
</p>
Estado basal: Evaluar el estado de reposo
</p>
Respiración prolongada: Evaluar al mantener la respiración por 10 segundos y el estado basal
</p>
Ejercicio intenso:Se realizo dintintos ejercicios por 5 minutos.


## **Resultados** <a name="id4"></a>
---

### **Conexión usada** <a name="id5"></a>
#


Se posicionaron los electrodos en base las guías mencionadas:
<p align="center"><img src="https://user-images.githubusercontent.com/89707896/231556282-5514bddb-7edd-44c2-b25a-eff7b03f8c3e.png" width="500" height="200"></p>
<p align="center">Figura 6. Posición de los electrodos según la guía.

<p align="center"><img src="https://user-images.githubusercontent.com/55772705/231652569-8c111952-0d50-4b4b-83f3-a2abce33c01e.PNG" width="400" height="400"></p>
<p align="center">Figura 7. Muestra una configuración del sensor de ECG BiTalino para la derivación I de Einthoven.
     
### **Videos de la señal** <a name="id6"></a>
#
| Ojos cerrados | Ojos abiertos |
| ------------ |  :------------------------------------: |
| <video src="https://user-images.githubusercontent.com/89707896/233197727-682b0923-7b51-4526-8751-70370731e366.mp4" width="200" /> | <video src="https://user-images.githubusercontent.com/89707896/233197777-92d52158-9e99-42b4-be4b-fcc7c056249f.mp4" width="200" /> |
</div>

<div align="center">
Ejercicio con luz
<video src="https://user-images.githubusercontent.com/89707896/233197893-0dfe0211-f1a8-4637-9764-13d50fc77269.mp4" width="400"/>
</div>

| Ejercicio complejo |     Ejercicio problema matemático     |
| ------------ |  :------------------------------------: |
|<video src="" width="200"/> | <video src="" width="200" />  |
</div>


### **Ploteo de la señal en OpenSignal** <a name="id7"></a>
#
     a)   Estado basal
<p align="center">
     <img width="500" height="300" src="https://user-images.githubusercontent.com/55772705/231611835-3ffa0a24-5e16-4ac8-97a3-a59e8c0362e2.PNG">
</p>
<p align="center">
Figura 8. Ploteo de la señal en OpenSignal en estado basal
</p>     
     
     b)   Manteniendo la respiración por 10 segundos
<p align="center">
     <img width="500" height="300" src="https://user-images.githubusercontent.com/55772705/231611939-2b79e311-fdce-487c-83f6-f0a795c2cbdf.PNG">
</p>
<p align="center">
Figura 9. Ploteo de la señal en OpenSignal manteniendo la respiración por 10 segundos
</p>

     
     c)   Reposo basal
<p align="center">
     <img width="500" height="300" src="https://user-images.githubusercontent.com/55772705/231611469-d7964526-ec59-44d6-ac3c-6fef92f0ee56.jpeg">
</p>
<p align="center">
Figura 10. Ploteo de la señal en OpenSignal en reposo basal
</p>


     d)   Después de una actividad física
<p align="center">
     <img width="500" height="300" src="https://user-images.githubusercontent.com/55772705/231612030-69c201ca-2f29-4105-8a93-d0597b2e2084.PNG">
</p>
<p align="center">
Figura 11. Ploteo de la señal en OpenSignal después de la actividad física
</p>

     
     e)  Simulacion 

| Paso 1 | Paso 2 |
| ------------ |  :------------------------------------: |
| <img width="500" height="300" src="https://user-images.githubusercontent.com/55772705/231613380-bc4d1eea-9a53-4a95-bbf3-8b3c3bdf9f80.jpeg"> | <img width="500" height="300" src="https://user-images.githubusercontent.com/55772705/231613426-d45de00e-70c8-4039-ac58-63dbafafc010.jpeg"> |
</div>

| Paso 3 | Paso 4 |
| ------------ |  :------------------------------------: |
| <img width="500" height="300" src="https://user-images.githubusercontent.com/55772705/231613472-04e57e10-6166-4e07-8003-f49d39aedff1.jpeg"> | <img width="500" height="300" src="https://user-images.githubusercontent.com/55772705/231613509-5cf80abe-d415-4e6e-a7e5-8639b53577d6.jpeg"> |
</div>

| Paso 5 | Paso 6 |
| ------------ |  :------------------------------------: |
| <img width="500" height="300" src="https://user-images.githubusercontent.com/55772705/231613554-b43c19d7-3913-409f-a09c-b13a39376668.jpeg"> | <img width="500" height="300" src="https://user-images.githubusercontent.com/55772705/231613604-e7f6adeb-2bd4-42c0-a769-8ee06ff7e381.jpeg"> |
</div>


### **Archivos** <a name="id8"></a>
Se encuentran en la carpeta del laboratorio 3.
#
### **Ploteo de la señal en Python** <a name="id9"></a>
#
     a)   Estado basal
Se observa el complejo QRS el cual indica un tiempo corto de despolarización de los ventrículos, lo que indicaría un corto periodo de movimiento dentro de estas cavidades. Asimismo, se observa una alta presencia de ruido en la región del ST, además existe una especie de pendiente en el segmento isoeléctrico lo que indicaría algo de actividad en el ventrículo incluso cuando no hay electricidad fluyendo a través de él.  Por último también se llegaría a notar una onda T, representativa de la repolarización de los ventrículos. [5]
<p align="center">
     <img width="500" height="300" src="https://user-images.githubusercontent.com/55772705/231612373-866789aa-8ddd-477b-8046-dcdd2fb0a006.jpeg">
</p>
<p align="center">
Figura 12. Ploteo de la señal en Python en estado basal
</p>    
<p align="center">
<img width="500" height="300" src="https://user-images.githubusercontent.com/55772705/231654224-cf1270e8-7896-4804-8997-df66e2c907c8.jpeg">
</p>
<p align="center">
Figura 13. Ploteo de la señal en Python en estado basal FFT.
</p> 
     


     b)   Manteniendo la respiración por 10 segundos
La inspiración profunda puede generar cambios tanto en la posición como en la orientación del corazón a través de un desplazamiento hacia abajo del diafragma que afectan la señal ECG. Estos cambios pueden observarse entre los 35 a 45 segundos en la siguiente gráfica [6].
 
<p align="center">
     <img width="500" height="300" src="https://user-images.githubusercontent.com/55772705/231612494-7170cc27-7967-43cf-8a9a-4b9723d330b5.jpeg">
</p>
<p align="center">
Figura 14. Ploteo de la señal en Python manteniendo la respiración por 10 segundos
</p>           
<p align="center">
<img width="500" height="300" src="https://user-images.githubusercontent.com/55772705/231654465-896baf32-5ccf-4387-bcfe-8d5befcd8ab7.jpeg">
</p>
<p align="center">
Figura 15. Ploteo de la señal en Python manteniendo la respiración por 10 segundos FFT.
</p> 

     c)   Reposo basal
En la interpretación de la señal en el reposo basal tras la respiración se puede observar una onda P superior al estado basal por lo que se puede deducir que en este caso existe una mayor despolarización auricular indicando mayor movimiento en estas cavidades debido a la recepción de sangre por parte del corazón. Posteriormente observamos una mayor amplitud entre los picos R y S dentro del complejo QRS lo que indicaría que existiría una mayor actividad en las ventriculas esto debido al mayor volumen de sangre que habían recibido las aurículas previamente antes de pasar por las válvulas. Por último, también son visibles las ondas T teniendo una alta actividad debido a la gran actividad llevada a cabo por los ventrículos previamente [5]  
<p align="center">
     <img width="500" height="300" src="https://user-images.githubusercontent.com/55772705/231618112-00da6811-468e-44a0-b59b-3a21ff3e670c.jpeg">
</p>
<p align="center">
Figura 16. Ploteo de la señal en Python en reposo basal
</p>     
     
  
     d)   Después de una actividad física
El aumento de frecuencia cardiaca debido al ejercicio físico desencadena cambios en la señal ECG como una mayor amplitud de la onda Q, disminución del intervalo RR, ondas T altas y puntiagudas, superposición de ondas P y ondas T [7].
<p align="center">
     <img width="500" height="300" src="https://user-images.githubusercontent.com/55772705/231612958-916cd9ab-8c21-4a5a-b14c-873c48aaed8d.jpeg">
</p>
<p align="center">
Figura 17. Ploteo de la señal en Python después de una actividad física
</p>

<p align="center">
     <img width="500" height="300" src="https://user-images.githubusercontent.com/55772705/231613142-dc8be0b0-f355-47f7-a7de-9e24b72ab6c3.jpeg">
</p>
<p align="center">
Figura 18. Ploteo de la señal en Python después de una actividad física
</p>
   
  
<p align="center">
<img width="500" height="300" src="https://user-images.githubusercontent.com/55772705/231654949-05231391-82a7-4dbd-87be-86b448262199.jpeg">
</p>
<p align="center">
Figura 19. Ploteo de la señal en Python despues de una actividad física FFT.
</p> 


      e)Simulacion
En la simulación del ejercicio son visibles la mayoría de segmentos y ondas de los dos estados anteriores, sin embargo, en este es visible, además de la falta de ruido, existe una menor diferencia entre los picos R y el  S dentro del complejo QRS en comparación a los datos obtenidos de la voluntaria en cuyo caso la diferencia es mucho mayor. También se puede notar una bastante visible y prolongada, que va de acuerdo a los altos picos dentro del segmento QRS. [5]
<p align="center">
     <img width="500" height="300" src="https://user-images.githubusercontent.com/55772705/231618251-0bdaa1b1-8cef-4617-b91a-030c0d1a37d3.jpeg">
</p>
<p align="center">
Figura 20. Ploteo de la simulación.
</p>

<p align="center">
<img width="500" height="300" src="https://user-images.githubusercontent.com/55772705/231655079-c854059d-2adf-4521-9d37-49811f2a2b9b.jpeg">
</p>
<p align="center">
Figura 21. Ploteo de la señal en Python de la simulación FFT.
</p> 

## Analisis de las gráficas FFT 
Las gráficas de FFT obtenidas experimentalmente (estado de reposo, respiración profunda y post ejercicio) son muy similares entre sí. Sin embargo, al compararlas con el simulador se puede observar la diferencia en el rango inicial del espectro. Aproximadamente, entre 0-25 Hz. Se ha comprobado que esta respuesta a la frecuencia es la que se debería obtener al filtrar la señal de forma correcta. Artículos indican que la forma de la densidad espectral es similar. Como se puede observar en la tercera gráfica, en la que se realizó un estudio acerca de la fft de la señal ECG en la primera derivación (DI).

<p align="center">
<img width="500" height="300" src="https://user-images.githubusercontent.com/55772705/231656084-6ae8dd1b-83f4-4a09-a60f-dd0eefe56aad.PNG">
</p>
<p align="center">
Figura 22. Representación de la densidad espectral de Potencia en DI [9].
</p> 

## **Resultados con Ultracortex** <a name="id10"></a>

## **Conexión usada** <a name="id11"></a>

## **Video de la señal** <a name="id12"></a>

## **Ploteo de la señal en OpenBCI** <a name="id13"></a>

## **Archivos** <a name="id14"></a>

## **Ploteo de la señal en Python** <a name="id15"></a>

## **Conclusiones** <a name="id16"></a>
-1) Estado de reposo: 
Se puede observar que la grafica obtenida de la simulacion y la parte experimental son parecidas ,por lo que se estima que el rango del valor del la frecuencia cardiaca de la persona estudiada esta en el rango normal de 60 a 100 lpm,el cual es el valor de una persona sana.Asi mismo el desempeño de la tarea el ritmo cardiaco se regularizaba significativamente de acuerdo a los valores obtenidos en condiciones de reposo.
</p>
-2)Estado de respiracion profunda:
Durante la respiración la morfología del latido esta influencia por dos mecanismos ,los cambios en la impedancia torácica y la orientación del eje eléctrico del corazón con respecto a los electrodos ECG,por lo la frecuencia cardiaca está en el rango de 60-100 lpm y la frecuencia respiratoria está en el rango de 15 -60 respiraciones por minuto.Por lo cual se debe apreciar un cambio en el espectro obtenido ,lo cual sucede en el segundo 40 ,ya que se puede apreciar en la gráfica un descenso cuando la persona empieza a tomar aire y lo contiene y hay un aumento cuando ella libera el oxígeno y vuelve a la respiración continua.

</p>
-3)Estado despues de la actividad fisica:
En este caso las frecuencia cardiacas de interés son la frecuencia cardiaca máxima y la frecuencia cardiaca mínima,ya que se puede corroborar con la primera el reflejo del trabajo anaeróbico producido por el ejercicio realizado.De igual forma ocurre con la frecuencia mínima,ya que está debe estar en los valores del intervalo de recuperación ,del estado basal.En este caso se obtuvo una cambio notorio en la amplitud de los picos de las señal obtenida en el estado de actividad física  teniendo un valor alrededor de 615 como máximo y mínimo de 350, lo cual supera los valores del estado de reposo que fueron de  570 como maximo y minimo de 360.

## **Referencias** <a name="id17"></a>
----

