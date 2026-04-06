from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.data: list[str] = []
        self.rank: int = 0

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def output(self) -> tuple[int, str]:
        value = self.rank
        self.rank += 1
        return value, self.data.pop(0)


class NumericProcessor(DataProcessor):
    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        print(f"Processing data: {data}")
        if isinstance(data, list):
            for n in data:
                self.data.append(str(n))
        else:
            self.data.append(str(data))

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            for n in data:
                if not isinstance(n, (int, float)):
                    return False
            return True
        elif isinstance(data, (int, float)):
            return True
        return False


class TextProcessor(DataProcessor):
    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        print(f"Processing data: {data}")
        if isinstance(data, list):
            for s in data:
                self.data.append(s)
        else:
            self.data.append(str(data))

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            for s in data:
                if not isinstance(s, str):
                    return False
            return True
        elif isinstance(data, str):
            return True
        return False


class LogProcessor(DataProcessor):
    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        print(f"Processing data: {data}")
        if isinstance(data, list):
            for dic in data:
                self.data.append(f"{dic['log_level']}: {dic['log_message']}")
        else:
            self.data.append(data)

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            for dic in data:
                if not isinstance(dic, dict):
                    return False
                for k, v in dic.items():
                    if not isinstance(k, str) or not isinstance(v, str):
                        return False
        elif not isinstance(data, dict):
            return False
        return True


def main():
    print("=== Code Nexus - Data Processor ===\n")

    print("Testing Numeric Processor...")
    n_processor = NumericProcessor()
    print(f"Trying to validate input '42': {n_processor.validate(42)}")
    print(f"Trying to validate input 'Hello': {n_processor.validate('Hello')}")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        n_processor.ingest("foo")
    except ValueError as e:
        print(f"Got exception: {e}")
    n_processor.ingest([1, 2, 3, 4, 5])
    print("Extracting 3 values...")
    for _ in range(3):
        rank, value = n_processor.output()
        print(f"Numeric value {rank}: {value}")

    print("\nTesting Text Processor...")
    t_processor = TextProcessor()
    print(f"Trying to validate input '42': {t_processor.validate(42)}")
    t_processor.ingest(["Hello", "Nexus", "World"])
    print("Extracting 1 value...")
    rank, value = t_processor.output()
    print(f"Text value {rank}: {value}")

    print("\nTesting Log Processor...")
    l_processor = LogProcessor()
    print(f"Trying to validate input 'Hello': {l_processor.validate('Hello')}")
    logs = [
        {
            "log_level": "NOTICE",
            "log_message": "Connection to server",
        },
        {
            "log_level": "ERROR",
            "log_message": "Unauthorized access!!",
        },
    ]
    l_processor.ingest(logs)
    print("Extracting 2 values...")
    for _ in range(2):
        rank, value = l_processor.output()
        print(f"Log entry {rank}: {value}")


if __name__ == "__main__":
    main()
