N = int(input("Enter the length of the pool N: ")) #Ввести длину N бассейна
M = int(input("Enter the width of the pool M: ")) #Ввести ширину M бассейна
x = int(input("Enter the distance to one side: ")) #Ввести расстояние до одного борта бассейна
y = int(input("Enter the distance to the other side: ")) #Ввести расстояние до второго борта бассейна

s = [x, y, M - x, N - y, M - y, N - x]
print(s)

pos = []
for i in s:
    if i >= 0:
        pos.append(i)
print("The shortest distance is: " + str(min(pos)))
