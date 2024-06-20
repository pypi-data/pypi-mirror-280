import os, sys, socket, json, psutil, threading, queue
import logging
logging.basicConfig(level = logging.DEBUG, format='%(message)s')

from ezhub.embed_build.embuild_common import Common_cli_data_struct, Embuild_Proctol
from ezhub.embed_build.embuild_common import Em_Socket_base

class Coordinating_server(Em_Socket_base):
    def __init__(self, port = Embuild_Proctol.COORDING_SERVER_PORT.value):
        self.counting_server_list = []
        self.event = threading.Event()
        self.socket_msg = queue.Queue()
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind(('0.0.0.0', int(port)))
        logging.debug(f"开启socket 协调服务, 等待连接")
        self.server.listen(60)
        self.connected_client_list = []

    def scan_counting_server(self):
        self.counting_server_list = []
        pass
    
    def acquire_counting_server(self):
        return "0.0.0.0" , 10000
        pass
    def release_counting_server(self):
        pass
    
    def one_time_handler(self, client, addr):
        connected_client, client_addr = client, addr
        one_time_socket = Em_Socket_base()
        one_time_socket.recv_thread_start(connected_client)
        msg = one_time_socket.base_get()
        logging.debug(f"DEBUG one_time_handler: {client_addr} 接收到的消息: {msg}")
        """
            todo:
            connected_client 可能是客户端的, 也可能是计算中心的, 需要区分
        """
        # msg 转发给counting server
        # counting_server = self.acquire_counting_server()
        # ip, port = counting_server
        counting_socket = socket.socket()
        counting_socket.connect(("192.168.43.185", 10000))
        counting_socket_handler = Em_Socket_base()
        logging.debug(f"counting_socket.getblocking(): {counting_socket.getblocking()}")
        counting_socket_handler.recv_thread_start(counting_socket)
        counting_socket_handler.base_send(counting_socket, msg)
        
        while True:
            counting_server_msg = counting_socket_handler.base_get()
            logging.debug(f"DEBUG one_time_handler: {client_addr} 接收到的消息: {counting_server_msg}")
            one_time_socket.base_send(connected_client, counting_server_msg)
            if counting_server_msg == Embuild_Proctol.FINISH.value:
                connected_client.close()
                break
        counting_socket_handler.base_send(counting_socket, Embuild_Proctol.FINISH.value)
        counting_socket.close()

    def main_thread(self):
        while True:
            # 阻塞直到连接
            logging.debug(f"DEBUG main_thread:  wait accept")
            connected_client, client_addr = self.server.accept()
            logging.debug(f"DEBUG main_thread: connected, {client_addr}")
            """
                在这里, 协调服务器会收到 计算中心的连接, 和客户端的连接
            """
            # 启动线程处理该连接
            socket_thread = threading.Thread(target=self.one_time_handler, args=(connected_client, client_addr))
            socket_thread.daemon = True
            socket_thread.start()
            # self.connected_client_list.append((connected_client, client_addr, socket_thread))

def embuild_coord_main(port):
    project = Coordinating_server(port)
    project.main_thread()

if __name__ == "__main__":
    embuild_coord_main(9999)