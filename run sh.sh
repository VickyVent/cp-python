#!/bin/bash/
echo "[!] Executando algoritmo 1: bbs"
resultado1=$(python3 bbs.py | grep -m 1 '\[?\] O programa levou:')
echo $resultado1
echo "[!] Executando algoritmo 2: mgs"
resultado2=$(python3 mgs.py | grep -m 1 '\[?\] O programa levou:')
echo $resultado2
echo "[!] Executando algoritmo 3: QuickSort"
resultado3=$(python3 quicksort.py | grep -m 1 '\[?\] O programa levou:')
echo $resultado3
