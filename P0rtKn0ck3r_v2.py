#!/usr/bin/python3

""" 
 ______   _______ _________   _______           _______                                              
(  __  \ (  ___  )\__   __/  (  ____ \|\     /|(  ____ \                                             
| (  \  )| (   ) |   ) (     | (    \/( \   / )| (    \/                                             
| |   ) || |   | |   | |     | (__     \ (_) / | (__                                                 
| |   | || |   | |   | |     |  __)     ) _ (  |  __)                                                
| |   ) || |   | |   | |     | (       / ( ) \ | (                                                   
| (__/  )| (___) |   | |     | (____/\( /   \ )| (____/\                                             
(______/ (_______)   )_(_____(_______/|/     \|(_______/                                             
                       (_____)                                                                       
 _______  _______  _______ _________   _        _        _______  _______  _        _______  _______ 
(  ____ )(  ___  )(  ____ )\__   __/  | \    /\( (    /|(  ___  )(  ____ \| \    /\(  ____ \(  ____ )
| (    )|| (   ) || (    )|   ) (     |  \  / /|  \  ( || (   ) || (    \/|  \  / /| (    \/| (    )|
| (____)|| |   | || (____)|   | |     |  (_/ / |   \ | || |   | || |      |  (_/ / | (__    | (____)|
|  _____)| |   | ||     __)   | |     |   _ (  | (\ \) || |   | || |      |   _ (  |  __)   |     __)
| (      | |   | || (\ (      | |     |  ( \ \ | | \   || |   | || |      |  ( \ \ | (      | (\ (   
| )      | (___) || ) \ \__   | |     |  /  \ \| )  \  || (___) || (____/\|  /  \ \| (____/\| ) \ \__
|/       (_______)|/   \__/   )_(     |_/    \/|/    )_)(_______)(_______/|_/    \/(_______/|/   \__/ 
 

"""
#Imports the socket module which is needed for any TCP type activity.
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Plug in your host (IPV4) and your Port you wish to scan. 
# I updaed the static input from code to an input box for user interaction.
# Also want to make it scan IP-Range and Port-Range in the not too distant future.
print("Who we 'bout to ping?")
host = raw_input("Enter Host: ")
print("What protocol we fuxing with today?")
port = input("Enter Port: ")

#Print statement for 1337 effects
print("Knocking on the sky...listenining to the sound!")

# Defines portScanner and tells it to ping the port to see if it's open.  
# If closed, then message.  If open then alt message.
def portScanner(port):
	if s.connect_ex((host, port)):
		print("You diddn't say the m4g1c w0rd! ")
	else: 
		print(" Port is OPEN, hunt all the VULNZ!")

# Runs the thing.
portScanner(port)

