kata1 = input("Masukkan kata pertama\t: ")
kata2 = input("Masukkan kata kedua\t: ")
isAnagram = []
for i in range(len(kata1)):
    isAnagram.append(kata1[i] in kata2)

if False in isAnagram:
    print(f"{kata1} dan {kata2} bukan anagram")
else:
    print(f"{kata1} dan {kata2} adalah anagram")
    
        