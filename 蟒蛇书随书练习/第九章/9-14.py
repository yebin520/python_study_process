from random import choice


"""初始化可能的彩票序列"""
possible_numbers = [i for i in range(1,11)]
other_words = ['A','B','C','D','Z']
for i in other_words:
    possible_numbers.append(i)

def make_randint_numbers(possible_numbers):
    last_numbers = []
    while len(last_numbers)<4:
        may_numbers = choice(possible_numbers)
        if may_numbers not in last_numbers:
            last_numbers.append(may_numbers)
        else :
            continue
    return last_numbers

def check(randint_numbers,winning_numbers):
    flag = True
    for i in range(len(randint_numbers)):
        if randint_numbers[i] not in winning_numbers:
            flag = False
            break
    return flag

winning_numbers = make_randint_numbers(possible_numbers)
print (winning_numbers)

play_times = 0
while True:
    play_times += 1
    randint_numbers = make_randint_numbers(possible_numbers)
    if check(randint_numbers,winning_numbers) == True:
        print ("Congraduation!You have winned the prize!")
        print (f"Your play's times is {play_times}")
        break
    else:
        continue