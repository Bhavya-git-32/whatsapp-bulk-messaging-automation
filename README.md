# WhatsApp Bulk Messaging Automation

## Overview

WhatsApp Bulk Messaging Automation is a Python-based automation tool that sends WhatsApp messages to multiple contacts using Selenium WebDriver and WhatsApp Web.

The application reads contacts from a CSV file, processes messages automatically, maintains execution logs, handles failures using retry mechanisms, and generates execution reports.

---

## Features

- Bulk WhatsApp messaging from CSV contacts
- Automated contact search
- Message delivery automation
- Retry mechanism for failed contacts
- Structured logging
- Exception handling
- Configurable execution settings
- Performance optimization
- Modular Python architecture

---

## Technology Stack

- Python
- Selenium WebDriver
- Pandas
- PyAutoGUI
- Pyperclip
- OpenPyXL
- Microsoft Edge WebDriver
- Git

---

## Project Structure
whatsapp-bulk-messaging-automation/

│
├── README.md
├── requirements.txt
├── .gitignore
│
├── docs/
│ ├── architecture.md
│ └── workflow.md
│
├── logs/
│ └── .gitkeep
│
├── sample_data/
│ ├── contacts_sample.csv
│ └── message_sample.txt
│
├── screenshots/
│ └── .gitkeep
│
└── src/
├── main.py
├── browser.py
├── config.py
├── data_loader.py
├── helpers.py
├── loggers.py
├── optimizer.py
├── retry.py
└── sender.py


---

# How It Works

The application workflow:

1. Reads contact details from a CSV file.
2. Loads the message content from a text file.
3. Initializes Selenium WebDriver.
4. Opens WhatsApp Web.
5. Searches contacts automatically.
6. Sends messages.
7. Tracks successful and failed executions.
8. Stores execution logs.
9. Retries failed contacts using retry logic.

---

