import unittest
from funciones import primo, cubica, saludo


class Testfunciones(unittest.TestCase):
    def test_primo(self):
        self.assertIn("No se permiten números negativos.", primo(-10)) #if num<0
       
        self.assertFalse(primo(0), 1) #if num<=1

        self.assertTrue(primo(2),2) #if num==2

        self.assertEqual(primo(8),0) # if num%2 

        self.assertEqual(primo(7),1) #for n
        self.assertEqual(primo(16),0)

    def test_cubica(self):
        self.assertEqual(cubica(0),0)
        self.assertEqual(cubica(1),1)
        self.assertEqual(cubica(-3), -27)
    
    def test_saludo(self):
        self.assertEqual(saludo("Israel"), "Hola, Israel")
        self.assertEqual(saludo("Francisco"), "Hola, Francisco")
        self.assertIn(saludo("Israel"), "Hola, Israel")
        self.assertIn(saludo("Israel"), "Hola, Israel")



if __name__=="__main__":
    unittest.main()
