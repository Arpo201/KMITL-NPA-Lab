import textfsm
import json
from netmiko import ConnectHandler

jsonFile = open("testcase.json", "r")
routersJson = json.load(jsonFile)
jsonFile.close()

device_params = []
for routerJson in routersJson:
    device_params.append(
        {
            'device_type': routerJson["Device_type"],
            'ip': routerJson["IP"],
            'username': routerJson["Username"],
            'password': routerJson["Password"]
        }
    )

with open('cisco_ios_show_interfaces.textfsm') as template:
    fsm = textfsm.TextFSM(template)
    with ConnectHandler(**device_params[0]) as ssh:
        result = ssh.send_command("sh int")
        result = fsm.ParseText(result)

# print(fsm.header)
print(result)
# print(result[0][0])
