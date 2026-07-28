# WhatsApp Bulk Messaging Automation

A Python-based automation tool that streamlines sending personalized WhatsApp messages to multiple contacts using **Selenium WebDriver**. The application reads contact details from an Excel spreadsheet, automates message delivery through WhatsApp Web, and follows a modular architecture for maintainability and scalability.

This project demonstrates Python automation, browser automation, Docker containerization, and Continuous Integration using GitHub Actions.

---

## 🚀 Features

* Send personalized WhatsApp messages to multiple contacts
* Read contact details from Excel spreadsheets
* Modular and reusable project architecture
* Retry mechanism for failed message delivery
* Configuration management
* Structured logging for easier troubleshooting
* Docker support for consistent deployment
* GitHub Actions workflow for Continuous Integration (CI)

---

## 🛠 Technology Stack

| Category         | Technologies       |
| ---------------- | ------------------ |
| Programming      | Python             |
| Automation       | Selenium WebDriver |
| Containerization | Docker             |
| CI/CD            | GitHub Actions     |
| Data Handling    | OpenPyXL           |
| Logging          | Python Logging     |
| Version Control  | Git & GitHub       |

---

## 📂 Project Structure

```text
whatsapp-bulk-messaging-automation/
│
├── .github/
│   └── workflows/
│
├── docs/
│
├── logs/
│
├── sample_data/
│
├── screenshots/
│
├── src/
│
├── tests/
│
├── .gitignore
├── Dockerfile
├── README.md
├── requirements.txt
└── LICENSE
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/Bhavya-git-32/whatsapp-bulk-messaging-automation.git
```

### Navigate to the project

```bash
cd whatsapp-bulk-messaging-automation
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

1. Open WhatsApp Web and scan the QR code.
2. Place the contact Excel file inside the `sample_data` folder.
3. Configure the required settings.
4. Run the application.

```bash
python src/main.py
```

---

## 🐳 Running with Docker

Build the Docker image:

```bash
docker build -t whatsapp-bulk-messaging-automation .
```

Run the container:

```bash
docker run whatsapp-bulk-messaging-automation
```

---

## 🔄 Continuous Integration

GitHub Actions is configured to automate parts of the development workflow. Depending on the workflow configuration, it can help validate changes and ensure the project remains consistent after new commits.

---

## 📸 Screenshots

Screenshots demonstrating the application workflow will be added in future updates.

---

## 🔮 Future Enhancements

* Schedule messages for a future date and time
* Support media attachments (images, documents, videos)
* Contact grouping and batch processing
* Custom message templates
* Improved reporting and delivery status
* Web-based user interface
* Cloud deployment

---

## 👩‍💻 Author

**Bhavya Sri**

* LinkedIn: https://linkedin.com/in/sattibhavyasri
* GitHub: https://github.com/Bhavya-git-32

---

## ⭐ If you found this project useful

If you found this repository helpful or interesting, consider giving it a ⭐ on GitHub.
