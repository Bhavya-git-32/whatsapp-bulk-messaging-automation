import os

# Base Project Directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Browser Configuration
EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
USER_DATA_DIR = os.path.join(BASE_DIR, "edge_user_data_whatsapp")
REMOTE_DEBUGGING_PORT = "9222"
MSEDGEDRIVER_PATH = os.path.join(BASE_DIR, "msedgedriver.exe")

# Input Files
CONTACTS_EXCEL_PATH = os.path.join(BASE_DIR, "sample_data", "contacts.xlsx")
MESSAGE_TXT_PATH = os.path.join(BASE_DIR, "sample_data", "message.txt")

# Output Files
LOG_FILE_PATH = os.path.join(BASE_DIR, "logs", "send_log_phase1.xlsx")
RETRY_LOG_FILE_PATH = os.path.join(BASE_DIR, "logs", "send_log_phase2.xlsx")
