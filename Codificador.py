# Disciplina: Algoritmos e Estruturas de Dados II
# T2 - 25/06/2020
# Grupo: Lucca Molon e Gustavo Demichei

# Abre o arquivo "king_james.txt" e exporta os codigos huffmna no arquivo "codes.txt"

from heapq import heappush, heappop, heapify
from collections import defaultdict

# Dado um dicionário, contendo cada caracter(key) e sua frequência(value) no texto, 
# cria um heap para definir a codificação de Huffman de cada elemento , a inserindo 
# na lista retornadapela função.
def encode(dict):
    heap = [[freq, [char, ""]] for char, freq in dict.items()]
    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

# Abre arquivo do texto a ser codificado
f = open("king_james.txt", "r")

# cria dicionário com os caracteres contidos no texto e a frequência com que aparecem.
dict = defaultdict(int)
for line in f:
    for chr in line:
        if chr in dict:
            dict[chr] += 1
        else:
            dict[chr] = 1

huffman = encode(dict)
print(type(huffman))

# cria arquivo destino, que será populado com os códigos Huffman
arquivo = open('codes.txt', 'w')

# imprime caracter, frequência e código Huffman e esqcreve o arquivo de saída com os dados.
print("char\tfreq\tcode")
for p in huffman:
    print((p[0], dict[p[0]], p[1]))
    char = p[0] # pois um dos characters e \n
    if char == "\n":
        char = "\\n"
    s = "{}: {}\n".format(char, p[1])
    arquivo.write(s)
arquivo.close()