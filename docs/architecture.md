# WhatsApp Bulk Messaging Automation - System Architecture

## Overview

WhatsApp Bulk Messaging Automation is a Python-based automation application that sends WhatsApp messages to multiple contacts using Selenium WebDriver and Microsoft Edge.

The application reads contact information from an Excel file, loads a predefined message from a text file, automates WhatsApp Web interactions, logs execution results, and retries failed deliveries to improve reliability.

---

# System Architecture

```text
                         +----------------------+
                         |   contacts.xlsx      |
                         +----------+-----------+
                                    |
                                    |
                                    v
                         +----------------------+
                         |    data_loader.py    |
                         +----------+-----------+
                                    |
                                    |
                                    v
                         +----------------------+
                         |      main.py         |
                         +----------+-----------+
                                    |
            +-----------------------+-----------------------+
            |                                               |
            v                                               v
 +------------------------+                    +------------------------+
 |      browser.py        |                    |      sender.py         |
 |------------------------|                    |------------------------|
 | Launch Edge            |                    | Search Contact         |
 | Connect Selenium       |                    | Send Message           |
 | Open WhatsApp Web      |                    | Handle Failures        |
 +-----------+------------+                    +-----------+------------+
             |                                             |
             +----------------------+----------------------+
                                    |
                                    v
                        +------------------------+
                        |      logger.py         |
                        | Save Execution Logs    |
                        +-----------+------------+
                                    |
                                    v
                        +------------------------+
                        |      retry.py          |
                        | Retry Failed Contacts  |
                        +------------------------+
```

---

# Project Components

## 1. main.py

The main entry point of the application.

### Responsibilities

- Launch the browser
- Connect Selenium
- Open WhatsApp Web
- Load contacts
- Load message
- Send bulk messages
- Save execution logs
- Retry failed messages
- Close browser session

---

## 2. browser.py

Responsible for browser management.

### Responsibilities

- Launch Microsoft Edge
- Connect Selenium using Remote Debugging
- Open WhatsApp Web
- Wait for successful login
- Manage browser session

---

## 3. data_loader.py

Handles all input data.

### Responsibilities

- Read contacts from Excel
- Read message from text file
- Validate input files
- Return structured data

---

## 4. sender.py

Core messaging engine.

### Responsibilities

- Search contacts
- Open conversations
- Paste message
- Send messages
- Capture failures
- Return execution status

---

## 5. retry.py

Handles failed deliveries.

### Responsibilities

- Read failed contacts
- Retry using direct WhatsApp URLs
- Record retry status
- Generate retry logs

---

## 6. logger.py

Responsible for execution logging.

### Responsibilities

- Generate Excel log files
- Store delivery status
- Save timestamps
- Maintain execution history

---

## 7. optimizer.py

Optimizes browser performance.

### Responsibilities

- Reduce unnecessary waiting
- Improve Selenium execution speed
- Configure browser behaviour

---

## 8. helpers.py

Contains reusable utility functions.

### Responsibilities

- Format phone numbers
- Display retry dialog
- Reusable helper methods

---

# Data Flow

```text
User
   │
   ▼
Load Contacts
   │
   ▼
Load Message
   │
   ▼
Launch Microsoft Edge
   │
   ▼
Connect Selenium
   │
   ▼
Open WhatsApp Web
   │
   ▼
Authenticate User
   │
   ▼
Read Next Contact
   │
   ▼
Search Contact
   │
   ▼
Send Message
   │
   ▼
Log Result
   │
   ▼
Next Contact
   │
   ▼
Retry Failed Contacts
   │
   ▼
Generate Final Report
```

---

# Error Handling

The application includes exception handling to improve reliability.

## Supported Scenarios

- Browser launch failures
- Selenium connection failures
- WhatsApp loading timeout
- Contact not found
- Invalid phone number
- Message sending failure
- Retry mechanism for failed deliveries

All failures are recorded in Excel log files for later analysis.

---

# Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Selenium WebDriver | Browser automation |
| Microsoft Edge | Web browser |
| Pandas | Excel data processing |
| OpenPyXL | Excel file handling |
| Tkinter | Retry confirmation dialog |
| PyAutoGUI | Keyboard automation |
| Pyperclip | Clipboard management |

---

# Project Structure

```text
whatsapp-bulk-messaging-automation/
│
├── docs/
│   ├── architecture.md
│   └── workflow.md
│
├── logs/
│
├── sample_data/
│
├── screenshots/
│
├── src/
│   ├── browser.py
│   ├── config.py
│   ├── data_loader.py
│   ├── helpers.py
│   ├── logger.py
│   ├── main.py
│   ├── optimizer.py
│   ├── retry.py
│   └── sender.py
│
├── tests/
│
├── README.md
├── requirements.txt
└── Dockerfile
```

---

# Future Enhancements

- Support media attachments
- Personalised message templates
- Scheduled message delivery
- Environment variable configuration
- Docker deployment
- CI/CD using GitHub Actions
- Automatic WebDriver updates
- Improved logging using Python's logging module
- Multi-language support
- Configuration through YAML or JSON files

---

# Design Principles

The project follows a modular architecture where each component has a single responsibility.

Key software engineering principles include:

- Modular design
- Separation of concerns
- Reusable utility functions
- Configuration-driven development
- Exception handling
- Retry mechanism for reliability
- Maintainable and scalable code structure

---

# Summary

This project demonstrates browser automation using Selenium WebDriver while following software engineering best practices such as modular design, configuration management, logging, retry mechanisms, and documentation. The architecture is designed to be maintainable, extensible, and suitable for future enhancements.
