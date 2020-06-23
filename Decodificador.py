# Disciplina: Algoritmos e Estruturas de Dados II
# T2 - 25/06/2020
# Grupo: Lucca Molon e Gustavo Demichei

# Abre arquivo "codes.txt" com os códigos de Huffman, o arquivo "codificado.txt", que tem o texto codificado e realiza a decodificação no arquivo "out.txt"


# Abre arquivo do texto a ser decodificado
import ast


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


# abre arquivo contendo os codigos e os insere no dict(codes).
codes = {}
f_codes = open("codes.txt", "r")
for code in f_codes:
    lst = code.split(":")
    codes[lst[1][1:-1]] = lst[0]

#cria raiz e isnere todos pares de codigo-char
root = Node()
for code, char in codes.items():
    root.insert(code, char)

#Abre texto codificado e arquivo a ser escrito
f_codificado = open("codificado.txt", "r")
texto = f_codificado.read()
nodo = root
f_out = open("out.txt", "w")
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