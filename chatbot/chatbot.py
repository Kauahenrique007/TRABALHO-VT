import json
from config import INTENTS_FILE
from nlp import process_input
from responses import get_response


class ChatBot:
    def __init__(self):
        try:
            with open(INTENTS_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.intents = data.get('intents', [])
        except FileNotFoundError:
            print(f"Erro: O arquivo {INTENTS_FILE} não foi encontrado.")
            self.intents = []
        except json.JSONDecodeError:
            print("Erro ao decodificar o arquivo de intents. Verifique se o JSON está correto.")
            self.intents = []

    def get_response(self, user_input: str) -> str:
        if not user_input.strip():
            return "Por favor, digite algo para que eu possa responder."

        processed = process_input(user_input)
        response = get_response(processed, self.intents)

        return response if response else "Desculpe, não entendi. Pode reformular?"
