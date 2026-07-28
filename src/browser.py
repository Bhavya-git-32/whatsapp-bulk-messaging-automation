import os
import socket
import subprocess
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
)

from config import (
    EDGE_PATH,
    USER_DATA_DIR,
    REMOTE_DEBUGGING_PORT,
)


def launch_edge():
    """
    Launch Microsoft Edge in remote debugging mode.
    """

    if not os.path.exists(USER_DATA_DIR):
        os.makedirs(USER_DATA_DIR)

    print("🚀 Starting Microsoft Edge...")

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

    for i in range(10):

        time.sleep(0.5)

        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            result = sock.connect_ex(
                ("localhost", int(REMOTE_DEBUGGING_PORT))
            )

            sock.close()

            if result == 0:
                print(f"✅ Edge ready in {(i + 1) * 0.5:.1f} seconds.")
                return

        except Exception:
            pass

    raise Exception("Unable to start Microsoft Edge.")


def connect_driver():
    """
    Connect Selenium to the running Edge browser.
    """

    print("🔌 Connecting Selenium...")

    options = webdriver.EdgeOptions()

    options.add_experimental_option(
        "debuggerAddress",
        f"localhost:{REMOTE_DEBUGGING_PORT}",
    )

    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-background-networking")
    options.add_argument("--disable-sync")
    options.add_argument("--disable-translate")
    options.add_argument("--disable-ipc-flooding-protection")

    options.page_load_strategy = "eager"

    # Selenium Manager automatically finds the correct EdgeDriver.
    driver = webdriver.Edge(options=options)

    driver.set_page_load_timeout(80)
    driver.implicitly_wait(1)

    print("✅ Selenium connected successfully.")

    return driver


def open_whatsapp(driver):
    """
    Open WhatsApp Web and wait until the user is logged in.
    """

    print("🌐 Opening WhatsApp Web...")

    driver.get("https://web.whatsapp.com")

    try:

        WebDriverWait(driver, 60).until(

            EC.presence_of_element_located(

                (
                    By.XPATH,
                    '//canvas[@aria-label="Scan me!"] | //div[@aria-label="Chat list"]',
                )

            )

        )

        try:

            driver.find_element(
                By.XPATH,
                '//div[@aria-label="Chat list"]',
            )

            print("✅ Already logged in.")

        except NoSuchElementException:

            print("📱 Please scan the QR code.")
            print("Waiting for login...")

            WebDriverWait(driver, 120).until(

                EC.presence_of_element_located(

                    (
                        By.XPATH,
                        '//div[@aria-label="Chat list"]',
                    )

                )

            )

            print("✅ Login successful.")

        time.sleep(1)

    except TimeoutException:

        driver.quit()

        raise Exception(
            "WhatsApp Web failed to load."
        )