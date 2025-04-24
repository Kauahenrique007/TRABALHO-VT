{
  "intents": [
    {
      "tag": "saudacao",
      "patterns": ["Oi", "Olá", "E aí", "Bom dia", "Boa tarde", "Boa noite", "Eae", "Opa", "Oi, tudo bem?", "Olá, como vai?"],
      "responses": ["Olá! Como posso te ajudar?", "Opa! Tudo certo?", "Fala aí!", "Diga ai meu mano!", "Oi! Precisa de algo?"]
    },
    {
      "tag": "despedida",
      "patterns": ["Tchau", "Até mais", "Falou", "Até logo", "Até a próxima", "Vou nessa"],
      "responses": ["Tchau! Até a próxima.", "Até mais!", "Falou mano!" "Volte sempre!", "Se cuida!"]
    },
    {
      "tag": "agradecimento",
      "patterns": ["Obrigado", "Valeu", "Fico agradecido", "Agradeço", "Muito obrigado", "Gratidão"],
      "responses": ["De nada!", "Sempre às ordens!", "Tamo junto!", "Tamo junto parceiro!", "Imagina, é um prazer ajudar!"]
    },
    {
      "tag": "duvida_python_if",
      "patterns": ["Como usar if em Python?", "Explica o if", "Python if else", "Estrutura condicional em Python"],
      "responses": [
        "O if em Python é usado para decisões. Exemplo:\n\n```python\nx = 10\nif x > 5:\n    print('Maior que 5')\n```",
        "Você pode usar if, elif e else para tomar decisões. Exemplo:\n\n```python\nif condicao:\n    ...\nelif outra:\n    ...\nelse:\n    ...\n```"
      ]
    },
    {
      "tag": "duvida_python_for",
      "patterns": ["Me explica for", "Como usar for em Python?", "Python for", "Laço for em Python"],
      "responses": [
        "O laço for é usado para repetir algo. Exemplo:\n\n```python\nfor i in range(5):\n    print(i)\n```",
        "Você pode percorrer listas, strings, e mais com for. Ex:\n\n```python\nfor letra in 'Python':\n    print(letra)\n```"
      ]
    },
    {
      "tag": "duvida_python_while",
      "patterns": ["O que faz o while?", "Explica o while", "While em Python", "Como funciona o while?"],
      "responses": [
        "While repete enquanto uma condição for verdadeira. Exemplo:\n\n```python\nx = 0\nwhile x < 5:\n    print(x)\n    x += 1\n```",
        "Use while quando não souber quantas vezes o código deve repetir, mas tiver uma condição."
      ]
    }
  ]
}