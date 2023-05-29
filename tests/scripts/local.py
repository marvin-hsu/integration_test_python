import logging
import subprocess


def start_local_project():
    logging.info("Start local project")
    # 在測試開始前啟動src中專案
    cmd = ["python", "-u", "-m", "src.demo"]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, universal_newlines=True)
    # 等待 process 印出 "Hello World!"
    while True:
        line = process.stdout.readline()
        if line.strip() == "Hello World!":
            break

    logging.info("Local project started")
