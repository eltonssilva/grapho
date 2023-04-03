#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 11:03:57 2020

@author: Elton de Sousa e Silva
"""
import funcGrafo as Grafo

def initGrafo():  #Dado um Arquivo Retorna Arestas e o Tipo de Grafo
    
    tipoGrafoArestas = Grafo.getArestasFromFile()
    tipoGrafo = tipoGrafoArestas[0]
    
    if tipoGrafo == 'ND':
        print('Tipo Grafo Não Direcionado')
    else:
        print('Tipo Grafo Direcionado')
        
    arestas = tipoGrafoArestas[1]
    print('')
    print('Lista de Arestas')
    print(arestas)
    print('')
    quantArestas = len(arestas)
    print('Quantidade de Arestas: ', quantArestas)
    vertices = Grafo.buscaVertices(arestas)
    print('')
    print('Lista de Vertices')
    print(vertices)
    print('')
    quantVertices = len(vertices)
    print('Quantidade de Vertices (Ordem): ', quantVertices)
    MatrizAdjacencia = Grafo.criarMatrizAdjacencia(vertices, arestas, tipoGrafo)
    print('')
    print('Matriz de Adjacencia')
    print (MatrizAdjacencia)
    
    
    print('')
    print('**************************************************')