#Try and except with input

try:
    value = int(input('Write the price of your product: '))
    print(value)

except ValueError:
    print('Please write a price with numbers!')

print('More code...')