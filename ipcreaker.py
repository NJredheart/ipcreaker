import requests
import json
import argparse
from termcolor import colored
import time
import os
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--ipaddress", help="Enter  your ip address")
    args = parser.parse_args()
    ip = args.ipaddress
    i = 10
    while i > 0:
        print(colored('''
                ~+

                 *       +
           '                  |
       ()    .-.,="``"=.    - o -
             '=/_       \     |
          *   |  '=._    |
               \     `=./`,        '
            .   '=.__.=' `='      *
   +                         +
        O      *        '       .
''',"red"))
        print(colored("\t\t\thttps://github.com/NJredheart","red"))
        print("\t\t\tVersion 0.1")
        '\n'
        '\n'
        '\n'
        print(colored("[*]1.NORMAL", "white"))
        print(colored("[*]2.JSON", "red"))
        print(colored("[*]3.XML", "green"))
        print(colored("[*]4.CSV", "yellow"))
        print(colored("[*]5.NEWLINE", "blue"))
        print(colored("[*]6.PHP", "magenta"))
        print(colored("[*]7.EXIT", "grey"))
        reslt = input("┌──(Enter@Your)-[~/Result/Format]")
        #reslt = input("Enter your Result Format:")
        os.system("clear")
        if reslt == "1":
            url = "http://ip-api.com/json/"+str(ip)
            res = requests.get(url)
            data = json.loads(res.content)
            print("\t[*]STATUS      :", data['status'])
            print("\t[*]COUNTRY     :", data['country'])
            print("\t[*]COUNTRYCODE :", data['countryCode'])
            print("\t[*]REGION      :", data['region'])
            print("\t[*]REGIONNAME  :", data['regionName'])
            print("\t[*]CITY        :", data['city'])
            print("\t[*]ZIP         :", data['zip'])
            print("\t[*]LAT         :", data['lat'])
            print("\t[*]LON         :", data['lon'])
            print("\t[*]TIMEZONE    :", data['timezone'])
            print("\t[*]ISP         :", data['isp'])
            print("\t[*]ORG         :", data['org'])
            print("\t[*]AS          :", data['as'])
            print("\t[*]IP          :", data['query'])
            time.sleep(10)
            os.system("clear")
        elif reslt == "2":
            url = "http://ip-api.com/json/"+str(ip)
            res = requests.get(url)
            color = res.content
            print(colored(color, "red"))
            time.sleep(10)
            os.system("clear")
        elif reslt == "3":
            url = "http://ip-api.com/xml/"+str(ip)
            res = requests.get(url)
            color = res.content
            print(colored(color, "green"))
            time.sleep(10)
            os.system("clear")
        elif reslt == "4":
            url = "http://ip-api.com/csv/"+str(ip)
            res = requests.get(url)
            color = res.content
            print(colored(color, "yellow"))
            time.sleep(10)
            os.system("clear")
        elif reslt == "5":
            url = "http://ip-api.com/line/"+str(ip)
            res = requests.get(url)
            color = res.content
            print(colored(color, "blue"))
            time.sleep(10)
            os.system("clear")
        elif reslt == "6":
            url = "http://ip-api.com/php/"+str(ip)
            res = requests.get(url)
            color = res.content
            print(colored(color, "magenta"))
            time.sleep(10)
            os.system("clear")
        else:
            print("Exiting........")
            time.sleep(1)
            exit()
