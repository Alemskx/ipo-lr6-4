search_string = input("Введи строку для поиска: ").lower()
count = 0
arr = []

with open('text.txt', encoding="UTF-8") as file:
    for line in file:
        line_lower = line.lower()
        if search_string in line_lower:
            count += 1
            arr.append(line)

arr.sort()

for i in range(len(arr)):
    print(arr[i])
print("Количество строк, содержащих подстроку '",search_string,"' = ",count)
