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
arduino.port='COM3' #CHANGE THIS TO YOUR OWN COM PORT
arduino.open()

def SensorSetup():
    w = wmi.WMI(namespace="root\OpenHardwareMonitor")
    hw_infos = w.Sensor()
    for sensor in hw_infos:
        ''' THE SENSORS HERE ARE THE ONES I FOUND IN MY SYSTEM, THEY WILL MOST LIKELY BE DIFFERENT FOR YOU DEPENDING WHAT HARDWARE YOU HAVE
        TO FIND YOUR OWN HARDWARE SENSORS RUN THE FOLLOWING SCRIPT
        
        import wmi
        w = wmi.WMI(namespace="root\OpenHardwareMonitor")
        hw_infos = w.Sensor()
        for sensor in hw_infos:
            print(sensor)
        '''
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
    time.sleep(1)
 
