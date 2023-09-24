from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from enum import Enum, auto


class ItemNotFoundException(Exception):
    pass


@dataclass
class Item:
    name: str
    price: Decimal
    quantity: int

    @property
    def subtotal(self) -> Decimal:
        return self.price * self.quantity


class DiscountType(Enum):
    PERCENT = auto()
    FIXED = auto()


@dataclass
class Discount():
    discount_code: str
    discount_value: Decimal
    discount_type: DiscountType

    def apply_discount(self, amount: Decimal) -> Decimal:
        if self.discount_type is DiscountType.FIXED:
            return Decimal(amount - self.discount_value)
        else:
            return Decimal(amount * (1-self.discount_value))


SAVE10 = Discount('SAVE10', Decimal(0.1), DiscountType.PERCENT)
BUCKSOFF5 = Discount('5BUCKSOFF', Decimal(5), DiscountType.FIXED)
FREE_SHIPPING = Discount('FREESHIPPING', Decimal(2), DiscountType.FIXED)
BLKFRIDAY = Discount('BLKFRIDAY', Decimal(0.2), DiscountType.PERCENT)


@dataclass
class ShoppingCart:
    items: List[Item] = field(default_factory=list)
    discount: Optional[Discount] = None

    def add_item(self, item: Item) -> None:
        self.items.append(item)

    def remove_item(self, item_name: str) -> None:
        found_item = self.find_item(item_name)
        self.items.remove(found_item)

    def find_item(self, item_name: str) -> Item:
        for item in self.items:
            if item.name == item_name:
                return item
        raise ItemNotFoundException(f"Item '{item_name}' not found.")

    @property
    def subtotal(self) -> Decimal:
        return Decimal(sum(item.subtotal for item in self.items))

    @property
    def total(self) -> Decimal:
        if self.discount:
            return self.discount.apply_discount(self.subtotal)
        else:
            return self.subtotal

    def display(self) -> None:
        # Print the cart
        print("Shopping Cart:")
        print(f"{'Item':<10}{'Price':>10}{'Qty':>7}{'Total':>13}")
        for item in self.items:
            print(
                f"{item.name:<12}${item.price:>7.2f}{item.quantity:>7}     ${item.subtotal:>7.2f}"
            )
        print("=" * 40)
        print(f"Subtotal: ${self.subtotal:>7.2f}")
        if self.discount:
            print(f"Discount: ${Decimal(self.subtotal - self.total):>7.2f}")
        print(f"Total:    ${self.total:>7.2f}")


def main() -> None:
    # Create a shopping cart and add some items to it
    cart = ShoppingCart(
        items=[
            Item("Apple", Decimal("1.50"), 10),
            Item("Banana", Decimal("2.00"), 2),
            Item("Pizza", Decimal("11.90"), 5),
        ],
        discount=SAVE10,
    )

    cart.display()


if __name__ == "__main__":
    main()
