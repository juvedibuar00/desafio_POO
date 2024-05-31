class Produto:
    def __init__(self, nome, codigo, preco, quantidade):
        self.__nome = nome
        self.__codigo = codigo
        self.__preco = preco
        self.__quantidade = quantidade

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    # Implementar getters e setters para os outros atributos

    def descricao(self):
        return f"{self.__nome}: Preço - {self.__preco} / Quantidade em estoque - {self.__quantidade}"


class Alimento(Produto):
    def __init__(self, nome, codigo, preco, quantidade, validade):
        super().__init__(nome, codigo, preco, quantidade)
        self.__validade = validade

    def descricao(self):
        return f"{super().descricao()} / Validade - {self.__validade}"


class Bebida(Produto):
    def __init__(self, nome, codigo, preco, quantidade, tipo):
        super().__init__(nome, codigo, preco, quantidade)
        self.__tipo = tipo

    def descricao(self):
        return f"{super().descricao()} / Tipo - {self.__tipo}"


class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def remover_produto(self, codigo):
        for produto in self.produtos:
            if produto.get_codigo() == codigo:
                self.produtos.remove(produto)
                return True
        return False

    def listar_produtos_disponiveis(self):
        for produto in self.produtos:
            print(produto.descricao())

    def mostrar_produtos_indisponiveis(self):
        for produto in self.produtos:
            if produto.get_quantidade() == 0:
                print(produto.descricao())


# Exemplo de uso
estoque = Estoque()
alimento1 = Alimento("Arroz", "A001", 5.99, 50, "20/06/2025")
bebida1 = Bebida("Refrigerante", "B001", 3.49, 100, "Refrigerante de cola")

estoque.adicionar_produto(alimento1)
estoque.adicionar_produto(bebida1)

estoque.listar_produtos_disponiveis()
estoque.mostrar_produtos_indisponiveis()
