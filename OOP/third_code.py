#OOP class : Great Learning(Youtube)

class Phone:
    def set_color(self,color: str):
        self.color = color

    def set_cost(self,cost: int):
        self.cost = cost

    def show_color(self):
        return self.color
    def show_cost(self):
        return self.cost

    def make_call(self):
        print("I am making a call")

    def play_game(self):
        print("I am playing a game")
#creting a object
Lava = Phone()
Lava.make_call()
Lava.play_game()
Lava.set_cost(5000)
print(Lava.show_cost())