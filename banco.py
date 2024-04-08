from colecaocontas import ColecaoContas, Conta
from excecoes import ContaInexistenteError, SaldoInsuficienteError

class Banco:
    def _init_(self):
        self.repositorio = ColecaoContas()

    def cria_conta(self, numero, saldo_inicial, tipo):
        if tipo == "comum":
            conta = Conta(numero, saldo_inicial)
            self.repositorio.cadastra_conta(conta)
        else:
            print("Tipo de conta não reconhecido.")

    def saca(self, numero, valor):
        try:
            conta = self.repositorio.procura_conta(numero)
            if conta.saldo >= valor:
                conta.saldo -= valor
                print(f"Saque de R${valor} realizado com sucesso. Saldo atual: R${conta.saldo}")
            else:
                raise SaldoInsuficienteError(conta.saldo)
        except (ContaInexistenteError, SaldoInsuficienteError) as e:
            print(f"Erro: {e}")

    def deposita(self, numero, valor):
        try:
            conta = self.repositorio.procura_conta(numero)
            conta.saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso. Saldo atual: R${conta.saldo}")
        except ContaInexistenteError as e:
            print(f"Erro: {e}")

if _name_ == "_main_":
    banco = Banco()

    while True:
        print("\nEscolha uma operação:")
        print("1. Criar conta")
        print("2. Sacar")
        print("3. Depositar")
        print("4. Sair")

        opcao = input("Digite a opção desejada (1/2/3/4): ")

        if opcao == "1":
            numero = input("Digite o número da conta: ")
            saldo_inicial = float(input("Digite o saldo inicial da conta (digite 0 se não houver saldo): "))
            tipo = input("Digite o tipo de conta (comum): ")  # Se você tiver outras classes de conta, pode adicionar opções aqui
            banco.cria_conta(numero, saldo_inicial, tipo)
        elif opcao == "2":
            numero = input("Digite o número da conta de onde deseja sacar: ")
            valor = float(input("Digite o valor a ser sacado: "))
            banco.saca(numero, valor)
        elif opcao == "3":
            numero = input("Digite o número da conta onde deseja depositar: ")
            valor = float(input("Digite o valor a ser depositado: "))
            banco.deposita(numero, valor)
        elif opcao == "4":
            print("Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")