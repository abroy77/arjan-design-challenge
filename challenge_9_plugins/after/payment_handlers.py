from decimal import Decimal
from typing import Callable, Dict, List


def process_payment_cc(total: Decimal) -> None:
    card_number = input("Please enter your credit card number: ")
    expiration_date = input("Please enter your credit card expiration date: ")
    ccv = input("Please enter your credit card CCV: ")
    card_number_masked = card_number[-4:].rjust(len(card_number), "*")
    ccv_masked = len(ccv) * "*"
    print(
        f"Processing credit card payment of ${total:.2f} with card number {card_number_masked}"
        f" and expiration date {expiration_date} and CCV {ccv_masked}..."
    )


def process_payment_paypal(total: Decimal) -> None:
    username = input("Please enter your PayPal username: ")
    password = input("Please enter your PayPal password: ")
    password_masked = len(password) * "*"
    print(
        f"Processing PayPal payment of ${total:.2f} with username {username} and password {password_masked}..."
    )


def process_payment_apple_pay(total: Decimal) -> None:
    device_id = input("Please enter your Apple Pay device ID: ")
    device_id_masked = device_id[-4:].rjust(len(device_id), "*")
    print(
        f"Processing Apple Pay payment of ${total:.2f} with device ID {device_id_masked}..."
    )


PaymentHandlerFn = Callable[[Decimal], None]

PAYMENT_HANDLERS: Dict[str, PaymentHandlerFn] = {
    "cc": process_payment_cc,
    "paypal": process_payment_paypal,
    "apple": process_payment_apple_pay,
}


def register_payment_handler(name: str, payment_func: PaymentHandlerFn) -> None:
    PAYMENT_HANDLERS[name] = payment_func


def unregister(name: str) -> None:
    PAYMENT_HANDLERS.pop(name, None)


def all_payments() -> List[str]:
    return list(PAYMENT_HANDLERS.keys())


def handler_exists(name: str) -> bool:
    return name in PAYMENT_HANDLERS.keys()


def get_handler(name: str) -> PaymentHandlerFn:
    return PAYMENT_HANDLERS[name]
