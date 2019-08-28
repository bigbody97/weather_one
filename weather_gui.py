import tkinter as tk
from PIL import ImageTk, Image


vheight = 700
vwidth = 800
root = tk.Tk()
root.title("G's Weather App")
canvas = tk.Canvas(root, height=vheight, width=vwidth)
canvas.pack()

back_ground_img = ImageTk.PhotoImage(Image.open('src/Cumulus_clouds.png'))
back_ground_label = tk.Label(root, image=back_ground_img)
back_ground_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#204a63', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text='Get Weather Now', bg='yellow', font=40)
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='#204a63', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)


root.mainloop()


