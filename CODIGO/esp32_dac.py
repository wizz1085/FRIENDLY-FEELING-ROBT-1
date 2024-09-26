import time
import sys
from machine import DAC, Pin, freq
import gc

gc.enable()
gc.collect()
freq(240000000)

dacPin1 = Pin(25)

dac1 = DAC( dacPin1 )

def playWavFile( fName ):
    monoFile = open(fName,"rb")
    mark = monoFile.read(4)
    if (mark != b'RIFF'):
        monoFile.close()
        sys.exit(1)
    fileSize = int.from_bytes(monoFile.read(4),"little")
    fileType = monoFile.read(4)
    if (fileType != b'WAVE'):
        monoFile.close()
        sys.exit(2)

    chunk = monoFile.read(4)
    lengthFormat = 0
    audioFormat = 0
    numChannels = 0
    sampleRate = 0
    byteRate = 0
    blockAlign = 0

    if (chunk == b'fmt '):
        lengthFormat = int.from_bytes(monoFile.read(4),"little")
        audioFormat = int.from_bytes(monoFile.read(2),"little") 
        numChannels = int.from_bytes(monoFile.read(2),"little")
        sampleRate = int.from_bytes(monoFile.read(4),"little")
        byteRate = int.from_bytes(monoFile.read(4),"little") 
        blockAlign = int.from_bytes(monoFile.read(2),"little") 
        bitsPerSample = int.from_bytes(monoFile.read(2),"little")
        
        minValue = 255
        maxValue = 0
    
        chunk = monoFile.read(4)
        if (chunk != b'data'):

            monoFile.close()
            sys.exit(5)
        dataSize = int.from_bytes(monoFile.read(4),"little")
#         print("Tamaño de datos = {}".format(dataSize))
        if (bitsPerSample > 8):
#             print("no debe ser superior a 8 bits por muestra")
            monoFile.close()
            sys.exit(6)
        buffer = monoFile.read(dataSize)
        
        for i in range(len(buffer)):
            if (buffer[i] > maxValue):
                maxValue = buffer[i]
            if (buffer[i]<minValue):
                minValue = buffer[i]
        
        xScale = 255.0/(maxValue-minValue)
        
        tm = int(1000000/sampleRate)
        for i in range(len(buffer)):
            data = int(((buffer[i]-minValue)*xScale))
            dac1.write( data )  
            time.sleep_us(tm)
    
    if (audioFormat != 1):
        monoFile.close()
        sys.exit(3)
    monoFile.close()
    dac1.write( 0 )
