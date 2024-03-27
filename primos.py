import unittest #esto se importa para que el programa sepa que es un test

def is_primo(value):
    if value % 2 !=0:
        return True
    elif value == 2:
        return True
    for i in range (2, value):
        if value % i == 0:
            return False
    return True
    
        

class TestPrimo(unittest.TestCase):
    def test_1(self):
        result = is_primo(1)
        self.assertEqual(result, True)
    
    def test_2(self):
        result = is_primo(2)
        self.assertEqual(result, True)
    
    def test_3(self):
        result = is_primo(3)
        self.assertEqual(result, True)
    
    def test_4(self):
        result = is_primo(4)
        self.assertEqual(result, False)
    
    def test_5(self):
        result = is_primo(5)
        self.assertEqual(result, True)

    def test_6(self):
        self.assertEqual(is_primo(6), False)

    

unittest.main() #esto es para que corra el test


