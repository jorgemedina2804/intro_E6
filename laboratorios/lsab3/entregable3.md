
# **LABORATORIO 3: – USO DE BITalino PARA EMG**
# **Tabla de contenidos**

1. [Objetivos](#id1)
2. [Materiales y equipos](#id2)
3. [Resultados](#id3)\
     3.1 [Conexión usada](#id4)\
     3.2 [Video de la señal](#id5)\
     3.3 [Ploteo de la señal en OpenSignal](#id6)\
     3.4 [Archivos](#id7)\
     3.5 [Ploteo de la señal en Python](#id8)



## **Objetivos** <a name="id1"></a>
* Adquirir señales biomédicas de EMG de un grupo muscular especifico.
* Hacer una correcta configuración de BiTalino.
* Extraer la información de las señales EMG  del software OpenSignals (r)evolution.



## **Materiales y equipos** <a name="id2"></a>

<div align="center">

|  **Modelo**  | **Descripción** | **Cantidad** |
|:------------:|:---------------:|:------------:|
| (R)EVOLUTION |   Kit BITalino  |       1      |
|       -      |      Laptop     |       1      |

</div>

<p align="justify">
<p align="center"><img src="https://i.postimg.cc/XNmdLX3Z/equipos.png" width="400" height="266"></p>
</p>

## **RESULTADOS** <a name="id3"></a>
### **Conexión usada** <a name="id4"></a>
Se utilizó la conexión EMG en la placa Bitalino utilizando el sensor EMG de 3 electrodos como se muestra a continuación.
<p align="justify">
<p align="center"><img src="https://i.postimg.cc/43WWwtJC/Whats-App-Image-2023-04-05-at-12-04-38-PM.jpg" width="400" height="266"></p>
</p>

El siguiente procedimiento consiste en colocar los electrodos EMG en el usuario de prueba. Para ello se utilizó la **Guía De Procedimiento de Electromiografía y velocidad de conducción de nervios periféricos** del año 2020 elaborada por el **Instituto Nacional del Niño de San Borja** para el Ministerio de Salud (MINSA).

### **Video de la señal y ploteo en Opensignal** <a name="id5"></a>
### PRUEBA 1 <br>

<p align="justify">
En la prueba 1 se tomo señales del reposo y contracción del dedo pulgar, teniendo la conexión de tierra en el dorso de la mano.<br>
</p>
<p align="center"><img src="https://i.postimg.cc/kMYzy0T1/Whats-App-Image-2023-04-05-at-12-04-45-PM.jpg" width="400" height="400"></p> 
<p align="center"><img src="https://i.postimg.cc/bN2C9sDr/equipo-texto.png" width="500" height="500"></p>
<div align="center">

[<img src="https://cdn.icon-icons.com/icons2/1713/PNG/512/iconfinder-videologoplayicon-3993847_112649.png" width="20%" height="20%">](https://www.youtube.com/playlist?list=PLZDUFkiHuQKhex5qfmNXrVl5pFNnRhcRX)

</div>

### PRUEBA 2 <br>

<p align="justify">
En la prueba 2 se tomo señales del reposo y contracción del biceps, teniendo la conexión de tierra a la altura de la muñeca.<br>
</p>
<p align="center"><img src="https://i.postimg.cc/pTf8dMp2/pu-o.png" width="400" height="300"></p>

<div align="center">

[<img src="https://cdn.icon-icons.com/icons2/1713/PNG/512/iconfinder-videologoplayicon-3993847_112649.png" width="20%" height="20%">](https://www.youtube.com/playlist?list=PLZDUFkiHuQKhhKAlygeNMoSdIRdmgaqWJ)

</div>

### **Archivos** <a name="id7"></a>
- [Documentos (.txt)](https://github.com/MariaRejas/intro_E6/blob/main/laboratorios/lsab3/Se%C3%B1al%20EMG%20Lab1.txt)
- [Programa de ploteo (Jupyter Notebook)](https://github.com/Grupo2-IntroduccionSenalesMedicas/S_biomedica/blob/main/Programaci%C3%B3n/Laboratorio%203/SignalPlot.ipynb)
### **Ploteo de la señal en Python** <a name="id8"></a>
<p align="justify">
La primera prueba se realizo con el dedo pulgar en el cuál se tomaron muestras del dedo en reposo, contra fuerza y en posición de pinza con el dedo índice.
</p>
- Señal de dedo con contrafuerza:
<p align="center"><img src="/Imagenes/Bitalino/EMG_Python_dedo_contrafuerza.jpg" width="800" height="500"></p>
- Señal de dedo en posición de pinza:
<p align="center"><img src="/Imagenes/Bitalino/EMG_Python_dedo_pinza.jpg" width="800" height="500"></p>

En la segunda prueba se realizó con el biceps del brazo el cual se sometio a contra fuerza y contracción máxima.
</p>
- Señal de biceps en contracción:
<p align="center"><img src="/Imagenes/Bitalino/EMG_Python_biceps_contraccion.jpg" width="800" height="500"></p>
- Señal de biceps con contrafuerza:
<p align="center"><img src="/Imagenes/Bitalino/EMG_Python_biceps_contrafuerza.jpg" width="800" height="500"></p>

En la tercera prueba, el usuario estuvo en posición sentado y parado, y de las dos formas se sometió a contracción el músculo gastrocnemio.
</p>
- Señal de contracción del gastrocnemio en posición parado:
<p align="center"><img src="/Imagenes/Bitalino/EMG_Python_pantorrilla_parado.jpg" width="800" height="500"></p>
- Señal de contracción del gastrocnemio en posición sentado:
<p align="center"><img src="/Imagenes/Bitalino/EMG_Python_pantorrilla_sentado.jpg" width="800" height="500"></p>
