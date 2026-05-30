def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))

    def count(current: int, total: int) -> None:
        if current > total:
            print("Harvest time!")
            return
        print(f"Day {current}")
        count(current + 1, total)

    count(1, days)

