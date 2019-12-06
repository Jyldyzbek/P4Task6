# Тип дома, общая площадь и список наименований мебели в новом доме 
# вообще нет мебели.
# Мебель имеет название и площадь, из которых кровать: 4 кв. м. шкаф:
#  2 кв. м. стол:
# 1,5 квадратных метра
# Добавьте вышеуказанные три предмета мебели в дом
# При печати дома требуется вывод: тип дома, общая площадь,
#  оставшаяся площадь,
# список имен мебели.




class Hause:
    def __init__(self):
        self.hause = 200
        print(f"Площадь пустого дома:{self.hause}")

    def hausehold_type(self, bad, wardrobe, table, *args):
        self.bad = bad
        self.table = table
        self.wardrobe = wardrobe
        self.kv = self.wardrobe + self.table + self.bad
        self.dop_kv = 0
        print(f'Bad, Tab, Wardrop {self.kv}кв м')

    def otvet(self):
        self.kvad = self.hause - self.kv
        print(f'В доме {self.kvad}кв м свободного места.')
ot = Hause()
ot.hausehold_type(4, 1.5, 2)
ot.otvet()