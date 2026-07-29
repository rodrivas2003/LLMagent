# anthropic_client.py

import anthropic

class AnthropicClient:
    def __init__(self, api_key=None, model="claude-haiku-4-5-20251001", max_tokens=1024):
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = model
        self.max_tokens = max_tokens

    def generate(self, system, prompt):
        response = self.client.messages.create(
            model=self.model,
            max_tokens=self.max_tokens,
            system=system,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text