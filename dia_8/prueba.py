import unittest
import BuscarErroresUnittest

class ProbarCambiaTexto(unittest.TestCase):
    

    def test_mayusculas(self):
        palabra = 'buen dia'
        resultado = BuscarErroresUnittest.todo_mayus(palabra)
        self.assertEqual(resultado,'BUEN DIA')

if __name__ == '__main__': #es una forma de decirle a python que debemos iniciar por aquí con main
    unittest.main()

