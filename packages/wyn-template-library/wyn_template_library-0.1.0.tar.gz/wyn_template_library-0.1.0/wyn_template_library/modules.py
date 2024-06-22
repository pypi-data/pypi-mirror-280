from openai import OpenAI


class ChatBot:
    def __init__(self, OPENAI_API_KEY, PROTOCOL, MODEL):
        self.api_key = OPENAI_API_KEY
        self.protocol = PROTOCOL
        self.model = MODEL
        self.client = OpenAI(api_key=self.api_key)
        self.history = [{"role": "system", "content": self.protocol}]

    def generate_response(self, prompt: str) -> str:
        self.history.append({"role": "user", "content": prompt})
        
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=self.history
        )
        
        response = completion.choices[0].message.content
        self.history.append({"role": "assistant", "content": response})
        
        return response

    def get_history(self) -> list:
        return self.history