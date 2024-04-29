a = [1, 2, 3, 4, 5]
b = [1, 1, 1, 0, 0]

hasil = []
temp = []

# Operasi konvolusi
for i in range(len(a)):
    for j in range(len(b)):
        temp.append(a[j]*b[i-1])
    hasil.append(sum(temp))
    temp = []
    
print(hasil)