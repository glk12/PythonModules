from typing import Generator
import random


def gen_event() -> Generator[tuple[str, str], None, None]:
    while True:
        names = ["alice", "bob", "charlie", "dylan"]
        actions = [
            "run",
            "eat",
            "sleep",
            "grab",
            "move",
            "climb",
            "swim",
            "release",
            "use",
        ]
        yield (random.choice(names), random.choice(actions))


def consume_event(
    events: list[tuple[str, str]],
) -> Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        index = random.randint(0, len(events))
        event = events[index]
        events.pop(index)
        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")
    for i in range(1000):
        name, action = next(gen_event())
        print(f"Event {i}: Player {name} did action {action}")

    events = []
    for i in range(10):
        events.append(next(gen_event()))
    print(f"Built list of 10 events: {events}")
    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")


if __name__ == "__main__":
    main()
