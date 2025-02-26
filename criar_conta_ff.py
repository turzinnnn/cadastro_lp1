from datetime import datetime
registros = []
def ler_valor_nao_vazio(nome_variavel):
    valor_lido = ''
    while valor_lido.strip() == '':
        print(f"\nO valor para {nome_variavel} não pode ser vazio!")
        valor_lido = input(f'\nEntre com o valor para o(a) {nome_variavel} da conta: ')

    return valor_lido

def criar_conta():
    execs=int(input('\nQuantos cadastros você irá fazer?:'))
    for i in range(execs):
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
    email = input("Digite o email da conta a ser excluída: ")
    for conta in registros:
        if conta['email'] == email:
            registros.remove(conta)
            print("Conta excluída com sucesso!\n")
            return
    print("Conta não encontrada.\n")


def modificar_conta():
    email = input("Digite o email da conta a ser modificada: ")
    for conta in registros:
        if conta['email'] == email:
            print("Deixe os campos em branco se não quiser alterá-los.")
            novo_nickname = input("Novo nickname: ") or conta['nickname']
            nova_dataNascimentoString = input("Nova data de nascimento (dd/mm/aaaa): ") or conta[
                'dataNascimento'].strftime('%d/%m/%Y')
            nova_dataNascimento = datetime.strptime(nova_dataNascimentoString, "%d/%m/%Y")
            nova_senha = input("Nova senha: ") or conta['senha']

            conta.update({
                "nickname": novo_nickname,
                "dataNascimento": nova_dataNascimento,
                "senha": nova_senha
            })
            print("Conta modificada com sucesso!\n")
            return
    print("Conta não encontrada.\n")

def menu():
    while True:
        print("\n******Bem vindo ao Fogaréu Grátis******")
        print("\nMenu:")
        print("1 - Adicionar nova conta")
        print("2 - Exibir todas as contas")
        print("3 - Modificar conta")
        print("4 - Excluir conta")
        print("5 - Sair")

        opcao = input("Escolha uma opção:")

        if opcao == '1':
            criar_conta()
        elif opcao == '2':
            imprimir_todos()
        elif opcao == '3':
            modificar_conta()
        elif opcao == '4':
            excluir_conta()
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")
menu()