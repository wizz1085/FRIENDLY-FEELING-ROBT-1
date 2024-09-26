from machine import Pin
import bluetooth
from BLE import BLEUART
import time
from esp32_dac import playWavFile

# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()


#RUEDAS
D1= Pin(13, Pin.OUT)
D2= Pin(12, Pin.OUT)
I1= Pin(27, Pin.OUT)
I2= Pin(14, Pin.OUT) 

#LEDS
R1 = Pin(4, Pin.OUT)
R2 = Pin(19, Pin.OUT)
R3 = Pin(23, Pin.OUT)
R4 = Pin(26, Pin.OUT)

A1 = Pin(2, Pin.OUT)
A2 = Pin(18, Pin.OUT)
A3 = Pin(22, Pin.OUT)
A4 = Pin(32, Pin.OUT)

V1 = Pin(15, Pin.OUT)
V2 = Pin(5, Pin.OUT)
V3 = Pin(21, Pin.OUT)
V4 = Pin(33, Pin.OUT)

#SwitchAplausos
Clap= Pin(34, Pin.IN)


#init BT

name = 'ESPISA'
print("Bluetooth activo")
ble = bluetooth.BLE()
uart = BLEUART(ble,name)

#Valores iniciales

A1.value(0)
A2.value(0)
A3.value(0)
A4.value(0)
V1.value(0)
V2.value(0)
V3.value(0)
V4.value(0)
R1.value(0)
R2.value(1)
R3.value(1)
R4.value(0)
Ojos = 'Inicio'
D1.value(0)
D2.value(0)
I1.value(0)
I2.value(0)

#BT RX event

def App():
    rx_buffer = uart.read().decode().strip()
    #uart.write('ESPBot says: ' +str(rx_buffer) + "\n")
    print(rx_buffer)
    
    if rx_buffer == 'CONECTADO':
        Ojos = 'conectado'
        Eyes(Ojos)
    elif rx_buffer == 'DESCONECTADO':
        Ojos = 'desconectado'
        Eyes(Ojos)
    elif rx_buffer == 'NORMAL':
        Ojos = 'normal'
        Eyes(Ojos)
    elif rx_buffer == 'UP':
        Ruedas(rx_buffer)
    elif rx_buffer == 'DOWN':
        Ruedas(rx_buffer)
    elif rx_buffer == 'D':
        Ruedas(rx_buffer)
    elif rx_buffer == 'I':
        Ruedas(rx_buffer)
    elif rx_buffer == 'NO':
        Ruedas(rx_buffer)
    elif rx_buffer == 'RELAX':
        Ojos = 'musical'
        Eyes(Ojos)
        playWavFile("/Relax3.wav")
        playWavFile("/Relax3.wav")
        playWavFile("/Relax3.wav")
        Ojos = 'normal'
        Eyes(Ojos)
    elif rx_buffer == 'EJ':
        Ojos = 'musical'
        Eyes(Ojos)
        playWavFile("/Deporte3.wav")
        playWavFile("/Deporte3.wav")
        playWavFile("/Deporte3.wav")
        Ojos = 'normal'
        Eyes(Ojos)
    elif rx_buffer == 'LOFI':
        Ojos = 'musical'
        Eyes(Ojos)
        playWavFile("/LoFi.wav")
        Ojos = 'normal'
        Eyes(Ojos)
    elif rx_buffer == 'WHITE':
        Ojos = 'musical'
        Eyes(Ojos)
        playWavFile("/Sonido Blanco.wav")
        playWavFile("/Sonido Blanco.wav")
        Ojos = 'normal'
        Eyes(Ojos)
    #else:    
    
def Ruedas(rx_buffer):
    if rx_buffer == 'UP':
        D1.value(1)
        D2.value(0)
        I1.value(1)
        I2.value(0)
    elif rx_buffer == 'DOWN':
        D1.value(0)
        D2.value(1)
        I1.value(0)
        I2.value(1)
    elif rx_buffer == 'D':
        D1.value(1)
        D2.value(0)
        I1.value(0)
        I2.value(0)
    elif rx_buffer == 'I':
        D1.value(0)
        D2.value(0)
        I1.value(1)
        I2.value(0)
    elif rx_buffer == 'NO':
        D1.value(0)
        D2.value(0)
        I1.value(0)
        I2.value(0)
    else:
        D1.value(0)
        D2.value(0)
        I1.value(0)
        I2.value(0)
    #else:
        
        
def Eyes(Ojos):
    if Ojos == 'conectado':
        A1.value(1)
        A2.value(0)
        A3.value(0)
        A4.value(0)
        V1.value(1)
        V3.value(0)
        R1.value(1)
        R2.value(0)
        R3.value(0)
        R4.value(0)
        V2.value(0)
        V4.value(0)
    elif Ojos == 'desconectado':
        A4.value(0)
        V1.value(0)
        V2.value(1)
        V3.value(0)
        V4.value(0)
        R1.value(0)
        R2.value(1)
        R3.value(1)
        R4.value(0)
        A1.value(0)
        A2.value(1)
        A3.value(0)
    elif Ojos == 'normal':
        V1.value(1)
        V2.value(0)
        V3.value(0)
        V4.value(1)
        R1.value(1)
        R2.value(0)
        R3.value(0)
        R4.value(0)
        A1.value(1)
        A3.value(0)
        A2.value(0)
        A4.value(1)
    elif Ojos == 'musical':
        R1.value(1)
        R2.value(1)
        R3.value(1)
        R4.value(1)
        A1.value(1)
        A2.value(0)
        A3.value(0)
        A4.value(1)
        V1.value(1)
        V2.value(0)
        V3.value(0)
        V4.value(1)
    #else:
        

#Register BT event
    
if __name__=="__main__":
    while True:

        uart.irq(handler=App)
        if Clap.value() == 0: 
            #print('clap')
            A1.value(0)
            A2.value(0)
            A3.value(0)
            A4.value(0)
            V1.value(0)
            V2.value(0)
            V3.value(0)
            V4.value(0)
            R2.value(1)
            R1.value(0)
            R3.value(1)
            R4.value(1)
            time.sleep(1)
            Ojos = 'normal'
            Eyes(Ojos)


     

        

    