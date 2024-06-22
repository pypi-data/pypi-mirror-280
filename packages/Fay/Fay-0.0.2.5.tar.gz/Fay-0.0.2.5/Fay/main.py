import os
import sys
from io import BytesIO

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication


current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)
sys.path.append(os.path.join(current_dir, 'ai_module'))
sys.path.append(os.path.join(current_dir, 'core'))
sys.path.append(os.path.join(current_dir, 'gui'))
sys.path.append(os.path.join(current_dir, 'utils'))
sys.path.append(os.path.join(current_dir, 'scheduler'))
sys.path.append(os.path.join(current_dir, 'test/ovr_lipsync'))

script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(script_dir, os.pardir))

from ai_module import ali_nls
from ai_module import nlp_langchain
from core import wsa_server
from gui import flask_server
from gui.window import MainWindow
from utils import config_util
from scheduler.thread_manager import MyThread
from core import content_db
import sys
sys.setrecursionlimit(sys.getrecursionlimit() * 5)
import hashlib
import os
import time
import argparse


def __clear_samples():
    if not os.path.exists(os.path.join(script_dir, 'samples')):
        os.mkdir(os.path.join(script_dir, 'samples'))
    for file_name in os.listdir(os.path.join(script_dir, 'samples')):
        if file_name.startswith('sample-'):
            os.remove(os.path.join(script_dir, 'sample') + file_name)


def __clear_songs():
    if not os.path.exists(os.path.join(script_dir, 'songs')):
        os.mkdir(os.path.join(script_dir, 'songs'))
    for file_name in os.listdir(os.path.join(script_dir, 'songs')):
        if file_name.endswith('.mp3'):
            os.remove(os.path.join(script_dir, 'songs') + file_name)

def __clear_logs():
    if not os.path.exists(os.path.join(script_dir, 'logs')):
        os.mkdir(os.path.join(script_dir, 'logs'))
    for file_name in os.listdir(os.path.join(script_dir, 'logs')):
        if file_name.endswith('.log'):
            os.remove(os.path.join(script_dir, 'logs') + file_name)
           


def main():
    __clear_samples()
    __clear_songs()
    __clear_logs()
    parser = argparse.ArgumentParser(description='Fay command line interface')
    parser.add_argument('command', choices=['start'], help='Command to execute')
    parser.add_argument('-config_path', type=str, help='Path to the configuration file', default='default_config_path')

    args = parser.parse_args()
    print(args.config_path)
    if args.command == 'start':
        config_util.set_config_path(args.config_path)
    config_util.load_config()
    contentdb = content_db.new_instance()
    contentdb.init_db()     
    ws_server = wsa_server.new_instance(port=10002)
    ws_server.start_server()
    web_ws_server = wsa_server.new_web_instance(port=10003)
    web_ws_server.start_server()
    #Edit by xszyou in 20230516:增加本地asr后，aliyun调成可选配置
    if config_util.ASR_mode == "ali":
        ali_nls.start()
    flask_server.start() 
    if config_util.key_chat_module == 'langchain':
        nlp_langchain.save_all()
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('icon.png'))
    win = MainWindow()
    time.sleep(1)
    win.show()
    app.exit(app.exec_())

if __name__ == '__main__':
    main()

    
