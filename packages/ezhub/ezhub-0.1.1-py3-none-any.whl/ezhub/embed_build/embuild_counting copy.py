import os, sys, socket, json, psutil, threading, queue

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
    
# 生成版本
def gen_bh_version():
    return
    try:
        result, ver = run_bash('git rev-parse HEAD')
        # %Y:%m:%d:%H:%M:%S
        result, cur_date = run_bash('date "+%Y:%m:%d:%H:%M:%S"')
        bh_version = f"{cur_date[:-1]}----{ver[:-1]}"
    except:
        bh_version = "default_version"
        # from bh_config.bh_version import bh_version
    return bh_version

if len(sys.argv) > 1:
    if sys.argv[1] == "version":
        print(gen_bh_version())
        sys.exit(0)

import logging
logging.basicConfig(level = logging.DEBUG, format='%(asctime)s %(message)s')
os.chdir(os.path.dirname(os.path.abspath(__file__)))



def misc_count_api(cmd_list, client_send_type):
    
    so_snd = None
    print(cmd_list)
    cmd = cmd_list["msg"]
    error_code, msg = run_bash(cmd)
    so_snd = msg

    # if client_send_type == 0:
    #     pass

    # elif client_send_type == 1:
    #     pass  
    # elif client_send_type == -1:
    #     so_snd = "错误"
    # else:
    #     so_snd = "未知操作"

    return so_snd


class bh_tech_cell_counter:
    def __init__(self):
        self.event = threading.Event()
        self.socket_msg = queue.Queue()
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind(('0.0.0.0', 9999))
        logging.debug(f"服务版号: {gen_bh_version()}")
        self.server.listen(5)
        logging.debug(f"服务版号: {gen_bh_version()}")
        logging.debug(f"开启socket 服务, 等待连接")
        self.client = None

    def socket_theading_function(self):
        # 1. 阻塞直到客户端连接
        self.client, client_addr = self.server.accept()
        self.socket_msg.put(f'connected, {client_addr}')
        valid_recv_msg = ""
        real_to_analyze = ""
        while True:
            try:
                msg = self.client.recv(10240)
                if len(msg) == 0:
                    self.socket_msg.put('client is broken')
                    self.client = None
                    self.client, client_addr = self.server.accept()
                    self.socket_msg.put(f'connected, {client_addr}')
                    continue

                # 2. utf-8 编码
                recv_msg_decoder = str(msg, encoding='utf-8')
                valid_recv_msg += recv_msg_decoder

                # 3. 读取数据
                if(len(valid_recv_msg) < len('bh_ceilxxxx')):
                    continue
                else:
                    lenght_16 = int(valid_recv_msg[7:11], 16)
                    if len(valid_recv_msg) < lenght_16 + len('bh_ceilxxxx'):
                        continue
                    else:
                        real_to_analyze = valid_recv_msg[len('bh_ceilxxxx'):lenght_16 + len('bh_ceilxxxx')]
                        valid_recv_msg=""
                        self.socket_msg.put(real_to_analyze)
            except:
                self.socket_msg.put("client is broken")
                # 1. 阻塞直到客户端连接
                self.client = None
                self.client, _ = self.server.accept()
                self.socket_msg.put('connected')

    def analysis_cmd(self, socket_string_msg):
        # 1. 字符串json转成字典
        try:
            cmd_dict = json.loads(socket_string_msg)
        except:
            logging.exception(f"转换字典错误: 接收到{socket_string_msg}\n, 类型:{type(socket_string_msg)}\n")
            return {}, -1
        if not isinstance(cmd_dict, dict):
            logging.debug(f"错误，不是字典: 接收到{cmd_dict}\n, 类型:{type(cmd_dict)}\n")
            return {}, -1
        # if not "clientSendType" in cmd_dict:
        #     logging.debug(f"错误， 没有 clientSendType 接收到{cmd_dict}\n, 类型:{type(cmd_dict)}\n")
        #     return {}, -1
        # 2. 返回结果
        return cmd_dict, cmd_dict

    def client_send(self, so_snd):
        # 发送返回值
        if self.client != None:
            if so_snd != None:
                so_snd = str(so_snd).replace("'",'"')
                logging.debug("发送的消息: " + so_snd)
                self.client.send(so_snd.encode('utf-8'))

        logging.debug(u'当前进程的内存使用: %.4f MB 总内存使用: %.4f MB' % (psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024 , psutil.virtual_memory().used/1024/1024))

    def run(self):
        socket_thread = threading.Thread(target=self.socket_theading_function)
        socket_thread.daemon = True
        socket_thread.start()
        logging.debug("waiting to get socket msg")

        self.need_restart = False
        while True:
            so_snd = None
            client_send_type = 0
            cmd_list = []
            msg = self.socket_msg.get()             # 阻塞直到有消息
            logging.debug("接收到的消息: " + msg)

            # 无需经过算法处理的操作
            if msg in ["connected", "tf add", "tf remove", "tf alarm"]:
                if msg == "connected":
                    logging.debug(f"connected")
                if msg == "tf add":
                    so_snd = {"serverSendType": 20}
                    so_snd = str(so_snd).replace("'",'"')
                    logging.info(f"tf 插入 {so_snd}")
                if msg == "tf alarm":
                    so_snd = {"serverSendType": 22}
                    so_snd = str(so_snd).replace("'",'"')
                    logging.info(f"tf 报警 {so_snd}")
                self.client_send(so_snd)
                continue

            # 断开连接, 退出app
            if msg == "client is broken":
                cmd_list, client_send_type = [], -2

            # 算法处理
            if client_send_type >= 0:
                cmd_list, client_send_type = self.analysis_cmd(msg)
            try:
                so_snd = misc_count_api(cmd_list, client_send_type)
            except Exception as e:
                error_message = str(e)
                if error_message == "bh_misc_handler_cnt_start optimize error":
                    self.need_restart = True
                logging.exception("count error")
                so_snd = {"data": {},"msg": "执行错误","result": "failed","serverSendType": client_send_type}

            # 发送算法处理结果
            self.client_send(so_snd)
            
            
            
            
            if(self.need_restart == True):
                cmd = "python3 " + os.path.join(os.getcwd(), "bh_boot.py") 
                os.system(cmd)


# cmd = r"UV4.exe -b D:\desktop\_OnMicro\om6681_sdk\btAudio_nochange\projects\dmbt_watch\core0\keil5\bt_audio_om6681a_core0.uvprojx -j0"

