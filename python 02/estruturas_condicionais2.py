#esse é o if aninhado, ou seja, pode ter ifs dentro de ifs.
conta_normal = True
conta_universitaria = False

saldo= 1000
saque= 1200
cheque_especial= 150

if conta_normal:
    if saque <= saldo:
        print("saque realizadp")
    elif saque <= (saldo + cheque_especial):
        print("saque realizado utilizando o cheque especial")
    else:
        print("saldo insuficiente")
elif conta_universitaria:
    if saque <= saldo:
        print("saque realizadp")
    else:
        print("saldo insuficiente")
else:
    print("sistema nao reconheceu seu tipo de conta")
