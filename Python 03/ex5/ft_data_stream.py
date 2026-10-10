import random
from typing import Generator

PLAYERS = ["alice", "bob", "charlie", "dylan"]

ACTIONS = ["run", "eat", "sleep", "grab", "move", "climb", "swim", "release"]


def gen_event() -> Generator[tuple[str, str], None, None]:
    while True:
        event = (random.choice(PLAYERS), random.choice(ACTIONS))
        yield event


def consume_event(
        events: list[tuple[str, str]]
        ) -> Generator[tuple[str, str], None, None]:
    while events:
        event = events.pop(random.randint(0, len(events) - 1))
        yield event


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    gen = gen_event()
    for i in range(1000):
        name, action = next(gen)
        print(f"Event {i}: Player {name} did action {action}")
    events: list[tuple[str, str]] = [next(gen) for _ in range(10)]
    print(f"Built list of 10 events: {events}")
    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")
