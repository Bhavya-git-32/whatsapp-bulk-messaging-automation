import pandas as pd


def load_contacts(path):
    """
    Reads contacts from Excel.
    """

    df = pd.read_excel(
        path,
        header=None,
        dtype={0: str}
    )

    contacts = df[0].dropna().tolist()

    return contacts


def load_message(path):
    """
    Reads message text file.
    """

    with open(path, "r", encoding="utf-8") as file:
        return file.read().strip()
