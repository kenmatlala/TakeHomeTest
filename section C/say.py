def number_to_words(number):
    # Define a list of words for numbers from 0 to 19
    ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    
    # Define a list of words for tens multiples from 20 to 90
    tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    
    if number < 0 or number > 999999:
        return 'Number out of range!'
    
    if number == 0:
        return 'zero'
    
    # Separate the number into hundred thousands, thousands, hundreds, tens, and ones places
    hundred_thousands = number // 100000
    thousands = (number // 1000) % 100
    hundreds = (number // 100) % 10
    tens_place = (number // 10) % 10
    ones_place = number % 10
    
    # Convert each place to its word representation
    words = ''
    if hundred_thousands > 0:
        words += ones[hundred_thousands] + ' hundred '
    
  # This is the part of the code that converts the thousands place to its word representation.
    if thousands > 0:
        if thousands >= 20:
            words += tens[(thousands // 10) - 2] + ' '
            if thousands % 10 != 0:
                words += ones[thousands % 10] + ' '
        else:
            words += ones[thousands] + ' '
        words += 'thousand '
    
  # This is the part of the code that converts the hundreds place to its word representation.
    if hundreds > 0:
        words += ones[hundreds] + ' hundred '
    
    # This is the part of the code that converts the tens place to its word representation.
    if tens_place > 1:
        words += tens[tens_place - 2] + ' '
        if ones_place > 0:
            words += ones[ones_place] + ' '
    elif tens_place == 1:
        words += ones[10 + ones_place] + ' '
    else:
        if ones_place > 0:
            words += ones[ones_place] + ' '
    
   # Removing any extra spaces from the string.
    return words.strip()
    


