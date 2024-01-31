from requests import Session


class RestClient:
    def __init__(self, url: str, logs: list[dict], chunk_size: int = 500) -> None:
        self.errs = []
        self.session = Session()
        self.url = url
        self.logs = self._create_chunks(logs, chunk_size)

    def _create_chunks(self, logs: list[dict], chunk_size: int):
        """split all the logs into chunks"""
        chunks = []
        for i in range(0, len(logs), chunk_size):
            chunk = logs[i : i + chunk_size]
            chunks.append(chunk)
        return chunks

    def upload_data(self):
        """upload the logs to the api on manageable chunks"""
        headers = {"Content-Type": "application/json"}
        for log in self.logs:
            response = self.session.post(self.url, json=log, headers=headers)
            if response.status_code != 200:
                self.errs.append({"e": response.text, "log": log})
