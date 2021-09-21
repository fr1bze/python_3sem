#prgrm2
#class Car: 
#    def __init__(self,capacity, speed, number):
#        self.capacity = capacity
#        self.speed = speed
#        self.number = number
#class RaceCar(Car):
#    def __init__(self, speed):
#        super().__init__(0, speed, None)
#c = Car(1000, 100, "a720po")
#print(c.capacity, c.speed, c.number)
#r = RaceCar(300)
#print(r.capacity, r.speed, r.number)

#prgrm3
#class MoneyBox:
#    # Конструктор и деструктор, если нужны
#    storage = {}
#    tmp_storage = 0
#    # Добавить монетку достоинством value
#    def add_coin(self, value):
#        if self.storage.get(value):
#            self.storage[value] += 1
#        else:
#            self.storage.setdefault(value, 1)
#    def get_coins_number(self):
#        return sum(v for k,v in self.storage.items())
#    # Получить текущее общее достоинство всех монеток
#    def get_coins_value(self):
#        return sum(k*v for k,v in self.storage.items())
   
#m = MoneyBox()
# Добавили монетку достоинством 10
#m.add_coin(10)
    # Добавили монетку достоинством 5
#m.add_coin(5)
    # Ожидаем, что монеток внутри 2 штуки
#print(m.get_coins_number())
   # Ожидаем, что общее достоинство всех монеток 15
#print(m.get_coins_value())

#4prgrm
#class Car: 
#    def __init__(self,capacity, speed, number):
#        self.capacity = capacity
#        self.speed = speed
#        self.number = number
#    def __str__(self):
#        return "<Car capacity:%s speed:%s number:%s" % (self.capacity, self.speed, self.number)
#c = Car(1000, 100, "a720po")
#print(c)

#5prgrm

class Car: 
    def __init__(self,capacity, speed, number):
        self.capacity = capacity
        self.speed = speed
        self.number = number
# Создадим несколько машин
# Причём a и c - одна и та же машина с точки зрения сравнения
a = Car(100, 100, "asd")
b = Car(100, 100, "zzz")
c = Car(200, 50, "asd")

# Эти не равны
print(a == b)
# Эти равны
print(a == c)

# А эта пара примеров должна не упасть
# и корректно сказать, что машина не равна ни None, ни целому числу
print(a == None)
print(a == 1)

# Попробуем сложить машины в set
s = set()
s.add(a)
s.add(b)
s.add(c)
s.add(a)
s.add(a)

# Ожидаем увидеть номера двух машин,
# так как всё остальное в описанной логике является дублями
print("=== Cars in set ===")
for z in sorted(s, key=lambda e: e.number):
    print(z.number)
