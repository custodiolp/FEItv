import os


# arquivos txt


ARQUIVO_USUARIOS = "usuarios.txt"
ARQUIVO_FILMES = "filmes.txt"
ARQUIVO_CURTIDAS = "curtidas.txt"
ARQUIVO_FAVORITOS = "favoritos.txt"


# verificar se os arquivos existem, caso contrário, criar arquivos vazios


arquivos = [
    ARQUIVO_USUARIOS,
    ARQUIVO_FILMES,
    ARQUIVO_CURTIDAS,
    ARQUIVO_FAVORITOS
]

for arquivo in arquivos:

    if not os.path.exists(arquivo):

        open(arquivo, "w").close()


# listas globais para armazenar os dados em memória


usuarios = []
filmes = []
curtidas = []
favoritos = []


# filmes padrão


FILMES_PADRAO = [

    ["1", "Círculo de Fogo", "Ação", "0"],
    ["2", "Transformers", "Ficção Científica", "0"],
    ["3", "Invocação do Mal 3", "Terror", "0"],
    ["4", "Como Mágica", "Fantasia", "0"],
    ["5", "Rei Leão", "Animação", "0"],
    ["6", "Velozes e Furiosos", "Ação", "0"]

]


# carregar dados dos arquivos para as listas globais


def carregar_dados():

    global usuarios
    global filmes
    global curtidas
    global favoritos

    usuarios = []
    filmes = []
    curtidas = []
    favoritos = []

    # usuários

    with open(ARQUIVO_USUARIOS, "r") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(";")
            if len(dados) == 3:
                usuarios.append(dados)

    # filmes

    with open(ARQUIVO_FILMES, "r") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(";")
            if len(dados) == 4:
                filmes.append(dados)

  

    if len(filmes) == 0:
        filmes.extend(FILMES_PADRAO)
        salvar_filmes()

    # curtidas

    with open(ARQUIVO_CURTIDAS, "r") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(";")
            if len(dados) == 2:
                curtidas.append(dados)

    # favoritos

    with open(ARQUIVO_FAVORITOS, "r") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(";")
            if len(dados) == 2:
                favoritos.append(dados)


# salvar usuarios


def salvar_usuarios():
    with open(ARQUIVO_USUARIOS, "w") as arquivo:
        for usuario in usuarios:
            arquivo.write(";".join(usuario) + "\n")


# salvar filmes


def salvar_filmes():
    with open(ARQUIVO_FILMES, "w") as arquivo:
        for filme in filmes:
            arquivo.write(";".join(filme) + "\n")


# salvar curtidas


def salvar_curtidas():
    with open(ARQUIVO_CURTIDAS, "w") as arquivo:
        for curtida in curtidas:
            arquivo.write(";".join(curtida) + "\n")


# salvar favoritos


def salvar_favoritos():
    with open(ARQUIVO_FAVORITOS, "w") as arquivo:
        for favorito in favoritos:
            arquivo.write(";".join(favorito) + "\n")


# logo do sistema


def logo():

    print("=" * 70)
    print(" " * 28 + "FEItv")
    print("=" * 70)
    print(" " * 20 + "Plataforma de Filmes ")
    print("=" * 70)


# menu inicial do sistema


def menu_inicial():

    while True:
        print("\n1 - Cadastrar usuário")
        print("2 - Fazer login")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()

        elif opcao == "2":
            usuario = login()

            if usuario:
                menu_usuario(usuario)

        elif opcao == "0":
            print("\nSistema encerrado!")
            break

        else:
            print("\nDigite uma opção válida!")


# cadastaro de usuário


def cadastrar_usuario():
    print("\n===== CADASTRO =====")

    nome = input("Digite seu nome: ")

    while True:
        email = input("Digite seu email: ")

        if "@" in email:

            break

        print("Email inválido!")

    while True:

        senha = input("Digite sua senha: ")
        confirmar = input("Confirme sua senha: ")

        if senha == confirmar:

            break

        print("As senhas não coincidem!")

    for usuario in usuarios:

        if usuario[1] == email:
            print("\nEsse email já está cadastrado!")
            return

    usuarios.append([nome, email, senha])

    salvar_usuarios()

    print("\nUsuário cadastrado com sucesso!")


# login de usuário


def login():
    print("\n===== LOGIN =====")

    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    for usuario in usuarios:

        if usuario[1] == email and usuario[2] == senha:
            print(f"\nBem-vindo(a), {usuario[0]}!")
            return usuario

    print("\nEmail ou senha incorretos!")
    return None


# menu do usuário


def menu_usuario(usuario):

    while True:

        print("\n" + "=" * 60)
        print("1 - Listar filmes")
        print("2 - Buscar filme")
        print("3 - Curtir filme")
        print("4 - Descurtir filme")
        print("5 - Adicionar favorito")
        print("6 - Remover favorito")
        print("7 - Ver favoritos")
        print("0 - Logout")
        print("=" * 60)

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_filmes()

        elif opcao == "2":
            buscar_filme()

        elif opcao == "3":
            curtir_filme(usuario)

        elif opcao == "4":
            descurtir_filme(usuario)

        elif opcao == "5":
            adicionar_favorito(usuario)

        elif opcao == "6":
            remover_favorito(usuario)

        elif opcao == "7":
            ver_favoritos(usuario)

        elif opcao == "0":
            print("\nLogout realizado!")
            break

        else:
            print("\nDigite uma opção válida!")


# listar filmes


def listar_filmes():

    print("\n" + "=" * 90)

    print(
        f'| {"ID":^5} | {"FILME":^30} | {"CATEGORIA":^25} | {"CURTIDAS":^10} |'
    )

    print("=" * 90)

    for filme in filmes:

        print(
            f'| {filme[0]:^5} | {filme[1][:30]:30} | {filme[2][:25]:25} | {filme[3]:^10} |'
        )

    print("=" * 90)


# buscar filme por Id


def buscar_filme():

    busca = input("\nDigite o id do filme: ").lower()

    encontrou = False

    for id_filme in filmes:

        if busca == id_filme[0]:

            encontrou = True

            print("\n" + "=" * 50)
            print(f"ID: {id_filme[0]}")
            print(f"Filme: {id_filme[1]}")
            print(f"Categoria: {id_filme[2]}")
            print(f"Curtidas: {id_filme[3]}")
            print("=" * 50)

    if not encontrou:

        print("\nNenhum filme encontrado!")


# curtir filme


def curtir_filme(usuario):

    listar_filmes()

    id_filme = input("\nDigite o ID do filme: ")

    for curtida in curtidas:

        if curtida[0] == usuario[1] and curtida[1] == id_filme:
            print("\nVocê já curtiu esse filme!")
            return

    for filme in filmes:

        if filme[0] == id_filme:

            filme[3] = str(int(filme[3]) + 1)

            curtidas.append([usuario[1], id_filme])

            salvar_filmes()
            salvar_curtidas()

            print("\nFilme curtido com sucesso!")
            return

    print("\nFilme não encontrado!")


# descurtir filme


def descurtir_filme(usuario):

    listar_filmes()

    id_filme = input("\nDigite o ID do filme: ")

    for curtida in curtidas:

        if curtida[0] == usuario[1] and curtida[1] == id_filme:

            curtidas.remove(curtida)

            for filme in filmes:

                if filme[0] == id_filme:

                    filme[3] = str(int(filme[3]) - 1)

            salvar_filmes()
            salvar_curtidas()

            print("\nCurtida removida!")
            return

    print("\nVocê não curtiu esse filme!")


# adicionar favorito


def adicionar_favorito(usuario):

    listar_filmes()

    id_filme = input("\nDigite o ID do filme favorito: ")

    for favorito in favoritos:

        if favorito[0] == usuario[1] and favorito[1] == id_filme:

            print("\nFilme já está nos favoritos!")
            return

    favoritos.append([usuario[1], id_filme])

    salvar_favoritos()

    print("\nFilme adicionado aos favoritos!")


# remover favorito


def remover_favorito(usuario):

    id_filme = input("\nDigite o ID do filme: ")

    for favorito in favoritos:

        if favorito[0] == usuario[1] and favorito[1] == id_filme:

            favoritos.remove(favorito)

            salvar_favoritos()

            print("\nFavorito removido!")
            return

    print("\nEsse filme não está nos favoritos!")


# ver favoritos


def ver_favoritos(usuario):

    print("\n===== FAVORITOS =====")

    encontrou = False

    for favorito in favoritos:

        if favorito[0] == usuario[1]:

            for filme in filmes:

                if filme[0] == favorito[1]:

                    encontrou = True

                    print("\n----------------------------")
                    print(f"ID: {filme[0]}")
                    print(f"Filme: {filme[1]}")
                    print(f"Categoria: {filme[2]}")
                    print("----------------------------")

    if not encontrou:

        print("\nNenhum favorito encontrado!")


# menu


carregar_dados()

logo()

menu_inicial()