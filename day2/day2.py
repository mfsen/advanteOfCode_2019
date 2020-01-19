file = open("/Users/mustafafatihsen/Desktop/codek/day2/input.txt")
data = file.readlines()
file.close()


data = data[0].split(",")
data = list(map(int, data))

for i in range(0,len(data),4):
    try:
        num1 = data[i+1]
        num2 = data[i+2]
        position = data[i+3]
    except:
        pass
    if data[i] == 1:
        data[position] = data[num1]+data[num2]
    elif data[i] == 2:
        data[position] = data[num1]*data[num2]
    elif data[i] == 99:
        break
    

print(data)


print("ok")