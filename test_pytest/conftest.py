import smtplib
import pytest


@pytest.fixture(scope="session")
def smtp_connection():
    return smtplib.SMTP("smtp.gmail.com", 587, timeout=5)
