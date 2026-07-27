import time
import pyperclip

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

class WhatsAppOptimizer:
    def __init__(self):
        self.cached_xpaths = {}
        self.performance_stats = {
            'contacts_processed': 0,
            'start_time': time.time(),
            'search_times': [],
            'send_times': []
        }

    def smart_wait_for_element(self, driver, xpath_options, timeout=10):
        """More robustly waits for an element to be present and then clickable."""
        element = None
        start_time = time.time()
        for xpath in xpath_options:
            try:
                # First, wait for the element to be present in the DOM
                element = WebDriverWait(driver, timeout - (time.time() - start_time)).until(
                    EC.presence_of_element_located((By.XPATH, xpath))
                )
                # Then, wait for the same element to be clickable
                element = WebDriverWait(driver, timeout - (time.time() - start_time)).until(
                    EC.element_to_be_clickable((By.XPATH, xpath))
                )
                if element:
                    return element
            except TimeoutException:
                continue
        raise TimeoutException(f"Element not found or not clickable after {timeout} seconds.")

    def ensure_search_ui_is_ready(self, driver):
        """
        Ensures the UI is clean before every search.
        This is critical because the UI can reset after sending a message.
        """
        try:
            # Close the "Turn on notifications" pop-up if it exists
            notification_close_button_xpath = '//div[@role="button" and @aria-label="Dismiss"]'
            close_button = WebDriverWait(driver, 1).until( # Faster check
                EC.element_to_be_clickable((By.XPATH, notification_close_button_xpath))
            )
            close_button.click()
        except TimeoutException:
            pass # Pop-up wasn't there, which is fine.

        try:
            # Click the search bar to dismiss the "Download for Windows" or other panes
            search_box_xpaths = [
                '//div[@title="Search input textbox"]',
                '//div[@role="textbox"][@title="Search input textbox"]'
            ]
            search_box = self.smart_wait_for_element(driver, search_box_xpaths, timeout=2)
            search_box.click()
            ActionChains(driver).send_keys(Keys.ESCAPE).perform() # Press escape to clear any focus
        except Exception:
            pass # If it fails, continue anyway.

    def search_contact(self, driver, contact):
        """Performs the search action for a contact."""
        search_box_xpaths = [
            '//div[@title="Search input textbox"]',
            '//div[@role="textbox"][@title="Search input textbox"]',
            '//div[contains(@class, "selectable-text")]//div[@contenteditable="true"]',
            '//div[@data-tab="3"][@contenteditable="true"]'
        ]
        search_box = self.smart_wait_for_element(driver, search_box_xpaths, timeout=8)

        # Clear the search box reliably
        search_box.click()
        ActionChains(driver).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()
        
        search_box.send_keys(contact)
        
        try:
            WebDriverWait(driver, 2).until(
                EC.presence_of_element_located((By.XPATH, '//div[@data-testid="chat-list-search-results"] | //div[contains(@class, "_ak_l")]'))
            )
        except TimeoutException:
            try:
                no_results_xpath = '//div[@data-testid="search-no-results-title"] | //span[contains(text(), "No results found for")]'
                WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, no_results_xpath)))
                ActionChains(driver).send_keys(Keys.ESCAPE).perform()
                return 'not_found'
            except TimeoutException:
                pass

        search_box.send_keys(Keys.ENTER)
        return 'searched'


    def instant_message_send(self, driver, message, timeout=15):
        """
        Sends the whole message at once using the clipboard for speed and reliability.
        The timeout is now configurable.
        """
        send_start = time.time()
        
        message_box_xpaths = [
            '//footer//div[@contenteditable="true"]'
        ]
        
        message_box = self.smart_wait_for_element(driver, message_box_xpaths, timeout=timeout)
        
        pyperclip.copy(message)
        
        message_box.click()
        ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).send_keys(Keys.ENTER).perform()

        send_time = time.time() - send_start
        self.performance_stats['send_times'].append(send_time)
        return send_time

    def close_current_chat(self, driver):
        """
        Closes the currently open chat to reset the UI state.
        """
        try:
            back_button_xpath = '//div[@role="button" and @title="Back"] | //button[@aria-label="Back"]'
            back_button = self.smart_wait_for_element(driver, [back_button_xpath], timeout=3)
            back_button.click()
        except TimeoutException:
            try:
                ActionChains(driver).send_keys(Keys.ESCAPE).perform()
            except:
                pass
