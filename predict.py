from cog import BasePredictor, Input, Path
import anthropic

class Predictor(BasePredictor):
    def setup(self):
        self.client = anthropic.Anthropic(
            api_key="your-anthropic-api-key-here"
        )

    def predict(self, prompt: str = Input(description="User question")) -> str:
        response = self.client.messages.create(
            model="claude-3.5-sonnet",  # replace if you have claude-3.7-sonnet access
            max_tokens=1024,
            temperature=0.2,
            messages=[
                {"role": "user", "content": f"Answer the following question based on Nelson Textbook of Pediatrics knowledge:\n{prompt}"}
            ]
        )
        return response.content
