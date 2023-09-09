import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):

        #main
        super().__init__()
        self.title("Body Mass Index Calculator")
        self.geometry('600x400+500+150')
        self.resizable(False,False)
        self.bind('<Escape>', lambda event: self.quit())

        #widgets
        self.Main = Main(self)

        self.mainloop()
        

class Main(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x = 0, y = 0, relwidth = 1, relheight = 1)

        self.create_widgets()

    def calc(self, BMI):
        BMI = round(BMI,2)
        label_string0.set("Your BMI is " + str(BMI) + "kg/m²") 
        BMI0 = (BMI - 16)/24
        progress.set(BMI0)
        if BMI <= 16:
            label9_text.set("You are severely underweight. Please seek medical attention.")
        elif BMI <= 17:
            label9_text.set("You are very underweight. Please seek medical attention.")
        elif BMI <= 18.5:
            label9_text.set("You are underweight. Please eat more.")
        elif BMI <= 25:
            label9_text.set("You are a healthy weight. Good.")
        elif BMI <= 30:
            label9_text.set("You are overweight. Try to reduce your calory intake and exercise.")
        elif BMI <= 40:
            label9_text.set("You are obese. Please reduce your calory intake and excersise.")
        elif BMI > 40:
            label9_text.set("You are extremely obese. You are at a high risk of diabetes.")

    def calc_metric(self):
        weight0 = weight.get()
        height0 = height.get()
        if (weight0 or height0):
            if int(weight0) > 0 or int(height0) > 0:
                weight0 = int(weight0)
                height0 = int(height0)
                BMI_metric = weight0 / ((height0/100)*(height0/100))
                self.calc(BMI_metric)
            else:
                label_string0.set("Please enter valid")
        else:
            label_string0.set("Please enter valid")


    def calc_imperial(self):
        lbs0 = lbs.get()
        ft0 = ft.get()
        inches0 = inches.get()
        if (lbs0 or ft0 or inches0):
            if int(lbs0) >= 0 or int(ft0) >= 0 or int(inches) >= 0:
                lbs0 = int(lbs0)
                ft0 = int(ft0)
                inches0 = int(inches0)
                BMI_imperial = (ft0 * 12) + inches0
                BMI_imperial = (lbs0 / (BMI_imperial * BMI_imperial)) * 703
                self.calc(BMI_imperial)
            else:
                label_string0.set("Please enter valid")
        else:
            label_string0.set("Please enter valid")
    

    def calculation(self): 
        try:
            if toggle == "off":
                self.calc_metric()
        except:
            self.calc_metric()
        if toggle == "on":
            self.calc_imperial()

                
    def switch_toggle(self):
        global toggle
        toggle = switch_var.get()
        if toggle == "on":
            self.switch_toggle_on()
        elif toggle == "off":
            self.switch_toggle_off()


    def switch_toggle_on(self):
        entry_frame0.pack_forget()
        entry_frame1.pack_forget()
        label2.pack_forget()
        label3.pack_forget()
        entry0.pack_forget()
        entry1.pack_forget()

        entry_frame5.pack(pady = 10)
        label7.pack(side = 'left', expand = True)
        entry3.pack(side = 'left', expand = True)

        entry_frame6.pack(pady = 10)
        label8.pack(side = 'left', expand = True)
        entry4.pack(side = 'left', expand = True, padx = 5)
        entry5.pack(side = 'left', expand = True)


    def switch_toggle_off(self):
        entry_frame5.pack_forget()
        entry_frame6.pack_forget()
        label7.pack_forget()
        label8.pack_forget()
        entry3.pack_forget()
        entry4.pack_forget()
        entry5.pack_forget()

        entry_frame0.pack(pady = 10)
        label2.pack(side = 'left', expand = True)
        entry0.pack(side = 'left', expand = True)

        entry_frame1.pack(pady = 10)
        label3.pack(side = 'left', expand = True)
        entry1.pack(side = 'left', expand = True)


    def ask(self):
        answer = messagebox.showwarning('WARNING', 
            'If you have or think you might have an eating disorder, we advise you not to use the BMI Calculator and get further advice from your GP.')


    def create_widgets(self):
    
        #initialise variables
        global label_string0
        global weight
        global height
        global inches
        global ft
        global inches
        global lbs
        global entry_frame1
        global progress
        global entry_frame0
        global entry_frame5
        global entry_frame6
        global label2
        global label3
        global label7
        global label8
        global entry0
        global entry1
        global entry3
        global entry4
        global entry5
        global switch_var
        global check_var0
        global check_var1
        global label9_text
        label_string0 = tk.StringVar()
        weight = tk.StringVar()
        height = tk.StringVar()
        lbs = tk.StringVar()
        ft = tk.StringVar()
        inches = tk.StringVar()
        switch_var = tk.StringVar(value="off")
        check_var0 = tk.StringVar(value="off")
        check_var1 = tk.StringVar(value="off")
        label9_text = tk.StringVar(value = '')

    
        #create widget
        entry_frame3 = ctk.CTkFrame(self, fg_color = 'transparent')
        label0 = ctk.CTkLabel(entry_frame3, text = 'Body Mass Index Calculator', font = ("Calibri 24 bold",20), pady = 10)
        label1 = ctk.CTkLabel(entry_frame3, text = 'Calculate your BMI', font = ("Calibri 24",20), pady = 10)

        entry_frame0 = ctk.CTkFrame(self, fg_color = 'transparent')
        label2 = ctk.CTkLabel(entry_frame0, text = "Weight in kg:", font = ("Calibri 24",20), padx = 10)
        entry0 = ctk.CTkEntry(entry_frame0, textvariable = weight)

        entry_frame1 = ctk.CTkFrame(self, fg_color = 'transparent')
        label3 = ctk.CTkLabel(entry_frame1, text = "Height in cm:", font = ("Calibri 24",20), padx = 10)
        entry1 = ctk.CTkEntry(entry_frame1, textvariable = height)

        button0 = ctk.CTkButton(self, text = 'Calculate', command = self.calculation)
        label4 = ctk.CTkLabel(self, text = '', font = ("Terminal",20), pady = 10, textvariable = label_string0)
        switch = ctk.CTkSwitch(self, text = 'Imperial', command = self.switch_toggle, variable = switch_var, onvalue = "on", offvalue = "off")
        button1 = ctk.CTkButton(self, text = 'Warning', command = self.ask, width = 80)
        checkbox0 = ctk.CTkCheckBox(self, text = "Male")
        checkbox1 = ctk.CTkCheckBox(self, text = "Female")

        entry_frame4 = ctk.CTkFrame(self, fg_color = 'transparent')
        progress = ctk.CTkProgressBar(entry_frame4, width = 400)
        label5 = ctk.CTkLabel(entry_frame4, text = 'Underweight', font = ("Calibri 24",10), padx = 10)
        label6 = ctk.CTkLabel(entry_frame4, text = 'Obese', font = ("Calibri 24",10), padx = 10)

        entry_frame7 = ctk.CTkFrame(self, fg_color = 'transparent')
        label9 = ctk.CTkLabel(entry_frame7, textvariable = label9_text, text = 'hi', font = ("Calibri 24",20), justify = 'center')

        #imperial widgets
        entry_frame5 = ctk.CTkFrame(self, fg_color = 'transparent')
        label7 = ctk.CTkLabel(entry_frame5, text = "Weight in lb:", font = ("Calibri 24",20), padx = 10)
        entry3 = ctk.CTkEntry(entry_frame5, textvariable = lbs)
        
        entry_frame6 = ctk.CTkFrame(self, fg_color = 'transparent')
        label8 = ctk.CTkLabel(entry_frame6, text = "Height in feet and inches:", font = ("Calibri 24",15), padx = 10)
        entry4 = ctk.CTkEntry(entry_frame6, textvariable = ft, width = 60)
        entry5 = ctk.CTkEntry(entry_frame6, textvariable = inches, width = 60)

        #place widgets
        entry_frame3.pack(pady = 10)
        label0.pack(expand = True, fill = 'both')
        label1.pack(expand = True, fill = 'both')

        entry_frame0.pack(pady = 10)
        label2.pack(side = 'left', expand = True)
        entry0.pack(side = 'left', expand = True)

        entry_frame1.pack(pady = 10)
        label3.pack(side = 'left', expand = True)
        entry1.pack(side = 'left', expand = True)

        button0.place(x = 240, y = 220)
        label4.place(x = 220, y = 260)
        switch.place(x = 500, y = 10)
        button1.place(x = 510, y = 50)
        checkbox0.place(x = 40, y = 118)
        checkbox1.place(x = 40, y = 155)

        entry_frame4.place(x = 40, y = 310)
        label5.pack(side = 'left')
        progress.pack(side = 'left', pady = 10)
        label6.pack(side = 'left')
        progress.set(0)

        entry_frame7.place(relx = 0.5, rely = 0.9, relwidth = 1, anchor = 'center')
        label9.pack(expand = True, fill = 'both', anchor = 'center')


App()