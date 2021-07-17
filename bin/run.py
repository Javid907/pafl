import os
import socket

from module import config

my_log_folder = config.get_config("log_folder")
my_log_server_ip_address = config.get_config("log_server_ip_address")
my_log_server_port = config.get_config("log_server_port")
all_files = os.listdir(my_log_folder)


def syslog(message):
    data = "<{priority}> {program} {log_message}".format(priority="INFO", program="pafl", log_message=message)
    UDPSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    UDPSock.sendto(data.encode(), (my_log_server_ip_address, my_log_server_port))
    UDPSock.close()


def pafl():
    while True:
        if len(os.listdir(my_log_folder)) == 0:
            print("Directory is empty")
        else:
            for log_file in all_files:
                username = log_file.split('.')[0]
                full_log_path = my_log_folder + "/" + log_file
                if os.stat(full_log_path).st_size != 0:
                    with open(full_log_path, "r") as f:
                        lines = f.readlines()
                    with open(full_log_path, "w") as f:
                        for line in lines:
                            my_log = username + " " + line
                            syslog(my_log)
                            f.write(line)

print("PaFL is Running")
pafl()
