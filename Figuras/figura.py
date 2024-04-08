from abc import ABC, abstractmethod

class FormasGeometricas(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass


class Desenhavel(ABC):
    @abstractmethod
    def desenha(self):
        pass


class Quadrado(FormasGeometricas, Desenhavel):
    def _init_(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return 4 * self.lado

    def desenha(self):
        for _ in range(self.lado):
            print('#' * self.lado)


class Retangulo(FormasGeometricas, Desenhavel):
    def _init_(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

    def desenha(self):
        for _ in range(self.altura):
            print('#' * self.base)


class Circulo(FormasGeometricas):
    def _init_(self, raio):
        self.raio = raio

    def area(self):
        return 3.14 * self.raio ** 2

    def perimetro(self):
        return 2 * 3.14 * self.raio


if _name_ == '_main_':
    while True:
        print("\n1. Quadrado")
        print("2. Retangulo")
        print("3. Circulo")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            lado = int(input("Informe o lado do quadrado: "))
            quad = Quadrado(lado)
            quad.desenha()
            print(f"\nÁrea: {quad.area()}\nPerímetro: {quad.perimetro()}")

        elif opcao == "2":
            base = int(input("Informe a base do retângulo: "))
            altura = int(input("Informe a altura do retângulo: "))
            ret = Retangulo(base, altura)
            ret.desenha()
            print(f"\nÁrea: {ret.area()}\nPerímetro: {ret.perimetro()}")

        elif opcao == "3":
            raio = int(input("Informe o raio do círculo: "))
            circ = Circulo(raio)
            print(f"\nÁrea: {circ.area()}\nPerímetro: {circ.perimetro()}")

        elif opcao == "4":
            print("Até breve!")
            break

        else:
            print("Opção inválida. Por favor, escolha novamente.")
