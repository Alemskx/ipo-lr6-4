str = str(input("Введи строку для поиска: "))
count = 0
arr =list()
with open('text.txt',encoding="UTF-8") as file:
    for line in file:
        if str in line:
            count+=1
            arr.append(line)
arr.sort()
for i in range(len(arr)):
    print(arr[i])
print("Количество строк содержащих подстроку ",str,":",count)
