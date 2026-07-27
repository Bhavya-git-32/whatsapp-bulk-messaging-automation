import re
import tkinter as tk
from tkinter import messagebox


def format_number_for_api(number):
    """Formats a phone number to the correct 91XXXXXXXXXX format for the API URL."""

    number = re.sub(r'\D', '', str(number))

    if len(number) == 12 and number.startswith('91'):
        return number

    elif len(number) == 10:
        return '91' + number

    elif number.startswith('91'):
        return number

    else:
        return number


def ask_for_retry():
    """Displays a GUI pop-up asking whether to retry failed contacts."""

    root = tk.Tk()
    root.withdraw()

    response = messagebox.askyesno(
        "Retry Failed Contacts",
        "Do you want to retry the failed contacts using the direct link method?"
    )

    root.destroy()

    return response
