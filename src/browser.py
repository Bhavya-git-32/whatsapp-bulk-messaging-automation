import os
import socket
import subprocess
import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from config import (
    EDGE_PATH,
    USER_DATA_DIR,
    REMOTE_DEBUGGING_PORT,
    MSEDGEDRIVER_PATH,
)
def launch_edge():
    """
    Launch Microsoft Edge in remote debugging mode.
    """

    if not os.path.exists(USER_DATA_DIR):
        os.makedirs(USER_DATA_DIR)

    creationflags = 0

    if os.name == "nt":
        creationflags = subprocess.DETACHED_PROCESS

    subprocess.Popen(
        [
            EDGE_PATH,
            f"--remote-debugging-port={REMOTE_DEBUGGING_PORT}",
            f"--user-data-dir={USER_DATA_DIR}",
            "--no-first-run",
            "--no-default-browser-check",
            "--disable-extensions",
            "--disable-plugins",
            "--disable-images",
            "--disable-background-timer-throttling",
        ],
        creationflags=creationflags,
    )

    for _ in range(10):

        time.sleep(0.5)

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        result = sock.connect_ex(("localhost", int(REMOTE_DEBUGGING_PORT)))

        sock.close()

        if result == 0:
            print("✅ Edge launched successfully.")
            return

    raise Exception("Unable to launch Edge.")
