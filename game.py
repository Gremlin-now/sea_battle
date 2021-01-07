import os

def game_area(area):
    s = 0
    str_ = ""
    for i in "АБВГДЕЖЗИК":
        str_ += i + " "
    print("\t" + str_)
    for i in "АБВГДЕЖЗИК":
        str_ = ""
        for a in range(10):
            str_ +=str(area[i][a]) + " "
        s += 1
        print(str(s)+ "\t" + str_.rstrip())
def dictionary():
    return{a : [0 for i in range(10)] for a in "АБВГДЕЖЗИК"}

str_ = ""
area_1 = dictionary()
area_2 = dictionary()
os.system("clear")
game_area(area_1)
print()
game_area(area_2)
