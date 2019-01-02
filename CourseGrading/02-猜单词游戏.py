import random

HANGMAN_LIST = [
"""
    +---+
        |
        |
        |
       ===
""",
"""
    +---+
    o   |
        |
        |
       ===
    """,
"""
    +---+
    o   |
    |   |
        |
       ===
""",
"""
    +---+
    o   |
   /|   |
        |
       ===
""",
"""
    +---+
    o   |
   /|\  |
        |
       ===
""",
"""
    +---+
    o   |
   /|\  |
   /    |
       ===
""",
"""
    +---+
    o   |
   /|\  |
   / \  |
       ===
""",
]

def input_guess(guess_letter):
    while True:
        g = input("你猜的下一个字母是：")
        g = g.lower()
        if len(g) != 1:
            print("只能输入1个字母！")
        elif not g.isalpha():
            print("必须输入*字母*！")
        elif g in guess_letter:
            print("你已经猜过这个字母。再猜一遍...")
        else:
            return g

def play_set(target_word):
    hitted_letter = ["_"] * len(target_word)
    missed_letters = ""
    guess_error = 0
    print("H A N G M A N")
    while guess_error < len(HANGMAN_LIST) - 1:
        print(HANGMAN_LIST[guess_error])
        print("缺失的字母：")
        print("".join(hitted_letter))

        if guess_error > 0:
            print("没猜中的字母：" + missed_letters)

        guess_letter = "".join(hitted_letter) + missed_letters
        g = input_guess(guess_letter)
        hit = False
        for i in range(len(target_word)):
            if target_word[i] == g:
                hitted_letter[i] = g
                hit = True
        if hit:
            if "_" not in hitted_letter:
                break
        else:
            missed_letters += g
            guess_error += 1

    if guess_error == len(HANGMAN_LIST) - 1:
        print("真不幸，你丢命了！")
        print(HANGMAN_LIST[guess_error])
        print("被猜的单词是：" + target_word)
    else:
        print("你猜对了！" + target_word)
        print("棒棒哒！")

def continue_to_play():
    print()
    print("你要继续玩吗？（yes or no)")
    return input().lower().startswith("y")


target_words_strs = ["apple banana berry lemon lichee mango orange pear", "dog cat tiger elephant monkey bird snake horse", "blue green red purple yellow pink white black", "bus car boat ship taxi plane train jeep", "head foot leg tooth hand ear eye nose ", "beef noodle dumpling rice chip bread sandwich  egg", "doctor nurse policeman engineer worker farmer singer teacher", "fine rainy cloudy windy stormy foggy sunny snowy"]



start_game = True
while start_game:
    target_words_str = random.choice(target_words_strs)
    if target_words_str in target_words_strs[0]:
        print("所猜单词为：水果类")
    elif target_words_str in target_words_strs[1]:
        print("所猜单词为：动物类")
    elif target_words_str in target_words_strs[2]:
        print("所猜单词为：颜色类")
    elif target_words_str in target_words_strs[3]:
        print("所猜单词为：交通类")
    elif target_words_str in target_words_strs[4]:
        print("所猜单词为：身体类")
    elif target_words_str in target_words_strs[5]:
        print("所猜单词为：食物类")
    elif target_words_str in target_words_strs[6]:
        print("所猜单词为：职业类")
    elif target_words_str in target_words_strs[7]:
        print("所猜单词为：天气类")
    target_words = target_words_str.split()
    target_word = random.choice(target_words)
    play_set(target_word)

    start_game = continue_to_play()

print("拜拜")


