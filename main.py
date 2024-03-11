import pickle
from pokemon import *
from pessoa import *

def escolher_pokemon_inicial(player):
    print(f"Olá, {player}, você poderá escolher agora o Pokémon que irá lhe acompanhar nessa jornada!")

    pikachu = PokemonEletrico("Pikachu", level=1)
    charmander = PokemonFogo("Charmander", level=1)
    squirtle = PokemonAgua("Squirtle", level=1)
    print()
    print("Você possui 3 escolhas: ")
    print("1 -",pikachu)
    print("2 -",charmander)
    print("3 -",squirtle)

    while True:
        escolha = input("Escolha o seu Pokémon: ")

        if escolha == "1":
            player.capturar(pikachu)
            break
        
        elif escolha == "2":
            player.capturar(charmander)
            break

        elif escolha == "3":
            player.capturar(squirtle)
            break

        else:
            print("Escolha inválida")


def salvar_jogo(player):
    try:
        with open("database.db","wb") as arquivo:
            pickle.dump(player,arquivo)
            print(">>>>> Jogo salvo com sucesso!")

    except Exception as error:
        print(">>>>> Erro ao salvar jogo!")
        print(error)


def carregar_jogo():
    try:
        with open("database.db","rb") as arquivo:
            player = pickle.load(arquivo)
            print(">>>>> Loading feito com sucesso!")
            return player
        
    except Exception as error:
        print("Save não encontrado")
        print(error)


#INÍCIO DO PROGRAMA
if __name__ == "__main__":
    print("-"*5,"Bem-vindo ao game Pokémon RPG de terminal","-"*5)

    player = carregar_jogo()

    if not player:
        nome = input("Olá, qual é o seu nome: ")
        player = Player(nome)
        print()
        print(f"Olá {player}, esse é um mundo habitado por pokémons, a partir de agora, a sua missão é se tornar um mestre de pokémons...")
        print("Capture o máximo de pokémons que conseguir e lute com seus inimigos...")
        print()
        print("Boa sorte.")
        print()

        player.mostrar_dinheiro()

        if player.pokemons:
            print("Já vi que você tem alguns pokémons")
            player.mostrar_pokemons()
        else:
            print("Você não tem nenhum pokémon, portanto, precisa escolher um")
            escolher_pokemon_inicial(player)

        print("Pronto, agora que você já possui um pokémon, enfrente o seu arqui-rival desde o seu jardim da infância, Gary...")
        gary = Inimigo(nome="Gary", pokemons=[PokemonAgua("Squirtle", level=1)])
        player.batalhar(gary)
        salvar_jogo(player)

    while True:
        print("--"*10)
        print("O que deseja fazer: ")
        print("1 - Explorar pelo mundão a fora")
        print("2 - Lutar com um inimigo")
        print("3 - Ver Pokédex")
        print("0 - Sair do jogo")
        escolha = input("Sua escolha: ")

        if escolha == "0":
            print("Fechando o jogo...")
            break

        elif escolha == "1":
            player.explorar()
            salvar_jogo(player)
        
        elif escolha == "2":
            inimigo_aleatorio = Inimigo()
            player.batalhar(inimigo_aleatorio)
            salvar_jogo(player)

        elif escolha == "3":
            player.mostrar_pokemons()

        else:
            print("Escolha inválida")

    
