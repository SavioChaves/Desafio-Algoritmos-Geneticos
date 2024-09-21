import random

def calcular_fitness(individuo, pesos, valores, peso_maximo):
    peso_total = sum(p * i for p, i in zip(pesos, individuo))
    valor_total = sum(v * i for v, i in zip(valores, individuo))
    return valor_total if peso_total <= peso_maximo else 0

def gerar_individuo(tamanho):
    return [random.randint(0, 1) for _ in range(tamanho)]

def crossover(pai1, pai2):
    ponto_corte = random.randint(1, len(pai1) - 1)
    return pai1[:ponto_corte] + pai2[ponto_corte:]

def mutacao(individuo, taxa_mutacao):
    for i in range(len(individuo)):
        if random.random() < taxa_mutacao:
            individuo[i] = 1 - individuo[i]
    return individuo

def algoritmo_genetico(pesos, valores, peso_maximo, numero_de_cromossomos, geracoes):
    tamanho = len(pesos)
    populacao = [gerar_individuo(tamanho) for _ in range(numero_de_cromossomos)]
    melhores_individuos = []

    for _ in range(geracoes):
        populacao.sort(key=lambda ind: calcular_fitness(ind, pesos, valores, peso_maximo), reverse=True)
        melhores_individuos.append(populacao[0])
        
        nova_populacao = populacao[:2]
        while len(nova_populacao) < numero_de_cromossomos:
            pai1, pai2 = random.choices(populacao[:10], k=2)
            filho = crossover(pai1, pai2)
            filho = mutacao(filho, 0.01)
            nova_populacao.append(filho)
        
        populacao = nova_populacao

    melhores = [(calcular_fitness(ind, pesos, valores, peso_maximo), ind) for ind in melhores_individuos]
    return melhores

pesos_e_valores = [[2, 10], [4, 30], [6, 300], [8, 10], [8, 30], [8, 300],
                   [12, 50], [25, 75], [50, 100], [100, 400]]
pesos = [item[0] for item in pesos_e_valores]
valores = [item[1] for item in pesos_e_valores]
peso_maximo = 100
numero_de_cromossomos = 150
geracoes = 50

resultado = algoritmo_genetico(pesos, valores, peso_maximo, numero_de_cromossomos, geracoes)
for valor, individuo in resultado:
    print(valor, individuo)
