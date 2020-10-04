from igraph import *

# Funcao responsavel por criar vertices
def CriaVertices(nVertices):
    
    # Variaveis auxiliares
    identificadoresDosVertices = []
    nVertices = int(nVertices)
    i = 0    

    verticesGerados = {}  # verticesGerados = {0: ['1','2'], 1: ['0','1'], 2: ['1']}
    
    #Laço responsável pela criação dos vertices
    while i < nVertices:
        
        # auxIdentificador = input('identificador do vertice ' + str(i) + ': ')        
        
        identificadoresDosVertices.append(i)
        
        auxVerticesAdjacentes = input('''Coloque SEPARADO POR '-' os vertices adjacentes do vertice: ''' + str(i) + ''': ''')
        
        auxVerticesAdjacentes = auxVerticesAdjacentes.split('-')

        # Funcao responsavel por verificar se a quantidade de vertifces adjacentes é compativel com o numero de vertices do grafo
        verticesAdjacentes = VerificaNosAdjacentes(nVertices, auxVerticesAdjacentes)


        verticesGerados[i] = verticesAdjacentes

        i+=1
    
    #visualização preliminar
    print('\n \n \n \n \n')
    print('####### Descrição do Grafo: #######'+ '\n')
    print('Vertices e seus adjacentes temporário: '+ str(verticesGerados) + '\n')
    return verticesGerados, identificadoresDosVertices

#Funcao Responsavel por verificar se os nos adjacentes são validos
def VerificaNosAdjacentes(nVertices, VerticesAdjacentes):

    while len(VerticesAdjacentes) > nVertices-1:
        VerticesAdjacentes = input(''' Por favor coloque até ''' + str(nVertices-1) + ''' vertices separados por: '-' : ''')
        
        VerticesAdjacentes = VerticesAdjacentes.split('-')
    else:
        return VerticesAdjacentes

# Cria as arestas a partir dos nos adjacentes
def CriaArestas(vertices):
    auxArestas = []
    
    for v in vertices:
        for a in vertices[v]:
            if str(a)+'-'+str(v) in auxArestas:  #verifica se ja existe aresta com nos ao contrario
                pass
            else:
                auxArestas.append(str(v)+'-'+str(a))

    #converte o vetor de arestas em um vetor de tuplas
    auxTupla = []
    aux = []
    for k in auxArestas: 
        aux = k.split('-')
        if aux[0]=='': #Veririca se é um vertice sem vertices adjacentes
            aux[0]=aux[1]        
        if aux[1] == '':
            aux[1]=aux[0]
        else:
            auxTupla.append((int(aux[0]),int(aux[1])))


    return auxTupla

#Funcao que cria o grafico utilizando a biblioteca igrapg
def PlotaGrafo(orientado, nVertices, arestas, verticesLabel):
    if orientado == 'sim':
        g = Graph(directed=True)
    else:
        g = Graph()
    
    g.add_vertices(nVertices)
    g.add_edges(arestas)

    salvar =  plot(g, vertex_label=verticesLabel, vertex_color="black", vertex_label_color = "white", bbox=(600,600))

    salvar.save('grafoTemp.png')

#verifica a aresta existente e retornar o indice dela
def VerificaEcistenciaAresta(arestaDesjeda, arestas):

    arestaDesjeda = arestaDesjeda.split('-')
    arestaDesjeda = (int(arestaDesjeda[0]), int(arestaDesjeda[1]))
    
    auxPosicaoAresta = 0
   
   #verifica se aresta é igual ou inverso da aresta desejada
    for are in arestas:
        if arestaDesjeda == are or arestaDesjeda == (are[1], are[0]):
            return auxPosicaoAresta
        auxPosicaoAresta+=1

    return False


#Funcao responsável por retornar o grafo com a aresta em evidencia
def plotaGrafoArestaId(orientado, nVertices, arestas, verticesLabel, indiceAresta):
    if orientado == 'sim':
        g = Graph(directed=True)
    else:
        g = Graph()
    
    g.add_vertices(nVertices) 
    g.add_edges(arestas)

    #Cria o vetor com a aresta em evidencia
    #Logica: Se for o valor da indice da aresta, então coloca ele em evidencia, coloca um alto peso, 12
    auxContador = 0
    auxEvidencia = []
    while auxContador < len(arestas):
        if auxContador == indiceAresta:
            auxEvidencia.append(12)
        else:
            auxEvidencia.append(1)        
        auxContador += 1
    
    #propriedades do grafo
    g.es['weight'] = auxEvidencia
    
    grafo = {}
    grafo["vertex_label"] = verticesLabel
    grafo["vertex_color"] = "black"
    grafo["vertex_label_color"] = "white"
    grafo["edge_width"] = g.es['weight']
 
    plot(g, **grafo)
    # plot(g, vertex_label=verticesLabel, vertex_color="black", vertex_label_color = "white", "edge_width" = g.es['weight'], bbox=(600,600) )

#Funcao responsavel por listar as questões do trabalho
def Questoes():
    alternativa = input(''' 
    ######################################### 
    Escolhe a opção que deseja: \n
    a - Verificar a existência de uma determinada aresta. 
    b - Informar o grau de um dado vértice.
    c - Informar a lista de adjacência de um dado vértice.
    d - Verificar se o grafo é cíclico.
    #########################################
    ''')
     
    return alternativa


#FUncao responsavel por listar o grau do vertice
def InformaGrauVertice(vertice, arestas):
    auxGrau = 0
    for are in arestas:
        if vertice == are[0] or vertice == are[1]:
            auxGrau +=1
        
    return auxGrau    

#Funcao responsavel por listar a adjacencia de um vertice
def AdjacenciaDeUmVertice(vertice, arestas):
    listaAdjacencia = []

    for are in arestas:
        if vertice == are[0]: 
            listaAdjacencia.append(are[1])
        if vertice == are[1]:
            listaAdjacencia.append(are[0])

    return listaAdjacencia    

#Funcao responsavel por analisar se o grafo é ciclico
def InformaSeCiclico(arestas):

    auxCiclico = False
    auxValorAnterior = arestas[0][0]
    auxPosicao = 0    

    while auxPosicao < len(arestas):

        if auxPosicao == len(arestas) - 1 and arestas[auxPosicao][1] == 0:
            auxCiclico = True
            return auxCiclico

        if arestas[auxPosicao][1] == auxValorAnterior+1:
            auxCiclico = True
            auxValorAnterior = arestas[auxPosicao][1]
            auxPosicao +=1
        else:
            return False    

    return auxCiclico



#Funcao principal
def main():

    #Input CLI das informações do grafos
    orientado = input('O grafo é orientado? ')
    nVertices = input('Número de vertices do grafo: ')
    
    vertices = CriaVertices(nVertices)  # Chama a funcao que cria os vertices
    
    nVertices =  int(nVertices)
    verticesCriados = vertices[1]
    arestasCriadas = CriaArestas(vertices[0]) #cria as arestas a partir dos vertices cr

    #Descrição do grafo
    print('Número de vertices: ' + str(nVertices) + '\n')
    print('Vertices do grafos: ' + str(verticesCriados) + '\n')
    print('Arestas do grafo: '+ str(arestasCriadas) + '\n')

    #Criação do grafo oreintado ou n orientado
    PlotaGrafo(orientado, nVertices, arestasCriadas, verticesCriados)

    
    
    #espera as questões
    while True:
        escolha = Questoes()

        #A)Verifica a existencia da aresta, se sim chama a funcao que plota o grafo
        if escolha == 'a':
            arestaASerEncontrada = input('''Qual aresta deseja verificar, coloque separado por '-' os vertices: ''')
            verificaA = VerificaEcistenciaAresta(arestaASerEncontrada, arestasCriadas)
            if type(verificaA) == int:
                plotaGrafoArestaId(orientado, nVertices, arestasCriadas, verticesCriados, verificaA)
            else:
                print('Aresta invalida')    
        ###########################################################################

        #B) Informar o grau de um dado vértice. 
        if escolha == 'b':
            verticeEscolhido = int(input('    Qual vertice voce quer verificar o grau? \n' ))
            print('    Grau do vertice: ' + str(InformaGrauVertice(verticeEscolhido, arestasCriadas)) + '\n')
        ###########################################################################


        #C) Informar a lista de adjacência de um dado vértice.
        if escolha == 'c':
            verticeEscolhido = int(input('    Qual vertice voce quer listar a adjacencia? \n' ))
            print('    Lista de adjacencia: ' + str(AdjacenciaDeUmVertice(verticeEscolhido, arestasCriadas)) + '\n')
        ###########################################################################

        #D) Informar se o grafo é cíclico
        if escolha == 'd':
            if InformaSeCiclico(arestasCriadas):
                print("    Grafo ciclico!")
            else:
                print("    Grafo não é ciclico!")        
            
        ###########################################################################
        


if __name__ == "__main__":
    main()

