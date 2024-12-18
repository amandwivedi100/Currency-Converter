import requests
from requests import Response

def taker_of_the_api(rate):
    response: Response = requests.get('https://v6.exchangerate-api.com/v6/3833a07127e441dd54610456/latest/USD')

    if response.status_code != 200:
        print(f"Error: Unable to fetch rates. Status Code: {response.status_code}")
        return None

    try:
        conversion_rates: float = response.json()['conversion_rates'][rate]
        return conversion_rates
    except KeyError:
        print(f"Invalid currency: '{rate}'. Please enter a valid currency")
        return None

def convert(amount: float, base: str, to: str) -> float:
    base: str = base.upper()
    to: str = to.upper()

    from_rate = taker_of_the_api(base)
    to_rate = taker_of_the_api(to)

    if from_rate is None or to_rate is None:
        print(f"Invalid currency input. Please enter a valid currency from the following: ")
        return 0

    if base == "USD":
        converted_amount = amount * to_rate
    elif to == "USD":
        converted_amount = amount / from_rate
    else:
        converted_amount = (amount / from_rate) * to_rate
    return converted_amount


def main() -> None:
    amount = 40
    base_currency = "USD"
    to_currency = "inr"

    result = convert(amount, base_currency, to_currency)

    if result is not None:
        print(f"{amount} {base_currency} is equal to {result} {to_currency}")

if __name__ == '__main__':
    main()

