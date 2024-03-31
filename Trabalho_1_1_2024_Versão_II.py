# -*- coding: utf-8 -*-
"""
Created on Sat Mar 15 08:10:42 2024

@author: Alexandre Stuart Ramos de Almeida
"""

import time
import random
import numpy as np

def busca_sequencial(V, chave):
    for i in range(len(V)):
        if V[i] == chave:
            return i
    return -1

def busca_sequencial_otimizada(V, chave):
    for i in range(len(V)):
        if V[i] == chave:
            return i
        elif V[i] > chave:
            return -1
    return -1

def busca_binaria(V, chave):
    esquerda, direita = 0, len(V) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if V[meio] == chave:
            return meio
        elif V[meio] < chave:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1

def analise_empirica(n, q):
    tempo_busca_sequencial = []
    tempo_busca_sequencial_otimizada = []
    tempo_busca_binaria = []

    for _ in range(q):
        chave = random.randint(1, n)
        V = sorted(random.sample(range(1, n*10), n)) # Gera uma sequência ordenada aleatória

        inicio = time.time()
        busca_sequencial(V, chave)
        fim = time.time()
        tempo_busca_sequencial.append(fim - inicio)

        inicio = time.time()
        busca_sequencial_otimizada(V, chave)
        fim = time.time()
        tempo_busca_sequencial_otimizada.append(fim - inicio)

        inicio = time.time()
        busca_binaria(V, chave)
        fim = time.time()
        tempo_busca_binaria.append(fim - inicio)

    return np.mean(tempo_busca_sequencial), np.mean(tempo_busca_sequencial_otimizada), np.mean(tempo_busca_binaria)

def main():
    tamanhos_sequencia = [10**4, 10**5, 10**6, 10**7]
    num_buscas = 100

    for n in tamanhos_sequencia:
        tempo_sequencial, tempo_sequencial_otimizado, tempo_binario = analise_empirica(n, num_buscas)
        print(f"Tamanho da sequência: {n}")
        print(f"Tempo médio busca sequencial: {tempo_sequencial}")
        print(f"Tempo médio busca sequencial otimizada: {tempo_sequencial_otimizado}")
        print(f"Tempo médio busca binária: {tempo_binario}\n")

if __name__ == "__main__":
    main()
"""

Neste código:


- `main`: Realiza a análise empírica para diferentes tamanhos de sequência.

Este código gera sequências aleatórias de tamanhos variados e executa buscas para avaliar o desempenho dos diferentes algoritmos de busca.
"""