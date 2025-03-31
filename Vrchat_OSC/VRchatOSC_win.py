from pythonosc import udp_client
from time import sleep
import psutil
import os
import time

current_dir = os.getcwd

def pc_status(cpu, rama):
    pc_stats = f": CPU: %{cpu} : RAM:{round(rama / 10000000) / 100}/32GB :\n: Ryzen 5 5600 GTX-1070 :"
    return pc_stats

#def time_update():
#    current_time = time.localtime()
#    formtime = time.strftime("%H:%M", current_time)
#    return formtime

word_count = 0
delay = 0
title = "" ## PERMANANT MESSAGE / TITLECARD!!! *optional*
base_sleep = 2
old_line = ""

ip = "127.0.0.1"  
port = 9000       
client = udp_client.SimpleUDPClient(ip, port)


while True:
    data = open(r"C:\Users\ellis_u20kar4\Downloads\VRchat\OSC\vrchat-osc-pluigin\data.txt", 'r')
    with data:
        for line in data:
            for word in line.split():
                word_count = word_count + 1
            delay = (word_count * 0.5) + base_sleep

            current_time = time.localtime()
            formtime = time.strftime("Local time-%H:%M", current_time)
            memory = psutil.virtual_memory()
            pc = pc_status(psutil.cpu_percent(interval=1), (memory.total - memory.available))
            word_count = 0           
            client.send_message("/chatbox/input", [formtime + '\n' + pc + '\n' + old_line.strip() + '\n' + line.strip() + '\n', True])
            old_line = line
            sleep(delay)

            