# Disciplina: Algoritmos e Estruturas de Dados II
# T2 - 25/06/2020
# Grupo: Lucca Molon e Gustavo Demichei

# Abre arquivo "codes.txt" com os códigos de Huffman, o arquivo "codificado.txt", que tem o texto codificado e realiza a decodificação no arquivo "out.txt"


# Abre arquivo do texto a ser decodificado
import ast
import sys


class Node:
    def __init__(self):
        self.val = None
        self.left = None
        self.right = None
        self.leaf = False

    #Insere char na arvore, conforme codigo dado..
    def insert(self, code, char):
        if not code:            # se node atual for uma folha, insere o char
            self.val = char
            self.leaf = True
            if self.val =="\\n":
                self.val = "\n"
        elif code[0] == '0':    # se codigo=0 ir para esquerda
            if self.left is None:
                self.left = Node()
            self.left.insert(code[1:], char)
        elif code[0] == '1':    # secodigo=1 ir para direita
            if self.right is None:
                self.right = Node()
            self.right.insert(code[1:], char)


# Abre arquivo contendo os codigos de huffman, o que contem texto codificado e arquivo a ser escrito
if len(sys.argv) >= 4:
    f_codes = open(sys.argv[1], "r")
    f_codificado = open(sys.argv[2], "r")
    f_out = open(sys.argv[3], "w")
else:
    f_codes = open("testes/decod.txt", "r")
    f_codificado = open("testes/codificado.txt", "r")
    f_out = open("testes/out.txt", "w")


# Insere no dict(codes) os pares de char-codigo encontrados no arquivo de entrada.
codes = {}
for code in f_codes:
    lst = code.split(":")
    codes[lst[1][1:-1]] = lst[0]

#cria raiz e isnere todos pares de codigo-char
root = Node()
for code, char in codes.items():
    root.insert(code, char)


texto = f_codificado.read()
nodo = root
out = ""
# Percorre a arvore enquanto há texto. Ao passar por uma folha, concatena seu valor no output, reseta nodo para root e volta a fazer o mesmo para o restante do texto codificado.
while texto:
    if texto[0] =='0':
        nodo = nodo.left
    elif texto[0] =='1':
        nodo = nodo.right
    if nodo.leaf:
        f_out.write(nodo.val)
        nodo = root
    texto = texto[1:]

f_out.close()
f_codificado.close()
f_codes.close()