from tkinter import *
from tkinter.messagebox import *
class Paint(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.brush_size = 10
        self.brush_color = "red"
        self.color = "red"
        self.setUI()
    def draw(self, event):
        self.canv.create_oval(event.x - self.brush_size,
                              event.y - self.brush_size,
                              event.x + self.brush_size,
                              event.y + self.brush_size,
                              fill=self.color, outline=self.color)
    def draw_rec(self, event):
        self.canv.create_rectangle(event.x - self.brush_size,
                              event.y - self.brush_size,
                              event.x + self.brush_size,
                              event.y + self.brush_size,
                              fill=self.color, outline=self.color)
    def set_figure(self,new_figure):
        self.figure = new_figure
    def set_color(self, new_color):
        self.color = new_color
    def set_brush_size(self, new_size):
        self.brush_size = new_size
    def setUI(self):
        self.parent.title("Demo Paint")
        self.pack(fill=BOTH, expand=1)
        self.columnconfigure(6, weight=1)
        self.rowconfigure(4, weight=1)
        self.canv = Canvas(self, bg="gray")
        self.canv.grid(row=4, column=0, columnspan=7, padx=5, pady=5, sticky=E + W + S + N)
        self.canv.bind("<B1-Motion>", self.draw)

        color_lab = Label(self, text="Color: ")
        color_lab.grid(row=0, column=0, padx=6)
        red_btn = Button(self, text="Purple", width=10, command=lambda: self.set_color("purple"))
        red_btn.grid(row=0, column=1)
        green_btn = Button(self, text="Green", width=10, command=lambda: self.set_color("green"))
        green_btn.grid(row=0, column=2)
        blue_btn = Button(self, text="Blue", width=10, command=lambda: self.set_color("blue"))
        blue_btn.grid(row=0, column=3)
        black_btn = Button(self, text="Black", width=10, command=lambda: self.set_color("black"))
        black_btn.grid(row=0, column=4)
        white_btn = Button(self, text="Yellow", width=10, command=lambda: self.set_color("yellow"))
        white_btn.grid(row=0, column=5)

        size_lab = Label(self, text="Brush size: ")
        size_lab.grid(row=1, column=0, padx=5)
        one_btn = Button(self, text="1x", width=10, command=lambda: self.set_brush_size(1))
        one_btn.grid(row=1, column=1)
        two_btn = Button(self, text="2x", width=10, command=lambda: self.set_brush_size(2))
        two_btn.grid(row=1, column=2)
        five_btn = Button(self, text="5x", width=10, command=lambda: self.set_brush_size(5))
        five_btn.grid(row=1, column=3)
        seven_btn = Button(self, text="7x", width=10, command=lambda: self.set_brush_size(7))
        seven_btn.grid(row=1, column=4)
        ten_btn = Button(self, text="10x", width=10, command=lambda: self.set_brush_size(10))
        ten_btn.grid(row=1, column=5)
        twenty_btn = Button(self, text="20x", width=10, command=lambda: self.set_brush_size(20))
        twenty_btn.grid(row=1, column=6, sticky=W)
        clear_btn = Button(self, text="Clear", width=10, command=lambda: self.canv.delete("all"))
        clear_btn.grid(row=0, column=6, sticky=W)

        figure_lab = Label(self, text="Figure: ")
        figure_lab.grid(row=2, column=0, padx=6)
        oval_btn=Button(self, text="Dot", width=10, command=lambda: self.canv.bind("<B1-Motion>", self.draw))
        oval_btn.grid(row=2, column=1)
        rec_btn=Button(self, text="Rectangle", width=10, command=lambda: self.canv.bind("<B1-Motion>", self.draw_rec))
        rec_btn.grid(row=2, column=2)

        bf_lab = Label(self,text="Background: ")
        bf_lab.grid(row=3, column=0)
        g_btn = Button(self, text="gray", width=10, command=lambda:self.canv.configure(bg="gray"))
        g_btn.grid(row=3,column=1)
        w_btn = Button(self, text="white", width=10, command=lambda:self.canv.configure(bg="white"))
        w_btn.grid(row=3,column=2)
        b_btn = Button(self, text="black", width=10, command=lambda: self.canv.configure(bg="black"))
        b_btn.grid(row=3,column=3)

def close_win():
  if askyesno("Exit", "Are you sure?"):
    root.destroy()
def about():
  showinfo("Demo Paint", "Easiest Paint on Python")
def main():
    global root
    root = Tk()
    root.geometry("800x600+300+300")
    app = Paint(root)
    m = Menu(root)
    root.config(menu=m)

    fm = Menu(m)
    m.add_cascade(label="File", menu=fm)
    fm.add_command(label="Exit", command=close_win)

    hm = Menu(m)
    m.add_cascade(label="Help", menu=hm)
    hm.add_command(label="About program", command=about)
    root.mainloop()

if __name__ == "__main__":
    main()