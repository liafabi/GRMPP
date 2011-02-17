#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      FRC
#
# Created:     11/02/2011
# Copyright:   (c) FRC 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import unittest
from Minimundo02 import Impressora
from Minimundo02 import Estacao
from Minimundo02 import Usuario
class test(unittest.TestCase):

##    def setUp(self):
##        self.imp = Impressora(1,"Impressora - 1", 200, "x")
##
##    def testa_lig_a_servidor(self):
##        '''Testa se a impressora esta ligada a algum servidor'''
##        self.assertTrue(self.imp.retorna_servidor())

##    def setUp(self):
##        self.estacao = Estacao( 1, "Estacao 1", 10, 400, "Macae")
##
##    def testa_estacao(self):
##        '''Testa se estacao e um micro'''
##        self.assertEqual(self.estacao.retornaPai(),"Micro")

    def setUp(self):
        self.usu = Usuario("Fabiola",123, 'NAO')
        self.est = Estacao(1,"Estacao 1",200,4,"macae")
        self.usu.usarEstacao(self.est)

    def testaNome(self):
        '''Testa se o usuario possui nome'''
        self.assertEqual(self.usu.retornaNome(),'Fabiola')

    def testaDescEstacacaoUsua(self):
        '''Verifica se o usuario esta conectado a uma estacao'''
        self.assertEqual(self.usu.estacao.descricao,"Estacao 1", )

    def testaConeccaoAtiva(self):
        '''verifica se usuario ja possui coneccao ATIVA'''
        self.assertEqual(self.usu.ConecAtiva, "SIM", "Usuario nao possui coneccao ATIVA")

    def podeImprimir(self):
        '''Verifica se usuario pode imprimir'''
        self.testaConeccaoAtiva()
        self.assertEqual(self.usu.permImpressao, "SIM", "Usuario possui permissao de impressao")

    def verificaUsuarioImpressora(self):
        '''Verifica se usuario escolhe a impressora'''
        self.assertTrue(self.usu.mostraImpressora())

if __name__ == "__main__":
    unittest.main()
