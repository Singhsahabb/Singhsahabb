import nltk
from nltk.chat.util import Chat, reflections
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox

import google.generativeai as genai 
GOOGLE_API_KEY ='AIzaSyAgXxN-nghKh3NwyiEimljPnrZSACJzUsI'
genai.configure(api_key = GOOGLE_API_KEY)
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
)

# Define chatbot pairs
pairs = [
    [
        r"my name is  Ankit ",
        ["Hello %1, How are you today?",]
    ],
    [
        r"hi|hey|hello|namaste",
        ["Hello!", "Hey there!",]
    ],
    [
        r"what is your name ?",
        ["I am a chatbot Abhi . You can call me Abhi.",]
    ],
    [
        r"where are you from ?",
        ["I am from computer application . You can call me abhi",]
    ],
    [
        r"nice to meet you ?",
        ["thanks you .",]
    ],
    [
        r"how are you ?",
        ["I'm doing good.\nHow about you?",]
    ],
    [
        r"sorry ",
        ["It's alright","It's OK, never mind.",]
    ],
    [
        r"I am  (good|well|okay|ok|fine)",
        ["Nice to hear that","Alright, great!"]
    ],
    [
        r"quit",
        ["Bye, take care. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
]

# Initialize Chatbot
chatbot = Chat(pairs, reflections)
chat_session  = model.start_chat()

def get_response(user_input):
    response1 = chat_session.send_message(user_input)
    response2 = chat_session.last.text


    if  response1 and response2:
        return   response2
    else:
        return "I am sorry, I didn't understand that. Can you please rephrase?"
    


# GUI Class
class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot")
        self.root.geometry("360x460")
        self.root.resizable(width=False, height=False)
        
        # Chat window
        self.chat_window = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, state='disabled', font=("Arial Bold", 10),bg="navy blue",fg="white")
        self.chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Entry frame
        self.entry_frame = tk.Frame(self.root)
        self.entry_frame.pack(padx=10, pady=10, fill=tk.X)
        
        self.user_input = tk.StringVar()
        self.input_entry = tk.Entry(self.entry_frame, textvariable=self.user_input, font=("Arial Bold", 10),bg="navy blue",fg="white")
        self.input_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 8))
        self.input_entry.bind("<Return>", self.send_message)
        
        self.send_button = tk.Button(self.entry_frame, text="Send", command=self.send_message, font=("Arial Bold", 10),bg="red",fg="gold")
        self.send_button.pack(side=tk.RIGHT)
        
        
        # Greet the user
        self.display_message("Chatbot\n","Hi, I am a chatbot. How can I help you today? Type ' quit ' to exit.\n")
    
    def display_message(self, sender, message):
        self.chat_window.config(state='normal')
        self.chat_window.insert(tk.END, f"{sender} {message}\n")
        self.chat_window.config(state='disabled')
        self.chat_window.yview(tk.END)
    
    def send_message(self, event=None ):
        chat_session = self.user_input.get().strip()
        if chat_session:
            self.display_message("you :- ", chat_session)
            self.user_input.set("")  # Clear input field
            
            
            # Get chatbot response
            response1 = get_response(chat_session)
            self.display_message("Chatbot :-", response1 )

            
            
            if chat_session.lower() == "quit":
                self.root.quit()

# Main Function
def main():
    root = tk.Tk()
    gui = ChatbotGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()


