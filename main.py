import numpy as np
import random

# distância entre a cidade j e i (de colunas para linhas)
distancias = np.array([
    [  0,  10,  15,  45,   5,  45,  50,  44,  30, 100,  67,  33,  90,  17,  50],
    [ 15,   0, 100,  30,  20,  25,  80,  45,  41,   5,  45,  10,  90,  10,  35],
    [ 40,  80,   0,  90,  70,  33, 100,  70,  30,  23,  80,  60,  47,  33,  25],
    [100,   8,   5,   0,   5,  40,  21,  20,  35,  14,  55,  35,  21,   5,  40],
    [ 17,  10,  33,  45,   0,  14,  50,  27,  33,  60,  17,  10,  20,  13,  71],
    [ 15,  70,  90,  20,  11,   0,  15,  35,  30,  15,  18,  35,  15,  90,  23],
    [ 25,  19,  18,  30, 100,  55,   0,  70,  55,  41,  55, 100,  18,  14,  18],
    [ 40,  15,  60,  45,  70,  33,  25,   0,  27,  60,  80,  35,  30,  41,  35],
    [ 21,  34,  17,  10,  11,  40,   8,  32,   0,  47,  76,  40,  21,  90,  21],
    [ 35, 100,   5,  18,  43,  25,  14,  30,  39,   0,  17,  35,  15,  13,  40],
    [ 38,  20,  23,  30,   5,  55,  50,  33,  70,  14,   0,  60,  30,  35,  21],
    [ 15,  14,  45,  21, 100,  10,   8,  20,  35,  43,   8,   0,  15, 100,  23],
    [ 80,  10,   5,  20,  35,   8,  90,   5,  44,  10,  80,  14,   0,  25,  80],
    [ 33,  90,  40,  18,  70,  45,  25,  23,  90,  44,  43,  70,   5,   0,  25],
    [ 25,  70,  45,  50,   5,  45,  20, 100,  25,  50,  35,  10,  90,   5,   0],
])

qtd_individuos = 100
tx_mutacao = 0.5
qtd_iteracoes = 1000
qtd_permutacoes_mutacao = 7

def calculo_fitness(individuo:np.ndarray):
    distancia_final = 0
    cidade_anterior = 0

    for cidade in individuo:
        distancia_final += distancias[cidade][cidade_anterior]
        cidade_anterior = cidade

    return (distancia_final + distancias[0][cidade_anterior])

def gerar_populacao(qtd_individuos):
    populacao = []

    for _ in range(qtd_individuos):
        populacao.append(np.random.permutation(range(1,15)))

    return populacao

def reproduzir(pai, mae):
    ponto_de_cruzamento = random.randint(1,len(pai)-2)
    contribuicao_do_pai = pai[:ponto_de_cruzamento]
    contribuicao_da_mae = [cidade for cidade in mae if not cidade in contribuicao_do_pai]
    
    return np.concatenate((contribuicao_do_pai, contribuicao_da_mae))

def mutacao(individuo):
    for _ in range(qtd_permutacoes_mutacao):
        if(random.random() < tx_mutacao):
            indice_1, indice_2 = gerar_indices_diferentes(14)
            
            individuo[indice_2], individuo[indice_1] = individuo[indice_1], individuo[indice_2]
    
    return individuo


def gerar_indices_diferentes(tamanho):
    
    indice_1 = random.randint(1, tamanho-1)
    indice_2 = random.randint(1, tamanho-1)
    
    while indice_1 == indice_2:
        indice_2 = random.randint(1, tamanho-1)
    
    return indice_1, indice_2


populacao = gerar_populacao(qtd_individuos)

for i in range(qtd_iteracoes):
    nova_populacao = []

    for _ in range(qtd_individuos):
        indice_1, indice_2 = gerar_indices_diferentes(qtd_individuos)

        pai = populacao[indice_1]
        mae = populacao[indice_2]

        filho = reproduzir(pai, mae)
        filho = mutacao(filho)
        nova_populacao.append(filho)
    # print(f"iteração: {i}")
    populacao = nova_populacao


nova_populacao.sort(key=lambda x:calculo_fitness(x))
print(f"melhor fitness: {calculo_fitness(nova_populacao[0])}")
print(f"melhor rota: {nova_populacao[0]}")

