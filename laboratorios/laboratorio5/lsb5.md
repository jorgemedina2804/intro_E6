# **LABORATORIO 5: – Uso de Ultracortex y BiTalino para EEG**
Realizado el 19 de abril de 2023
<p align="center">
     <img width="500" height="300" src="https://images.squarespace-cdn.com/content/v1/5f7b55a801226812a44f7180/1609441748072-S5NU5R5YSQF4LYBO7KZT/OpenBCI-WebXR-EEG.gif">
     <img width="500" height="300" src="https://user-images.githubusercontent.com/17307/31218894-586281e4-a9c4-11e7-81d8-bd6f3dfd4267.gif">
</p>

# **Tabla de contenidos**
1. [Introducción](#id0)
2. [Encefalograma](#id1)
3. [Objetivos](#id2)
4. [Materiales y equipos](#id3)
5. [Procedimiento](#id4)
6. [Resultados con BiTalino](#id5)\
     6.1 [Conexión usada](#id6)\
     6.2 [Videos de la señal](#id7)\
     6.3 [Ploteo de la señal en OpenSignal](#id8)\
     6.4 [Ploteo de la señal en Python](#id9)\
     6.5 [Archivos](#id10)

7. [Resultados con Ultracortex](#id11)\
     7.1 [Conexión usada](#id12)\
     7.2 [Videos de la señal](#id13)\
     7.3 [Ploteo de la señal en OpenBCI](#id14)\
     7.4 [Ploteo de la señal en Python](#id15)\
     7.5 [Archivos](#id16)
8. [Conclusiones](#id17)
9. [Referencias](#id18)

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
- FP: Frontal anterior
- T: Temporal
- C: Central
- P: Parietal
- O: Occipital
- A: Oreja o apófisis mastoides
- Z: Línea media

<p align="center">
     <img width="350" height="350" src="https://user-images.githubusercontent.com/89707896/233396071-6689f779-04d9-4820-a29f-eb8e542779c2.png">
</p>
<p align="center">
Figura 2. Posicionamiento de los electrodos en base al Sistema Internacional de Posicionamiento 10/20 [4]
</p>

<p align="justify">
Para poder realizar estas mediciones, en el presente laboratorio, se empleó la placa de desarrollo BiTalino y el Ultracortex EEG Headset, los cuales son herramientas que permiten registrar y analizar la actividad eléctrica de diversas zonas del cuerpo, entre ellas la del cerebro, sin la necesidad de ser invasiva y permitiendo obtener resultados en tiempo real.
</p>

## **Encefalograma** <a name="id1"></a>
---
### Tipos de ondas cerebrales
<p align="justify">
Las neuronas se comunican entre ellas a través de pequeños impulsos eléctricos que se pueden medir. A esto le llamamos ondas cerebrales. Estas ondas tienen diferentes tipos de frecuencia, unas son más rápidas y otras más lentas. Si se separan a través de filtros, las podemos observar con más claridad.

Para ello deberemos realizar un Electroencefalograma (EEG) registrando la actividad eléctrica cerebral mediante unos sensores colocados en el cuero cabelludo que permiten ver estos potenciales eléctricos en forma de ondas.

La frecuencia de las ondas cerebrales se mide en ciclos por segundo o Hertz (Hz). La corriente eléctrica en Europa tiene una frecuencia de 50 Hz, es decir, cada segundo tiene 50 ciclos. [5]
</p>
<p align="center">
     <img width="500" height="400" src="https://user-images.githubusercontent.com/89707896/233399122-3aadc67c-1394-4a74-a4cc-42378bf65795.png">
</p>
<p align="center">
Tabla 1.Descripción de los tipos de ondas cerebrales [6]
</p>
<p align="center">
     <img width="500" height="400" src="https://user-images.githubusercontent.com/89707896/233401548-81492942-6ee3-4516-a577-19b9b98b5840.png">
</p>
<p align="center">
Figura 3.Ondas cerebrales.[7]
</p>

### Topologías de medición de EEG
<p align="justify">
Dependiendo de la configuración del montaje de los electrodos, se puede distinguir en tres tipologías diferentes: 

- Monopolar: Se registra la diferencia de potencial entre los electrodos ubicados en las zonas de interés y un electrodo de referencia. El electrodo de referencia generalmente se coloca en la oreja. [8] 
- Bipolar: Se sitúan los electrodos sobre las diferentes zonas de interés y se adquieren diferencias de potenciales entre estos puntos. [8]
- Laplaciana: Al igual que la configuración monopolar, se adquieren las diferencias de potenciales entre los electrodos de interés, o activos, y un valor de referencia; sin embargo en este caso la referencia es el promedio de varios electrodos situados alrededor del electrodo activo. [8]
</p>


## **Objetivos** <a name="id2"></a>
---
Los objetivos del laboratorio son:
* Adquirir señales biomédicas de EEG.
* Hacer una correcta configuración de BiTalino y Ultracortex.
* Extraer la información de las señales EEG del software OpenSignals (r)evolution y OpenBCI GUI


## **Materiales y equipos** <a name="id3"></a>

---
<div align="center">

|  **Imagen**  | **Producto** | **Cantidad** |
|:------------:|:---------------:|:------------:|
| <img width="200" height="150" src="https://i.postimg.cc/VvLXqb8P/14022-01a.jpg"> |   Kit BITalino  |       1      |
| <img width="200" height="150" src="https://user-images.githubusercontent.com/89707896/233160701-4bf7cd35-220c-4483-8847-bb7abb28feb1.png"> |   Ultracortex Mark IV EEG Headset  |       1      |
| <img width="200" height="150" src="https://cdn.shopify.com/s/files/1/0613/9353/products/DSC02779_1445x.jpg?v=1614761059"> |   OpenBCI Cyton 8-channel Board  |       1      |
| <img width="200" height="150" src="https://i.postimg.cc/XNmdLX3Z/equipos.png"> |      Laptop     |       1      |
| <img width="200" height="150" src="https://www.mevesur.com/6039-large_default/electrodo-ecg-alta-adhesividad-meditrace-530-foam-bolsa-30-600-unidades.jpg"> |      Electrodos pediátricos con gel    |       3     |

</div>



## **Procedimiento** <a name="id4"></a>
<p align="justify">
Para la conexión electrodos al cuerpo utilizamos la guía proporcionada por el propio Bitalino de nombre: "BITalino HOME-GUIDE #3 ELECTROencephaloGRAPHY (EEG) Exploring Brain Signals".
</p>

Registro de la señal EEG: Se grabó la señal en 5 momentos
- Bitalino: 
     - Con los ojos cerrados por 30 segundos
     - Con los ojos abiertos
     - Con los ojos abiertos y luz
     - Tras realizar un ejercicio complejo
     - Tras realizar un problema matemático

- Ultracortex: 
     - Con los ojos cerrados
     - Con los ojos abiertos y cerrados cada 5 segundos
     - Descanso de 30 segundos
     - Tras realizar un problema matemático
     - Tras realizar un ejercicio simple
     
### Adquisición y medición de señal EEG con OpenBCI
Sensor EEG
<p align="justify">
Cuyo esquemático podemos ver la figura x,está diseñado con una configuración bipolar que le permite tomar como valor de referencia un electrodo para obtener la diferencia de señal entre esta y la tomada con otro electrodo,eliminando las señales sin importancia para el posterior procesado. [9] </p>
<p align="center">
     <img width="800" height="500" src="https://user-images.githubusercontent.com/89707896/233418088-fb835b67-191a-4213-892c-ae365f3fd1de.png">
</p>
<p align="center">
Figura 4 .Ubicación del sensor EEG en la placa Bitalino[10].
</p>


### Protocolo de adquisición
La adquisición por medio del sensor EEG y los electrodos
<p align="justify">
La adquisición de esta señal se hará mediante el cable de tres electrodos,el cual uno de ellos será tomado como tierra.Debido a esto,vamos a colocar el electrodo de toma de tierra en el hueso detrás de la oreja y los dos restantes en ambos lados de la cabeza,tal como se muestra en la figura X,cabe resaltar que es muy importante para la toma de esta señal estar muy relajado ya que ,sino la señal se satura debido a la gran ganancia que tiene este sensor. [9]
</p>
<p align="center">
     <img width="400" height="300" src="https://user-images.githubusercontent.com/89707896/233419747-c0a71b2c-b120-4820-bcde-b9dd66fe984a.png">
</p>
<p align="center">
Figura 5.Posicionamiento de los electrodos para la adquisición de la señal EEG según la guía Bitalino (r)evolution. [11]
</p>

La adquisición de datos mediante el software
<p align="justify">
La adquisición de los datos se da mediante el software OpenSignal ,el cual será conectado al equipo de Bitalino por vía bluetooth.Dentro del sistema se realizarán las especificaciones como el tipo de frecuencia a utilizar(1000Hz) y el canal que se activara (canal 4).Finalmente se iniciara con la toma de datos.
En este laboratorio se realizaron las siguientes:
- Registrar una línea base de señal con poco ruido y sin movimientos (respiración normal,sin movimientos oculares/ojos cerrados) durante 30 segundos.

- Repetir un ciclo de OJOS ABIERTOS - OJOS CERRADOS cinco veces, manteniendo ambas fases durante cinco segundos.

- Registre otra fase de referencia de 30 segundos.

- Que uno de tus compañeros lea en voz alta una serie de ejercicios matemáticos y resuelva cada uno de ellos mentalmente enfocando tu mirada en un punto específico para evitar artefactos.
</p>
<p align="center">
     <img width="1000" height="300" src="https://user-images.githubusercontent.com/89707896/233421138-b8e7e98a-5e46-4411-8a20-01abe463811a.png">
</p>
<p align="center">
Figura 6.Lista de problemas para la última prueba.[12]
</p>
</p>

## **Resultados con BiTalino** <a name="id5"></a>
---
### **Conexión usada** <a name="id6"></a>
<p align="justify">
Colocar su sensor BITalino EEG ensamblado es la posición FP2 en la frente (sobre su ojo derecho) y en la posición FP1  (sobre su ojo izquierdo) de acuerdo con el sistema internacional 10-20, vea la Figura 7. Usando esta configuración, puede medir la actividad de ondas beta ( nivel de pensamiento activo).ya que  en  la  región  prefrontal  se evidencian  cambios  en  el  EEG  relacionados  con  la  atención,orientación y razonamiento. [13]
</p>
<p align="center">
     <img width="400" height="300" src="https://user-images.githubusercontent.com/89707896/233426112-afffa6fe-dc1b-4654-b55d-2b4624a41456.png">
</p>
<p align="center">
Figura 7.Colocación de los electrodos positivo,negativo y de referencia de la guia bitalino. [11]
</p>

Se posicionaron los electrodos en base las guías mencionadas:
<p align="center">
     <img width="400" height="400" src="https://user-images.githubusercontent.com/89707896/233424011-2b687f7c-b9e4-4e21-8e84-8206a8eb5824.png">
     <img width="400" height="400" src="https://user-images.githubusercontent.com/89707896/233424306-f8a4ce7a-634d-4ee5-b544-55a150708315.png">
</p>
<p align="center">
Figura 8.Colocación de los electrodos positivo,negativo y de referencia en el participante según  la guía bitalino. [Elaboración propia]
</p>
</p>

     
### **Videos de la señal** <a name="id7"></a>
---
#
| Ojos cerrados | Ojos abiertos |
| ------------ |  :------------------------------------: |
| <video src="https://user-images.githubusercontent.com/89707896/233197727-682b0923-7b51-4526-8751-70370731e366.mp4" width="200" /> | <video src="https://user-images.githubusercontent.com/89707896/233197777-92d52158-9e99-42b4-be4b-fcc7c056249f.mp4" width="200" /> |
</div>

<div align="center">
Ejercicio con luz
 <video src="https://user-images.githubusercontent.com/89707896/233197893-0dfe0211-f1a8-4637-9764-13d50fc77269.mp4">
</p>

| Ejercicio complejo |     Problema matemático     |
| ------------ |  :------------------------------------: |
|<video src="" width="200"/> | <video src="" width="200" />  |
</div>
