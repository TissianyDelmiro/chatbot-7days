from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from langchain.llms import HuggingFacePipeline
from langchain.prompts.prompt import PromptTemplate
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferWindowMemory
import chainlit as cl
from chainlit import AskUserMessage, Message, on_chat_start

# Dia 4: modelo, tokenizador e pipeline
model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name, device_map="auto", torch_dtype="auto"
)

pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=150,
    temperature=0.7,
    do_sample=True,
    return_full_text=False,
    repetition_penalty=1.2,
    eos_token_id=tokenizer.eos_token_id,
)

llm = HuggingFacePipeline(pipeline=pipe)

# Dia 5: template + memória + chain
template = """You are a helpful assistant. Reply with ONE short, natural answer to the human's last message. Do NOT continue the conversation or write multiple turns.

{history}
Human: {input}
Assistant:"""

prompt = PromptTemplate(input_variables=["history", "input"], template=template)
memory = ConversationBufferWindowMemory(k=5)
chain = ConversationChain(llm=llm, prompt=prompt, memory=memory, verbose=False)

@on_chat_start
async def start():
    res = await AskUserMessage(content="Welcome! What is your name?", timeout=99999).send()
    if res:
        palavras = res['output'].strip().split()
        nome = palavras[-1].replace(",", "").replace(".", "").replace("!", "")

        cl.user_session.set("nome", nome)
        cl.user_session.set("apresentado", True)
        # salva o nome no histórico da conversa
        memory.save_context(
            {"input": f"My name is {nome}"},
            {"output": f"Nice to meet you {nome}!"}
        )

        await Message(
            content=f"Hi {nome}! How can I help you today?",
        ).send()

@cl.on_message
async def handle_message(message: cl.Message):

    if not cl.user_session.get("apresentado"):
        return

    content = message.content.lower().strip()

    if content in ["hello", "hi", "hey"]:
        resposta = "Hello! How can I help you?"
    elif content in ["thanks", "thank you"]:
        resposta = "You're welcome! 😊"
    elif content in ["who are you", "what are you"]:
        resposta = "I'm a chatbot powered by TinyLlama! How can I help?"
    elif content in ["what can you do"]:
        resposta = "I can answer questions and have a conversation with you!"
    elif content in ["bye", "goodbye", "see you", "thanks, bye"]:
        nome = cl.user_session.get("nome")
        await cl.Message(content=f"Goodbye {nome}! See you later! 👋").send()
        cl.user_session.set("apresentado", False)
        return
    elif content in ["help"]:
        resposta = "Sure! Tell me what you need."
    else:
        msg = cl.Message(content="⏳ Thinking...")
        await msg.send()

        resposta = await chain.apredict(input=content)

        for stop in ["\nHuman:", "Human:", "\nUser:", "User:", "\nAssistant:", "Conclusion:", "Reply"]:
            if stop in resposta:
                resposta = resposta.split(stop)[0]

        resposta = resposta.strip()
        if not resposta:
            resposta = "Sorry, could you rephrase that?"

        msg.content = resposta
        await msg.update()
        return

    await cl.Message(content=resposta).send()
