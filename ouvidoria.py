#metodos que são direcionados ao menu
#from inserir import nomeCliente
from operacoesbd import *
conexao = criarConexao('localHost','root','12345','myouvidoria')

def listarManifestacoes(conexao):
    consulta = 'select * from ouvidoria'
    manifestacoes = listarBancoDados(conexao, consulta)

    if len(manifestacoes) == 0:
        print("Resolução:")
        print("Não possuem manifestações em aberto")
    else:
        for manifestacao in manifestacoes:
            print(f"-Código:{manifestacao[0]}. \n-Nome: {manifestacao[1]}. \n-Protocolo: {manifestacao[2]}. "
                  f"\n-Tipo de manifestação: {manifestacao[3]}\n-Manifestação:{manifestacao[4]}".strip())


def inserirManifestacao(conexao):

    nome= input("Informe o seu nome: ")
    numeroProtocolo = int(input("Informe o protocolo: "))
    tipo = input(
        "- Reclamação.\n"
        "- Denúncia.\n"
        "- Elogio.\n"
        "- Sugestão.\n"
        "- Solicitar   informação.\n"
        "- Pedido de simplificação de serviços públicos.\n\n"
        "Informe o tipo: "
    )

    manifestacao = input("Informe sua manifestação: ")

    consulta = 'insert into ouvidoria (nome,protocolo,tipoManifestacao,manifestacao) values (%s,%s,%s,%s)'
    dados = [nome, numeroProtocolo, tipo, manifestacao]

    novaManifestacao = insertNoBancoDados(conexao, consulta, dados)
    print("Manifestação realizada com sucesso", novaManifestacao)





def exibir_manifestacao(manifestacoes):
    for manifestacao in manifestacoes:
        print(f"Código:{manifestacao[0]}. \nNome: {manifestacao[1]}. \nProtocolo: {manifestacao[2]}. "
              f"\nTipo de manifestação: {manifestacao[3]}\n Manifestação:{manifestacao[4]}".strip())






def pesquisarManifestacao(conexao):
    while True:
        print("\n1° Pesquisar por protocolo")
        print("2° Pesquisar por código")
        print("3° Pesquisar por tipo de manifestação")
        print("4° Sair da pesquisa\n")

        try:
            opcao = int(input("Digite a opção desejada: "))
        except ValueError:
            print("Digite um número válido.")
            continue

        if opcao == 1:
            # Validação do protocolo com exatamente 15 dígitos
            #strip(): retira espaços.
            #isdigit(): verifica se uma string só tem números.
            while True:
                protocolo = input("Informe o protocolo (15 dígitos numéricos): ").strip()
                if not protocolo.isdigit() or len(protocolo) != 15:
                    print("Protocolo inválido. Deve conter exatamente 15 dígitos numéricos.")
                    continue
                break

            consulta = 'SELECT * FROM ouvidoria WHERE protocolo = %s'
            dados = [protocolo]
            manifestacoes = listarBancoDados(conexao, consulta, dados)

            if manifestacoes:
                exibir_manifestacao(manifestacoes)
            else:
                print("Protocolo não encontrado.")

        elif opcao == 2:
            # Validação de código (apenas números, qualquer quantidade)
            while True:
                codigo = input("Informe o código (somente números): ").strip()
                if not codigo.isdigit():
                    print("Código inválido. Digite apenas números.")
                    continue
                break

            consulta = 'SELECT * FROM ouvidoria WHERE codigo = %s'
            dados = [codigo]
            manifestacoes = listarBancoDados(conexao, consulta, dados)

            if manifestacoes:
                exibir_manifestacao(manifestacoes)
            else:
                print("Código não encontrado.")

        elif opcao == 3:
            # Validação de tipo de manifestação (não pode ser vazio)
            while True:
                tipo = input("Informe o tipo de manifestação (ex: Reclamação, Elogio): ").strip()
                if not tipo:
                    print("O tipo de manifestação não pode estar vazio.")
                    continue
                break

            consulta = 'SELECT * FROM ouvidoria WHERE tipoManifestacao = %s'
            dados = [tipo]
            manifestacoes = listarBancoDados(conexao, consulta, dados)

            if manifestacoes:
                exibir_manifestacao(manifestacoes)
            else:
                print("Tipo de manifestação não encontrado.")

        elif opcao == 4:
            print("Encerrando a pesquisa...")
            break

        else:
            print("Opção inválida. Tente novamente.")



def numeroManifestacoes(conexao):
    consulta = 'select count(*) from ouvidoria'
    quantidade = listarBancoDados(conexao, consulta)


    if len(quantidade) == 0:
        print("Não possui manifestações em aberto")
    else:
        print(f"Numero de manifestações: {quantidade[0][0]} manifestações.")



def excluirManifestacao(conexao):
    codigo = int(input("Informe o codigo da manifestação que deseja cancelar:"))
    dados = [codigo]
    consulta = 'DELETE  FROM ouvidoria WHERE   codigo = %s'
    excluirBancoDados(conexao, consulta, dados)

    if len([codigo]) == 0:
        print("Não possui manifestações em aberto")
    else:
        print(f"Excluído com sucesso")



def mensagemSair(conexao):
    print("Saindo...")


def valorInvalido(conexao):
    print("Opção invalida")


encerrarConexao(conexao)
