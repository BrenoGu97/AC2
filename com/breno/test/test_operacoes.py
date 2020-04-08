from unittest import TestCase
from com.breno.operacoes import Operacoes

class TestOperacoes(TestCase):

    def setUp(self):
        self.operacoes = Operacoes()
    
    def test_soma(self):
        self.assertEqual(self.operacoes.soma([9, 1]), 10, "Retorna 10")