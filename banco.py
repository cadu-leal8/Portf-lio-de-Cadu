class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
        self.transacoes = []  # Lista para armazenar todas as transações realizadas
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.transacoes.append(f"Depósito de R${valor}")
            print(f"Você depositou R${valor}. Novo saldo: R${self.saldo}.")
        else:
            print("Valor de depósito deve ser positivo.")
    
    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            self.transacoes.append(f"Saque de R${valor}")
            print(f"Você sacou R${valor}. Novo saldo: R${self.saldo}.")
        elif valor > self.saldo:
            print("Saldo insuficiente para o saque.")
        else:
            print("Valor de saque deve ser positivo.")
    
    def consultar_saldo(self):
        print(f"Saldo atual: R${self.saldo}.")
    
    def listar_transacoes(self):
        if self.transacoes:
            print("Transações realizadas:")
            for transacao in self.transacoes:
                print(transacao)
        else:
            print("Nenhuma transação realizada.")
    
    def transferir(self, valor, conta_destino):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            conta_destino.saldo += valor
            self.transacoes.append(f"Transferência de R${valor} para a conta de {conta_destino.titular}")
            conta_destino.transacoes.append(f"Recebimento de R${valor} de {self.titular}")
            print(f"Você transferiu R${valor} para a conta de {conta_destino.titular}.")
        elif valor > self.saldo:
            print("Saldo insuficiente para a transferência.")
        else:
            print("Valor de transferência deve ser positivo.")
    
