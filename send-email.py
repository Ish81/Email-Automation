import smtplib
import ssl
from email.message import EmailMessage

# Define email sender and receiver
email_sender = 'legend1brawls@gmail.com'
email_password = 'iunf vfgr akew hunw'
email_receiver = 'shilp.9119@gmail.com'  # Replace with your investor's email

# Set the subject and body of the email
subject = 'Exciting Update: Our Startups Progress and Future Plans'

body = """
Dear [Investor's Name],

I hope this email finds you well. I'm reaching out to share an exciting update on our startup's recent progress and our ambitious plans moving forward.

Over the past few months, we've achieved significant milestones:
- Successfully developed our core product with improved market validation.
- Gained traction with [X] early adopters, receiving valuable feedback.
- Built a strong, diverse team, covering web development, app development, AI/ML, cloud computing, and Web3 technologies.

Looking ahead, we're scaling operations and exploring new markets — and we'd love to discuss how your continued support can help accelerate this journey.

Would you be available for a quick call next week to dive into the details?  

Thank you once again for believing in our vision. I'm confident we're on track to create something truly impactful.

Looking forward to hearing from you.

Best regards,  
[Your Name]  
[Your Position]  
[Your Startup Name]  
[Your Contact Info]
"""

# Create email
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

# Secure the connection with SSL
context = ssl.create_default_context()

# Send the email
try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
