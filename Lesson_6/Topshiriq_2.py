word = "Lorem ipsum dolor ipsum sit amet, consectetur elit adipisicing elit. Ratione qui reiciendis aliquid qui!"
def cleaner():
    word2 = ''
    for i in word.split():
        if word.count(i) == 1:
            word2 += f"{i} "
    print(word2)
cleaner()