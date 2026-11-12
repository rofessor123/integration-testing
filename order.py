
from payment import process_payment

def place_order(amount):
    result = process_payment(amount)

    if result == "Payment Successful":
        return "Order Confirmed"
    return "Order Failed"
