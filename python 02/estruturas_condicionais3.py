#é um if em uma unica linha. uma instrucao em uma unica linha, deixa o codigo mais legivel.
saldo= 20
saque= 141

status= "sucesso" if saque <= saldo else "falha"
print(status)