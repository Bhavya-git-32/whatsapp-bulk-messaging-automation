import random
import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def send_messages(driver, contacts, message, optimizer):
    """
    Send WhatsApp messages using search.
    """

    log = []

    random.shuffle(contacts)

    print(f"🔀 Shuffled {len(contacts)} contacts.")

    for index, contact in enumerate(contacts):

        contact = str(contact).strip()

        if contact.endswith(".0"):
            contact = contact[:-2]

        if not contact:
            continue

        start = time.time()

        print(
            f"[{index+1}/{len(contacts)}] {contact}",
            end=""
        )

        try:

            optimizer.ensure_search_ui_is_ready(driver)

            result = optimizer.search_contact(
                driver,
                contact
            )

            if result == "not_found":
                raise TimeoutException()

            optimizer.instant_message_send(
                driver,
                message,
                timeout=7
            )

            elapsed = time.time() - start

            print(f" ✅ {elapsed:.2f}s")

            log.append(
                [
                    contact,
                    "Success",
                    f"{elapsed:.2f}s"
                ]
            )

            optimizer.close_current_chat(driver)

        except TimeoutException:

            elapsed = time.time() - start

            print(f" ❌ {elapsed:.2f}s")

            log.append(
                [
                    contact,
                    "Failed",
                    f"{elapsed:.2f}s"
                ]
            )

            try:

                popup = '//div[contains(text(),"is not on WhatsApp")]'

                ok = '//div[@role="button" and text()="OK"]'

                WebDriverWait(driver,2).until(
                    EC.presence_of_element_located(
                        (By.XPATH,popup)
                    )
                )

                driver.find_element(
                    By.XPATH,
                    ok
                ).click()

            except:

                try:

                    ActionChains(driver).send_keys(
                        Keys.ESCAPE
                    ).perform()

                except:
                    pass

        except Exception as e:

            elapsed = time.time()-start

            print(f" ❌ {e}")

            log.append(
                [
                    contact,
                    "Script Error",
                    f"{elapsed:.2f}s"
                ]
            )

    return log
