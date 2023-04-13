# **LABORATORIO 4: – Uso de BiTalino para EMG y ECG**
Realizado el 12 de abril de 2023
<p align="center">
     <img width="500" height="300" src="https://i0.wp.com/prevencionsaludproactiv.com/wp-content/uploads/2019/02/723563_orig.gif?resize=620%2C324&ssl=1">
</p>

# **Tabla de contenidos**
1. [Introducción](#id0)
2. [Objetivos](#id1)
3. [Materiales y equipos](#id2)
4. [Procedimiento](#id3)
5. [Resultados](#id4)\
     4.1 [Conexión usada](#id5)\
     4.2 [Video de la señal](#id6)\
     4.3 [Ploteo de la señal en OpenSignal](#id7)\
     4.4 [Archivos](#id8)\
     4.5 [Ploteo de la señal en Python](#id9)
6. [Conclusiones](#id10)
7. [Referencias](#id11)

## **Introducción al laboratorio** <a name="id0"></a>
---
<p align="justify">
El electrocardiograma (ECG) es un procedimiento simple, indoloro y rápido que registra la actividad eléctrica que realiza el corazón. [1] Para que la toma de las señales se de en las mejores condiciones posibles el paciente no debería hacer ejercicio ni tomar agua fría previo; ya que, ello puede generar datos erróneos [2], afectando la detección de anomalías, como:
</p>

- Infarto al miocardio previo
- Ritmo cardíaco anómalo (arritmia)
- Aporte inadecuado de sangre y oxígeno al corazón (isquemia)
- Engrosamiento excesivo de las paredes del músculo del corazón (hipertrofia) [1]
<p align="center">
     <img width="500" height="300" src="https://user-images.githubusercontent.com/89707896/231624436-12893b5c-e62a-44d9-b5b8-714867acc55d.png">
</p>
<p align="center">
Figura 1. ECG con anomalías [3]
</p>

<p align="justify">
Como se aprecia a la derecha la señal está conformada por ondas con picos, los cuales presentan 3 segmentos:
</p>

- Onda P: Representa la despolarización auricular.
- <p align="justify"> Intervalo QRS: Este conjunto de ondas representan la despolarización ventricular, donde la onda Q corresponde a la despolarización del tabique intraventricular; la R refleja la despolarización con la masa principal de los ventrículos; y la onda S muestra la despolarización final de los ventrículos, en la base del corazón.</p>
- Onda T: Representa la repolarización ventricular. [4]

<p align="center">
     <img width="600" height="400" src="https://user-images.githubusercontent.com/89707896/231624484-29bb445b-f900-44dc-813e-313048c5e51c.png">
</p>
<p align="center">
Figura 2. Onda ECG con sus características generales [4]
</p>

<p align="justify">
Para poder realizar estas mediciones, en el presente laboratorio, se empleó la placa de desarrollo BiTalino, la cual es una herramienta que permite registrar y analizar la actividad eléctrica de diversas zonas del cuerpo, entre ellas la del corazón, sin la necesidad de ser invasiva y permitiendo obtener resultados en tiempo real.
</p>

## ¿Cómo interpretar el ECG?
<p align="justify">Para interpretar la señal correspondiente a la actividad eléctrica se verifica que cada onda encaje con características propias de lo estandarizado como "normal":</p>
- Verificación de la onda P
     - El intervalo normal es de 0.12 a 0.22 segundos, siendo el límite superior de referencia de 0.20 segundos en adultos jóvenes
     - Si el intervalo supera los 0.22 segundos ello es compatible con un bloqueo AV de primer grado.
     - Si el intervalo es menor a los 0.12 segundos se muestra la presencia de una vía accesoria.
<p align="center">
     <img width="600" height="400" src="https://user-images.githubusercontent.com/89707896/231641526-d6332f48-6716-4be5-9d4c-ed7c9ae295c5.png">
</p>
<p align="center">
Figura 3. Onda P normal [4]
</p>

- Verificación del intervalo PR:
     - Es positiva en las derivaciones aVL, aVF, -aVR, I, V4, V5 y V6; pero negativo en aVR.
     - La deflexión negatifa es normalmente < 1 mm.
     - La duración de la onda P debe ser menor o igual a 0.12 segundos.
     - La amplitud de la onda P debe ser < 2.5 mm en las derivaciones de las extremidades.
<p align="center">
     <img width="700" height="200" src="https://user-images.githubusercontent.com/89707896/231639903-7d6e72e1-c4d4-454f-be24-cfa87fe27aea.png">
</p>
<p align="center">
Figura 4. Intervalo PR normal, prolongado y acortado [4]
</p>

- Complicaciones del complejo QRS:
     - La prolongación implica que la despolarización ventricular es más lenta del rango normal, < 0.12 s, si se excede a ello se denomina que el complejo es anormalmente ancho, considerándose como sus causas:
          - Bloqueo de la rama del haz
          - Hiperpotasemia
          - Medicamentos arrítmicos de clase I, antidepresivos tricíclicos, entre otros
          - Preexitación (Síndrome de Wolf-Parkinson-White)
          - Ritmo ventricular, ectopia ventricular y marcapasos con estimulación ventricular
          - Conducción ventricular aberrante
<p align="center">
     <img width="700" height="200" src="https://user-images.githubusercontent.com/89707896/231642861-8e227c7d-0287-4140-a98d-e869829e868b.png">
</p>
<p align="center">
Figura 5. Complejo QRS normal y prolongado [4]
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

|  **Imagen**  | **Dispositivo** | **Cantidad** |
|:------------:|:---------------:|:------------:|
| <img width="200" height="100" src="https://i.postimg.cc/VvLXqb8P/14022-01a.jpg"> |   Kit BITalino  |       1      |
| <img width="200" height="100" src="https://i.postimg.cc/XNmdLX3Z/equipos.png"> |      Laptop     |       1      |
</div>



## **Procedimiento** <a name="id3"></a>


 
## **Resultados** <a name="id4"></a>
---

### **Conexión usada** <a name="id5"></a>
#

Se posicionaron los electrodos en base las guías mencionadas:
<p align="center"><img src="https://user-images.githubusercontent.com/89707896/231556282-5514bddb-7edd-44c2-b25a-eff7b03f8c3e.png" width="300" height="200"></p>
<p align="center">Figura 6. Posición de los electrodos según la guía.    
<p align="center"><img src="https://user-images.githubusercontent.com/89707896/231556405-814106b1-2997-4640-9138-44929aaa6f14.jpeg" width="300" height="300"></p>
<p align="center">Figura 7. Conexión con el Bitalino.</p>
     
### **Videos de la señal** <a name="id6"></a>
#
| Estado Basal | Mantener la respiración por 10 segundos |
| ------------ |  :------------------------------------: |
| <video src="https://user-images.githubusercontent.com/89707896/231572641-61aeebae-f397-4627-aebc-913bb9464915.mp4" width="200" /> | <video src="https://user-images.githubusercontent.com/89707896/231574043-44222491-d595-4d5a-9ac8-112adb20757c.mp4" width="200" /> |
</div>

| Reposo Basal |     Después de una actividad física     |
| ------------ |  :------------------------------------: |
|<video src="https://user-images.githubusercontent.com/89707896/231574106-c6608652-e7dd-4194-b84f-53ea09ec712c.mp4" width="200"/> | <video src="https://user-images.githubusercontent.com/89707896/231574355-354b84ab-f131-4c7e-962c-d6c0341358ed.mp4" width="200" />  |
</div>


### **Ploteo de la señal en OpenSignal** <a name="id7"></a>
#
     a)   Estado basal
<p align="center">
     <img width="500" height="300" src="https://user-images.githubusercontent.com/55772705/231611835-3ffa0a24-5e16-4ac8-97a3-a59e8c0362e2.PNG">
</p>
<p align="center">Figura 8. Info [Elaborado propia]</p>     
     
     b)   Manteniendo la respiración por 10 segundos
<p align="center">
     <img width="500" height="300" src="https://user-images.githubusercontent.com/55772705/231611939-2b79e311-fdce-487c-83f6-f0a795c2cbdf.PNG">
</p>
<p align="center">Figura 9. Info [Elaborado propia]</p>

     
     c)   Reposo basal
<p align="center">
     <img width="500" height="300" src="https://user-images.githubusercontent.com/55772705/231611469-d7964526-ec59-44d6-ac3c-6fef92f0ee56.jpeg">
</p>
<p align="center">Figura 10. Info [Elaborado propia]</p>


     d)   Después de una actividad física
<p align="center">
     <img width="500" height="300" src="https://user-images.githubusercontent.com/55772705/231612030-69c201ca-2f29-4105-8a93-d0597b2e2084.PNG">
</p>
<p align="center">Figura 11. Info [Elaborado propia]</p>

     
     e)  Simulacion 
<div align="center">
     
     
| Paso 1 | Paso 2 |
| --- |  :---: |
| <img width="500" height="300" src="https://user-images.githubusercontent.com/55772705/231613380-bc4d1eea-9a53-4a95-bbf3-8b3c3bdf9f80.jpeg"> | <img width="500" height="300" src="https://user-images.githubusercontent.com/55772705/231613426-d45de00e-70c8-4039-ac58-63dbafafc010.jpeg"> |

| Paso 3 | Paso 4 |
| --- |  :---: |     
| <img width="500" height="300" src="https://user-images.githubusercontent.com/55772705/231613472-04e57e10-6166-4e07-8003-f49d39aedff1.jpeg"> | <img width="500" height="300" src="https://user-images.githubusercontent.com/55772705/231613509-5cf80abe-d415-4e6e-a7e5-8639b53577d6.jpeg"> |
     
| Paso 5 | Paso 6 |
| --- |  :---: |     
| <img width="500" height="300" src="https://user-images.githubusercontent.com/55772705/231613554-b43c19d7-3913-409f-a09c-b13a39376668.jpeg"> | <img width="500" height="300" src="https://user-images.githubusercontent.com/55772705/231613604-e7f6adeb-2bd4-42c0-a769-8ee06ff7e381.jpeg"> |
</div>

### **Archivos** <a name="id8"></a>
#
### **Ploteo de la señal en Python** <a name="id9"></a>
#
     a)   Estado basal
<p align="center">
     <img width="500" height="300" src="https://user-images.githubusercontent.com/55772705/231612373-866789aa-8ddd-477b-8046-dcdd2fb0a006.jpeg">
</p>
<p align="center">Figura 12. Info [Elaborado propia]</p>    


     b)   Manteniendo la respiración por 10 segundos
<p align="center">
     <img width="500" height="300" src="https://user-images.githubusercontent.com/55772705/231612494-7170cc27-7967-43cf-8a9a-4b9723d330b5.jpeg">
</p>
<p align="center">Figura 13. Info [Elaborado propia]</p>         


     c)   Reposo basal
<p align="center">
     <img width="500" height="300" src="https://user-images.githubusercontent.com/55772705/231618112-00da6811-468e-44a0-b59b-3a21ff3e670c.jpeg">
</p>
<p align="center">Figura 14. Info [Elaborado propia]</p>    

  
     d)   Después de una actividad física
<p align="center">
     <img width="500" height="300" src="https://user-images.githubusercontent.com/55772705/231612958-916cd9ab-8c21-4a5a-b14c-873c48aaed8d.jpeg">
</p>
<p align="center">Figura 15. Info [Elaborado propia]</p>  

<p align="center">
     <img width="500" height="300" src="https://user-images.githubusercontent.com/55772705/231613142-dc8be0b0-f355-47f7-a7de-9e24b72ab6c3.jpeg">
</p>
<p align="center">Figura 16. Info [Elaborado propia]</p>  

      e)simulacion
<p align="center">
     <img width="500" height="300" src="https://user-images.githubusercontent.com/55772705/231618251-0bdaa1b1-8cef-4617-b91a-030c0d1a37d3.jpeg">
</p>
<p align="center">Figura 17. Info [Elaborado propiao]</p>  



## **Conclusiones** <a name="id10"></a>
---
## **Referencias** <a name="id11"></a>
---
1. Electrocardiograma. (2023, 28 de febrero). MedlinePlus. https://medlineplus.gov/spanish/pruebas-de-laboratorio/electrocardiograma/#:~:text=Un%20electrocardiograma%20(ECG)%20es%20un,circula%20a%20través%20de%20él.
2. Electrocardiograma: MedlinePlus enciclopedia mÃ©dica. (2022, 5 de agosto). MedlinePlus - Health Information from the National Library of Medicine. https://medlineplus.gov/spanish/ency/article/003868.htm#:~:text=No%20haga%20ejercicio%20ni%20tome,acciones%20pueden%20causar%20resultados%20falsos.
3. Cascino, T., & Shea, M. J. (2021, 6 de julio). Electrocardiografía - Trastornos del corazón y los vasos sanguíneos - Manual MSD versión para público general. Manual MSD versión para público general. https://www.msdmanuals.com/es-es/hogar/trastornos-del-corazón-y-los-vasos-sanguíneos/diagnóstico-de-las-enfermedades-cardiovasculares/electrocardiografía#:~:text=En%20un%20ECG%20pueden%20observarse,las%20pareces%20del%20músculo%20cardíaco.
4. ECG interpretation: Characteristics of the normal ECG (P-wave, QRS complex, ST segment, T-wave). (2019). ECG & ECHO. https://ecgwaves.com/topic/ecg-normal-p-wave-qrs-complex-st-segment-t-wave-j-point/
