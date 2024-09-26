def luhn_check(card_number):
    digits = str(card_number)[::-1]
    total_sum = 0
    for i in range(len(digits)):
        n = int(digits[i])  
        
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total_sum += n  

    return total_sum % 10 == 0

card_number = 4532015112830366  
is_valid = luhn_check(card_number)
print("Card number:",card_number ,"is",'valid' if is_valid else 'invalid')
