import gradio as gr
import re
import random

with gr.Blocks() as demo:
    chatbot = gr.Chatbot(type="messages", height=300)
    msg = gr.Textbox()

    patterns = {
        r"oi|plá": ["Olá!", "Oi!", "Saudações!"],
        r"tudo bem": ["Estou bem, obrigado por perguntar!", "Tudo bem!"],
        r"qual seu nome": ["Pode me chamar de Chatty!", "Sou o Chatty!"],
        r"tchau|até mais": ["Tchau!", "Te vejo mais tarde!"],
        r"(.*)": ["Não entendi isso. Pode perguntar novamente?"]
    }

    def respond(message, chat_history):
        for pattern, response in patterns.items():
            match = re.search(pattern, message.lower())
            if match:
                bot_message = random.choice(response)
                chat_history.append({"role": "user", "content": message})
                chat_history.append({"role": "assistant", "content": bot_message})
                return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])

demo.launch(server_name="0.0.0.0")