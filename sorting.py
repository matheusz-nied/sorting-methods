import util
import time

# InsertionSort


def InsertionSort(array):
    ini = time.time()
    quantidade_troca = 0
    quantidade_comparacao = 0
    tempo_gasto = 0

    i = 0
    temp = []
    for data in array:

        j = i
        i += 1

        quantidade_comparacao += 1
        while(j > 0 and array[j][0] < array[j - 1][0]):
            quantidade_comparacao += 1

            temp = array[j]
            array[j] = array[j - 1]
            j = j - 1
            array[j] = temp
            quantidade_troca += 1

    fim = time.time()
    tempo_gasto = fim - ini

    return quantidade_comparacao, quantidade_troca, tempo_gasto


# SelectionSort
def SelectionSort(array):
    ini = time.time()
    quantidade_troca = 0
    quantidade_comparacao = 1
    tempo_gasto = 0

    number_lines = util.count_array(array)
    i = 0
    for data in array:
        menor = i
        j = i + 1

        while(j < number_lines):
            quantidade_comparacao += 1
            if(array[j][0] < array[menor][0]):
                menor = j
            j += 1

        quantidade_comparacao += 1
        if(menor != i):
            quantidade_troca += 1
            temp = array[i]
            array[i] = array[menor]
            array[menor] = temp

        i += 1

    fim = time.time()
    tempo_gasto = fim - ini
    return quantidade_comparacao, quantidade_troca, tempo_gasto


# MergeSort
def MergeSort(array):
    ini = time.time()
    quantidade_troca = [0]
    quantidade_comparacao = [0]
    tempo_gasto = 0

    def ordena_mergesort(array, aux, esquerda, direita, quantidade_comparacao, quantidade_troca):
        quantidade_comparacao[0] += 1
        if direita <= esquerda:
            return
        meio = (esquerda + direita) // 2

        # Ordena a primeira metade do arranjo.
        ordena_mergesort(array, aux, esquerda, meio, quantidade_comparacao, quantidade_troca)

        # Ordena a segunda metade do arranjo.
        ordena_mergesort(array, aux, meio + 1, direita, quantidade_comparacao, quantidade_troca)

        # Combina as duas metades ordenadas anteriormente.
        merge(array, aux, esquerda, meio, direita, quantidade_comparacao, quantidade_troca)

    def merge(array, aux, esquerda, meio, direita, quantidade_comparacao, quantidade_troca):

        for k in range(esquerda, direita + 1):
            aux[k] = array[k]
        i = esquerda
        j = meio + 1
        for k in range(esquerda, direita + 1):
            quantidade_comparacao[0] += 1
            if i > meio:
                quantidade_troca[0]+=1
                array[k] = aux[j]
                j += 1
            elif j > direita:
                quantidade_comparacao[0] += 1
                quantidade_troca[0]+=1
                array[k] = aux[i]
                i += 1
            elif aux[j] < aux[i]:
                quantidade_comparacao[0] += 1
                quantidade_troca[0]+=1
                array[k] = aux[j]
                j += 1
            else:
                quantidade_comparacao[0] += 1
                array[k] = aux[i]
                i += 1

    aux = [0] * len(array)
    ordena_mergesort(array, aux, 0, len(array) - 1, quantidade_comparacao, quantidade_troca)

    fim = time.time()
    tempo_gasto = fim - ini
    return quantidade_comparacao, quantidade_troca, tempo_gasto


# QuickSort
def QuickSort(array):
    ini = time.time()
    quantidade_troca = [0]
    quantidade_comparacao = [0]
    tempo_gasto = 0
    
    tamanho_array = len(array)
    
    def quick_sort(lista, inicio, fim, quantidade_comparacao, quantidade_troca):
        quantidade_comparacao[0] += 1
        if inicio > fim:
            return
        anterior = inicio
        posterior = fim
        pivo = lista[inicio]

        quantidade_comparacao[0] += 1
        while anterior < posterior:
            quantidade_comparacao[0] += 1

            while anterior < posterior and lista[posterior] > pivo:
                quantidade_comparacao[0] += 1
                posterior = posterior - 1

            quantidade_comparacao[0] += 1
            if anterior < posterior:
                lista[anterior] = lista[posterior]
                anterior = anterior + 1
                quantidade_troca[0] +=1
            
            while anterior < posterior and lista[anterior] <= pivo:
                quantidade_comparacao[0] += 1
                anterior = anterior + 1
                
            quantidade_comparacao[0] += 1
            
            if anterior < posterior:
                lista[posterior] = lista[anterior]
                posterior = posterior - 1
                quantidade_troca[0] +=1

            lista[anterior] = pivo
            quantidade_troca[0] +=1
        quick_sort(lista, inicio, anterior - 1, quantidade_comparacao, quantidade_troca)
        quick_sort(lista, anterior + 1, fim, quantidade_comparacao, quantidade_troca)

    quick_sort(array, 0, tamanho_array - 1, quantidade_comparacao, quantidade_troca)

    fim = time.time()
    tempo_gasto = fim - ini
    return quantidade_comparacao, quantidade_troca, tempo_gasto