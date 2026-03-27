my_list = ["Abacaxi", "Banana", "Caju", "Goiaba", "Kiwi", "Laranja", "Manga", "Morango", "Pera", "Uva"]


def menuInterativo():
    opcao = 0
    while True:

        print('\n+'+'-'.ljust(27, '-')+'+')
        print('|     Sistema De Frutas     |')
        print('+' + '-'.ljust(27, '-') + '+')
        print('| 1- Buscar    | 2- Listar  |')
        print('| 3- Adicionar | 4- Remover |')
        print('| 5- Alterar   | 6- Sair    |')
        print('+'+'-'.ljust(27, '-')+'+')

        try:
            opcao = int(input('Opção: '))
        except:
            print('Digite um número válido!')
            continue
        if opcao == 1:
            buscaFruta()
        elif opcao == 2:
            visualizarLista()
        elif opcao == 3:
            adicionarFruta()
        elif opcao == 4:
            removerFruta()
        elif opcao == 5:
            alterarFruta()
        elif opcao == 6:
            print('Saindo...')
            break
        else:
            print('Opção inválida!')


def pesquisaBinaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = ((baixo + alto) // 2)
        chute = lista[meio]
        if chute == item:
            return meio
        elif chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None


def buscaFruta():
    fruta = input('Fruta: ').capitalize()
    posicao_fruta = pesquisaBinaria(my_list, fruta)
    if posicao_fruta is not None:
        print(f'{fruta} está localizado(a) na posição: {posicao_fruta}.')
    else:
        print(f'{fruta} não encontrado(a).')


def visualizarLista():
    print(' === FRUTAS === ')
    my_list.sort()
    for fruta in my_list:
        print(fruta)


def adicionarFruta():
    adicionar_fruta = input('Nome da fruta: ').capitalize()

    if adicionar_fruta not in my_list:
        my_list.append(adicionar_fruta)
        my_list.sort()
        print(f'{adicionar_fruta} adicionado(a).')
    else:
        print(f'{adicionar_fruta} já está na lista.')


def removerFruta():
    remover_fruta = input('Nome da fruta: ').lower()

    for fruta in my_list:
        if fruta.lower() == remover_fruta:
            my_list.remove(fruta)
            print(f'{fruta} removido(a).')
            return

    print(f'{remover_fruta} não encontrado(a).')


def alterarFruta():
    old_fruta = input('Nome da fruta: ').lower()

    for fruta in my_list:
        if fruta.lower() == old_fruta:
            new_fruta = input('Nova fruta: ').capitalize()

            if new_fruta in my_list:
                print(f'{new_fruta} já está na lista.')
                return

            indice = my_list.index(fruta)
            my_list[indice] = new_fruta
            my_list.sort()
            print(f'{old_fruta} alterado(a) para: {new_fruta}.')
            return

    print(f'{old_fruta} não encontrado(a).')