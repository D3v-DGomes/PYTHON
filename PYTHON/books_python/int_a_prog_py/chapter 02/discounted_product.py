'''
Write a program that requests the price of a product
and the discount percentage. Display the discount amount
and the price to be paid.
'''
product_price = float(input('Enter the product value: $'))
product_discount = float(input('Enter the discount percentage: '))

discount_price = product_price * (product_discount / 100)
final_price = product_price - discount_price

print(f'Discount amount: ${discount_price:.2f}')
print(f'Amount to be paid: ${final_price:.2f}')