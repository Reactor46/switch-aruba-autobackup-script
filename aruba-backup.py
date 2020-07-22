from netmiko import ConnectHandler
import json
import datetime

dateNow = datetime.datetime.now()

with open('devices.json') as json_file:
    devices = json.load(json_file)
    for device in devices:
        fileName = device["deviceName"]+'-'+'[' + dateNow.strftime("%Y-%m-%d") +']'
        print("Processing Backup " + fileName)

        hp_aruba2530 = {
            'device_type': 'hp_procurve',
            'host':   device["deviceIp"],
            'username': device["username"],
            'password': device["password"]
        }

        net_connect = ConnectHandler(**hp_aruba2530)
        output = net_connect.send_command('show run')
        file = open(fileName +'.txt', 'w')
        file.write(''.join(output))
        file.close()
        print("Backup " + fileName + " Finish")
