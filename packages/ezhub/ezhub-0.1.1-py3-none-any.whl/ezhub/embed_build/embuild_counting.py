"""
    计算服务器, 编译在该服务器上完成, 一般是windows平台
"""
import os, sys, socket, json, psutil, threading, queue, time
import logging, time, random
logging.basicConfig(level = logging.DEBUG, format='%(message)s')
from ezhub.embed_build.embuild_common import Common_cli_data_struct, Embuild_Proctol
from ezhub.embed_build.embuild_common import Em_Socket_base



import subprocess
import re
import os

def get_network_drives():
    # 运行 'wmic logicaldisk where "DriveType=4" get DeviceID,ProviderName' 命令
    output = subprocess.check_output('wmic logicaldisk where "DriveType=4" get DeviceID,ProviderName', shell=True, text=True)
    
    # 初始化列表存储网络驱动器信息
    network_drives = []
    
    # 按行解析输出并跳过表头
    lines = output.strip().split('\n')[1:]
    print(lines)
    for line in lines:
        parts = line.split(maxsplit=1)
        if len(parts) == 2:
            drive_letter = parts[0].strip()
            remote_path = parts[1].strip()
            ip_match = re.search(r'\\\\(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\\', remote_path)
            if ip_match:
                ip_address = ip_match.group(1)
            else:
                ip_address = None
            network_drives.append({
                'drive_letter': drive_letter,
                'remote_path': remote_path,
                'ip_address': ip_address
            })
    
    # 检查每个驱动器是否可访问
    accessible_drives = []
    for drive in network_drives:
        print(drive['drive_letter'])
        if os.path.exists(drive['drive_letter']):
            accessible_drives.append(drive)
    
    return accessible_drives

# 获取网络驱动器信息
network_drives = get_network_drives()
for drive in network_drives:
    print(f"Drive Letter: {drive['drive_letter']}, IP Address: {drive['ip_address']}, Remote Path: {drive['remote_path']}")



class Counting_Server:
    def __init__(self, coordinating_addr=None, coordianting_port=None):
        logging.debug(f"coordinating_addr is: {coordinating_addr}, coordianting_port is: {coordianting_port}")
        self.check_runtime_env()
        if 0:
            self.heartbeat_thread = threading.Thread(target=self.heartbeat, args=(coordinating_addr,coordianting_port,))
            self.heartbeat_thread.daemon = True
            self.heartbeat_thread.start()
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind(('0.0.0.0', 10000))
        logging.debug(f"DEBUG: 开启socket 计算服务, 等待连接")
        self.server.listen(1)
        self.cout_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def check_runtime_env(self):
        platform = sys.platform
        if platform != "win32":
            logging.error("ERROR: only support windows platform")
            sys.exit(-1)

    def heartbeat(self, coordinating_addr, coordinating_port):
        self.alive = False
        em_base = Em_Socket_base()
        while True:
            try:
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.connect((coordinating_addr, coordinating_port))
                em_base.recv_thread_start(client)
                em_base.base_send(client, Embuild_Proctol.HEARTBEAT.value)
                recv = em_base.base_get()
                if recv == Embuild_Proctol.HEARTBEAT_ACK.value.encode('utf-8'):
                    self.alive = True
                    client.close()
                else:
                    logging.error(f"DEBUG: heartbeat ack error: {recv}")
                    self.alive = False
            except:
                logging.debug(f"DEBUG: heartbeat error")
                self.alive = False
            time.sleep(5)

    def count(self):
        while True:
            # 阻塞直到连接
            logging.debug(f"DEBUG main_thread:  wait accept")
            connected_client, client_addr = self.server.accept()
            logging.debug(f"DEBUG main_thread:  get  accepted")
            em_socket_base_count = Em_Socket_base()
            em_socket_base_count.recv_thread_start(connected_client)
            msg = em_socket_base_count.base_get()
            logging.debug(f"DEBUG main_thread: {client_addr} 接收到的消息: {msg}")
            
            ###########################################################################################
            # 
            #
            #
            #   run bash and get the result
            #
            #
            #
            ###########################################################################################
            send_times = 0
            while True:
                if random.randint(0, 4) == 0:
                    # connected_client.send(Embuild_Proctol.FINISH.value.encode('utf-8'))
                    em_socket_base_count.base_send(connected_client, Embuild_Proctol.FINISH.value)
                    logging.debug(f"DEBUG main_thread: {client_addr} send finish")
                    break
                else:
                    snd_msg = f"{send_times} {time.time()}"
                    em_socket_base_count.base_send(connected_client, snd_msg)
                    logging.debug(f"DEBUG main_thread: {client_addr} send: {snd_msg}")
                    send_times += 1
            # check if the client is closed
            if getattr(connected_client, '_closed') == True:
                logging.debug(f"DEBUG main_thread: {client_addr} is closed")
        
    def main_thread(self):
        socket_thread = threading.Thread(target=self.count)
        socket_thread.daemon = True
        socket_thread.start()
        # socket_thread.join()
        while True:
            import time
            try:
                time.sleep(0.1)
                # pass
            except KeyboardInterrupt:
                break
def embuild_count_main(coord_addr = None, coord_port = None):
    counting_server = Counting_Server(coord_addr, coord_port)
    counting_server.main_thread()

if __name__ == "__main__":
    # import sys
    # coordinating_addr = sys.argv[1]
    # coordinating_port = int(sys.argv[2])
    # embuild_count_main(coordinating_addr, coordinating_port)
    get_network_drives()