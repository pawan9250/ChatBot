from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp

engine=pp.init()

voices = engine.getProperty('voices')
print(voices)

engine.setProperty('voice', voices[1].id)

def speak(word):
    engine.say(word)
    engine.runAndWait()


bot = ChatBot("my bot")

convo = [
    "Hello",
    "Hi there!",
    "what is your name?",
    "my name is ChatBot.",
    "what's your age?",
    "I'm creat just now.",
    "Who made you?",
    "I created by Pawan.",
    "which language can you speek?",
    "I'm comfurtable in english."
    "how are you?",
    "I'm ChatBot.",
    "happy birthday.",
    "thank you."
]
trainer = ListTrainer(bot)
trainer.train(convo)
#answer = bot.get_response("what is your name")
#print(answer)

#print("talk to bot")
#while True:
#	query = input()
#	if query == 'exit':
#		break
#	answer = bot.get_response(query)
#	print("bot :", answer)


main = Tk()
main.geometry("500x600")

main.title("my chat bot")


def ask_from_bot():
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END, "you : " + query)
    print(type(answer_from_bot))
    msgs.insert(END, "bot : " + str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0, END)
    msgs.yview(END)


frame = Frame(main)

sc = Scrollbar(frame)
msgs = Listbox(frame, width=50, height=25, yscrollcommand=sc.set)

sc.pack(side=RIGHT, fill=Y)

msgs.pack(side=LEFT, fill=BOTH, pady=0)

frame.pack()

textF = Entry(main, font=("verdana", 20))
textF.pack(fill=X, pady=20)

btn = Button(main, text="Ask", font=("Verdana", 20), command =ask_from_bot)
btn.pack()

def enter_function(event):
    btn.invoke()

main.bind('<Return>', enter_function)
main.mainloop()