from operacoesbd import*
from ouvidoria import *

conexao = criarConexao('localHost','root','12345','myouvidoria')
opcao = 0

while opcao!=6:
    print("\n1° Listar manifestações")
    print("2° Realizar uma nova manifestação")
    print("3° Verificar quantidade de manifestações")
    print("4° Pesquisar uma manifestação")
    print("5° Excluir uma manifestação")
    print("6° Sair\n")

    try:
        opcao = int(input("Informe a opção no qual deseja: "))
    except ValueError:
        print("Valor incorreto")

    if opcao == 1:
        listarManifestacoes(conexao)

    elif opcao == 2:
        inserirManifestacao(conexao)

    elif opcao == 3:
        numeroManifestacoes(conexao)

    elif opcao == 4:
        pesquisarManifestacao(conexao)

    elif opcao == 5:
        excluirManifestacao(conexao)

    elif opcao == 6:
        mensagemSair(conexao)

    else:
        valorInvalido(conexao)

print("\nPrograma finalizado com sucesso!")
encerrarConexao(conexao)