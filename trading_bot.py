from binance.client import Client
from binance.exceptions import BinanceAPIException
from utils import load_credentials
from logger import get_logger


def get_user_input():
    print("Welcome to the Trading Bot")
    symbol = input("Enter trading symbol (e.g., BTCUSDT): ").upper()

    while True:
        order_type = input("Enter order type (market / limit / stop-limit): ").lower()
        if order_type in ["market", "limit", "stop-limit"]:
            break
        print("Invalid order type. Choose 'market', 'limit', or 'stop-limit'.")

    while True:
        side = input("Enter side (buy / sell): ").lower()
        if side in ["buy", "sell"]:
            break
        print("Invalid side. Choose 'buy' or 'sell'.")

    quantity = float(input("Enter quantity (e.g., 0.001): "))
    price = None
    stop_price = None

    if order_type == "limit":
        price = float(input("Enter limit price: "))
    elif order_type == "stop-limit":
        stop_price = float(input("Enter stop price: "))
        price = float(input("Enter limit price: "))

    return symbol, order_type, side, quantity, price, stop_price


class BasicBot:
    def __init__(self):
        api_key, api_secret = load_credentials()
        self.client = Client(api_key, api_secret)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

        self.logger = get_logger("BasicBot")
        self.logger.info("Bot initialized")

    def place_order(self, symbol, order_type, side, quantity, price=None, stop_price=None):
        try:
            self.logger.info(f"Placing {order_type.upper()} {side.upper()} order for {symbol}")

            if order_type == "market":
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side.upper(),
                    type="MARKET",
                    quantity=quantity
                )
            elif order_type == "limit":
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side.upper(),
                    type="LIMIT",
                    quantity=quantity,
                    price=price,
                    timeInForce="GTC"
                )
            elif order_type == "stop-limit":
                if not stop_price or not price:
                    raise ValueError("Both stop price and limit price must be provided for stop-limit orders.")

                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side.upper(),
                    type="STOP_MARKET",
                    stopPrice=stop_price,
                    closePosition=False,
                    quantity=quantity,
                    price=price,
                    timeInForce="GTC",
                    workingType="MARK_PRICE"
                )
            else:
                raise ValueError("Unsupported order type.")

            self.logger.info("Order placed successfully")
            self.logger.info(order)
            print("Order executed:")
            print(order)

        except BinanceAPIException as e:
            self.logger.error("Binance API error", exc_info=True)
            print(f"Binance API error: {e.message}")
        except Exception as e:
            self.logger.error("Unknown error", exc_info=True)
            print(f"An error occurred: {e}")
    def show_balance(self):
        try:
            balance = self.client.futures_account_balance()
            for b in balance:
                if b['asset'] == 'USDT':
                    print("Connected! Here's your USDT balance:")
                    print(f"USDT Balance: {b['balance']}")
                    return
            print("USDT balance not found.")
        except Exception as e:
            print("Not connected properly:", str(e))


if __name__ == "__main__":
    symbol, order_type, side, quantity, price, stop_price = get_user_input()
    bot = BasicBot()
    bot.show_balance()
    bot.place_order(symbol, order_type, side, quantity, price, stop_price)
