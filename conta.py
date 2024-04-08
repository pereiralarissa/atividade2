
class NegativeNumberError(Exception):
    """Exceção para valores negativos."""
    pass


class SaldoInsuficienteError(Exception):
    """Exceção para saques maiores que o saldo disponível."""
    pass


class Conta:
    def _init_(self, numero: str, saldo: float = 0.0):
        self._numero = numero
        self._saldo = saldo

    @property
    def numero(self) -> str:
        """Getter para o número da conta."""
        return self._numero

    @property
    def saldo(self) -> float:
        """Getter para o saldo da conta."""
        return self._saldo

    def deposita(self, valor: float):
        """Método para depositar um valor na conta."""
        if valor < 0:
            raise NegativeNumberError("Não é permitido depositar valores negativos.")
        self._saldo += valor

    def saca(self, valor: float):
        """Método para sacar um valor da conta."""
        if valor < 0:
            raise NegativeNumberError("Não é permitido sacar valores negativos.")
        if valor > self._saldo:
            raise SaldoInsuficienteError("Saldo insuficiente para realizar o saque.")
        self._saldo -= valor


if _name_ == "_main_":
    numero = input("Digite o número da conta: ")
    saldo_inicial = float(input("Digite o saldo inicial da conta (digite 0 se não houver saldo): "))

    conta = Conta(numero, saldo_inicial)
    print(f"Conta {conta.numero} criada com sucesso! Saldo atual: R${conta.saldo}")

    while True:
        print("\nEscolha uma operação:")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Ver saldo")
        print("4. Sair")

        opcao = input("Digite a opção desejada (1/2/3/4): ")

        try:
            if opcao == "1":
                valor = float(input("Digite o valor a ser depositado: "))
                conta.deposita(valor)
                print(f"Depósito realizado! Saldo atual: R${conta.saldo}")
            elif opcao == "2":
                valor = float(input("Digite o valor a ser sacado: "))
                conta.saca(valor)
                print(f"Saque realizado! Saldo atual: R${conta.saldo}")
            elif opcao == "3":
                print(f"Saldo atual: R${conta.saldo}")
            elif opcao == "4":
                print("Até mais!")
                break
            else:
                print("Opção inválida. Tente novamente.")
        except (NegativeNumberError, SaldoInsuficienteError, ValueError) as e:
            print(f"Erro: {e}")