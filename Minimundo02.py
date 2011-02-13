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


class Micro(object):

    def __init__(self, codigo, desc, capacidade, mem):
        self.codigo_patrimonio = codigo
        self.descricao = desc
        self.capacidade = capacidade
        self.memoria = mem


class Estacao(Micro):

     def __init__(self, codigo, desc, capacidade, mem, local):
        Micro.__init__(self, codigo, desc, capacidade, mem)
        self.localizacao = local

     def retornaPai(self):
        self.pai = Estacao.__bases__
        return self.pai

     def retornaDescEstacao(self):
        return self.descricao

class Servidor(Micro):

    def __init__(self, codigo, desc, capacidade, mem, tamBuffer, qtdMaxBuffer):
        Micro.__init__(self, codigo, desc, capacidade, mem)
        self.tamBuffer = tamBuffer
        self.qtdMaxBuffer = qtdMaxBuffer

    def retornaPai(self):
        self.pai = Servidor.__bases__
        return self.pai

class Usuario():

    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

    def retornaNome(self):
        return self.nome

    def usarEstacao(self, Estacao):
        self.estacao = Estacao

    def retornaEstacao(self):
        return self.estacao.retornaDescEstacao()


