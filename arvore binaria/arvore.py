import os 
os.system('cls') #isso é so pra limpar o terminal do vscode
class no:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class ArvoreBinaria:
    def __init__(self):
        self.root = None

    def inserir(self, key):
        self.root = self.organiza(self.root, key)

    def organiza(self, root, key):
        if not root:
            return no(key)
        if key < root.key:
            root.left = self.organiza(root.left, key)
        elif key > root.key:
            root.right = self.organiza(root.right, key)
        return root

    def ordem(self):
        resultados = []
        self.valoresLista(self.root, resultados)
        return resultados

    def valoresLista(self, root, result):
        if root:
            self.valoresLista(root.left, result)
            result.append(root.key)
            self.valoresLista(root.right, result)

    def buscar_valor(self, key):
        return self.percorre_valores(self.root, key)

    def percorre_valores(self, root, key):
        if not root or root.key == key:
            return root
        if key < root.key:
            return self.percorre_valores(root.left, key)
        return self.percorre_valores(root.right, key)

    def remove(self, key):
        if self.percorre_valores(self.root, key) is None:
            print(f'\033[1;31;49mNão tem vomo excluir o número {n} pois ele não esta na arvore.')
        else:     
            self.root = self.remove_no(self.root, key)
            print(f'\033[1;32;49mO numero {n} foi removido da árvore.\033[m') 
    
    def remove_no(self, root, key):
        if not root:
            return root

        if key < root.key:
            root.left = self.remove_no(root.left, key)
        elif key > root.key:
            root.right = self.remove_no(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            root.key = self.menor_valor(root.right)
            root.right = self.remove_no(root.right, root.key)

        return root

    def menor_valor(self, root):
        while root.left:
            root = root.left
        return root.key

a = ArvoreBinaria()

while True:
    print(f"\n\033[0;32;49mÁrvore em ordem:\033[m {a.ordem()}")
    escolha = input("1: \033[1;32;49mInserir\033[m, 2: \033[1;31;49mRemover\033[m, 3: \033[0;34;49mBuscar\033[m, 4: \033[0;33;49mSair\033[m\nEscolha uma operação:\033[m ")
    if escolha == '1':
        n = int(input("\033[0;35;49mDigite um valor para se ter na arvore:\033[m "))
        a.inserir(n)
    elif escolha == '2':
        n = int(input("\033[0;36;49mDigite um valor para remover da arvore:\033[m "))
        a.remove(n)
    elif escolha == '3':
        n = int(input("\033[0;34;49mDigite um valor para buscar na arvore:\033[m "))
        r = a.buscar_valor(n)
        if r:
            print(f"\033[1;32;49mO número {n} foi encontrado na árvore.\033[m")
        else:
            print(f"\033[1;31;49mO número {n} não foi encontrado na árvore.\033[m")
    elif escolha == '4':
        print('~'*14)
        print("\033[0;33;49mAté a próxima!\033[m")
        print('~'*14)
        break
    else:
        print("\033[1;31;43mOpção inválida. Tente novamente.\033[m")
#esses codigos de "\033" são para dar cor as escritas