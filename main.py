#from funcGrafo import *
import funcGrafo as Grafo
import initGrafo as init


vertices = []
arestas = []
quantVertices = 0
quantArestas = 0
tipoGrafo = ''
MatrizAdjacencia = []


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

#endfile = 'grafo1.txt'







while(True):
    print('Escolha umas das opções Abaixo:')
    print('1 - Vericas se dois vertices são adjacentes')
    print('2 - Calcula Grau de um Vertices')
    print('3 - Busca Vizinhos de um Vertice Qualquer')
    print('4 - Visitar todas as Arestas do Grafo')
    print('5 - Desenha Grafo')
    print('6 - Carregar outro Arquivo de Vertices')
    print('7 - Sair')
    
    opcao = input("Opção: ")
    
    if opcao == '1':
        vertice1 = input("Entre com a vertice 1: ")
        vertice2 = input("Entre com a vertice 2: ")
        isAdjacentes = Grafo.verAdjacenciaVertices(vertice1, vertice2, vertices, MatrizAdjacencia)
        if isAdjacentes:
            print('')
            print('As vertices ', vertice1, ' e ', vertice2 ,' são adjacentes')
            print('')
        else:
            print('')
            print('As vertices', vertice1, ' e ', vertice2 ,' não são adjacentes')
            print('')
    elif opcao == '2':
        vertice1 = input("Entre com a vertice: ")
        grauVertice = Grafo.calcularGrauVertices(vertice1, vertices, MatrizAdjacencia, tipoGrafo)
        print('')
        print(grauVertice)
        print('')
    elif opcao == '3':
        vertice1 = input("Entre com a vertice: ")
        vizinhos = Grafo.buscaVerticesVizinhas(vertice1, vertices, MatrizAdjacencia, tipoGrafo)
        print('')
        print(vizinhos)
        print('')
    elif opcao == '4':
        print('')
        Grafo.visitarVertices(vertices, MatrizAdjacencia)
        print('')
    elif opcao == '5':
        print('')
        Grafo.desenhaDiGrafo(arestas, tipoGrafo)
        print('')
    elif opcao == '6':
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
    elif opcao == '7':
        quit()










        

