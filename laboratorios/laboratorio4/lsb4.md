# **LABORATORIO 4: – USO DE BiTalino PARA EMG y ECG**
Fecha: 12-04-2023


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

## **Objetivos** <a name="id1"></a>
---
Los objetivos del laboratorio son:
* Adquirir señales biomédicas de ECG.
* Hacer una correcta configuración de BiTalino.
* Extraer la información de las señales ECG del software OpenSignals (r)evolution 


## **Materiales y equipos** 

---


## **Procedimiento** <a name="id3"></a>


 
## **Resultados** <a name="id4"></a>
---

### **Conexión usada** <a name="id5"></a>
#

Se posicionaron los electrodos en base las guías mencionadas:
<p align="center"><img src="https://user-images.githubusercontent.com/89707896/231556282-5514bddb-7edd-44c2-b25a-eff7b03f8c3e.png" width="500" height="200"></p>
<p align="center">Figura X. Posición de los electrodos según la guía.

<p align="center"><img src="https://user-images.githubusercontent.com/89707896/231556405-814106b1-2997-4640-9138-44929aaa6f14.jpeg" width="400" height="400"></p>
<p align="center">Figura X. Conexión con el Bitalino.
     
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

     b)   Manteniendo la respiración por 10 segundos
     
  
![res](https://user-images.githubusercontent.com/55772705/231611939-2b79e311-fdce-487c-83f6-f0a795c2cbdf.PNG)


     c)   Reposo basal
     
  ![WhatsApp Image 2023-04-12 at 1 09 27 PM](https://user-images.githubusercontent.com/55772705/231611469-d7964526-ec59-44d6-ac3c-6fef92f0ee56.jpeg)


     d)   Después de una actividad física
     

![ejercicio](https://user-images.githubusercontent.com/55772705/231612030-69c201ca-2f29-4105-8a93-d0597b2e2084.PNG)

     e)  Simulacion 
     
  

| Figura | Pasos de la simulación|
| --- |  :---: |
| ![WhatsApp Image 2023-04-12 at 1 10 23 PM](https://user-images.githubusercontent.com/55772705/231613380-bc4d1eea-9a53-4a95-bbf3-8b3c3bdf9f80.jpeg) | 1 |
|  ![WhatsApp Image 2023-04-12 at 1 10 23 PM (1)](https://user-images.githubusercontent.com/55772705/231613426-d45de00e-70c8-4039-ac58-63dbafafc010.jpeg)| 2 |
|![WhatsApp Image 2023-04-12 at 1 10 24 PM](https://user-images.githubusercontent.com/55772705/231613472-04e57e10-6166-4e07-8003-f49d39aedff1.jpeg)  | 3 |
| ![WhatsApp Image 2023-04-12 at 1 10 24 PM (1)](https://user-images.githubusercontent.com/55772705/231613509-5cf80abe-d415-4e6e-a7e5-8639b53577d6.jpeg) | 4 |
| ![WhatsApp Image 2023-04-12 at 1 10 24 PM (2)](https://user-images.githubusercontent.com/55772705/231613554-b43c19d7-3913-409f-a09c-b13a39376668.jpeg) | 5 |
| ![WhatsApp Image 2023-04-12 at 1 10 24 PM (3)](https://user-images.githubusercontent.com/55772705/231613604-e7f6adeb-2bd4-42c0-a769-8ee06ff7e381.jpeg) | 6 |

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

