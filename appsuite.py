import tkinter
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("200x400")

def button1f():
    print("button pressed")
def button2f():
    print("button 2 pressed")
def button3f():
    print("button 3f pressed")
# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app, text="CTkButton", command=button1f)
button.place("30x100")

button2 = customtkinter.CTkButton(master=app, text="CTkButton", command=button2f)
button2.place(relx=0.5, rely=0.5)

button3 = customtkinter.CTkButton(master=app, text="CTkButton", command=button3f)
button3.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

app.mainloop()