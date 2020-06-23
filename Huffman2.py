# Disciplina: Algoritmos e Estruturas de Dados II
# T1 - 22/04/2020
# Grupo: Lucca Molon e Gustavo Demichei

# Abre arquivo do texto a ser decodificado
import ast


class Node:
    def __init__(self):
        self.val = None
        self.left = None
        self.right = None
        self.leaf = False

    def insert(self, code, char):
        if not code:
            self.val = char
            self.leaf = True
        elif code[0] == '0':
            if self.left is None:
                self.left = Node()
            self.left.insert(code[1:], char)
        elif code[0] == '1':
            if self.right is None:
                self.right = Node()
            self.right.insert(code[1:], char)

    def copy(self):
        return self


codes = {}
f_text = open("king_james.txt", "r")
f_codes = open("codes.txt", "r")

for code in f_codes:
    lst = code.split(":")
    codes[lst[1][1:-1]] = lst[0]

root = Node()

for code, char in codes.items():
    root.insert(code, char)

print(root.right.left.left.right.val)

nodo = root
texto = "01000100010001000100010001000100010001000100010001000100"
out = ""
print(nodo.left.right.left.left.val)
# Percorre a arvore enquanto há tempo. Ao passar por uma folha, concatena seu valor no output, reseta nodo para root e volta a fazer o mesmo para o restante do texto codificado.
while texto:
    if texto[0] =='0':
        nodo = nodo.left
    elif texto[0] =='1':
        nodo = nodo.right
    if nodo.leaf:
        out += nodo.val
        nodo = root
    texto = texto[1:]
