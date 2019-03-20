#!/usr/bin/env /usr/bin/python3
import os
import json
from nmsObject import nmsModem
from nmsObject import nmsRFfeed
from nmsRequest import nmsRequest

print("You agreement the NMsAutoTest System\n"
      "Please, enter the IP address and api key of the tested NMS\n")
NMS_IP = input("NMS IP address:")
API_KEY = input("API key:")
#
_nms_ = nmsRequest(NMS_IP, API_KEY)
#
_rffeed = nmsRFfeed()
_rffeed.t_id = int((json.loads((_nms_.insert(_rffeed.t_obj, _rffeed.t_data())).text))["result"]["id"])
_rffeed.s_id = int((json.loads((_nms_.insert(_rffeed.s_obj, _rffeed.s_data())).text))["result"]["id"])
_rffeed.rf_id = int((json.loads((_nms_.insert(_rffeed.rf_obj, _rffeed.rf_data())).text))["result"]["id"])


def clear_console():
    # For windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For nix like system
    else:
        _ = os.system('clear')


#
clear_console()
print("Thanks! Now add the modem for tests\n")
_modem_list = []
quit_code = ['no', 'No', 'NO', 'Q', 'q', 'exit', 'close', 'quit', 'Quit', 'QUIT', 'by']
modem_quit = None

while (modem_quit not in quit_code):
    modem_name = input("Enter a modem name:")
    modem_ip = input("Enter a modem IP:")
    modem_serial = input("Enter a modem serial:")
    modem_platform = input("Enter a modem paltform (UHP 200 - 1; UHP 100 - 2):")
    _modem = nmsModem(modem_name, modem_ip, modem_serial, modem_platform)
    _modem.set_rffeed(_rffeed.t_id, _rffeed.rf_id)
    _modem.id = (json.loads((_nms_.insert(_modem.obj, _modem.data())).text))["result"]["id"]
    _modem_list.append(_modem)
    clear_console()
    modem_quit = input("Enter a one more modem (yes/no)?:")
print(_modem_list)