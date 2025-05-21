class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class BST:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        self.raiz = self._inserir_recursivo(self.raiz, valor)

    def _inserir_recursivo(self, no, valor):
        if no is None:
            return Node(valor)
        if valor < no.valor:
            no.esquerda = self._inserir_recursivo(no.esquerda, valor)
        else:
            no.direita = self._inserir_recursivo(no.direita, valor)
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

    def print_arvore(self, no=None, nivel=0):
        if no is None:
            no = self.raiz
        if no.direita:
            self.print_arvore(no.direita, nivel + 1)
        print("    " * nivel + f"-> {no.valor}")
        if no.esquerda:
            self.print_arvore(no.esquerda, nivel + 1)

def main():
    print("\n" + "="*40)
    print(" ARVORE BINARIA DE BUSCA (BST)")
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

        print("\n" + "-"*40)
        print(" Estrutura da árvore (vista de lado):")
        print("-"*40)
        arvore.print_arvore()
        print("-"*40)

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
##ESSA ARVORE BUGADAAAAAAAAAA