#!/usr/bin/env python3
import argparse
import json, time, copy, socket, time, logging, datetime, os, queue, sys
import threading
logging.basicConfig(level = logging.DEBUG, format='%(message)s')
from ezhub.embed_build.embuild_common import Common_cli_data_struct, Embuild_Proctol, Em_Socket_base

def analysis_dot_config():
    path = os.getcwd()
    _config_file = os.path.join(path, ".config")
    if os.path.exists(_config_file) == False:
        return None
    with open('.config', "r") as f:
        all_lines = f.readlines()
        project_name = ""
        for line in all_lines:
            cur_line = line.strip()
            if cur_line.startswith('#'):
                continue
            if len(cur_line) == 0:
                continue
            cur_line_list = cur_line.split('=')
            if "CONFIG_PROJECT" == cur_line_list[0]:
                project_name = cur_line_list[1]
        return project_name


class Embuild_Client():
    def __init__(self, cmd_type = 'keil'):
        coordinating_addr = os.environ.get('EMBUILD_COORDINATING_ADDR')
        coordinating_port = os.environ.get('EMBUILD_COORDINATING_PORT')
        logging.debug(f"coordinating_addr is: {coordinating_addr}, coordianting_port is: {coordinating_port}")
        if coordinating_addr == None or coordinating_port == None:
            coordinating_addr = "127.0.0.1"
            coordinating_port = Embuild_Proctol.COORDING_SERVER_PORT.value
        coordinating_port = int(coordinating_port)
        if 0:
            self.project_name = analysis_dot_config()
            if self.project_name == None:
                logging.error("ERROR: project not found")
                sys.exit(-1)
            logging.debug(f"DEBUG: project name: {self.project_name}")

        self.cmd_type = cmd_type
        self.client = socket.socket()
        self.client.connect((coordinating_addr, coordinating_port))
        self.em_socket_base_clinet = Em_Socket_base()

        snd_struct = Common_cli_data_struct()
        if self.cmd_type == 'iar':
            snd_struct.platform_set_to_iar()
        elif self.cmd_type == 'keil':
            snd_struct.platform_set_to_keil()
        self.em_socket_base_clinet.recv_thread_start(self.client)
        self.em_socket_base_clinet.base_send(self.client, str(snd_struct.get_cli_data_copy()))
        self.em_socket_base_clinet.base_send(self.client, Embuild_Proctol.FINISH.value)
        
        while True:
            msg = self.em_socket_base_clinet.base_get()
            if msg == Embuild_Proctol.FINISH.value:
                logging.info(msg)
                break
            else:
                logging.info(msg)

if __name__ == "__main__":
    times = 1
    while True:
        try:
            logging.debug("DEBUG: start embuid client: times: %d" % times)
            times += 1
            Embuild_Client()
        except KeyboardInterrupt:
            break