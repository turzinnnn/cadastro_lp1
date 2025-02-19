#falta colocar opção no menu de modificar e excluir.

from datetime import datetime
registros = []
def ler_valor_nao_vazio(nome_variavel):
    valor_lido = ''
    while valor_lido.strip() == '':
        valor_lido = input(f'Entre com o valor para o(a) {nome_variavel} da conta: ')
    if valor_lido == '':
        print(f"o valor para {nome_variavel} não pode ser vazio!")
    return valor_lido

def criar_conta():
    for x in range(3):
        pass
        nickname = ler_valor_nao_vazio('nickname')
        email = ler_valor_nao_vazio('email')
        dataNascimentoString = input('Entre com a data de nascimento (dd/mm/aaaa): ')
        dataNascimento = datetime.strptime(dataNascimentoString, "%d/%m/%Y")
        senha = ler_valor_nao_vazio('senha')

    conta = {
        'nickname': nickname,
        'email': email,
        'dataNascimento': dataNascimento,
        'senha': senha
    }
    registros.append(conta)
    print("Conta criada com sucesso!\n")

    return conta

def imprimir_conta(conta):
    print(f"Nickname:\t\t{conta['nickname']}")
    print(f"Email:\t\t{conta['email']}")
    print(f"Data:\t\t{conta['dataNascimento'].strftime('%d/%m/%Y')}")
    print(f"Senha:\t\t{'*' *len(conta['senha'])}")
    print("_"* 30)

def imprimir_todos():
    if not registros:
        print("Nenhum registro encontrado.\n")
    else:
        print("\n===== Lista de Contas =====")
        for conta in registros:
            imprimir_conta(conta)

def excluir_conta():
    print(registros)
    excluir = input('escolha a conta que deseja excluir')

def menu():
    while True:
        print("\n******Bem vindo ao Fogaréu Grátis******")
        print("\nMenu:")
        print("1 - Adicionar nova conta")
        print("2 -  Exibir todas as contas")
        print("3 - Sair")

        opcao = input("Escolha uma opção:")

        if opcao == '1':
            criar_conta()
        elif opcao == '2':
            imprimir_todos()
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")
menu()
minha_conta = criar_conta()
imprimir_conta(minha_conta)