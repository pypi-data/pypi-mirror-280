import os
import sys
import subprocess
import logging
logging.basicConfig(level=logging.DEBUG, format='%(message)s')
from shutil import copy2

USAGE_TXT = """
patch包中包含一个记录了文本差异信息的.patch文件
如果有二进制文件的更新,那么还会有若干文件夹目录

按照以下步骤进行patch更新:
1. 将 xx.patch 文件之外的文件复制到原SDK的根目录下
2. 在git bash中切换路径为原SDK的根目录
3. 在git bash中运行以下命令:(将命令中的patch_path替换成 xx.patch文件的实际路径)
patch -p0 -u -E --binary < patch_path
"""

HELP_TEXT = """
生成patch:
1. 在svn仓库下
2. 运行 om_patch gen <pre_version>
pre_version: 之前的版本号
"""


def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Command failed with error: {result.stderr}")
        sys.exit(1)
    return result.stdout.strip()

def copy_file_with_structure(src, dest_root):
    dest = os.path.join(dest_root, src)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    copy2(src, dest)
    print(f"Copied {src} to {dest}")


def patch_generate(pre_vesion):
    initial_version = pre_vesion
    updated_version = run_command("svn info --show-item revision")
    logging.info(f"patch is from {updated_version} to {initial_version}")
    bin_file_extensions = [".bin", ".exe", ".dll", ".lib", '.a', '.elf', '.flm']    
    diff_output = run_command(f"svn diff --summarize -r {initial_version}:{updated_version}")
    working_url = run_command("svn info --show-item url")
    working_dir = working_url.split('/')[-1]
    update_dir = f"./_patch_{working_dir}_{updated_version}_{initial_version}"

    if not os.path.exists(update_dir):
        os.makedirs(update_dir)

    for line in diff_output.splitlines():
        if line.startswith(('A', 'M')):  # Check if file is added or modified
            filepath = line.split()[-1]
            if any(filepath.endswith(ext) for ext in bin_file_extensions):
                copy_file_with_structure(filepath, update_dir)
                print(f"Copied {filepath} to {update_dir}")

    # 生成patch文件
    
    patch_filename = f"{updated_version}_{initial_version}.patch"
    patch_filename = os.path.join(update_dir, patch_filename)
    
    logging.debug(f"patch file name: {patch_filename}")
    with open(os.path.join(update_dir, "README.txt"), "w") as f:
        f.write("==========================================================================\n")
        f.write("使用说明\n")
        f.write("==========================================================================\n")
        f.write(USAGE_TXT)
        f.write("\n\n\n\n")
        f.write("==========================================================================\n")
        f.write("改动摘要\n")
        f.write("==========================================================================\n")
        f.write(f"Patch from {updated_version} to {initial_version}\n")
        f.write("==========================================================================\n")
        f.write(diff_output)
    run_command(f"svn diff -r {initial_version}:{updated_version} > {patch_filename}")
    run_command(f"zip -r {update_dir}.zip {update_dir}")
    logging.info(f"Patch file created: {patch_filename}")

def patch_apply():
    if len(sys.argv) != 2:
        print("Usage: script.py <patch_file>")
        sys.exit(1)
    patch_file = sys.argv[1]
    run_command(f"patch -p0 < {patch_file}")
    logging.info(f"Patch applied successfully")



def main():
    valid_args = ['gen', 'aply']

    import argparse

    # 创建ArgumentParser对象
    parser = argparse.ArgumentParser(description=HELP_TEXT)

    # 添加位置参数, compiler_ide
    parser.add_argument('operate', type=str, choices=valid_args, help='generate or apply patch')

    parser.add_argument('preversion', type=str, help='preversion')

    # 添加可选参数 --service

    # 解析命令行参数
    args = parser.parse_args()

    if args.operate == 'gen':
        preversion = args.preversion
        patch_generate(preversion)
    elif args.operate == 'aply':
        patch_apply()

if __name__ == "__main__":
    main()

# if __name__ == "__main__":
#     if len(sys.argv) < 2:
#         print("Usage: script.py <generate|apply> <initial_version>")
#         sys.exit(1)
#     if sys.argv[1] == "generate":
#         patch_generate()
#     elif sys.argv[1] == "apply":
#         patch_apply()
#     else:
#         print("Usage: script.py <generate|apply> <initial_version|patch_path>")
#         sys.exit(1)
