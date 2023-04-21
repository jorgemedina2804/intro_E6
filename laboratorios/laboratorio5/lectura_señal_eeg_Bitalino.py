import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import re

def ploteo(tiempo,señal,canal,titulo):
    X1=señal[:,canal]
    plt.plot(tiempo,X1)
    plt.title(titulo)
    plt.grid(linestyle=":")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.show()

def ploteo_acotado(tiempo,t1,t2,señal,canal,titulo):
    t_1=t1*1000
    t_2=t2*1000
    
    T1=tiempo[t_1:t_2]
    x1=señal[t_1:t_2, canal]
    
    plt.plot(T1,x1)
    plt.title(titulo)
    plt.grid(linestyle=":")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.show()

def fft(señal,title):
    N=2**10
    signal1 = señal[:,-2]

    signal_fft = np.fft.fft(signal1, N)           # fft magtinud
    signal_fft = np.round(np.abs(signal_fft),3)[0:N//2] # nos quedamos con los componente de la derecha de la FFT
    signal_aux = signal_fft/signal_fft.max()     # hallamos el maximo para pasar la magnitud a escala db

    with np.errstate(divide='ignore'):
        signal_fft_db = 10*np.log10(signal_aux)  # , out=signal_aux, where=signal_aux >= 0 para evitar division por zero

    F_list = np.linspace(0,Fs/2, N//2)
    F = np.round(F_list[np.argmax(signal_fft_db)], 1)   # argmax, encuentra el argumento max en un array

    plt.plot(F_list, signal_fft_db)  #10 * np.log10(P / Pref) , decibelios
    plt.text(F,0, f"{F}Hz")
    plt.grid(linestyle=":")
    plt.ylabel("Magnitud (db)")
    plt.xlabel("Frecuencias (Hz)")
    plt.title(title)
    plt.xlim([0,200])
    #plt.xticks(np.arange(0,200,10))
    plt.show()

#################################################
# Ejercicio con bitalino
f1 = open("Lab5_ejerciciocomplejo.txt","r")
raw_data1 = f1.readline()  # con f.read() leemos todo el contenido
f1.close()

f2 = open("Lab5_ojocerrados 30.txt","r")
raw_data2 = f2.readline()  # con f.read() leemos todo el contenido
f2.close()

f3 = open("Lab5_ojos abiertos.txt","r")
raw_data3 = f3.readline()  # con f.read() leemos todo el contenido
f3.close()

f4 = open("Lab5_ojos con luz telefono.txt","r")
raw_data4 = f4.readline()  # con f.read() leemos todo el contenido
f4.close()

f5 = open("Lab5_pensando.txt","r")
raw_data5 = f5.readline()  # con f.read() leemos todo el contenido
f5.close()

f6 = open("Lab5_problema 1.txt","r")
raw_data6 = f6.readline()  # con f.read() leemos todo el contenido
f6.close()

## Expresion regular para buscar automaticamente el contenido de un numero dentro de un string
x1 = re.findall("[0-5][0-9]\d", raw_data1)

x2 = re.findall("[0-5][0-9]\d", raw_data2)

x3 = re.findall("[0-5][0-9]\d", raw_data3)

x4 = re.findall("[0-5][0-9]\d", raw_data4)

x5 = re.findall("[0-5][0-9]\d", raw_data5)

x6 = re.findall("[0-5][0-9]\d", raw_data6)

Fs = 1000  #Obtenido de bitalino
Ts=1/Fs

print(f" Fs={Fs} hz\n Ts={Ts} s")

signal1 = np.genfromtxt("./Lab5_ejerciciocomplejo.txt", delimiter="	",skip_header = 2)
signal2 = np.genfromtxt("./Lab5_ojocerrados 30.txt", delimiter="	",skip_header = 2)
signal3 = np.genfromtxt("./Lab5_ojos abiertos.txt", delimiter="	",skip_header = 2)
signal4 = np.genfromtxt("./Lab5_ojos con luz telefono.txt", delimiter="	",skip_header = 2)
signal5 = np.genfromtxt("./Lab5_pensando.txt", delimiter="	",skip_header = 2)
signal6 = np.genfromtxt("./Lab5_problema 1.txt", delimiter="	",skip_header = 2)

M1 = signal1[:,-2].shape[0]
n1 = np.arange(0,M1)

M2 = signal2[:,-2].shape[0]
n2 = np.arange(0,M2)

M3 = signal3[:,-2].shape[0]
n3 = np.arange(0,M3)

M4 = signal4[:,-2].shape[0]
n4 = np.arange(0,M4)

M5 = signal5[:,-2].shape[0]
n5 = np.arange(0,M5)

M6 = signal6[:,-2].shape[0]
n6 = np.arange(0,M6)

t_1 = n1*Ts
ploteo(t_1,signal1,-2,"Señal ejercicio complejo")
ploteo_acotado(t_1,66,100,signal1,-2,"Señal ejercicio complejo acotado")

t_2 = n2*Ts
ploteo(t_2,signal2,-2,"Señal ojos cerrados")
ploteo_acotado(t_2,0,30,signal2,-2,"Señal ojos cerrados acotado")

t3 = n3*Ts
ploteo(t3,signal3,-2,"Señal ojos abiertos")
ploteo_acotado(t3,0,30,signal3,-2,"Señal ojos abiertos acotada")

t4 = n4*Ts
ploteo(t4,signal4,-2,"Señal ojos con luz")
ploteo_acotado(t4,0,30,signal4,-2,"Señal ojos con luz acotada")

t5 = n5*Ts
ploteo(t5,signal5,-2,"Señal memorizando")
ploteo_acotado(t5,65,75,signal5,-2,"Señal memorizando acotada")

t6 = n6*Ts
ploteo(t6,signal6,-2,"Señal problema 1")
ploteo_acotado(t6,0,60,signal6,-2,"Señal problema 1 acotada")

#Comparación
ta=1000*0
tb=1000*30
T3=t3[ta:tb]
T2=t_2[ta:tb]
x3=signal3[ta:tb,-2]
x2=signal2[ta:tb,-2]
plt.plot(T3,x3,label="ojo abierto")     # graficamos la señal segun tiempo acotado
plt.plot(T2,x2,label="ojo cerrado")
plt.title("Comparación de señales")
plt.grid(linestyle=":")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.legend(loc="upper right")
plt.show()

#Comparación
ta=1000*0
tb=1000*30
T3=t3[ta:tb]
T4=t4[ta:tb]
x3=signal3[ta:tb,-2]
x4=signal4[ta:tb,-2]
plt.plot(T3,x3,label="ojo abierto")     # graficamos la señal segun tiempo acotado
plt.plot(T4,x4,label="ojo con luz")
plt.title("Comparación de señales")
plt.grid(linestyle=":")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.legend(loc="upper right")
plt.show()

##############################################
# Para array1
fft(signal1,"FFT en decibelios para señal ejercicio complejo")
# Para array2
fft(signal2,"FFT en decibelios para señal ojos cerrados")
# Para array3
fft(signal3,"FFT en decibelios para señal ojos abiertos")
# Para array4
fft(signal4,"FFT en decibelios para señal ojos con luz")
# Para array5
fft(signal5,"FFT en decibelios para señal memorizando")
# Para array6
fft(signal6,"FFT en decibelios para señal problema 1")
