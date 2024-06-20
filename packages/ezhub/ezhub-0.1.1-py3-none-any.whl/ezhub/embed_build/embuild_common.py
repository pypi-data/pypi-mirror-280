import os, sys, json, time, copy
import subprocess, threading, queue
import  socket, logging
from enum import Enum
logging.basicConfig(level = logging.DEBUG, format='%(asctime)s - %(message)s')


class Embuild_Proctol(Enum):
    START                   = "start"
    FINISH                  = "finished"
    HEAERTBEAT              = "heartbeat"
    HEAERTBEAT_ACK          = "heartbeat_ack"
    COORDING_SERVER_PORT    = "9999"
    COUNTING_SERVER_PORT    = "10000"
    CLIENT_PORT             = "10001"
    MSG_HEADER              = "embuild"
    MSG_LEN_BYTES           = "4"

"""
    embuild 公用的数据约定
"""
class Common_cli_data_struct:
    def __init__(self):
        self.common_cli_data = {}
        self.common_cli_data["user"] = whoami()
        self.common_cli_data["path"] = os.getcwd()
        self.common_cli_data["compiler_platform"] = "KEIL"
        self.common_cli_data["project"] = None
        self.common_cli_data["msg"] = None


    def platform_set_to_iar(self):
        self.common_cli_data["compiler_platform"] = "IAR"


    def platform_set_to_keil(self):
        self.common_cli_data["compiler_platform"] = "KEIL"


    def get_cli_data_copy(self):
        return copy.deepcopy(self.common_cli_data)


    def project_set(self, project):
        self.common_cli_data["project"] = project

class Em_Socket_base:
    def __init__(self, socket_handler = None):
        self.recv_queue = queue.Queue()

    def receive_thread_function(self, handler):
        valid_recv_msg = ""
        real_to_analyze = ""
        msg_header = Embuild_Proctol.MSG_HEADER.value
        msg_header_len = len(msg_header)
        msg_len_bytes = Embuild_Proctol.MSG_LEN_BYTES.value
        msg_len_bytes = int(msg_len_bytes)
        msg_headerB_len = msg_header_len + msg_len_bytes
        self.thread_alive = True
        while_stop = False
        while True:
            if while_stop == True:
                break
            try:
                msg = handler.recv(10240)
                if len(msg) > 0:
                    recv_msg_decoder = str(msg, encoding='utf-8')
                    valid_recv_msg += recv_msg_decoder
                if(len(valid_recv_msg) < msg_headerB_len):
                    continue
                while len(valid_recv_msg) >= msg_headerB_len:
                    lenght_16 = int(valid_recv_msg[msg_header_len:msg_headerB_len], 16)
                    if len(valid_recv_msg) < lenght_16 + msg_headerB_len:
                        break
                    real_to_analyze = valid_recv_msg[msg_headerB_len:lenght_16 + msg_headerB_len]
                    valid_recv_msg = valid_recv_msg[lenght_16 + msg_headerB_len:]
                    self.recv_queue.put(real_to_analyze)
                    if real_to_analyze == Embuild_Proctol.FINISH.value:
                        while_stop = True
            except:
                logging.exception("recv_thread_function: exception")

    def recv_thread_start(self, handler):
        self.recv_thread = threading.Thread(target=self.receive_thread_function, args=(handler,))
        self.recv_thread.daemon = True
        self.recv_thread.start()
    
    def recv_thread_wait(self):
        self.recv_thread.join()

    def recv_thread_stop(self):
        self.thread_alive = False

    def base_send(self, client, msg):
        msg_len = len(msg)
        msg = Embuild_Proctol.MSG_HEADER.value + "{:04x}".format(msg_len) + msg
        client.send(msg.encode('utf-8'))
    
    def base_get(self):
        return self.recv_queue.get()
"""

"""
# 运行命令, 返回命令执行错误码和结果。会阻塞直到命令执行完成
def run_bash(command, logging_call_back = None):
    import subprocess
    if logging_call_back:
        logging_call_back("start run cmd:"+command)
    error_code = 0
    rtv_msg = ""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            # 命令执行成功
            output = result.stdout
            error_code = 0
            rtv_msg = output
        else:
            # 命令执行错误
            error_code = result.returncode
            error_message = result.stderr
            error_code = error_code
            rtv_msg = error_message
    except Exception as e:
        error_code = -1
        rtv_msg = str(e)
    if logging_call_back is not None:
        logging_call_back(str(error_code)+": "+rtv_msg)
    return error_code, rtv_msg


def whoami():
    # can both run in windows and linux
    e, msg = run_bash("whoami")
    return msg.strip()

# '/data/zhuxi/btAudio_4_09/btAudio'
# 


def keil_compiler_command(project_path):
    exe = 'UV4'

if __name__ == "__main__":
    data = Common_cli_data_struct().get_cli_data_copy()
    print(data)