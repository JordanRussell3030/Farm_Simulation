from animal_class import *

class Cow(Animal):
    def __init__(self):
        super().__init__(1, 5, 4)
        self._type = "Cow"

    def grow(self, food, water):
        if food >= self._food_need and water >= self._water_need:
            self._weight += self._growth_rate
        self._days_growing += 1
        self._update_status()
