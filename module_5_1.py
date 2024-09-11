class House:

    def __init__(self, name, q_floor):
        self.name = name
        self.q_floor = q_floor


    def go_to(self, new_floor):
        if new_floor == 0 or new_floor > self.q_floor:
            print('Нет такого этажа!')
            return
        for i in range(0, new_floor):
            print(i + 1)


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
