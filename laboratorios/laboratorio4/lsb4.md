# **LABORATORIO 4: – Uso de BiTalino para EMG y ECG**
Realizado el 12 de abril de 2023


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
El electrocardiograma (ECG) es un procedimiento simple, indoloro y rápido que registra la actividad eléctrica que realiza el corazón. Para que la toma de las señales se de en las mejores condiciones posibles el paciente no debería hacer ejercicio ni tomar agua fría previo; ya que, ello puede generar datos erróneos, afectando la detección de anomalías, como:
</p>

- Infarto al miocardio previo
- Ritmo cardíaco anómalo (arritmia)
- Aporte inadecuado de sangre y oxígeno al corazón (isquemia)
- Engrosamiento excesivo de las paredes del músculo del corazón (hipertrofia)
<p align="center">
     <img width="500" height="300" src="https://user-images.githubusercontent.com/89707896/231624436-12893b5c-e62a-44d9-b5b8-714867acc55d.png">
</p>
<p align="center">
Figura 1. ECG con anomalías
</p>

<p align="justify">
Como se aprecia a la derecha la señal está conformada por ondas con picos, los cuales presentan 3 segmentos:
</p>

- Onda P: Representa la despolarización auricular.
- <p align="justify"> Intervalo QRS: Este conjunto de ondas representan la despolarización ventricular, donde la onda Q corresponde a la despolarización del tabique intraventricular; la R refleja la despolarización con la masa principal de los ventrículos; y la onda S muestra la despolarización final de los ventrículos, en la base del corazón.</p>
- Onda T: Representa la repolarización ventricular.

<p align="center">
     <img width="600" height="400" src="https://user-images.githubusercontent.com/89707896/231624484-29bb445b-f900-44dc-813e-313048c5e51c.png">
</p>
<p align="center">
Figura 2. Onda ECG con sus características generales
</p>

<p align="justify">
Para poder realizar estas mediciones, en el presente laboratorio, se empleó la placa de desarrollo BiTalino, la cual es una herramienta que permite registrar y analizar la actividad eléctrica de diversas zonas del cuerpo, entre ellas la del corazón, sin la necesidad de ser invasiva y permitiendo obtener resultados en tiempo real.
</p>


## **Objetivos** <a name="id1"></a>
---
Los objetivos del laboratorio son:
* Adquirir señales biomédicas de ECG.
* Hacer una correcta configuración de BiTalino.
* Extraer la información de las señales ECG del software OpenSignals (r)evolution 


## **Materiales y equipos** 

---
<div align="center">

|  **Modelo**  | **Descripción** | **Cantidad** |
|:------------:|:---------------:|:------------:|
| (R)EVOLUTION |   Kit BITalino  |       1      |
|       -      |      Laptop     |       1      |

</div>

<p align="justify">
<p align="center"><img src="https://i.postimg.cc/XNmdLX3Z/equipos.png" width="400" height="266"></p>
</p>


## **Procedimiento** <a name="id3"></a>


 
## **Resultados** <a name="id4"></a>
---

### **Conexión usada** <a name="id5"></a>
#

Se posicionaron los electrodos en base las guías mencionadas:
<p align="center"><img src="https://user-images.githubusercontent.com/89707896/231556282-5514bddb-7edd-44c2-b25a-eff7b03f8c3e.png" width="500" height="200"></p>
<p align="center">Figura 1. Posición de los electrodos según la guía.

<p align="center"><img src="https://user-images.githubusercontent.com/89707896/231556405-814106b1-2997-4640-9138-44929aaa6f14.jpeg" width="400" height="400"></p>
<p align="center">Figura 2. Conexión con el Bitalino.
     
### **Video de la señal** <a name="id6"></a>
#
***Estado basal***
     <div align="center">
          <video src="https://user-images.githubusercontent.com/89707896/231572641-61aeebae-f397-4627-aebc-913bb9464915.mp4" width="400" />
     </div>

***Manteniendo la respiración por 10 segundos***
     <div align="center">
          <video src="https://user-images.githubusercontent.com/89707896/231574043-44222491-d595-4d5a-9ac8-112adb20757c.mp4" width="400" />
     </div>

***Reposo basal***
     <div align="center">
          <video src="https://user-images.githubusercontent.com/89707896/231574106-c6608652-e7dd-4194-b84f-53ea09ec712c.mp4" width="400" />
     </div>

***Después de una actividad física***
     <div align="center">
          <video src="https://user-images.githubusercontent.com/89707896/231574355-354b84ab-f131-4c7e-962c-d6c0341358ed.mp4" width="400" />
     </div>

### **Ploteo de la señal en OpenSignal** <a name="id7"></a>
#
     a)   Estado basal
     
   
![basal](https://user-images.githubusercontent.com/55772705/231611835-3ffa0a24-5e16-4ac8-97a3-a59e8c0362e2.PNG)
<p align="center">Figura 3.Estado basal.
     </div>
     b)   Manteniendo la respiración por 10 segundos
     
  
![res](https://user-images.githubusercontent.com/55772705/231611939-2b79e311-fdce-487c-83f6-f0a795c2cbdf.PNG)

<p align="center">Figura 4.Manteniendo la respiración por 10 segundos.
     </div>
     c)   Reposo basal
     
  ![WhatsApp Image 2023-04-12 at 1 09 27 PM](https://user-images.githubusercontent.com/55772705/231611469-d7964526-ec59-44d6-ac3c-6fef92f0ee56.jpeg)
<p align="center">Figura 5.Reposo basal.
</div>

     d)   Después de una actividad física
     

![ejercicio](https://user-images.githubusercontent.com/55772705/231612030-69c201ca-2f29-4105-8a93-d0597b2e2084.PNG)
<p align="center">Figura 6.Después de una actividad física.
     
</div>
     
     e)  Simulacion 
     
  

| Figura | Pasos de la simulación|
| --- |  :---: |
| ![WhatsApp Image 2023-04-12 at 1 10 23 PM](https://user-images.githubusercontent.com/55772705/231613380-bc4d1eea-9a53-4a95-bbf3-8b3c3bdf9f80.jpeg) | 1 |
|  ![WhatsApp Image 2023-04-12 at 1 10 23 PM (1)](https://user-images.githubusercontent.com/55772705/231613426-d45de00e-70c8-4039-ac58-63dbafafc010.jpeg)| 2 |
|![WhatsApp Image 2023-04-12 at 1 10 24 PM](https://user-images.githubusercontent.com/55772705/231613472-04e57e10-6166-4e07-8003-f49d39aedff1.jpeg)  | 3 |
| ![WhatsApp Image 2023-04-12 at 1 10 24 PM (1)](https://user-images.githubusercontent.com/55772705/231613509-5cf80abe-d415-4e6e-a7e5-8639b53577d6.jpeg) | 4 |
| ![WhatsApp Image 2023-04-12 at 1 10 24 PM (2)](https://user-images.githubusercontent.com/55772705/231613554-b43c19d7-3913-409f-a09c-b13a39376668.jpeg) | 5 |
| ![WhatsApp Image 2023-04-12 at 1 10 24 PM (3)](https://user-images.githubusercontent.com/55772705/231613604-e7f6adeb-2bd4-42c0-a769-8ee06ff7e381.jpeg) | 6 |
</div>

### **Archivos** <a name="id8"></a>
#
### **Ploteo de la señal en Python** <a name="id9"></a>
#
     a)   Estado basal
  ![WhatsApp Image 2023-04-12 at 12 28 37 PM](https://user-images.githubusercontent.com/55772705/231612373-866789aa-8ddd-477b-8046-dcdd2fb0a006.jpeg)


     b)   Manteniendo la respiración por 10 segundos
     
    
![WhatsApp Image 2023-04-12 at 12 19 35 PM](https://user-images.githubusercontent.com/55772705/231612494-7170cc27-7967-43cf-8a9a-4b9723d330b5.jpeg)


     c)   Reposo basal
     
![WhatsApp Image 2023-04-12 at 7 33 53 PM](https://user-images.githubusercontent.com/55772705/231618112-00da6811-468e-44a0-b59b-3a21ff3e670c.jpeg)


  
     d)   Después de una actividad física
     
  ![WhatsApp Image 2023-04-12 at 12 25 26 PM](https://user-images.githubusercontent.com/55772705/231612958-916cd9ab-8c21-4a5a-b14c-873c48aaed8d.jpeg)

![WhatsApp Image 2023-04-12 at 12 41 58 PM](https://user-images.githubusercontent.com/55772705/231613142-dc8be0b0-f355-47f7-a7de-9e24b72ab6c3.jpeg)

      e)simulacion
      
   
![WhatsApp Image 2023-04-12 at 7 35 38 PM](https://user-images.githubusercontent.com/55772705/231618251-0bdaa1b1-8cef-4617-b91a-030c0d1a37d3.jpeg)



## **Conclusiones** <a name="id10"></a>
---
## **Referencias** <a name="id11"></a>
---

