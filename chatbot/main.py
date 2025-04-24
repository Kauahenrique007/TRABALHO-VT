import logging
from chatbot import ChatBot
from config import LOG_FILE

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
    print("🤖 Olá! Sou seu chatbot inteligente. Digite 'sair' para encerrar.\n")
    
    bot = ChatBot()

    while True:
        try:
            user_input = input("Você: ")
            if user_input.lower() in ['sair', 'exit', 'quit']:
                print("🤖 Chat encerrado. Até logo!")
                break

            response = bot.get_response(user_input)
            print(f"Bot: {response}")

        except KeyboardInterrupt:
            print("\n🤖 Chat encerrado por interrupção do usuário.")
            break
        except Exception as e:
            logging.error(f"Erro inesperado: {e}", exc_info=True)
            print("🤖 Ocorreu um erro. Verifique os logs para mais detalhes.")

if __name__ == "__main__":
    main()
