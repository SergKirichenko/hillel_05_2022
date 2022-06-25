import requests
from bs4 import BeautifulSoup


def convert_currency(src: str, dst: str, amount: float) -> float:
    if src != dst:

        def get_digits(text) -> float:
            new_text = ""
            for c in text:
                if c.isdigit() or c == ".":
                    new_text += c
            return float(new_text)

        url = f"https://www.xe.com/currencyconverter/convert/?Amount={amount}&From={src}&To={dst}"
        content = requests.get(url).content
        soup = BeautifulSoup(content, "html.parser")
        exchange_rate_html = soup.find_all("p")[2]
        return round(get_digits(exchange_rate_html.text), 2) * (-1 if amount < 0 else 1)
    else:
        return amount


# if __name__ == "__main__":
# source_currency = "UAH"
# destination_currency = "USD"
# money = float(-20000)
# exchange_rate = convert_currency(source_currency, destination_currency, money)
#
# print(f"{money} {source_currency} = {exchange_rate} {destination_currency}")
