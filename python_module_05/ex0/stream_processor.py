from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            print("Validation: Error")
            return "Data needs to be a list of numbers."
        print("Validation: Numeric data verified")
        total = 0
        for n in data:
            total += n
        avg = total / len(data)
        return self.format_output(
            f"Processed {len(data)} numeric values, sum={total}, avg={avg}"
        )

    def validate(self, data: Any) -> bool:
        if isinstance(data, (list, tuple)):
            for n in data:
                if not isinstance(n, (int, float)):
                    return False
            return True
        return False


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            print("Validation: Error")
            return "Data needs to be text."
        print("Validation: Text data verified")
        text = data.strip()
        c_count = len(text)
        w_count = len(text.split())
        return self.format_output(
            f"Processed text: {c_count} characters, {w_count} words"
        )

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        return False


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            print("Validation: Error")
            return "Data must be an [ALERT] or [ERROR] log"
        print("Validation: Log entry verified")
        text = data.strip()

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            if data.split()[0] == "[ALERT]" or "[ERROR]":
                return True
        return False

    def format_output(self, result: str) -> str:
        return f"Processed text: {c_count}, {w_count} words"


def main():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    print("Initializing Numeric Processor...")
    nums = [1, 2, 3, 4, 5]
    n_processor = NumericProcessor()
    print(f"Processing data: {nums}")
    print(n_processor.process(nums))

    print("\nInitializing Text Processor...")
    s = "Hello Nexus World"
    t_processor = TextProcessor()
    print(f'Processing data: "{s}"')
    print(t_processor.process(s))


if __name__ == "__main__":
    main()
