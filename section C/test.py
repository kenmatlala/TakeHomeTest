from say import number_to_words

def test_number_to_words():
    assert number_to_words(0) == 'zero'
    assert number_to_words(5) == 'five'
    assert number_to_words(12) == 'twelve'
    assert number_to_words(20) == 'twenty'
    assert number_to_words(25) == 'twenty five'
    assert number_to_words(47) == 'forty seven'
    assert number_to_words(100) == 'one hundred'
    assert number_to_words(125) == 'one hundred twenty five'
    assert number_to_words(1000) == 'one thousand'
    assert number_to_words(1025) == 'one thousand twenty five'
    assert number_to_words(1100) == 'one thousand one hundred'
    assert number_to_words(1111) == 'one thousand one hundred eleven'
    assert number_to_words(10000) == 'ten thousand'
    assert number_to_words(11205) == 'eleven thousand two hundred five'
    assert number_to_words(102000) == 'one hundred two thousand'
    assert number_to_words(123456) == 'one hundred twenty three thousand four hundred fifty six'
    assert number_to_words(999999) == 'nine hundred ninety nine thousand nine hundred ninety nine'
    assert number_to_words(-1) == 'Number out of range!'
    assert number_to_words(1000000) == 'Number out of range!'
    
test_number_to_words()