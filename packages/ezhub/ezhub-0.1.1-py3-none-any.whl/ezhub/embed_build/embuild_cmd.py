import argparse


def embuild_cmd_run(cmd_type):
    from ezhub.embed_build.embuild_client import Embuild_Client
    Embuild_Client(cmd_type)

def main():
    valid_args = ['iar', 'keil']
    parser = argparse.ArgumentParser(description="Example command line tool")
    parser.add_argument('compiler_ide', type=str, choices=valid_args, help='using IDE keil or iar')
    # 添加可选参数 --project
    parser.add_argument('--project', type=str, help='project name')

    # 解析命令行参数
    args = parser.parse_args()

    embuild_cmd_run(args.compiler_ide)

def deploy():
    
    from ezhub.embed_build.embuild_common import Embuild_Proctol
    from ezhub.embed_build.embuild_counting import embuild_count_main
    from ezhub.embed_build.embuild_coordinating import embuild_coord_main

    default_port = Embuild_Proctol.COORDING_SERVER_PORT.value
    default_addr = "127.0.0.1"

    valid_args = ["coord", "count"]
    parser = argparse.ArgumentParser(description="deploy embuild server")
    parser.add_argument('deploy_type', type=str, choices=valid_args, help='deploy type')    
    parser.add_argument('port', default=9999, type=int, help='deploy type')
    parser.add_argument('addr', default = default_addr,type=str, help='deploy type') 
    args = parser.parse_args()
    if args.deploy_type == "coord":
        embuild_coord_main(args.port)
    elif args.deploy_type == "count":
        default_port = int(default_port)
        addr = args.addr
        port = args.port
        embuild_count_main(addr, port)


if __name__ == "__main__":
    main()