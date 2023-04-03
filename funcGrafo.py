#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 09:13:29 2020

@author: Elton de Sousa e Silva
"""

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path
import os


class Vertice:
    label = ''
    def __init__(self, label):
        self.label = label          #Nome ou Identificação da Vertice
        self.visitado = False       #Inicie a Vertice como não visitado Claro
    def visitado(self):             #Crio uma função para setar a vertice como visitado
        self.visitado = True
    def __str__(self):              # Metodo Print Padrão
        return self.label
    def __repr__(self):             #Metodo Print Padrão quando em uma lista
        return self.label

def getArestasFromFile():  #Dado um Arquivo Retorna Arestas e o Tipo de Grafo
    os.system('clear')
    print('Bom dia Professor Blz..')
    endOK = True
    while(endOK):
        endfile = input("Qual a localização do arquivo: ")
        my_file = Path(endfile)
        if (my_file.is_file()==False):
            os.system('clear')
            print('Erro ao Localizar o Arquivo')
            print('Verifique o endereço digitado.')
            endOK = True
        else:
            os.system('clear')
            print('Arquivo Aberto: ', endfile)
            print('')
            endOK = False
    _file = open(endfile,'r')
    linhasarquivos = []
    for linha in _file:
        linhasarquivos.append(linha.split()[0]);
    _file.close()
    tipografo = linhasarquivos[0]
    del linhasarquivos[0]
    _arestas = [tipografo, linhasarquivos]
    return _arestas              #Na Posicao 0 o tipo de Grafo na Posicao 1 as arestas



def busca(aresta):
    print('Tipo Grafo Direcionado:', aresta)
    return

def criarMatrizAdjacencia(_vertices, _arestas, _tipoGrafo):
    _matriz = np.zeros(shape=(len(_vertices),len(_vertices)))
    if _tipoGrafo == 'ND':
        for j in _arestas:
            _itemExplodido = j.split(',');
            linha = _vertices.index(_itemExplodido[3])
            coluna = _vertices.index(_itemExplodido[5])
            _matriz[linha][coluna] = 1
            _matriz[coluna][linha] = 1
    else:
        for j in _arestas:
            _itemExplodido = j.split(',');
            linha = _vertices.index(_itemExplodido[3])
            coluna = _vertices.index(_itemExplodido[5])
            _matriz[linha][coluna] = 1
    return _matriz

def visitarVertices(_vertices, _MatrizAdjacencia):
    isVisitado = np.zeros(shape=(len(_vertices),len(_vertices)))
    x = 0
    for i in _vertices:
        y = 0
        for j in _vertices:
            if y == 0:
                print ('Vertice ' + i)
            if _MatrizAdjacencia[x][y] == 1 and isVisitado[y][x] !=1:
                isVisitado[x][y] =1
                print ('        ' + j + ' Visitado')
            y = y+1
        x = x+1
    return
    


def remove_repetidos(lista):    #Remover Itens repedidos das listas e ordena as vertices
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l

    
def buscaVertices(_arestas):         #Recebe uma lista de Aresta e Devolve uma Lista de Vertices
    listavertice = []
    for item in _arestas:
        itemExplodido = item.split(',');
        listavertice.append(itemExplodido[3])
        listavertice.append(itemExplodido[5])
        listavertice = remove_repetidos(listavertice)
    return listavertice

def calcularGrauVertices(_vertice, _vertices, _MatrizAdjacencia,  _tipoGrafo):  #Calcula o Grau de um Vertice 
    if _tipoGrafo == 'ND':
        if _vertice not in _vertices:
            return 'A Vertice ' + _vertice + ' não pertece ao grafo'
        linha = _vertices.index(_vertice)
        print(linha)
        linhaGrau = _MatrizAdjacencia[linha]
        colunaGrau = _MatrizAdjacencia.T[linha]
        _grau = np.sum(linhaGrau)
        
        return 'A vertice ' + str(_vertice)  + ' tem grau '+  str(_grau)
    else:
        if _vertice not in _vertices:
            return 'A Vertice ' + _vertice + ' não pertece ao grafo'
        linha = _vertices.index(_vertice)
        print(linha)
        linhaGrau = _MatrizAdjacencia[linha]
        colunaGrau = _MatrizAdjacencia.T[linha]
        _grausaida = np.sum(linhaGrau)
        _grauentrada = np.sum(colunaGrau)
        return  'A vertice ' + str(_vertice) + ' tem: ' + str(_grausaida) + ' de Saide e ' + str(_grauentrada)  + ' de Entrada'  
    
def verAdjacenciaVertices(_vertice1, _vertice2 , _vertices, _MatrizAdjacencia):
    if _vertice1 not in _vertices:
        return  False #Verifica se a Vertice Pertence ao grafo
    if _vertice2 not in _vertices:
        return  False #Verifica se a Vertice Pertence ao grafo
    linha = _vertices.index(_vertice1)
    coluna = _vertices.index(_vertice2)
    if _MatrizAdjacencia[linha][coluna] == 1:
        return True
    else:
        return False
def buscaVerticesVizinhas(_vertice, _vertices, _MatrizAdjacencia, _tipoGrafo):  #Busca Vertices Vizinhas
    if _vertice not in _vertices:
        return 'A Vertice ' + _vertice + ' não pertece ao grafo'
    linha = _vertices.index(_vertice)
    if _tipoGrafo == 'ND':
        _linhaAdj = _MatrizAdjacencia[linha]
        vizinhos = ''
        j = 0;
        for i in _linhaAdj:
            if i == 1:
                vizinhos = vizinhos + _vertices[j] + ' - '
            j = j+1
        return 'Vizinhos da Vertice ' + _vertice + ': ' + vizinhos
    else:
        _MatrizAdjacenciaT = _MatrizAdjacencia.T
        _linhaAdj = _MatrizAdjacencia[linha] + _MatrizAdjacenciaT[linha]
        
        vizinhos = ''
        j = 0;
        for i in _linhaAdj:
            if i >= 1:
                vizinhos = vizinhos + _vertices[j] + ' - '
            j = j+1
        return 'Vizinhos da Vertice ' + _vertice + ': ' + vizinhos

def desenhaDiGrafo(_arestas, _tipoGrafo):          #Função para Plotar Digrafo com a Biblioteca NetWorks
    G = nx.DiGraph()
    if _tipoGrafo == 'ND':
        print('Entrou nao direct')
        G = nx.Graph()
    
    newVertices = parseVertices(_arestas)
    G.add_edges_from(newVertices)
    nx.draw(G, with_labels=True,  node_size = 1500)
    plt.draw()
    plt.show()
    return

def parseVertices(_arestas):           #Transforma minhas vertices no formato aceito pela API.
    newVertices = []
    for item in _arestas:
        itemExplodido = item.split(',');
        newVertices.append((itemExplodido[3], itemExplodido[5]))
    return newVertices




    



