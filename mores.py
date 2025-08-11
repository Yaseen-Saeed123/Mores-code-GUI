from tkinter import *
from tkinter import ttk
from tkinter import messagebox

morse_code_dict = {
    'A': '.-',     'B': '-...',   'C': '-.-.', 
    'D': '-..',    'E': '.',      'F': '..-.',
    'G': '--.',    'H': '....',   'I': '..',
    'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',
    'S': '...',    'T': '-',      'U': '..-',
    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..', 

    '0': '-----',  '1': '.----',  '2': '..---',
    '3': '...--',  '4': '....-',  '5': '.....',
    '6': '-....',  '7': '--...',  '8': '---..',
    '9': '----.'
}

def mores():
    user_text = text.get(1.0, "end").upper().strip()
    mores_text = []
    if not user_text:
        message = messagebox.showerror(title="Missing", message="You must type a word to convert it to mores code")
        return
    else:
        for letter in user_text:
            if letter in morse_code_dict.keys():
                mores_text.append(f"{morse_code_dict[letter]} ")
            else:
                mores_text.append("?")

    mores_message = " ".join(mores_text)
    message = messagebox.showinfo(title="Result", message=mores_message)
    text.delete(1.0, "end")
    text.focus_set()
    return

root = Tk()
root.title("Mores code")
root.geometry("200x200")
root.resizable(False, False)

label = Label(root, text="English Mores code", font="Calibre 13 bold")
label.pack()

label2 = Label(root, text="Enter a word to be encrypted", font="Calibre 10 bold")
label2.pack()

text = Text(root, font="Arial 10 normal", bd=1, width= 20, height= 5, relief="solid")
text.focus_set()
text.pack(pady=10)

btn = ttk.Button(root, text="Convert", command=mores)
btn.pack()

root.mainloop()