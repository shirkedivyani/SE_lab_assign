import smtplib
import random
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def is_valid_email(email):
    """Validate the email format."""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email)

def generate_otp():
    """Generate a one-time password (OTP) with 4-8 digits."""
    otp_length = random.randint(4, 8)
    otp = ''.join([str(random.randint(0, 9)) for _ in range(otp_length)])
    return otp

def send_email(receiver_email, otp):
    """Send the OTP to the given email address."""
    sender_email = "chaitanyamote2004@gmail.com"  # Replace with your email
    sender_password = "ubxz zfei hppr cgnx"       # Replace with your email password

    try:
        # Set up the email server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)

        # Create the email content
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = "Your One-Time Password (OTP)"
        body = f"Your OTP is: {otp}"
        message.attach(MIMEText(body, "plain"))

        # Send the email
        server.sendmail(sender_email, receiver_email, message.as_string())
        print(f"OTP sent successfully to {receiver_email}.")

        server.quit()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    email = input("Enter your email: ")
    if is_valid_email(email):
        otp = generate_otp()
        print(f"Generated OTP: {otp}")
        send_email(email, otp)
    else:
        print("Invalid email format. Please try again.")
