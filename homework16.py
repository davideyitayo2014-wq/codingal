def calculate_due(bill_amount, paid_amount):
    return bill_amount - paid_amount


print(calculate_due(bill_amount=100, paid_amount=70))
print(calculate_due(bill_amount=50, paid_amount=50))