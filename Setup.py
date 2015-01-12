import os
import winsound
import time

print ("Hello and welcome to Oasis 1.1 (Alpha)")
os.system("pause")
os.system("color 17")
os.system("cls")
print ("What is your Name, or what you wish to be refered to as?")
PN = (input(": "))
print("unpacking files...")
time.sleep[2]

file = open("netuser.bat", "w")
file.write("@echo off" + "\n" + "color 17" + "\n" + "echo here is a list of users on this computer:" + "\n" + "net user" + "\n" + "pause")
file.close()

os.system("start netuser.bat")
print("A program has just started up. please do not close it but spell exactly your username")
time.sleep[2]
un = (input("So what is your UserName (spell it exactly): "))
print ("Thank you " + PN + "!")
time.sleep[2]
print ("hold on " + PN + ", were just setting up some final programs!")
NOT FINISHED
