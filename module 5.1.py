class House:
    def __init__(self, name, num):
        self.name = name
        self.number_of_floors = num
    def go_to(self, new_flor):
        if 1 <= new_flor and new_flor <= self.number_of_floors:
            for i in range(1, new_flor + 1):
                print(i)
        else:
            print('Такого этажа не существует')
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)