"""Intelligence providers (off-by-default local models)."""
from __future__ import annotations


class ModelProvider:
    def generate(self, prompt: str) -> str:
        return ""


class OllamaProvider(ModelProvider):
    def __init__(self, enabled: bool = False, base_url: str = "http://localhost:11434", model: str = "llama3") -> None:
        self.enabled = enabled
        self.base_url = base_url
        self.model = model

    def generate(self, prompt: str) -> str:
        if not self.enabled:
            return ""
        return ""
