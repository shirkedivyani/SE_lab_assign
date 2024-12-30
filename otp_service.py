import random
import re


class OTPService:
    """
    A class to generate and validate OTPs and simulate sending emails.
    """

    def generate_otp(self, digits=6):
        """Generate a random OTP with the specified number of digits."""
        if digits < 4 or digits > 8:
            raise ValueError("OTP length must be between 4 and 8 digits.")
        return str(random.randint(10**(digits - 1), 10**digits - 1))

    def validate_email(self, email):
        """Validate the email address format."""
        regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return bool(re.match(regex, email))

    def send_otp(self, email, otp):
        """Simulate sending an OTP. Returns True if successful."""
        if not self.validate_email(email):
            raise ValueError("Invalid email address.")
        print(f"Simulated email sent to {email} with OTP: {otp}")
        return True
