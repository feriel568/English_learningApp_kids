import tkinter
import customtkinter  # <- import the CustomTkinter module


root_tk = tkinter.Tk()  # create the Tk window like you normally do
root_tk.geometry("1000x500")
root_tk.title("CustomTkinter Test")


root_tk.minsize(1000,500)
root_tk.maxsize(1000,500)

bg = tkinter.PhotoImage(file = "kids.png")
#Position the image
label1 = tkinter.Label( root_tk, image = bg)
label1.place(relx= 0, rely = 0)

label = customtkinter.CTkLabel(master=root_tk, 
                               text="The best english",
                               width=350,
                               height=50,
                              
                               text_color="#008ECC",
                               text_font="Consolas,100",
                               )
label2 = customtkinter.CTkLabel(master=root_tk, 
                               text="learning application",
                               width=350,
                               height=50,
                             
                               text_color="#008ECC",
                               text_font="Consolas,100"
                               )
label3 = customtkinter.CTkLabel(master=root_tk, 
                               text="for your kids",
                               width=350,
                               height=50,
                               text_color="#008ECC",
                               text_font="Consolas,100"
                               )


label.place(x=10, y=20)
label2.place(x=10, y=60)
label3.place(x=10, y=100)

def moveToHomePage():
    root_tk.destroy()
    import homePage
startBtn=customtkinter.CTkButton(master=root_tk,
                                text="START",
                                 width=120,
                                 height=32,
                                 bg_color="#008ECC",
                                 corner_radius=0,
                                  text_color="white",
                                  text_font="Consolas",
                                  command=lambda:moveToHomePage()
                                
                                 )
startBtn.place(relx=0.5, rely=0.9 , anchor=tkinter.S)

root_tk.mainloop()

