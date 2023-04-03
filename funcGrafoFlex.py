#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 09:13:29 2020

@author: Elton de Sousa e Silva
"""

import numpy as np
import networkx as nx
import pydot
from networkx.drawing.nx_agraph import write_dot, graphviz_layout
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
        endfile = 'devices.txt'
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
        linhasarquivos.append(linha.split()[0])
    _file.close()
    tipografo = 'D'
    #del linhasarquivos[0]
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

def listarNomes(_arestas):         #Recebe uma lista de Aresta e Devolve uma Lista de Nomes
    listaNomes = []
    for item in _arestas:
        itemExplodido = item.split(',');
        listaNomes.append(itemExplodido[3])
        listaNomes.append(itemExplodido[5])
        listaNomes = remove_repetidos(listaNomes)
    return listaNomes



def desenhaDiGrafo(_arestas, _tipoGrafo):          #Função para Plotar Digrafo com a Biblioteca NetWorks
    G = nx.DiGraph()
    if _tipoGrafo == 'ND':
        print('Entrou nao direct')
        G = nx.Graph()
    
    newVertices = parseVertices(_arestas)
    print(newVertices)
    G.add_edges_from(newVertices)
    nx.nx_agraph.write_dot(G,'test.dot')

    return
    T = nx.bfs_tree(G,'MASTER',  '806A')
    pos = nx.layout.planar_layout(T)
    plt.figure(figsize=(10,6))

    nx.draw_networkx_nodes(T, pos, node_size=500, node_color='lightblue', node_shape='o')
    nx.draw_networkx_edges(T, pos, edge_color='gray', width=2, alpha=0.8, arrows=False)
    nx.draw_networkx_labels(T, pos, font_size=14, font_weight='bold', font_family='sans-serif')
    
    #nx.draw(T,  with_labels=True,  node_size = 1500)
    #plt.axis('off')
    plt.draw()
    plt.show()
    return

def parseVertices(_arestas):           #Transforma minhas vertices no formato aceito pela API.
    newVertices = []
    for item in _arestas:
        itemExplodido = item.split(',');
        newVertices.append((itemExplodido[3], itemExplodido[5]))
    return newVertices




    



