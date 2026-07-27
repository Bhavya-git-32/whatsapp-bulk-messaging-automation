import re
import tkinter as tk
from tkinter import messagebox


def format_number(number):

    number = re.sub(r"\D", "", str(number))

    if len(number) == 10:
        return "91" + number

    return number


def ask_retry():

    root = tk.Tk()

    root.withdraw()

    response = messagebox.askyesno(
        "Retry Failed Contacts",
        "Retry failed contacts?"
    )

    root.destroy()

    return response
