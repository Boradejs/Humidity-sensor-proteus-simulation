import serial
import time
import schedule
import urllib
from urllib.request import urlopen

def update_data(a,b):
    data = urlopen('https://api.thingspeak.com/update?api_key=C55FLZUXKPOCPSLU&field1='+str(a)+"&field2="+str(b))
    print('updated data', data)

def main_func1():
    arduino = serial.Serial('COM2',9600)
    print('Established serial connction to arduino')

    arduino_data = arduino.readline()
    print(arduino_data)
    decoded_values = str(arduino_data[0:len(arduino_data)].decode("utf-8"))
    list_values = decoded_values.split('x')
    for item in list_values:
        list_in_floats.append(float(item))
    a = list_in_floats[0]
    b = list_in_floats[1]

    update_data(a,b)  
 
    print(f'collected readings from Arduino: {list_in_floats}')

    arduino_data = 0
    list_in_floats.clear()
    list_values.clear()
    arduino.close()

#---------------------

#Main code

list_values = []
list_in_floats=[]

print("program started")

schedule.every(4).seconds.do(main_func1)

while True:
    schedule.run_pending()
    time.sleep(1)