import tkinter as tk

root = tk.Tk()
root.title("G's Weather App")
canvas = tk.Canvas(root, height='700', width='800')
canvas.pack()
frame = tk.Frame(root, bg='#204a63')
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')
entry = tk.Entry(frame, font=50)
entry.place(relwidth=0.65, relheight=1)
button = tk.Button(frame, text='This should work', bg='yellow')
button.place(relx=0.7, rely=0, relwidth=0.25, relheight=0.25)

root.mainloop()


