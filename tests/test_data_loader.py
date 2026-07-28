import os
from src.config import CONTACTS_EXCEL_PATH

def test_contacts_file_exists():
    assert os.path.exists(CONTACTS_EXCEL_PATH)