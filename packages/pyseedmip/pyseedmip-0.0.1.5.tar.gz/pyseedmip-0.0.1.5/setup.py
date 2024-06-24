from setuptools import setup, Extension, Command, find_packages
import os
import sys
from setuptools.command.install import install

class CustomInstallCommand(install):
    def run(self):
        env = os.environ
        bin_path = ''

        # 判断是否在虚拟环境
        if "CONDA_PREFIX" in env:
            bin_path = os.path.join(env["CONDA_PREFIX"], "bin/")
        # 使用 --user 标记
        elif "--user" in sys.argv:
            bin_path = os.path.expanduser("~/.local/bin/")
        # 系统级别安装
        else:
            bin_path = "/usr/local/bin/"

        # 创建所需目录并复制文件
        if not os.path.exists(bin_path):
            os.makedirs(bin_path)

        # 这里假设要复制的文件在 lib_file_path 和 bin_file_path 路径下
        bin_file_path = 'license/build/seedmip_actv'  # 请替换为实际的二进制文件路径
        
        os.system(f"cp {bin_file_path} {bin_path}")

        install.run(self)

class UninstallCommand(Command):
    description = "uninstall package"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        env = os.environ
        bin_path = ''

        # 判断是否在虚拟环境
        if "CONDA_PREFIX" in env:
            bin_path = os.path.join(env["CONDA_PREFIX"], "bin/")
        # 使用 --user 标记
        elif "--user" in sys.argv:
            bin_path = os.path.expanduser("~/.local/bin/")
        # 系统级别安装
        else:
            bin_path = "/usr/local/bin/"

        # 这里假设要移除的文件在 bin_file_path 路径下
        bin_file_path = os.path.join(bin_path, 'seedmip_actv')  # 请替换为实际的二进制文件名称

        if os.path.exists(bin_file_path):
            os.remove(bin_file_path)

setup(
    name="pyseedmip",
    version="0.0.1.5",
    aduthor="seed",
    description="seedmip for python",
    packages=find_packages(),   # automatically find all python packages
    package_data={'pyseedmip': ['pyseedmip.cpython-39-x86_64-linux-gnu.so']},
    cmdclass={
        'install': CustomInstallCommand,
        'uninstall': UninstallCommand,  
    },
)
