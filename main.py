import io
str = str(input("Введи строку для поиска: "))
count = 0
arr =list()
with io.open('text.txt',encoding="UTF-8") as file:
    for line in file:
        if str in line:
            count+=1
            arr.append(line)
arr.sort()

print(arr)
print("Количество строк содержащих подстроку ",str,":",count)