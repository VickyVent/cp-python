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


# Definindo a lista

try:
    with open("words.txt", "r") as file:
        wordlist = file.read().split(",")
        wordlist = [word.lower() for word in wordlist]
except:
    print('[!] Não foi possível importar a lista, verifique se o arquivo está na mesma pasta que o programa')

### Criando a função de ordenação

def mgs(arr):
    left_half = []  # Criando as listas que separam o array original
    right_half = []
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        mgs(left_half)
        mgs(right_half)

    
    i = j = k = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j+=1
        k+=1

    while i < len(left_half):
        arr[k] = left_half[i]
        i+=1
        k+=1

    while j < len(right_half):
        arr[k] = right_half[j]
        j+=1
        k+=1

# Função reversa
def mgsrev(arr):
    left_half = []  # Criando as listas que separam o array original
    right_half = []
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        mgsrev(left_half)
        mgsrev(right_half)

    
    i = j = k = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] > right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j+=1
        k+=1

    while i < len(left_half):
        arr[k] = left_half[i]
        i+=1
        k+=1

    while j < len(right_half):
        arr[k] = right_half[j]
        j+=1
        k+=1



### Executando as funções e imprimindo os resultados

print('[!] Organizando as listas...')
time.sleep(2)    # Aguarde por 2 segundos
print('\n')

# BENCHMARK

start_time = time.time()

# Executando a lista alfabeticamente

try:
    mgs(wordlist)
    with open("mgs.txt", "w") as f:
        f.write(','.join(wordlist))
    print(f'[+] Os 10 primeiros itens da lista ordenada alfabeticamente: {wordlist[:10]} (...)')
except:
    print('[!] Não foi possível organizar as listas, tente novamente...')

# Executando a lista alfabeticamente invertida

try:
    mgsrev(wordlist)
    with open("mgsRev.txt", "w") as f:
        f.write(','.join(wordlist))
    print(f'[+] Os 10 primeiros itens da lista ordenada invertida: {wordlist[:10]} (...)')
except:
     print('[!] Não foi possível organizar as listas, tente novamente...')
   

end_time = time.time()

# Imprimindo o resultado final

print(f'[?] O programa levou: {round(end_time - start_time, 4)} segundo para executar o algoritmo!')
print('[INFO] A lista completa com 1000 itens está organizada em dois arquivos: mgs.txt e mgsRev.txt')
