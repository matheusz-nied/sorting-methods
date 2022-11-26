import util
import sorting
import sys

# Altera o limite de recursão do Python
sys.setrecursionlimit(6000)

paths = util.list_files()

i = 0

for path in paths:
    print(i, "- " + path)
    i += 1

print("Escolha um arquivo para ser ordenado(digite o número dele):")
file = int(input())

array = util.open_file(paths[file - 1])

print("Escolha um método de ordenação(digite o número dele):")
print("1 - InsertionSort")
print("2 - SelectionSort")
print("3 - MergeSort")
print("4 - QuickSort")

metodo_ordenacao = int(input())

if(metodo_ordenacao == 1):
    comp, troca, tempo = sorting.InsertionSort(array)
    
elif(metodo_ordenacao == 2):
    comp, troca, tempo = sorting.SelectionSort(array)
    
elif(metodo_ordenacao == 3):
    comp, troca, tempo = sorting.MergeSort(array)
    
elif(metodo_ordenacao == 4):
    comp, troca, tempo = sorting.QuickSort(array)


util.print_array(array)

