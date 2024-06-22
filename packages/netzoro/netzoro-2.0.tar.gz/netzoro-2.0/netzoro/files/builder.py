class House:
    def __init__(self):
        self.walls = None
        self.roof = None
        self.windows = None
        self.doors = None

    def __str__(self):
        return f"House with {self.walls} walls, {self.roof} roof, {self.windows} windows, and {self.doors} doors."

class HouseBuilder:
    def __init__(self):
        self.house = House()

    def build_walls(self, walls):
        self.house.walls = walls
        return self

    def build_roof(self, roof):
        self.house.roof = roof
        return self

    def build_windows(self, windows):
        self.house.windows = windows
        return self

    def build_doors(self, doors):
        self.house.doors = doors
        return self

    def get_house(self):
        return self.house

# Usage
builder = HouseBuilder()
house = builder.build_walls("brick").build_roof("shingle").build_windows(4).build_doors(2).get_house()
print(house)
