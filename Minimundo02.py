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

class Impressora:

    def __init__(self,codigo,desc, vel,serv):
        self.codigo = codigo
        self.descricao = desc
        self.velocidade = vel
        self.servidor = serv

    def retorna_servidor(self):
        return self.servidor


class Micro:

    def __init__(self, codigo, desc, capacidade, mem):
        self.codigo_patrimonio = codigo
        self.descricao = desc
        self.capacidade = capacidade
        self.memoria = mem


class Estacao(Micro):

     def __init__(self, codigo, desc, capacidade, mem, local):
        Micro.__init__(self, codigo, desc, capacidade, mem)
        self.localizacao = local



