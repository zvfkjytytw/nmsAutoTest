#!/usr/bin/env /usr/bin/python3
import os
import sys

print("You agreement the NMsAutoTest System\n"
      "Please enter the IP address and api key of the tested NMS\n")
NMS_IP = input("NMS IP address:")
API_KEY = input("API key:")
#
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
modem_list=[]
quit_code=['Q', 'q', 'exit', 'close', 'quit', 'Quit', 'QUIT', ]
modem_i = 1
while(modem_name not in quit_code):
    modem_name = input("Enter a modem name or quit for return to main menu:")


