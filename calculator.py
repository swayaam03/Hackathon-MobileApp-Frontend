def calculate_total(price, tax):
    tax_amount = price * tax
    total = price + tax_amount
    return total


def main():
    price = 100
    tax = 0.10

    total = calculate_total(price, tax)
    print(f"Total price: ₹{total:.2f}")


if __name__ == "__main__":
    main()
