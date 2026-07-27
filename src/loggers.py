import pandas as pd


def save_phase1_log(log_data, log_file_path):
    """
    Saves the Phase 1 execution log to an Excel file.
    """

    log_df = pd.DataFrame(
        log_data,
        columns=["Contact", "Status", "Time"]
    )

    log_df.to_excel(log_file_path, index=False)

    return log_df


def save_phase2_log(retry_log_data, retry_log_file_path):
    """
    Saves the Phase 2 retry log to an Excel file.
    """

    retry_log_df = pd.DataFrame(
        retry_log_data,
        columns=["Contact", "Status", "Time"]
    )

    retry_log_df.to_excel(retry_log_file_path, index=False)

    return retry_log_df
