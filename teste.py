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
class test(unittest.TestCase):

##    def setUp(self):
##        self.imp = Impressora(1,"Impressora - 1", 200, "x")
##
##    def testa_lig_a_servidor(self):
##        '''Testa se a impressora esta ligada a algum servidor'''
##        self.assertTrue(self.imp.retorna_servidor())

    def setUp(self):
        self.estacao = Estacao( 1, "Estacao 1", 10, 400, "Macae")

    def testa_estacao(self):
        '''Testa se estacao e um micro'''
        self.assertEqual(Estacao.__bases__,"Micro")

if __name__ == "__main__":
    unittest.main()
