print("Oyuna Hoşgeldin")

playing = input("Başlayalım mı ? ")


if playing.lower() != "evet":
    quit()

score = 0

print("Tamam Hadi Oynayalım :) ")

answer = input("Neyim Ben? ")
if answer.lower() == "bilgisayar":
    print("Doğru")
    score += 1
else:
    print("Yanlış")

answer = input("Bu oyunu hazırlayan kim ?  ")
if answer.lower() == "rıfat":
    print("Doğru")
    score += 1
else:
    print("Yanlış")

answer = input("Peki Ne işle uğraşıyor? ")
if answer.lower() == "yazılım":
    print("Doğru")
    score += 1
else:
    print("Yanlış")

answer = input("Başarılı Olacak mı ? ")
if answer.lower() == "evet":
    print("Doğru")
    score += 1
else:
    print("Yanlış")

answer = input("Peki Sen kimsin ? ")
if answer.lower() == "hasan":
    print("Doğru")
    score += 1
else:
    print("Yanlış")

print("Sonuç " + str(score) + " Doğru Cevap")
print("Başarın " + str((score / 5) * 100) + "%.")# littlecodes
