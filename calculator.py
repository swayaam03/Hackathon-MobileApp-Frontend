def calculate_total(price, tax):
    tax_amount = price * tax
    discount = price * 0.20
    total = price + tax_amount - discount
    return total-10


def main():
    price = 100
    tax = 0.10

    total = calculate_total(price, tax)
    print(f"Final payable amount: ₹{total:.2f}")


if __name__ == "__main__":
    main()
