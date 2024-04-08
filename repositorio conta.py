from abc import ABC, abstractmethod
from conta import Conta

class RepositorioContas(ABC):

    @abstractmethod
    def cadastra_conta(self, conta: Conta):
        """Método para cadastrar uma conta."""
        pass

    @abstractmethod
    def procura_conta(self, numero: str) -> Conta:
        """Método para procurar uma conta pelo número."""
        pass

class RepositorioContasEmMemoria(RepositorioContas):
    def _init_(self):
        self._contas = {}

    def cadastra_conta(self, conta: Conta):
        if conta.numero in self._contas:
            print("Conta já cadastrada!")
        else:
            self._contas[conta.numero] = conta
            print(f"Conta {conta.numero} cadastrada com sucesso!")

    def procura_conta(self, numero: str) -> Conta:
        return self._contas.get(numero, None)

if _name_ == "_main_":
    repositorio = RepositorioContasEmMemoria()

    while True:
        print("\nEscolha uma operação:")
        print("1. Cadastrar conta")
        print("2. Procurar conta pelo número")
        print("3. Sair")

        opcao = input("Digite a opção desejada (1/2/3): ")

        if opcao == "1":
            numero = input("Digite o número da conta: ")
            saldo_inicial = float(input("Digite o saldo inicial da conta (digite 0 se não houver saldo): "))
            conta = Conta(numero, saldo_inicial)
            repositorio.cadastra_conta(conta)
        elif opcao == "2":
            numero = input("Digite o número da conta que você deseja procurar: ")
            conta_encontrada = repositorio.procura_conta(numero)
            if conta_encontrada:
                print(f"Conta encontrada! Número: {conta_encontrada.numero}, Saldo: R${conta_encontrada.saldo}")
            else:
                print("Conta não encontrada!")
        elif opcao == "3":
            print("Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")