#first code


import random

top_of_range = input("Numara Tipi: ")



if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Lütfen 0 dan büyük bir rakam seçin! ")
        quit()
else:
    print("Lütfen 1 ila 10 arası bir numara tahmini yapın ")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Bir numara tahmini yapın : ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Lütfen 1 ila 10 arası bir numara tahmini yapın ")
        continue

    if user_guess == random_number:
        print("Bravooo! ")
        break
    elif user_guess > random_number:
        print("Daha Düşük bir numara seç ")
    else:
        print("Daha Yüksek bir numara seç ")

print("Tamamladın", guesses, "Tahminde")
# littlecodes
