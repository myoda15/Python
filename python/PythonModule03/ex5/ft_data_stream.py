import random
import typing

PLAYERS: list[str] = ["alice", "bob", "charlie", "dylan"]
ACTIONS: list[str] = [
    "run", "jump", "eat", "sleep", "move",
    "climb", "swim", "grab", "use", "release",
]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        yield (random.choice(PLAYERS), random.choice(ACTIONS))


def consume_event(
    events: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        idx: int = random.randint(0, len(events) - 1)
        event: tuple[str, str] = events[idx]
        events.pop(idx)
        yield event


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")

    generator = gen_event()
    for i in range(1000):
        name, action = next(generator)
        print(f"Event {i}: Player {name} did action {action}")

    generator2 = gen_event()
    event_list: list[tuple[str, str]] = [next(generator2) for _ in range(10)]
    print(f"Built list of 10 events: {event_list}")

    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")
