
from tkinter import *
from tkinter import messagebox


def on_closing():
    if messagebox.askokcancel("Выход из приложения", "Хотите выйти из приложения?"):
        tk.destroy()

tk = Tk()
tk.protocol("WM_DELETE_WINDOW", on_closing)
tk.title("Транслитерация")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
# tk.iconbitmap("bomb-3175208_640.ico")

canvas = Canvas(tk, width=800, height=600, bg="white", highlightthickness=0)
canvas.pack()

def start_window_1():
    new_window_1 = Toplevel(tk)
    new_window_1.title("старт")
    new_window_1.resizable(0, 0)
    new_window_1.wm_attributes("-topmost", 1)
    canvas_1 = Canvas(new_window_1, width=600, height=400, bg="white", highlightthickness=0)
    canvas_1.pack()
    canvas_1.create_rectangle(50, 50, 275, 350, fill="lightgray", outline="")
  
    canvas_1.create_rectangle(500, 50, 275, 350, fill="lightgreen", outline="")





b0 = Button(tk, text="старт", command=start_window_1)
b0.place(x=200, y=200)

# canvas.create_oval(100, 100, 300, 300, fill="yellow", outline="")
# canvas.create_oval(120, 120, 280, 280, fill="white", outline="")
#
# canvas.create_rectangle(400,100,500,500, fill="lightgreen")
# canvas.create_rectangle(420,120,480,480, fill="darkgreen", outline="")
#
# canvas.create_text(200,500,text="Hello World!", font=("Arial", 40),fill="white")


tk.mainloop()
