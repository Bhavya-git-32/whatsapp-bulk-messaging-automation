# WhatsApp Bulk Messaging Automation

## Overview

WhatsApp Bulk Messaging Automation is a Python application that automates sending WhatsApp messages to multiple contacts using Selenium WebDriver and WhatsApp Web.

The application reads contacts from an Excel file, sends messages automatically, records execution logs, and retries failed deliveries to improve reliability.

---

## Features

- Bulk WhatsApp messaging from Excel contacts
- Automated contact search
- Retry mechanism for failed messages
- Excel-based execution logging
- Explicit waits for improved reliability
- Performance optimizations
- Exception handling
- Simple GUI prompt for retrying failed contacts

---

## Technology Stack

- Python
- Selenium WebDriver
- Pandas
- Tkinter
- PyAutoGUI
- Pyperclip
- Microsoft Edge WebDriver
- Microsoft Excel

---

## Project Structure

```text
whatsapp-bulk-messaging-automation/
│
├── README.md
├── requirements.txt
├── .gitignore
├── src/
├── sample_data/
├── logs/
└── screenshots/
```

---

## How It Works

1. Reads contact details from an Excel file.
2. Loads the message from a text file.
3. Opens WhatsApp Web.
4. Searches for each contact.
5. Sends the message automatically.
6. Records successful and failed deliveries.
7. Retries failed contacts using the direct WhatsApp URL method.

---

## Future Enhancements

- Personalized message templates
- Media attachments
- Scheduled messaging
- Configuration through environment variables
- Docker support
- Multi-language support

---

## Author

**Bhavya Sri**

 Software Analyst | AWS Cloud | Python | Automation
