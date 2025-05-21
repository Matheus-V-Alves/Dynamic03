from collections import deque

class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class BST:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        self.raiz = self.ins_recursivo(self.raiz, valor)

    def ins_recursivo(self, no, valor):
        if no is None:
            return Node(valor)
        if valor < no.valor:
            no.esquerda = self.ins_recursivo(no.esquerda, valor)
        else:
            no.direita = self.inse_recursivo(no.direita, valor)
        return no

    def encontrar_k_esimo_menor(self, k):
        self.contador = 0
        self.k_esimo = None
        self._in_order(self.raiz, k)
        return self.k_esimo

    def _in_order(self, no, k):
        if no is None or self.k_esimo is not None:
            return
        self._in_order(no.esquerda, k)
        self.contador += 1
        if self.contador == k:
            self.k_esimo = no.valor
            return
        self._in_order(no.direita, k)

    def print_com_ramos(self):
        def altura(no):
            if no is None:
                return 0
            return 1 + max(altura(no.esquerda), altura(no.direita))

        def preencher(no, linha, col, matriz, espaco):
            if no is None or linha >= len(matriz) or col < 0 or col >= len(matriz[0]):
                return
            matriz[linha][col] = str(no.valor)
            if no.esquerda:
                matriz[linha + 1][col - espaco] = '/'
                preencher(no.esquerda, linha + 2, col - espaco * 2, matriz, espaco // 2)
            if no.direita:
                matriz[linha + 1][col + espaco] = '\\'
                preencher(no.direita, linha + 2, col + espaco * 2, matriz, espaco // 2)

        alt = altura(self.raiz)
        linhas = alt * 2 - 1
        colunas = 2 ** (alt + 1)
        matriz = [[" " for _ in range(colunas)] for _ in range(linhas)]

        preencher(self.raiz, 0, colunas // 2, matriz, colunas // 8)

        print("\n" + "-" * 40)
        print(" Estrutura da árvore com ramos:")
        print("-" * 40)
        for linha in matriz:
            print("".join(linha).rstrip())
        print("-" * 40 + "\n")

def main():
    print("\n" + "="*40)
    print(" ARVORE BINARIA DE BUSCA (nossa BST)")
    print("="*40)
    
    entrada = input(">>> Digite os numeros separados por espaco:\n->  ")
    
    try:
        numeros = list(map(int, entrada.split()))
        N = len(numeros)
        if N == 0:
            print("-X- Você precisa inserir pelo menos um número.")
            return

        arvore = BST()
        for num in numeros:
            arvore.inserir(num)

        arvore.print_com_ramos()

        print(f"\n>>> Digite o valor de k (1 ≤ k ≤ {N}):")
        k = int(input("->  "))
        if not (1 <= k <= N):
            print(f"-X- Valor inválido! k deve estar entre 1 e {N}.")
            return

        resultado = arvore.encontrar_k_esimo_menor(k)
        print("\n" + "-"*40)
        print(f" O {k}-ésimo menor elemento da BST é: {resultado}")
        print("-"*40 + "\n")

    except ValueError:
        print("-X- Entrada inválida. Certifique-se de digitar apenas números inteiros.")

if __name__ == "__main__":
    main()
