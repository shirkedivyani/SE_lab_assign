import pytest
from otp_service import OTPService


@pytest.fixture
def otp_service():
    """Fixture to create an OTPService instance."""
    return OTPService()


def test_generate_otp_valid_lengths(otp_service):
    """Test OTP generation for valid lengths."""
    otp = otp_service.generate_otp(6)
    assert len(otp) == 6
    assert otp.isdigit()

    otp = otp_service.generate_otp(4)
    assert len(otp) == 4
    assert otp.isdigit()

    otp = otp_service.generate_otp(8)
    assert len(otp) == 8
    assert otp.isdigit()


def test_generate_otp_invalid_lengths(otp_service):
    """Test OTP generation with invalid lengths."""
    with pytest.raises(ValueError, match="OTP length must be between 4 and 8 digits."):
        otp_service.generate_otp(3)

    with pytest.raises(ValueError, match="OTP length must be between 4 and 8 digits."):
        otp_service.generate_otp(9)


def test_validate_email_valid_cases(otp_service):
    """Test valid email addresses."""
    valid_emails = [
        "test@example.com",
        "user.name+tag@domain.co.in",
        "user_name@sub.domain.com",
    ]
    for email in valid_emails:
        assert otp_service.validate_email(email)


def test_validate_email_invalid_cases(otp_service):
    """Test invalid email addresses."""
    invalid_emails = ["plainaddress", "@missingusername.com", "username@.com"]
    for email in invalid_emails:
        assert not otp_service.validate_email(email)


def test_send_otp_success(otp_service):
    """Test sending OTP to a valid email."""
    otp = otp_service.generate_otp(6)
    assert otp_service.send_otp("test@example.com", otp)


def test_send_otp_invalid_email(otp_service):
    """Test sending OTP to an invalid email."""
    otp = otp_service.generate_otp(6)
    with pytest.raises(ValueError, match="Invalid email address."):
        otp_service.send_otp("invalid_email", otp)
