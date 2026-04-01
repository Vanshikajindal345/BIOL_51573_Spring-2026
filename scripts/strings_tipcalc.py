#!/usr/bin/env python3
# problem 4 

bill = input('Enter the bill amount: ')
tip_percent = input('Enter the tip percentage: ')

bill = float(bill)
tip_percent = float(tip_percent)
tip_amount = bill*(tip_percent/100)
total = bill + tip_amount

print(f'Bill: ${bill}')
print(f'Tip ({tip_percent})%: ${tip_amount:.2f}')
print('--------------------')
print(f'Total: ${total:.2f}')