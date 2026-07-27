from browser import (
    launch_edge,
    connect_driver,
    open_whatsapp
)

from optimizer import WhatsAppOptimizer
from data_loader import load_contacts, load_message
from sender import send_messages
from retry import retry_failed_contacts
from logger import save_log
from helpers import ask_retry, format_number

from config import (
    CONTACTS_EXCEL_PATH,
    MESSAGE_TXT_PATH,
    LOG_FILE_PATH,
    RETRY_LOG_FILE_PATH
)


def main():

    launch_edge()

    driver = connect_driver()

    open_whatsapp(driver)

    optimizer = WhatsAppOptimizer()

    contacts = load_contacts(CONTACTS_EXCEL_PATH)

    message = load_message(MESSAGE_TXT_PATH)

    log = send_messages(
        driver,
        contacts,
        message,
        optimizer
    )

    save_log(
        log,
        LOG_FILE_PATH
    )

    failed_contacts = [
        row[0]
        for row in log
        if "Failed" in row[1]
    ]

    if failed_contacts and ask_retry():

        retry_log = retry_failed_contacts(
            driver,
            failed_contacts,
            message,
            optimizer,
            format_number
        )

        save_log(
            retry_log,
            RETRY_LOG_FILE_PATH
        )

    driver.quit()


if __name__ == "__main__":
    main()
