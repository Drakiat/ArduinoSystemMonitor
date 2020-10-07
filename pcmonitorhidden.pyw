import wmi
import math
import serial
import time
global GPUTemp
global UsedRAM
global UsedGPU
global CPUTemp
global data
w = wmi.WMI(namespace="root\OpenHardwareMonitor")
hw_infos = w.Sensor()
arduino = serial.Serial()
arduino.bauderate=9600
arduino.port='COM3'
arduino.open()

def SensorSetup():
    w = wmi.WMI(namespace="root\OpenHardwareMonitor")
    hw_infos = w.Sensor()
    for sensor in hw_infos:
        if sensor.SensorType=="Temperature" and sensor.Name=="GPU Core":
            GPUTemp=math.ceil(sensor.Value)
            print("GPU Temp:"+str(GPUTemp)+"°C")
            
        if sensor.Name==u'Memory':
            UsedRAM=math.ceil(sensor.Value)
            print("Used RAM:"+str(UsedRAM)+"%")
       
        if sensor.Identifier==u'/nvidiagpu/0/load/4':
            UsedGPU=math.ceil(sensor.Value)
            print("Used GPU:"+str(UsedGPU)+"%")
        
        if sensor.Identifier==u'/amdcpu/0/temperature/0':
            CPUTemp=math.ceil(sensor.Value)
            print("CPU Temp:"+str(CPUTemp)+"°C")
    return CPUTemp,UsedRAM,UsedGPU,GPUTemp
while True:
    values=SensorSetup()
    CPUTemp=values[0]
    UsedRAM=values[1]
    UsedGPU=values[2]
    GPUTemp=values[3]
    data =("a"+str(GPUTemp)+"b"+str(UsedRAM)+"c"+str(UsedGPU)+"d"+str(CPUTemp)+"e")
    print("Data sent:"+ data)
    arduino.write(data.encode())
    time.sleep(3)



    
"""for sensor in hw_infos:
    if sensor.Name==u'GPU Memory':
        print(sensor)"""
"""for sensor in hw_infos:
    if sensor.SensorType==u'Data':
        print(sensor.Value)
    if sensor.Name == u'Used Memory':
        print ("Used Memory: "+str(sensor.Value))
    elif sensor.Name == u'Available Memory':
        print("Available Memory: "+str(sensor.Value))
    if sensor.SensorType==u'Temperature':
        print("Temperature: "+str(sensor.Value))
    if sensor.Name == u'CPU Package':
        print("CPU Package: "+str(sensor.Value))
    elif sensor.Name == u'GPU Core':
        print("GPU Core: "+str(sensor.Value))
    if sensor.SensorType==u'Clock':
        print("Clock: "+str(sensor.Value))
    if sensor.Name == u'CPU Core #1':
        print("CPU Core #1: "+str(sensor.Value))
    elif sensor.Name == u'GPU Core':
        print("GPU Core: "+str(sensor.Value))
    if sensor.SensorType==u'Data':
        print("Data: "+str(sensor.Value))
    if sensor.Name == u'Used Memory':
        print("Used Memory: "+str(sensor.Value))"""

 
