import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("300x450")

entry = tk.Entry(root, width=16, font=('Arial', 24), bd=5, relief=tk.RIDGE, justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def click(event):
    text = event.widget["text"]
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "DEL":
        current_text = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, current_text[:-1])
    else:
        entry.insert(tk.END, text)

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['00', '0', '=', '+'],
    ['C', 'Remove']
]

for i, row in enumerate(buttons):
    for j, btn_text in enumerate(row):
        btn = tk.Button(root, text=btn_text, font=('Arial', 18), width=5, height=2)
        btn.grid(row=i+1, column=j, padx=5, pady=5)
        btn.bind("<Button-1>", click)

root.mainloop()
