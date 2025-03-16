import gradio as gr
import random

class ChatApp:
    def __init__(self):
        self.responses = [
            "なるほど。",
            "そうですね。",
            "わかります。",
            "それは面白いですね。",
            "なるほど、なるほど。"
        ]

    def generate_response(self, message):
        return random.choice(self.responses)

    def run(self):
        with gr.Blocks() as demo:
            chatbot = gr.Chatbot()
            with gr.Row():
                msg = gr.Textbox()
                submit_btn = gr.Button("送信", variant="primary")

            clear = gr.Button("Clear")

            def respond(message, chat_history):
                bot_message = self.generate_response(message)
                chat_history.append((message, bot_message))
                return "", chat_history

            submit_btn.click(respond, [msg, chatbot], [msg, chatbot])
            msg.submit(respond, [msg, chatbot], [msg, chatbot])
            clear.click(lambda: None, None, chatbot, queue=False)

        demo.launch()

if __name__ == "__main__":
    app = ChatApp()
    app.run()
