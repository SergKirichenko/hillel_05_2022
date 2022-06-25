from converter import convert_currency


class Price:
    def __init__(self, amount: float, currency: str) -> None:
        self.amount: float = amount
        self.currency: str = currency

    def __str__(self) -> str:
        return f"({self.amount}, {self.currency})"

    def _get_double_exchange(self, other: "Price") -> "Price":
        base_currency = "USD"
        if self.currency != other.currency:
            amount = convert_currency(
                src=other.currency, dst=base_currency, amount=other.amount
            )
            other.amount = convert_currency(
                src=base_currency, dst=self.currency, amount=amount
            )
            other.currency = self.currency
            return Price(other.amount, other.currency)

    def __add__(self, other: "Price") -> "Price":
        Price._get_double_exchange(self, other)
        return Price(amount=(self.amount + other.amount), currency=self.currency)

    def __sub__(self, other: "Price") -> "Price":
        Price._get_double_exchange(self, other)
        return Price(amount=(self.amount - other.amount), currency=self.currency)

    def exchange_currency(self, new_currency: str) -> None:
        self.amount = convert_currency(
            src=self.currency, dst=new_currency, amount=self.amount
        )
        self.currency = new_currency


if __name__ == "__main__":

    def test():
        price_one = Price(20000, "UAH")
        gun = Price(50000, "UAH")
        price_macbook = Price(3000, "EUR")
        price_phone = Price(1500, "USD")

        print(price_one)
        print(price_macbook)
        print(price_one + gun)

        total_c = price_phone + price_one
        print(total_c)

        total_b = gun + price_macbook
        print(total_b)
        price_macbook.exchange_currency("EUR")
        value = price_macbook - price_phone
        print(value)

    # test()
