from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def output(self) -> tuple[int, str]:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def ingest(self, data: Any) -> None:
        try:

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            for n in data:
                if not isinstance(n, (int, float)):
                    return False
            return True
        elif isinstance(data, (int, float)):
            return True
        return False


def main():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATI ===\n")

    print("Testing Numeric Processor...")
    n = 42
    s = "Hello"
    n_processor = NumericProcessor()
    print(f"Trying to validate input '{n}': {n_processor.validate(n)}")
    print(f"Trying to validate input '{s}': {n_processor.validate(s)}")
    print("Test invalid ingestion of string 'foo' without prior validation:")



if __name__ == "__main__":
    main()
