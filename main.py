import sys
import re

from io import TextIOWrapper

from clean_logs import Log
from data import Data
from rest import RestClient

errs = []


def check_file() -> TextIOWrapper:
    """validate if is the file used as arg in the script"""
    if len(sys.argv) != 2:
        raise Exception("file not fount")

    file_path = sys.argv[1]

    return open(file_path, "r")


def parse_file(file: TextIOWrapper) -> list[Log]:
    """read the file and return the right sctructure for manipulation"""
    pattern = r"(?P<timestamp>\d{1,2}-\w{3}-\d{4} \d{2}:\d{2}:\d{2}\.\d{3}) queries: info: client @(?P<client_name>0x[\da-f]+) (?P<client_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})#\d+ \((?P<name>[^\s]+)\): query: (?P=name) IN (?P<type>\w)"
    parsed_logs = []
    for log in file:
        match = re.search(pattern, log.strip())
        if not match:
            errs.append(
                {
                    "e": "no items matched",
                    "log": log,
                }
            )
            pass
        log = Log(**match.groupdict()).model_dump()
        parsed_logs.append(log)

    return parsed_logs


def main():
    file = check_file()

    logs = parse_file(file)

    path = "https://api.lumu.io/collectors/5ab55d08-ae72-4017-a41c-d9d735360288/dns/queries?key=d39a0f19-7278-4a64-a255-b7646d1ace80"

    # upload data to api
    rest = RestClient(path, logs)
    rest.upload_data()
    print(rest.errs)

    # read and analyze the data
    data = Data(logs)
    data.__str__()

    if "file" in locals():
        file.close()


if __name__ == "__main__":
    main()
