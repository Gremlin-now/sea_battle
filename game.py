import os

def game_area(area):
    s = 0
    str_ = ""
    for i in "АБВГДЕЖЗИК":
        str_ += i + " "
    print("\t" + str_)
    for a in range(10):
        str_ = ""
        for i in "АБВГДЕЖЗИК":
            str_ +=str(area[i][a]) + " "
        s += 1
        print(str(s)+ "\t" + str_.rstrip())
def dictionary():
    return{a : [0 for i in range(10)] for a in "АБВГДЕЖЗИК"}

str_ = ""
area_1 = dictionary()
area_2 = dictionary()
st = [[4, 1], [3, 2], [2, 3], [1, 4]]
while st[0][0] != 0 or st[1][0] != 0 or st[2][0] != 0 or st[3][0] != 0:
    os.system("clear")
    game_area(area_1)
    print("""Раставьте корабли на поле
    Выберите тип корабля:
    1. 1-х палубный[{}]
    2. 2-х палубный[{}]
    3. 3-х палубный[{}]
    4. 4-х палубный[{}]""".format(st[0][0], st[1][0], st[2][0], st[3][0]))
    a = int(input("\n..:"))
    try:
        for i in range(st[a-1][0]):
            for s in range(st[a-1][1]):
                print("Осталось корблей: {}".format(st[a-1][0]))
                area_1[input("Введите столбец: ").upper()][int(input("Введите строку: "))-1] = "\033[32m\033[1m{}\033[0m".format(a)
                os.system("clear")
                game_area(area_1)
            st[a-1][0] -= 1
    except KeyError or ValueError:
        print("Ошибка!!!")
