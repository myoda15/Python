class Plant:
    def __init__(self) -> None:
        self.name: str = ""
        self.height: float = 0.0
        self._age: int = 0
        self.growth_rate: float = 0.8

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self._age} days old")

    def grow(self) -> None:
        self.height = round(self.height + self.growth_rate, 1)

    def age(self, days: int = 1) -> None:
        self._age += days


if __name__ == "__main__":
    rose = Plant()
    rose.name = "Rose"
    rose.height = 25.0
    rose._age = 30
    rose.growth_rate = 0.8

    print("=== Garden Plant Growth ===")
    start_height: float = rose.height
    rose.show()
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow()
        rose.age()
        rose.show()
    total_growth: float = round(rose.height - start_height, 1)
    print(f"Growth this week: {total_growth}cm")
