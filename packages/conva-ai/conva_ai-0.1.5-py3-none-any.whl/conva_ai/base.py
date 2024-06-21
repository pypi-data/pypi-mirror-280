import uuid
import requests


class BaseClient:

    def __init__(
        self, assistant_id: str, assistant_version: str, api_key: str, host: str = "https://infer-v2.conva.ai"
    ):
        self.assistant_id: str = assistant_id
        self.api_key: str = api_key
        self.assistant_version: str = assistant_version
        self.host: str = host
        self.keep_conversation_history: bool = True
        self.domain: str = ""
