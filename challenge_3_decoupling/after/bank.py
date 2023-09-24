from dataclasses import dataclass
from decimal import Decimal
from typing import Protocol
from enum import Enum, auto


class AccountType(Enum):
    SAVINGS = auto()
    CHECKING = auto()


@dataclass
class Account:
    account_number: str
    balance: Decimal
    account_type: AccountType

    def deposit(self, amount: Decimal) -> None:
        print(f'Depositing {amount} into {self.account_type} account: {self.account_number}')
        self.balance += amount

    def withdraw(self, amount: Decimal) -> None:
        print(f'Withdrawing {amount} from {self.account_type} account: {self.account_number}')
        self.balance -= amount


class PaymentService(Protocol):
    def process_payment(self, amount: Decimal) -> None:
        ...

    def process_payout(self, amount: Decimal) -> None:
        ...


def deposit(amount: Decimal, account: Account, payment_service: PaymentService) -> None:
    payment_service.process_payment(amount)
    account.deposit(amount)


def withdraw(amount: Decimal, account: Account, payment_service: PaymentService) -> None:

    payment_service.process_payout(amount)
    account.withdraw(amount)
