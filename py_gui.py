import tkinter as tk


class RCServoGUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("RC Servo Example - [Preview]")
        self.root.geometry("500x300")

        self.pos = tk.IntVar()

        self.btn1 = tk.Radiobutton(self.root, text="0", variable=self.pos, value=0, command=self.give_angle)
        self.btn1.grid(row=0, column=0, sticky="w")

        self.btn2 = tk.Radiobutton(self.root, text="45", variable=self.pos, value=45, command=self.give_angle)
        self.btn2.grid(row=0, column=1, pady=50)

        self.btn3 = tk.Radiobutton(self.root, text="90", variable=self.pos, value=90, command=self.give_angle)
        self.btn3.grid(row=0, column=2)
        #
        self.btn4 = tk.Radiobutton(self.root, text="135", variable=self.pos, value=135, command=self.give_angle)
        self.btn4.grid(row=0, column=3)

        self.btn5 = tk.Radiobutton(self.root, text="180", variable=self.pos, value=180, command=self.give_angle)
        self.btn5.grid(row=0, column=4)

        self.click_btn = tk.Button(self.root, text="Release Motor", command=self.release_motor)
        self.click_btn.grid(row=0, column=5, sticky="we")

        self.slider = tk.Scale(self.root, from_=0, to=180, orient=tk.HORIZONTAL, length=200, command=self.give_angle)
        self.slider.grid(row=1, column=5, sticky="we")

        self.root.mainloop()

    def give_angle(self, str_value=None):
        print(self.pos.get(), self.slider.get())
        return self.pos.get()

    def release_motor(self):
        pos_value = self.pos.get()
        pos_value = None
        print(pos_value)
        return not pos_value


servo_gui = RCServoGUI()
