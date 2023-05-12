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

### Definindo a Lista
try:
    with open("words.txt", "r") as file:
        wordlist = file.read().split(',')
        wordlist = [word.lower() for word in wordlist]
except:
    print('[!] Não foi possível importar a lista, verifique se o arquivo está na mesma pasta que o programa')

 ### Criando as funções de ordenação

def bbs(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def bbsrev(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

### Organizando as listas e imprimindo os resultados

print('[!] Organizando as listas...')
time.sleep(2)

# BENCHMARK

start_time = time.time()

# Organizando a lista alfabeticamente

try:
    bbs(wordlist)
    with open("bbs.txt", "w") as f:
        f.write(','.join(wordlist))
    print(f'[+] Aqui está os 10 primeiros itens da lista ordenados alfabeticamente: {wordlist[:10]}')
except:
    print('[!] Não foi possível organizar as listas, tente novamente...')

# Organizando a lista inversa

try:
    bbsrev(wordlist)
    with open("bbsRev.txt", "w") as f:
        f.write(','.join(wordlist))
    print(f'[+] Aqui está os 10 primeiros itens da lista inversa: {wordlist[:10]}')
except:
     print('[!] Não foi possível organizar as listas, tente novamente...')
   
end_time = time.time()

print(f'[?] O programa levou: {round(end_time - start_time, 4)} segundo para executar o algoritmo!')
print('[INFO] A lista completa com 1000 itens está organizada em dois arquivos: bbs.txt e bbsRev.txt')