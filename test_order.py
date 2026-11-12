
from order import place_order

def test_order_payment_integration():
    result = place_order(500)

    assert result == "Order Confirmed"
    print("Integration Test Passed!")
