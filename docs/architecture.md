
# WhatsApp Bulk Messaging Automation Architecture

## Overview

This project automates bulk WhatsApp messaging using Selenium WebDriver and Microsoft Edge. It reads contact information from an Excel file, loads a message template, sends messages through WhatsApp Web, records execution logs, and retries failed deliveries.

---

## High-Level Architecture
            +---------------------+
            |  contacts.xlsx      |
            +----------+----------+
                       |
                       v
            +---------------------+
            |   data_loader.py    |
            +----------+----------+
                       |
                       v
            +---------------------+
            |      main.py        |
            +----------+----------+
                       |
    +------------------+------------------+
    |                                     |
    v                                     v+--------------------+ +--------------------+
| browser.py | | sender.py |
| Launch Edge | | Send Messages |
| Connect Selenium | | Search Contacts |
| Open WhatsApp | | Send Text |
+---------+----------+ +---------+----------+
| |
+----------------+------------------+
|
v
+---------------------+
| logger.py |
| Save Excel Logs |
+----------+----------+
|
v
+---------------------+
| retry.py |
| Retry Failed |
+---------------------+


---

## Components

### browser.py
- Launches Microsoft Edge
- Connects Selenium
- Opens WhatsApp Web
- Maintains browser session

### data_loader.py
- Reads contacts
- Reads message template
- Validates input files

### sender.py
- Searches contacts
- Sends WhatsApp messages
- Handles failures

### logger.py
- Stores execution results
- Creates Excel log reports

### retry.py
- Retries failed contacts
- Uses direct WhatsApp URLs

### optimizer.py
- Controls wait times
- Improves automation performance

### helpers.py
- Utility functions
- Number formatting
- Retry confirmation

---

## Error Handling

- TimeoutException
- NoSuchElementException
- Invalid contacts
- Retry mechanism
- Logging of failures

---

## Future Improvements

- Media attachments
- Scheduled messaging
- Personalized templates
- Docker deployment
- Environment variable configuration
- CI/CD integration