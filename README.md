 ## Diário de Hábitos Saudáveis (Python)
 Este projeto é um sistema simples e eficiente desenvolvido em Python que permite registrar e acompanhar hábitos saudáveis do dia a dia — como beber água, fazer exercícios, dormir cedo, entre outros. Inclui tanto uma interface de linha de comando quanto uma interface gráfica com Tkinter para facilitar a interação do usuário.

📌 Funcionalidades
📋 Modo Terminal (arquivo: diario_habitos.py)

✅ Adicionar novos hábitos

🗓️ Marcar hábitos como feitos no dia

📊 Visualizar progresso (número de vezes que um hábito foi realizado)

💾 Salvar e carregar dados automaticamente no arquivo habitos.txt

🖥️ Interface Gráfica (arquivo: interface.py)
🧑 Entrada de nome do usuário

👋 Exibição de mensagem de boas-vindas personalizada

🪟 Interface intuitiva com Tkinter

## ⚙️ Como Usar
▶️ Executar o Modo Terminal
bash
Copiar
Editar
python diario_habitos.py
Escolha uma das opções do menu:

[1] Adicionar hábito

[2] Marcar hábito como feito

[3] Ver progresso

[4] Sair e salvar

## ▶️ Executar a Interface Gráfica
bash
Copiar
Editar
python interface.py
Digite seu nome

Clique em "Enviar"

Veja a mensagem personalizada

 ## 🧱 Estrutura do Projeto
graphql
Copiar
Editar
diario-habitos/
│
├── diario_habitos.py     # Versão com menu interativo no terminal
├── interface.py          # Interface gráfica com Tkinter
├── habitos.txt           # Arquivo de armazenamento dos dados
└── README.md             # Documentação do projeto
🧠 Tecnologias Utilizadas
Python 3

Tkinter (para GUI)

Manipulação de arquivos .txt

Estruturas básicas: listas, dicionários, condicionais, loops, funções

 ## ✅ Pré-requisitos
Certifique-se de ter o Python 3.6 ou superior instalado em sua máquina.

Verifique sua versão:
bash
Copiar
Editar
python --version
