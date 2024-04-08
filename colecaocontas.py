from repositoriocontas import RepositorioContas, Conta

class ContaInexistenteError(Exception):
    """Exceção lançada quando a conta não é encontrada."""
    pass

class ColecaoContas(RepositorioContas):
    def _init_(self):
        self._contas = {}

    def cadastra_conta(self, conta: Conta):
        if conta.numero in self._contas:
            print("Conta já cadastrada!")
        else:
            self._contas[conta.numero] = conta
            print(f"Conta {conta.numero} cadastrada com sucesso!")

    def procura_conta(self, numero: str) -> Conta:
        if numero not in self._contas:
            raise ContaInexistenteError(f"Conta {numero} não encontrada!")
        return self._contas[numero]

if _name_ == "_main_":
    colecao = ColecaoContas()

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
            colecao.cadastra_conta(conta)
        elif opcao == "2":
            numero = input("Digite o número da conta que você deseja procurar: ")
            try:
                conta_encontrada = colecao.procura_conta(numero)
                print(f"Conta encontrada! Número: {conta_encontrada.numero}, Saldo: R${conta_encontrada.saldo}")
            except ContaInexistenteError as e:
                print(f"Erro: {e}")
        elif opcao == "3":
            print("Até mais!")
            break
        else:
            print("Opção inválida. Tente novamen") 
    