from random import randrange

class Pet(object):
    "Um Animalzinho Virtual"
    fun_reduce = 1
    fun_max = 15
    fun_warning = 4
    hungry_reduce = 1
    hungry_max = 15
    hungry_warning = 4
    vocab = ['"Grrr..."','"Olá dono!!"' ]

    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type
        self.hungry = randrange(self.hungry_max)
        self.fun = randrange(self.fun_max)
        self.vocab = self.vocab[:]

    def __clock_tick(self):
        self.fun -= 1
        self.hungry -= 1


    def mood(self):
        if self.hungry > self.hungry_warning and self.fun > self.fun_warning:

            return f"""\n------------------------------------------\n    
                                      _         _
                                    /  \.-" "-./  \.
                                    \             /
                                    |    ꓥ   ꓥ    |
                                     \  .-'''-.  /
                                      '-\_Y_Y_/-'
                                         `---`
                 \nEstou me sentindo muito bem!"""

        elif self.hungry < self.hungry_warning:

            return f"""\n------------------------------------------\n   
                                      _         _
                                    /  \.-" "-./  \.
                                    \    \   /    /
                                    |    o   o    |
                                     \  .-'''-.  /
                                      '-\_Y_Y_/-'
                                         `---`
                             \nEstou com fome!!\n>:("""

        else:

            return f"""\n------------------------------------------\n  
                                      _         _
                                    /  \.-" "-./  \.
                                    \             /
                                    |    -   -    |
                                     \  .-'''-.  /
                                      '-\_Y_Y_'-'
                                         `---`
                                         \nEstou com Tédio\n"""

    def __str__(self):
        return "\nEu sou" + self.name + "." + "\ne estou " + self.mood + "."

    def teach(self, word):
        self.vocab.append(word)
        print(f"""\n------------------------------------------\n   
                                              _         _
                                            /  \.-" "-./  \.
                                            \             /
                                            |    ꓥ   ꓥ    |
                                             \  .-'''-.  /
                                              '-\_Y_Y_/-'
                                                 `---`
                                                 \nQue legal!\nAgora sei falar""", word)
        self.__clock_tick()

    def talk(self):
        print('Eu sou ', self.name, ',', 'e estou \n', self.mood(), '\n')
        self.__clock_tick()

    def feed(self):
        print(f"""\n------------------------------------------\n   
                                      _         _
                                    /  \.-" "-./  \.
                                    \             /
                                    |    ꓥ   ꓥ    |
                                     \  .-'''-.  /
                                      '-\_Y_Y_/-'
                                         `---`
                                         \nHmmmm.\nQue delícia!""")
        meal = randrange(self.hungry, self.hungry_max)
        self.hungry += meal

        if self.hungry < self.hungry_warning:
            self.hungry = self.hungry_warning
            print(f"""\n------------------------------------------\n   
                                      _         _
                                    /  \.-" "-./  \.
                                    \    \   /    /
                                    |    o   o    |
                                     \  .-'''-.  /
                                      '-\_Y_Y_/-'
                                         `---`
                                         \nAinda estou com fome!!\n:(""")
        elif self.hungry > self.hungry_max:
            self.hungry = self.hungry_max
            print(f"""\n------------------------------------------\n   
                                      _         _
                                    /  \.-" "-./  \.
                                    \    -   -    /
                                    |    o   o    |
                                     \  .-'''-.  /
                                      '-\_Y_Y_/-'
                                         `---`
                                                     \nEstou cheio!\nMuito obrigado""")
        self.__clock_tick()

    def play(self):
        print(f"""\n------------------------------------------\n   
                                      _         _
                                    /  \.-" "-./  \.
                                    \             /
                                    |    ꓥ   ꓥ    |
                                     \  .-'''-.  /
                                      '-\_Y_Y_/-'
                                         `---`
                                                             \nVocê é muito engraçado!! \nHAHAHAHAHAHA""")
        happiness = randrange(self.fun, self.fun_max)
        self.fun += happiness
        if self.fun < 0:
            self.fun = 0
            print(f"""\n------------------------------------------\n     
                                      _         _
                                    /  \.-" "-./  \.
                                    \             /
                                    |    ¬   ¬    |
                                     \  .-'''-.  /
                                      '-\_Y_Y_/-'
                                         `---`
                \nChato!\n>:(""")
        elif self.fun > self.fun_max:
            self.fun = self.fun_max
            print(f"""\n------------------------------------------\n    
                                      _         _
                                    /  \.-" "-./  \.
                                    \             /
                                    |    ꓥ   ꓥ    |
                                     \  .-'''-.  /
                                      '-\_Y_Y_/-'
                                         `---`
                \nEstou muito feliz!""")
        self.__clock_tick()


def main():
    player_name = input("Qual é o seu nome? ")
    pet_name = input('Qual é o nome do seu Pet? ')

    my_pet = Pet(pet_name, player_name)

    input(
        """
                    ****INTERAJA COM SEU PET***
    
                        \n------------------------------------------\n   
                                         _         _
                                        /  \.-" "-./  \.   Olá, Eu sou """+ my_pet.name +""" 
                                        \             /    Bem-vindo!!!
                                        |    ꓥ   ꓥ    |
                                         \  .-'''-.  /
                                          '-\_Y_Y_/-'
                                             `---`
             \nPressione enter para começar.
        """
    )

    choice = None

    while choice != 0:
        print(
            """
            ****INTERAJA COM SEU PET***
                
                \n------------------------------------------\n   
                                      _         _
                                    /  \.-" "-./  \.  Olá,""",player_name,"""
                                    \    -   -    /   Como vai ?
                                    |    o   o    |
                                     \  .-'''-.  /
                                      '-\_Y_Y_/-'
                                         `---`
         \n
    
            1 - Fale com seu Pet
            2 - Alimente com seu Pet
            3 - Brinque com seu Pet
            4 - Ensine seu Pet novas palavras
            0 - Sair
            """)

        choice = input("Escolha: ")

        if choice == '0':
            print('Tchau Tchau')
            quit()
        elif choice == '1':
            my_pet.talk()
        elif choice == '2':
            my_pet.feed()
        elif choice == '3':
            my_pet.play()
        elif choice == '4':
            new_word = input("Qual palavra você quer que "+ my_pet.name + " aprenda ? ")
            my_pet.teach(new_word)
        else:
            print('Esta opção é inválida! :/ ')

main()
