# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 11:04:35 2023

@author: paulo
"""
def max_idx(numbers):
    #calcula máximo da lista e retorna o máximo e o indice
    first_max = 0
    first_idx = 0
    for i in range(len(numbers)):
        if first_max < numbers[i]:
            first_max = numbers[i]
            first_idx = i
    
    #retorna a tupla com o máximo e o indice
    return (first_max, first_idx)


def max_pairwise_product(numbers):   
    #running time O(2n)
    #calcula primeiro máximo
    first_max_tuple = max_idx(numbers)
     
    #exclui primeiro máximo da lista    
    del(numbers[first_max_tuple[1]])
    
    #calcula segundo máximo
    second_max_tuple = max_idx(numbers)     

    #retorna o produto dos máximos encontrados
    return first_max_tuple[0] * second_max_tuple[0]



def max_pairwise_product_naive(numbers):
    #running time O(n^2)
    product = 0
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            product = max(product, numbers[i]*numbers[j])
    
    return product


def max_pairwise_product_sort(numbers):
    #running time O(nlogn)
    numbers.sort()
    return numbers[-1]*numbers[-2]


if __name__ == '__main__':
    #entrada não usada serve para dizer o tamanho da lista
    _ = int(input()) 
    
    #entrada da sequencia usada pelo algoritmo
    input_numbers = list(map(int, input().split()))  
    
    #imprime na tela o resultado da chamada a função
    print(max_pairwise_product(input_numbers))
    

##############  Testes #####################
def test_max_idx_msg(sequencia, valor_esperado):
    if max_idx(sequencia) != valor_esperado:
        print("ERRO na função max_idx() => Valor retornado: ", max_idx(sequencia), ", Valor esperado: ", valor_esperado)
        print("***") 
        
def test_max_idx():    
    test_max_idx_msg( [1,2,3,4,5] , (5,4) )  
    test_max_idx_msg( [1,2] , (2,1) )
    test_max_idx_msg( [2,1] , (2,0) )
    test_max_idx_msg( [0,1] , (1,1) )
    test_max_idx_msg( [0] , (0,0) )
    test_max_idx_msg( [0,0,0] , (0,0) )
    test_max_idx_msg( [2,2,2,2] , (2,0) )
    test_max_idx_msg( [0,2,2,0] , (2,1) )
    

def test_max_pairwise_product_msg(sequencia, valor_esperado):  
    import time    
    #medição do tempo        
    antes = time.time()
    resultado = max_pairwise_product(sequencia)
    depois = time.time()        
    tempo = depois - antes      
        
    if  resultado != valor_esperado:
        print("ERRO na função max_pairwise_product() => Valor retornado: ", max_pairwise_product(sequencia), ", Valor esperado: ", valor_esperado)
        print("***") 
    else:
        print("Tempo de execução de sequencia de comprimento " + str(len(sequencia)+1) + ": " + str(tempo) + " segundos." )
        
def test_max_pairwise_product():    
    test_max_pairwise_product_msg( [1,2,3,4,5] , 20 )          
    test_max_pairwise_product_msg( [1,2,3] , 6 )      
    test_max_pairwise_product_msg( [7,5,14,2,8,8,10,1,2,3] , 140 )  
    test_max_pairwise_product_msg( [0,1] , 0 )  
    test_max_pairwise_product_msg( [0] , 0 )
    test_max_pairwise_product_msg( [1] , 0 )
    test_max_pairwise_product_msg( [1,1,1,1,1,1] , 1 )
    test_max_pairwise_product_msg( [2,2,2,2,2,2] , 4 )
    test_max_pairwise_product_msg( sequencia_ones_random_2(100) , 2 )
    test_max_pairwise_product_msg( sequencia_ones_random_2(1000) , 2 )
    test_max_pairwise_product_msg( sequencia_ones_random_2(10000) , 2 )
    
    sequencia_tupla_stress = sequencia_2x10eN(5)
    test_max_pairwise_product_msg( sequencia_tupla_stress[0] , sequencia_tupla_stress[1] )



def sequencia_ones_random_2(n):    
    import numpy as np
    tamanho = int(np.random.rand(1)*n)
    #print("tamanho: ", tamanho)
    
    lista_ones = []    
    for i in range(tamanho):
        lista_ones.append(1)    
    
    #print("list_ones: ", lista_ones)

    indice = int(np.random.rand(1)*(tamanho-1))
    #print("indice:", indice)
    sequencia = lista_ones[:]
    #print("sequencia antes:", sequencia)
    sequencia[indice] = 2
    #print("sequencia depois: ", sequencia)
    
    return sequencia
  

    
def sequencia_2x10eN(n):    
    sequencia = []
    i = 1
    while i <= (2*10**n):
        sequencia.append(i)
        i = i + 1    
    
    produto = sequencia[-1] * sequencia[-2]     
    return sequencia, produto


def aleatorio_entre(inicio, fim):
    import numpy as np
    n_random = np.random.default_rng()
    n_array = n_random.integers(low=inicio, high=fim+1, size=1)
    
    return n_array[0]


def lista_aleatoria_entre(inicio, fim, tamanho):
    lista = []
    for i in range(tamanho):
        lista.append(aleatorio_entre(inicio, fim))
        
    return lista


def stress_test(N,M):
    import numpy as np   
    import time    
            
     
    
    saida = True
    while saida == True:
        n = aleatorio_entre(2, N)        
        a = []
        for i in range(0, n):
            m = aleatorio_entre(0, M)
            a.append(m)
        
        print(a)
        
        b=a[:]
        c=a[:]
        d=a[:]
        
        antes_fast = time.time()
        resultado_fast = max_pairwise_product(b)
        depois_fast = time.time()        
        tempo_fast = depois_fast - antes_fast 
        
        antes_naive = time.time()
        resultado_naive = max_pairwise_product_naive(c)
        depois_naive = time.time()        
        tempo_naive = depois_naive - antes_naive 
        
        antes_sort = time.time()
        resultado_sort = max_pairwise_product_sort(d)
        depois_sort = time.time()        
        tempo_sort = depois_sort - antes_sort
        
        print("Resultado Fast: ", resultado_fast , ", Resultado Naive: ", resultado_naive , ", Resultado Sort: ", resultado_sort)
        print("Tempo Fast: ", tempo_fast*1000 , "ms, Tempo Naive: ", tempo_naive*1000, "ms, Tempo Sort: ", tempo_sort*1000, "ms.")
        
        if resultado_fast == resultado_naive == resultado_sort:
            print("OK")
        else:
            print("Wrong answer: ", resultado_fast, resultado_naive, resultado_sort)
            saida = False
        
    return a, resultado_fast, resultado_naive, resultado_sort
    
    
    
    
    
    
    