import random
import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def retry_failed_contacts(driver, failed_contacts, message, optimizer, format_number):
    """
    Retry failed contacts using WhatsApp direct URL.
    """

    retry_log = []

    random.shuffle(failed_contacts)

    print(f"\nRetrying {len(failed_contacts)} failed contacts...")

    for contact in failed_contacts:

        start = time.time()

        print(f"Retrying {contact}...", end="")

        formatted_number = format_number(contact)

        url = (
            f"https://web.whatsapp.com/send?"
            f"phone={formatted_number}&text&app_absent=0"
        )

        try:

            driver.get(url)

            try:

                invalid_popup = (
                    '//div[contains(text(),'
                    '"Phone number shared via url is invalid")]'
                )

                WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located(
                        (By.XPATH, invalid_popup)
                    )
                )

                raise Exception("Invalid phone number")

            except TimeoutException:
                pass

            optimizer.instant_message_send(
                driver,
                message,
                timeout=15
            )

            elapsed = time.time() - start

            print(f" ✅ {elapsed:.2f}s")

            retry_log.append(
                [
                    contact,
                    "Success on Retry",
                    f"{elapsed:.2f}s"
                ]
            )

            driver.get("https://web.whatsapp.com")

            time.sleep(1)

        except Exception:

            elapsed = time.time() - start

            print(f" ❌ {elapsed:.2f}s")

            retry_log.append(
                [
                    contact,
                    "Failed on Retry",
                    f"{elapsed:.2f}s"
                ]
            )

    return retry_log
