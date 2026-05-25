word = input("digite uma palavra que voce disconhe para descobrir o resultado, escreva em letra maiuscula").upper()

meme_dict = {
            "AURA": "é como ganhar uma estrelinha, faz algo legal",
            "67": "é o nome de um time de basquete (meu esporte favorito) e significa 2 metros de altura em pes",
    "SIGMA": "pessoa muito top/legal"
            }

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("eita essa ate nois disconhece, adolecentes loucos kkk")
