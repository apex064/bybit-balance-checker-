from exchange.bybit import Bybit  # Update path if needed
from utils.logger import logger

def print_menu():
    print("\n=== BYBIT TEST MENU ===")
    print("1. Get Balance")
    print("2. Get Open Positions")
    print("3. Get Funding Rate")
    print("4. Get Current Price")
    print("5. Open Position")
    print("6. Close Position")
    print("7. Exit")

def run_tests():
    bybit = Bybit()

    while True:
        print_menu()
        choice = input("\nEnter your choice (1-7): ")

        if choice == "1":
            balance = bybit.get_balance()
            print(f"\n[Balance] USDT: {balance}")

        elif choice == "2":
            positions = bybit.get_open_positions()
            print("\n[Open Positions]:")
            for symbol, pos in positions.items():
                print(f"{symbol}: {pos}")

        elif choice == "3":
            coin = input("Enter coin (e.g. BTC): ").upper()
            rate = bybit.get_funding_rate(coin)
            print(f"\n[Funding Rate] {coin}: {rate}")

        elif choice == "4":
            coin = input("Enter coin (e.g. BTC): ").upper()
            price = bybit._get_current_price(coin)
            print(f"\n[Current Price] {coin}: {price}")

        elif choice == "5":
            coin = input("Enter coin (e.g. BTC): ").upper()
            size = float(input("Enter position size (e.g. 0.01): "))
            leverage = int(input("Enter leverage (e.g. 5): "))
            side = input("Enter side (long/short): ").lower()
            order_type = input("Enter order type (market/limit): ").lower()

            order_id = bybit.open_position(
                coin=coin,
                size=size,
                leverage=leverage,
                side=side,
                order_type=order_type
            )
            print(f"\n[Open Position] Order ID: {order_id}")

        elif choice == "6":
            coin = input("Enter coin to close (e.g. BTC): ").upper()
            result = bybit.close_position(coin)
            print(f"\n[Close Position] {coin}: {result}")

        elif choice == "7":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    run_tests()
