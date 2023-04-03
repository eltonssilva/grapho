#from funcGrafo import *
import funcGrafoFlex as Grafo
import initGrafo as init

vertices = []
arestas = []
quantVertices = 0
quantArestas = 0
tipoGrafo = ''
MatrizAdjacencia = []

tipoGrafoArestas = Grafo.getArestasFromFile()
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


Grafo.desenhaDiGrafo(arestas, tipoGrafo)