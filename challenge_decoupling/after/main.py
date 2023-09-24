from decimal import Decimal
from bank import Account, AccountType, deposit, withdraw
from stripe_service import StripePaymentService


def main() -> None:
    savings_account = Account("SA001", Decimal("1000"), account_type=AccountType.SAVINGS)
    checking_account = Account("CA001", Decimal("500"), account_type=AccountType.CHECKING)

    stripe_payment_service = StripePaymentService()
    stripe_payment_service.set_api_key('my-api-key')

    deposit(Decimal("200"), savings_account, payment_service=stripe_payment_service)
    deposit(Decimal("300"), checking_account, payment_service=stripe_payment_service)

    withdraw(Decimal("100"), savings_account, payment_service=stripe_payment_service)
    withdraw(Decimal("200"), checking_account, payment_service=stripe_payment_service)

    print(f"Savings Account Balance: {savings_account.balance}")
    print(f"Checking Account Balance: {checking_account.balance}")


if __name__ == "__main__":
    main()
