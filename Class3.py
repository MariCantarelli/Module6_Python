#Else and finally

try:
    value = int(input('Write the price of your product: '))
    print(value)

except ValueError:
    print('Please write a price with numbers!')

finally:
    print('code ok')


'''else:
    print('Client write a correct price')
    result = value * 2 
    print (result)'''

print('More code...')