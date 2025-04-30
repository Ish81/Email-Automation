# 📧 Python Email Sender using Gmail SMTP

This project allows you to send personalized, professional emails via Gmail using Python's `smtplib`. Perfect for sending updates to investors, team members, or clients.

---

## 🚀 Features

- Sends emails via Gmail SMTP with SSL encryption  
- Customizable subject and body  
- Clean structure using Python's `email.message` module  
- Exception handling for safe email delivery

---

## 📁 Project Structure

📂 email-sender-script/ ├── send_email.py # Main Python script ├── README.md # This documentation file └── .gitignore # (Optional) Ignore sensitive files like .env


---

## 🛠️ Requirements

- Python 3.x  
- Gmail account with [App Passwords](https://support.google.com/accounts/answer/185833?hl=en)

### Install dependencies (optional):

```bash
pip install python-dotenv
```
## Example Email Body
```Subject: Exciting Update: Our Startup’s Progress and Future Plans

Dear [Name],

I hope this email finds you well.
[...email content continues...]

Best regards,  
[Your Name]  
[Your Position]  
[Your Startup Name]  
[Your Contact Info]
```

## ✅ How to Use
Clone the repo:
```
git clone https://github.com/YOUR_USERNAME/email-sender-script.git
cd email-sender-script
```

- Edit send_email.py with your sender, receiver, subject, and body.

## Run the script:
```
python send_email.py
```
## 📬 Output
If successful:
```
Email sent successfully!
```
If failed:
```
Failed to send email: <error message>
```
