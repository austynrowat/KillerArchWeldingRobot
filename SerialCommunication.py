#!/usr/bin/python
####in progress (threading)
import serial
import threading
import time

comPort=None



def TransmitThread():
    while comPort:
        for n in range(0,100):
            if comPort:
                inputstring=str(n%2)
                comPort.write(str.encode(inputstring + '\r\n'))
                comPort.flush()
                print(n,'inTransmit1\n')
                time.sleep(1)

def ReceiveThread():
    while comPort:
        if comPort.inWaiting() > 0:
            c=comPort.readline()
            print(c)
            print('\ninReceive\n')
        else:
            time.sleep(0.1)

def LoopbackTest(comPortName):
    global comPort

    comPort=serial.Serial('/dev/ttyACM0',9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS) # /dev/ttyACM0 for tx and rx, /dev/ttyUSB0 for usb ports, /dev/ttyS0

    threading.Thread(target=TransmitThread).start()
    threading.Thread(target=ReceiveThread).start()

    try:
        while True:
            time.sleep(1)
    except:
        comPort=None

if __name__ == "__main__":
    LoopbackTest("/dev/ttyACM0")


######in progress
##import serial
##import time
##ser=serial.Serial('/dev/ttyACM0',9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS) # /dev/ttyACM0 for tx and rx, /dev/ttyUSB0 for usb ports
##ser.isOpen()
##print('Enter your commands below. \nInsert "exit" to leave the application.')
##inputstring=1
##count=0
##while 1:
##    #get keyboard input
##    ++count
##    print(count)
##    inputstring = str(0)
##    #print(inputstring)
##    #Python 3 users
##    if inputstring == 'exit':
##        ser.close()
##        exit()
##    else:
##        ser.write(str.encode(inputstring + '\r\n'))
##        #out=''
##        time.sleep(1)
##        while ser.inWaiting() > 0:
##            #out =''
##            out = ser.readline()#.decode('ascii')
##            print(out)





            
###!/usr/bin/python
######working
##import serial
##import time
##ser=serial.Serial('/dev/ttyACM0',9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS) # /dev/ttyACM0 for tx and rx, /dev/ttyUSB0 for usb ports
##ser.isOpen()
##print('Enter your commands below. \nInsert "exit" to leave the application.')
##inputstring=1
##while 1:
##    #get keyboard input
##    inputstring = input(">>")
##    #Python 3 users
##    if inputstring == 'exit':
##        ser.close()
##        exit()
##    else:
##        ser.write(str.encode(inputstring + '\r\n'))
##        out=''
##        time.sleep(0.0021)
##        while ser.inWaiting() > 0:
##            out =''
##            out = ser.readline().decode('ascii')
##            print(">>" + out)
