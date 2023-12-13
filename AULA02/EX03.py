class Conta:
    def __init__(self, numero_conta, titular, saldo):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        return f"Depósito de R${valor} realizado com sucesso"

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return f"Saque de R${valor} realizado com sucesso"
        else:
            return "Saldo insuficiente para saque"

    def transferir(self, conta_destino, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            conta_destino.saldo += valor
            return f"Transferência de R${valor} realizada para {conta_destino.titular}"
        else:
            return "Saldo insuficiente para transferência"

class ContaCorrente(Conta):
    def __init__(self, numero_conta, titular, saldo, limite=0):
        super().__init__(numero_conta, titular, saldo)
        self.limite = limite

    def sacar(self, valor):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
            return f"Saque de R${valor} realizado com sucesso"
        else:
            return "Limite de saque excedido"

    def transferir(self, conta_destino, valor):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
            conta_destino.saldo += valor
            return f"Transferência de R${valor} realizada para {conta_destino.titular}"
        else:
            return "Limite de transferência excedido"

    def taxa_deposito(self):
        return 0.002  # 0.2%

class ContaPoupanca(Conta):
    def calcular_juros(self):
        juros = self.saldo * 0.005  # 0.5%
        self.saldo += juros
        return f"Juros de R${juros} creditados na conta"

    def taxa_deposito(self):
        return 0.005  # 0.5%

class ContaInvestimento(Conta):
    def investir_acoes(self, valor):
        # Lógica para investimento em ações
        return f"Investimento de R${valor} em ações realizado com sucesso"

    def taxa_deposito(self):
        return 0.008  # 0.8%

# Exemplos de uso
conta_corrente = ContaCorrente("12345", "João", 1000, 500)
print(conta_corrente.depositar(100))
print(conta_corrente.sacar(300))
print(conta_corrente.transferir(Conta("54321", "Maria", 500), 400))
print(f"Taxa de depósito da conta corrente: {conta_corrente.taxa_deposito()}")

conta_poupanca = ContaPoupanca("67890", "Ana", 2000)
print(conta_poupanca.depositar(500))
print(conta_poupanca.calcular_juros())
print(f"Taxa de depósito da conta poupança: {conta_poupanca.taxa_deposito()}")

conta_investimento = ContaInvestimento("13579", "Pedro", 3000)
print(conta_investimento.depositar(1000))
print(conta_investimento.investir_acoes(500))
print(f"Taxa de depósito da conta investimento: {conta_investimento.taxa_deposito()}")
