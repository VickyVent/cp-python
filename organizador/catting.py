# Script que lê as 1000 primeiras linhas da rockyou.txt e escrevê-as
# em um novo arquivo .txt, separando-as por vírgulas e em uma única linha
# para facilitar a criação da array no código

with open("rockyou.txt", "r", encoding="utf-8", errors="ignore") as input_file:
    with open("words.txt", "w") as f:
        words = [line.strip() for line in input_file.readlines()[:1000]]
        f.write(','.join(words))