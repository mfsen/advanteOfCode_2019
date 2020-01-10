def calculatefuel(fuel):
    tot =0
    while fuel>6:
        fuel = int(fuel/3)-2
        tot += fuel
    return tot

def calfuelforweith(weight):
    fuel = int(weight/3)-2
    return fuel

requretfuel =0 
personsfile = open("codekday1.txt","r")
persons = personsfile.readlines()

for i in persons:

    f = calfuelforweith(int(i))
    r = calculatefuel(f)
    requretfuel = requretfuel+f+r

print(requretfuel)

