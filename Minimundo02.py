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

    def __init__(self,codigo,desc, vel,serv):  #Contrutor da classe Impressora
        self.codigo = codigo
        self.descricao = desc
        self.velocidade = vel
        self.servidor = serv

    def retorna_servidor(self):
        return self.servidor

class Arquivo:
    def __init__(self, nomeArq):
        self.nomeArquivo = nomeArq

class Micro(object):

    def __init__(self, codigo, desc, capacidade, mem):  #Contrutor da classe Micro
        self.codigo_patrimonio = codigo
        self.descricao = desc
        self.capacidade = capacidade
        self.memoria = mem


class Estacao(Micro):

     def __init__(self, codigo, desc, capacidade, mem, local):    #Contrutor da classe Estacao
        Micro.__init__(self, codigo, desc, capacidade, mem)
        self.localizacao = local

     def __del__(self):      #Destrutor da classe Estacao
        print "Destrutor chamado."

     def retornaPai(self):
        self.pai = Estacao.__bases__
        return self.pai

     def retornaDescEstacao(self):
        return self.descricao

class Servidor(Micro):

    def __init__(self, codigo, desc, capacidade, mem, tamBuffer, qtdMaxBuffer):  #Contrutor da classe Servidor
        Micro.__init__(self, codigo, desc, capacidade, mem)
        self.tamBuffer = tamBuffer
        self.qtdMaxBuffer = qtdMaxBuffer

    def retornaPai(self):
        self.pai = Servidor.__bases__
        return self.pai

class Usuario():

    def __init__(self, nome, senha, permImpressao):  #Contrutor da classe Usuario
        self.nome = nome
        self.senha = senha
        self.ConecAtiva = 'NAO'
        if permImpressao == 'SIM' or permImpressao == 'NAO':
            self.permImpressao = permImpressao
        else:
            print "Permissao para impressao somente pode ser 'SIM' ou 'NAO'."

    def retornaNome(self):
        return self.nome

    def usarEstacao(self, Estacao):
        #verificar se usu?rio j? possui coneccao ativa
        if self.ConecAtiva == 'SIM':
            print "Usuario %s ja possui coneccao ATIVA na estacao %s" %(self.nome, self.estacao.descricao)
        elif self.ConecAtiva == 'NAO':
            self.estacao = Estacao
            self.ConecAtiva = 'SIM'

    def sairEstacao(self, Estacao):
        self.ConecAtiva = 'NAO'
        self.estacao = Estacao.__del__ #chamada do destrutor da classe Estacao

    def mostraEstacaoUsuario(self):
        if self.ConecAtiva == 'NAO':
            print "Usuario %s nao possui coneccao ATIVA em nenhuma estacao" %(self.nome)
        elif self.ConecAtiva == 'SIM':
            print " Codigo: %f \n Descricao: %s \n Capacidade: %f \n Memoria: %f \n Local: %s" %(self.estacao.codigo_patrimonio,self.estacao.descricao,self.estacao.capacidade, self.estacao.memoria, self.estacao.localizacao)

    def criarArquivo(self, nomeArq):
        self.arquivo = Arquivo(nomeArq)   #verificar como fazer para cada vez que o mesmo usu?rio criar um arquivo o mesmo ser armazenado em uma lista

    def solicitarImpressaoArq(self, Arquivo, Impressora):
        if self.ConecAtiva == 'NAO':
            print "Usuario %s nao possui coneccao ATIVA, portanto n?o pode imprimir" %(self.nome)
        elif self.permImpressao == 'NAO':
            print "Usuario %s nao tem permissao para imprimir arquivo" %(self.nome)
        elif self.ConecAtiva == 'SIM' and self.permImpressao == 'SIM':
            self.impressora = Impressora
            print "O arquivo %s ser? impresso na impressora %s" %(self.arquivo.nomeArquivo, self.impressora.descricao)

    def teste(self):
        pass