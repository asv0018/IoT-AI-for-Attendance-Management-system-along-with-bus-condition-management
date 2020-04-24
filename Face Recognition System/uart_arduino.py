import serial
import requests
import json
import time as tim
from datetime import *
datafrmMcu = serial.Serial(port="/dev/ttyUSB0",baudrate=9600,timeout=0,rtscts=0,xonxoff=0)
while 1:
    rx = datafrmMcu.readline()
    rx_data=rx[0:len(rx)-2].decode("utf-8")
    tim.sleep(1)
    try:
        json_data = json.loads(rx_data)       
    except:
        pass
    else:
        print("http://aishwarya.thinkfinitylabs.com/bushealth.php?status="+str(json_data['fuel'])+
              "&temp="+str(json_data['tem'])+"&time="+str((datetime.now()).strftime("%H:%M")))
        data_to_db=requests.get("http://aishwarya.thinkfinitylabs.com/bushealth.php?status="+str(json_data['fuel'])+
                                "&temp="+str(json_data['tem'])+"&time="+str((datetime.now()).strftime("%H:%M")),headers={"User-Agent": "XY"})
        print(data_to_db.text)
        tim.sleep(60)
    
