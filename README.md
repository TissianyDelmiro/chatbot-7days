# 🤖 Chatbot 7DaysOfCode

Chatbot conversacional desenvolvido durante o desafio **#7DaysOfCode** da Alura, utilizando um modelo de linguagem local e interface interativa.

## 📌 Sobre o projeto

O desafio foi aceito com um objetivo claro: **aprender, se desafiar e fazer algo diferente**. Ao longo de 7 dias, o projeto evoluiu desde a configuração do ambiente até a implementação completa de um chatbot com memória de conversa, handlers e interface web.

Um detalhe curioso: o projeto deveria ser feito no **Google Colab**, mas no início foi desenvolvido no **VS Code** — o que gerou alguns reajustes no caminho. Faz parte do aprendizado! 😄

## 🚀 Tecnologias utilizadas

- **TinyLlama 1.1B** — modelo de linguagem local
- **LangChain** — gerenciamento de memória e pipeline de conversa
- **Chainlit** — interface web do chatbot
- **Hugging Face Transformers** — carregamento do modelo
- **Google Colab + GPU T4** — ambiente de execução
- **Ngrok** — acesso público ao chatbot

## ⚙️ Funcionalidades

- ✅ Boas-vindas personalizadas com o nome do usuário
- ✅ Memória de conversa (últimas 5 mensagens)
- ✅ Respostas rápidas para palavras-chave (hi, bye, help, thanks...)
- ✅ Respostas geradas pelo TinyLlama para perguntas abertas
- ✅ Corte de alucinações do modelo
- ✅ Indicador visual de processamento (⏳ Thinking...)
- ✅ Despedida personalizada com o nome do usuário
- ✅ Nome do usuário salvo no histórico da conversa

## 📁 Estrutura do projeto
chatbot-7days/
│
├── app.py        # código principal do chatbot
└── README.md     # documentação do projeto
## 🧠 O que foi aprendido

- Como criar e gerenciar **memória de conversa** com LangChain
- Como implementar **handlers** no Chainlit (`@on_chat_start` e `@on_message`)
- Como subir um projeto no **GitHub pelo Google Colab**
- Como usar **GPU T4 no Colab** para rodar modelos de linguagem
- Como expor um servidor local com **Ngrok**

## 🐛 Dificuldades e erros enfrentados

- **Ambiente errado** — o projeto foi iniciado no VS Code quando deveria ser no Google Colab, o que exigiu reajustes
- **Alucinações do modelo** — o TinyLlama inventava continuações de conversa, simulando respostas do próprio usuário. Resolvido cortando o texto ao detectar padrões como `Human:` e `User:`
- **Memória da conversa** — implementar a memória corretamente para o modelo não perder o contexto foi um dos maiores desafios
- **Indentação** — erros de indentação no Python travaram o Chainlit algumas vezes durante o desenvolvimento
- **Limite de GPU** — o Colab gratuito tem limite de horas de GPU por dia, o que exigiu pausas no desenvolvimento

## 🔧 Como rodar

1. Abra o notebook no Google Colab
2. Ative a GPU: `Runtime → Change Runtime Type → T4 GPU`
3. Execute todas as células em ordem
4. Aguarde o modelo carregar (~5 minutos)
5. Acesse o link gerado pelo Ngrok

## 👩‍💻 Desenvolvido por

**Tissiany Delmiro**

[![GitHub](https://img.shields.io/badge/GitHub-TissianyDelmiro-black?logo=github)](https://github.com/TissianyDelmiro)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Tissiany%20Delmiro-blue?logo=linkedin)](https://www.linkedin.com/in/tissiany-delmiro-157b8a384/)

Desenvolvido durante o **#7DaysOfCode** da [Alura](https://www.alura.com.br/) 🚀
