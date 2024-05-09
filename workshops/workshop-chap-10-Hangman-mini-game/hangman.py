import random                             # для случайного выбора слова

def hangman():
    list_words=['программа',
                'бекенд',
                'дата сайнс',
                'кибербезопасность',
                'айти',                    # список со словами
                'сис админ',
                'фронтенд',
                'джава',
                'пайтон',
                'джаваскрипт']
    wrongs=0                               # кол-во ошибок
    stages=["",
            "________      ",
            "|      |      ",
            "|      0      ",              # стадии
            "|     /|\     ",
            "|     / \     ",
            "|"]

    word=random.choice(list_words)

    letters=list(word)                     # список угаданных букв, которые будут помечаться как $, пользователь не видит
    board=['__']*len(word)                 # доска угаданных букв, пользователь видит
    win=False                              # статус победы

    print('\n\nДобро пожаловать на казнь!\n')

    while wrongs<len(stages)-1:            # цикл, код выполняется когда кол-во ошибок меньше стадий

        msg=input('Введите букву (Пробел в слове тоже может быть!): ')      # ввод буквы
        if msg in letters:                                                  # если мы угадываем букву
            index=letters.index(msg)
            board[index]=msg
            letters[index]='$'

        else:                                                              # если мы не угадываем букву
            wrongs+=1

        print(' '.join(board))                # вывод угаданной буквы и стадий
        e=wrongs+1
        print('\n'.join(stages[:e]))

        if '__' not in board:                                           # если мы угадали все буквы
            print('Вы выйграли! Было загадано слово: {}'.format(word))
            print(' '.join(board))
            win=True
            break

    if not win:
        print('\n'.join(stages))
        print('\nВы проиграли! Было загадано слово: {}'.format(word))  # пройгрыш

hangman()