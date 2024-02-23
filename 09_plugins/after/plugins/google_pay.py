from decimal import Decimal
from payment_handlers import register_payment_handler


def process_payment_google(total: Decimal) -> None:
    email = input("Please enter your Gmail ID")
    password = input("please enter your password")
    password_masked = password[-4:].rjust(len(password), "*")

    print(f"Processing for email {email}")
    print(f"password {password_masked}")
    print(f"Total value of a paltry {total:.2f}")


def initialize():
    register_payment_handler("google_pay", process_payment_google)
