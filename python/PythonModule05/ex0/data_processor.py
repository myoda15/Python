import abc
import typing


class DataProcessor(abc.ABC):

    def __init__(self) -> None:
        self._data: list[tuple[int, str]] = []
        self._total: int = 0
        self._rank: int = 0
        self.name: str = "Data Processor"

    @property
    def total(self) -> int:
        return self._total

    @property
    def remaining(self) -> int:
        return len(self._data)

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._data:
            raise IndexError("No data in processor")
        return self._data.pop(0)


class NumericProcessor(DataProcessor):

    def __init__(self) -> None:
        super().__init__()
        self.name = "Numeric Processor"

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, bool):
            return False
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list) and data:
            return all(
                isinstance(x, (int, float)) and not isinstance(x, bool)
                for x in data
            )
        return False

    def ingest(
        self,
        data: typing.Union[int, float, list[typing.Union[int, float]]]
    ) -> None:
        if not self.validate(data):
            raise TypeError("Improper numeric data")
        items: list[typing.Union[int, float]]
        if isinstance(data, list):
            items = data
        else:
            items = [data]
        for item in items:
            self._data.append((self._rank, str(item)))
            self._rank += 1
            self._total += 1


class TextProcessor(DataProcessor):

    def __init__(self) -> None:
        super().__init__()
        self.name = "Text Processor"

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list) and data:
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: typing.Union[str, list[str]]) -> None:
        if not self.validate(data):
            raise TypeError("Improper text data")
        items: list[str]
        if isinstance(data, list):
            items = data
        else:
            items = [data]
        for item in items:
            self._data.append((self._rank, item))
            self._rank += 1
            self._total += 1


class LogProcessor(DataProcessor):

    def __init__(self) -> None:
        super().__init__()
        self.name = "Log Processor"

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, dict):
            return all(
                isinstance(k, str) and isinstance(v, str)
                for k, v in data.items()
            )
        if isinstance(data, list) and data:
            return all(
                isinstance(x, dict) and all(
                    isinstance(k, str) and isinstance(v, str)
                    for k, v in x.items()
                )
                for x in data
            )
        return False

    def ingest(
        self,
        data: typing.Union[dict[str, str], list[dict[str, str]]]
    ) -> None:
        if not self.validate(data):
            raise TypeError("Improper log data")
        items: list[dict[str, str]]
        if isinstance(data, list):
            items = data
        else:
            items = [data]
        for item in items:
            log_str = f"{item['log_level']}: {item['log_message']}"
            self._data.append((self._rank, log_str))
            self._rank += 1
            self._total += 1


def main() -> None:
    print("=== Code Nexus - Data Processor ===")
    print()

    print("Testing Numeric Processor...")
    num_proc = NumericProcessor()
    print(f" Trying to validate input '42': {num_proc.validate(42)}")
    print(
        f" Trying to validate input 'Hello': {num_proc.validate('Hello')}"
    )
    print(
        " Test invalid ingestion of string 'foo' without prior validation:"
    )
    try:
        num_proc.ingest("foo")  # type: ignore
    except TypeError as e:
        print(f" Got exception: {e}")
    data_num = [1, 2, 3, 4, 5]
    print(f" Processing data: {data_num}")
    num_proc.ingest(data_num)
    print(" Extracting 3 values...")
    for _ in range(3):
        rank, val = num_proc.output()
        print(f" Numeric value {rank}: {val}")

    print()

    print("Testing Text Processor...")
    txt_proc = TextProcessor()
    print(f" Trying to validate input '42': {txt_proc.validate(42)}")
    data_txt: list[str] = ['Hello', 'Nexus', 'World']
    print(f" Processing data: {data_txt}")
    txt_proc.ingest(data_txt)
    print(" Extracting 1 value...")
    rank, val = txt_proc.output()
    print(f" Text value {rank}: {val}")

    print()

    print("Testing Log Processor...")
    log_proc = LogProcessor()
    print(
        f" Trying to validate input 'Hello': {log_proc.validate('Hello')}"
    )
    data_log: list[dict[str, str]] = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
    ]
    print(f" Processing data: {data_log}")
    log_proc.ingest(data_log)
    print(" Extracting 2 values...")
    for _ in range(2):
        rank, val = log_proc.output()
        print(f" Log entry {rank}: {val}")


if __name__ == "__main__":
    main()
