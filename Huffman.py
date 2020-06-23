# Disciplina: Algoritmos e Estruturas de Dados II
# T1 - 22/04/2020
# Grupo: Lucca Molon e Gustavo Demichei
import functools
from heapq import heappush, heappop, heapify
from collections import defaultdict


# Dado um dicionário, contendo cada caracter(key) e sua frequência(value) no texto,
# cria um heap para definir a codificação de Huffman de cada elemento , a inserindo 
# na lista retornadapela função.
@functools.total_ordering
class Node:
    def __init__(self, char=None, freq=None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
        self.code = ""

    def __eq__(self, other):
        return self.freq == other.freq

    def __ne__(self, other):
        return not self.freq == other.freq

    def __lt__(self, other):
        return self.freq < other.freq


def encode(dict):
    Q = []
    for char, freq in dict.items():
        heappush(Q, Node(char, freq))
    print(len(Q))
    i = 1
    for i in range(len(Q) - 1):
        z = Node()
        z.left = x = heappop(Q)
        z.left.code = '0'
        z.right = y = heappop(Q)
        z.right.code = '1'
        z.freq = x.freq + y.freq
        heappush(Q, z)
    return heappop(Q)


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

# huffman = encode(dict)
# print(type(huffman))
huffman_tree = encode(dict)

# cria arquivo destino, que será populado com os códigos Huffman
input_text = open('codes_1.txt', 'r')
output_coded = open('codes_out.txt', 'w')



def code(in_file, dict, T):
    def process(t, c, cod=""):
        if t.left is None and t.right is None and t.char == c:
            print({c}--{cod})
            return
        process(t.left, c, cod+"0")
        process(t.right, c, cod + "1")

    for char in input_text.readline():
        process(T, char)


code(input_text, dict, huffman_tree)
print(huffman_tree.right.right.right.code)
a = 1
b = 2
