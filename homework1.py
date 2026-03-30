import tkinter as tk

def main():
    count = 0

    def on_click():
        nonlocal count
        count += 1
        label.config(text=f"Нажато: {count} раз")

    root = tk.Tk()
    root.title("Счётчик")

    label = tk.Label(root, text="Нажато: 0 раз")
    label.pack()

    button = tk.Button(root, text="Нажми меня", command=on_click)
    button.pack()

    root.mainloop()

main()