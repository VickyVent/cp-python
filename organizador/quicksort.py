"""CODING FOR SECURITY - CHECKPOINT 2
1TDCG - Ettore Sec
Carolina Camacho - RM98171
Guilherme Kussuki Barboza - RM550518
Guilherme Valloto - RM550353
Victoria Oliveira Ventrilho - RM94872"""


### HEADER
print("------------------//-------------------")
print("BEM-VINDO(A) AO ORDENADOR DE LISTAS!")
print("""
    ________  __                     _____          
   / ____/ /_/ /_____  ________     / ___/___  _____
  / __/ / __/ __/ __ \/ ___/ _ \    \__ \/ _ \/ ___/
 / /___/ /_/ /_/ /_/ / /  /  __/   ___/ /  __/ /__  
/_____/\__/\__/\____/_/   \___/   /____/\___/\___/  
                                                    
""")
print("------------------//-------------------")

import time


# Definido a lista
try:
    with open("words.txt", "r") as file:
        wordlist = file.read().split(",")
        wordlist = [word.lower() for word in wordlist]
except:
    print('[!] Não foi possível importar a lista, verifique se o arquivo está na mesma pasta que o programa')

### Criando as funções de ordenação

# Criando a função partition, para particionar a lista wordlist
def partition(arr, low, high):

    i = (low-1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

# Criando a função que irá executar o QuickSort
def qs(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        qs(arr, low, pi-1)
        qs(arr, pi+1, high)

def rev_list(arr):
    n = len(arr)
    for i in range(n//2):
        arr[i], arr[n-i-1] = arr[n-i-1], arr[i]

    return arr

### Organizando as listas e imprimindo o resultado final

print('[!] Organizando as listas...')
time.sleep(2)
print('\n')

# BENCHMARK

start_time = time.time()

# Ordenando a lista alfabeticamente

try:
    qs(wordlist, 0, len(wordlist)-1)
    with open("QuickSort.txt", "w") as f:
        f.write(','.join(wordlist))
    print(f'[+] Aqui está os 10 primeiros itens da lista ordenada alfabeticamente: {wordlist[:10]}')
except:
    print('[!] Não foi possível organizar as listas, tente novamente...')

# Organizando a lista de forma reversa

try:
    reverse_list = rev_list(wordlist)
    with open("QuickSortRev.txt", "w") as f:
        f.write(','.join(wordlist))
    print(f'[+] Aqui está os 10 primeiros itens da lista invertida: {reverse_list[:10]}')
except:
    print('[!] Não foi possível organizar as listas, tente novamente...')


end_time = time.time()

# Imprimindo o resultado

print(f'[?] O programa levou: {round(end_time - start_time, 4)} segundo para executar o algoritmo!')
print('[INFO] A lista completa com 1000 itens está organizada em dois arquivos: QuickSort.txt e QuickSortRev.txt')
