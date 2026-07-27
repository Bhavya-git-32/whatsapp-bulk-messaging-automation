import pandas as pd


def save_log(log, file_path):
    """
    Save logs to Excel.
    """

    df = pd.DataFrame(
        log,
        columns=[
            "Contact",
            "Status",
            "Time"
        ]
    )

    df.to_excel(file_path, index=False)
