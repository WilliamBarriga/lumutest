from pandas import DataFrame


class Data:
    total_records: int
    rank_clients: DataFrame
    rank_hosts: DataFrame

    def __init__(self, df: list[dict]) -> None:
        self.df = DataFrame(df)
        self._total_records()
        self._rank_clients()
        self._rank_hosts()

    def _total_records(self):
        "set the total of records"
        self.total_records = len(self.df)

    def _ranks(self, column: str) -> DataFrame:
        "create a rank with total and percentage of the desired column"
        count = self.df[column].value_counts().reset_index()
        count.columns = [column, "count"]
        count = count.sort_values(by="count", ascending=False)
        count["percentage"] = round((count["count"] / self.total_records) * 100, 2)
        return count

    def _rank_clients(self) -> list[dict]:
        "create the rank for the clients"
        self.rank_clients = self._ranks("client_ip")

    def _rank_hosts(self) -> list[dict]:
        "create the rank for the hosts"
        self.rank_hosts = self._ranks("name")

    def __str__(self) -> str:
        "directly print on console statisc of the data"
        print(f"total records: {self.total_records}")

        print(f"Client IPs Rank")
        print(f"--------------- --- -----")
        print(self.rank_clients.head(10))

        print(f"Host Rank")
        print(f"--------------- --- -----")
        print(self.rank_hosts.head(10))
