import tkinter
from tkinter import messagebox , PhotoImage
import customtkinter  # <- import the CustomTkinter module
import vlc


root_tk = tkinter.Tk()  # create the Tk window like you normally do
root_tk.geometry("1000x500")
root_tk.title("CustomTkinter Test")


root_tk.minsize(1000,500)
root_tk.maxsize(1000,500)


#The menu frame
menu=tkinter.Frame(root_tk,bg="#008ECC")
menu.pack(side=tkinter.LEFT)
menu.pack_propagate(False)
menu.configure(width=200,height=500)

#The content frame
content=tkinter.Frame(root_tk,bg="#EDEDED")
content.pack(side=tkinter.LEFT)
content.pack_propagate(False)
content.configure(height=500,width=800)




def exit():
    root_tk.destroy()
    import EnglishLanguageApp
def readingPage():
    readingFrame=tkinter.Frame(content)
    # global img1
    # img1=PhotoImage(file="D:\\PCAP\\Project\\ff.png")
    # lb=tkinter.Label(readingFrame,image=img1, height=55, width=150)
    # lb.place(relx=0.5,rely=0.2)

    Text1 = (''' Good friends are really important for our happiness. They share good times with us — we have fun together, laugh together and they make us smile. But good friends are also there for us when things aren't so great. They listen to us, help us and support us through difficult times.

                        What makes a good friend?
                        A good friend is always there for you, whatever happens. They don't judge you — they accept you, value you and respect you for who you are. You can be yourself when you're around them. A good friend is kind, loyal and honest and isn't afraid to tell you the truth, even if it's difficult. You enjoy spending time together and maybe share some hobbies or interests. 

                        What is the International Day of Friendship?
                        Friendship is so important that, in 2011, the United Nations decided to make a special day for it! The International Day of Friendship takes place on 30 July every year. The idea is that friendship between different groups of people, countries and cultures can help us live more peacefully together.

                        Friendship Days around the world
                        The International Day of Friendship on 30 July is not the only day celebrating friendship around the world. Some countries celebrate on different days. For example, Argentina, Brazil and Spain celebrate Friend's Day on 20 July, and in India and the USA, they celebrate it on the first Sunday in August. In Finland and Estonia, people celebrate Friendship Day on the same day as Valentine's Day, 14 February.

                        What do people do on the International Day of Friendship?
                        The main aim of the International Day of Friendship is to show your friends that you care about them and that you value their friendship. You could make a card or write a note telling them why they're such a great friend. You could make them a small present, such as a friendship bracelet, or bake a cake for them. Whatever you do on this day, it's a time to have fun and celebrate with friends, and perhaps make some new ones! Happy International Day of Friendship!''')
    readingText1=tkinter.Text(readingFrame,
                            #  wrap=tkinter.WORD,  # Wrap text by word
                            font=("Helvetica", 11),
                            fg="black",
                            bd=0,
                            # height=6,  # Adjust the height as needed
                            # width=40,
                            bg="#EDEDED")
    readingText1.pack()
    readingText1.insert(tkinter.END,Text1)
    nextBtn=customtkinter.CTkButton(master=readingFrame,
                                text="NEXT",
                                 width=120,
                                 height=32,
                                 bg_color="#008ECC",
                                 corner_radius=0,
                                  text_color="white",
                                  text_font="Consolas",
                                command=lambda:switchPage(readingFrame,readingPage2)
                                  
                                
                                 )
    
    nextBtn.pack(padx=10,pady=10)
    readingFrame.pack(pady=20)
def readingPage2():
    readinFrame2=tkinter.Frame(content)
  

    
    questions = [
    "Good friends make us laugh and smile.",
    "Good friends are only important when you're having fun.",
    "Good friends prefer to lie to you than to say something you don't like.",
    "The International Day of Friendship started in 2021.",
    ]

    answers = [
    True, False, False, False
    ]

# Function to check the answers
    def check_answers_text():
            correct_count = 0
            for i in range(len(questions)):
                if user_answers[i].get() == answers[i]:
                    correct_count += 1

            result = f"You got {correct_count} out of {len(questions)} correct!"
            messagebox.showinfo("Quiz Result", result)

# Create labels and radio buttons for questions
    user_answers = []
    for i in range(len(questions)):
        label = tkinter.Label(readinFrame2, text=questions[i])
        label.pack(pady=5)

        answer_var = tkinter.BooleanVar()
        user_answers.append(answer_var)

        true_radio = tkinter.Radiobutton(readinFrame2, text="True", variable=answer_var, value=True)
        true_radio.pack()
        false_radio = tkinter.Radiobutton(readinFrame2, text="False", variable=answer_var, value=False)
        false_radio.pack()

    # Create "Check Result" button
    check_button = tkinter.Button(readinFrame2, text="Check Result", command=check_answers_text)
    check_button.pack(pady=10)

    prevBtn=customtkinter.CTkButton(master=readinFrame2,
                                text="PREV",
                                 width=120,
                                 height=32,
                                 bg_color="#008ECC",
                                 corner_radius=0,
                                text_color="white",
                                text_font="Consolas",
                                command=lambda:switchPage(readinFrame2,readingPage)
                                 )
    nextBtn=customtkinter.CTkButton(master=readinFrame2,
                                text="NEXT",
                                width=120,
                                height=32,
                                bg_color="#008ECC",
                                corner_radius=0,
                                text_color="white",
                                text_font="Consolas",
                                # command=lambda:switchPage(grammarFrame2,grammarPage3)
                                 )
    

    prevBtn.pack(padx=10, pady=10)
    nextBtn.pack()
    lb=tkinter.Label(text="gjkdfslkfsd",)
    lb.pack
    readinFrame2.pack(pady=20)
    
def grammarPage():
    grammarFrame=tkinter.Frame(content,bg="#EDEDED")
    
    #Label adjectives
    adj=tkinter.Label(grammarFrame,
                      text="Adjectives",
                      font=("Helvetica",30),
                      fg="#008ECC",
                      bg="#EDEDED")
    adj.pack()
    #first paragraph
    firstParaText = ("We can use adjectives to describe people, places and things.\n"
                    "We've got a small car.\nI saw a white bird.\nThis book isn't very old.")
    firstPara = tkinter.Text(grammarFrame,
                             wrap=tkinter.WORD,  # Wrap text by word
                             font=("Helvetica", 15),
                             fg="black",
                             bd=0,
                             height=6,  # Adjust the height as needed
                             width=40,
                             bg="#EDEDED")  # Adjust the width as needed
    firstPara.pack()
    firstPara.insert(tkinter.END, firstParaText)
    firstPara.tag_configure("bold", font=("Helvetica", 15, "bold"))
    for word in ["small", "white", "old"]:
        start = "1.0"
        while start:
            start = firstPara.search(word, start, stopindex=tkinter.END)
            if start:
                end = f"{start}+{len(word)}c"
                firstPara.tag_add("bold", start, end)
                start = end

    #How to use label
    useAdj=tkinter.Label(grammarFrame,
                      text="How to use them",
                      font=("Helvetica",30),
                      fg="#008ECC",
                      bg="#EDEDED")
    useAdj.pack()
    #Second paragraph
    secondtParaText = ("We don't add s to the adjective when it's plural.\n"
                    "My brothers are short.\nWe've got three black cats.\nShe watched some old films.\n"
                    "Put size adjectives before colour adjectives.\n"
                    "I've got a big, blue ball.\nThat building is tall and grey.")
    secondPara = tkinter.Text(grammarFrame,
                             wrap=tkinter.WORD,  # Wrap text by word
                             font=("Helvetica", 15),
                             fg="black",
                             bd=0,
                             height=8,  # Adjust the height as needed
                             width=40,
                             bg="#EDEDED")  # Adjust the width as needed
    secondPara.pack()
    secondPara.insert(tkinter.END, secondtParaText)
    secondPara.tag_configure("bold", font=("Helvetica", 15, "bold"))
    for words in ["short", "black", "old","big","nlue","tall","grey"]:
        start = "1.0"
        while start:
            start = secondPara.search(words, start, stopindex=tkinter.END)
            if start:
                end = f"{start}+{len(words)}c"
                secondPara.tag_add("bold", start, end)
                start = end
    # let's practise label
    nextBtn=customtkinter.CTkButton(master=grammarFrame,
                                text="NEXT",
                                 width=120,
                                 height=32,
                                 bg_color="#008ECC",
                                 corner_radius=0,
                                  text_color="white",
                                  text_font="Consolas",
                                  command=lambda:switchPage(grammarFrame,grammarPage2)
                                  
                                
                                 )
    
    nextBtn.place(relx=0.88, rely=1, anchor=tkinter.S )
 

    grammarFrame.pack(pady=20)


def grammarPage2():
    grammarFrame2=tkinter.Frame(content)
    paragraph = "The__1__beggar hasn’t eaten in days.\nMary had a__2__lamb.\nThe__3__giant didn’t allow the children to enter his garden."

    correct_answers = {
        "1": "homeless",
        "2": "little",
        "3": "selfish"
    }

    paragraph_label = tkinter.Label(grammarFrame2, text=paragraph, wraplength=300,font=("Helvetica", 10) )
    paragraph_label.pack(padx=10, pady=10)

    user_answers = {}
    for blank_number in correct_answers.keys():
        label = tkinter.Label(grammarFrame2, text=f"Blank {blank_number}:")
        label.pack()
        entry = tkinter.Entry(grammarFrame2)
        entry.pack()
        user_answers[blank_number] = entry

    def check_answers():
        correct = True
        for blank_number, entry in user_answers.items():
            user_answer = entry.get()
            if user_answer.lower() != correct_answers[blank_number]:
                correct = False
                break
        if correct:
            result = "All answers are correct!"
        else:
            result = "Some answers are incorrect. Please try again."
        messagebox.showinfo("Result", result)
    answer_label = tkinter.Label(grammarFrame2, text="Choose from this list : homeless-little-selfish", wraplength=300,font=("Helvetica", 10) )
    answer_label.pack(padx=10, pady=10)
    check_button = tkinter.Button(grammarFrame2, text="Check Result", command=check_answers)
    check_button.pack(pady=10)

    prevBtn=customtkinter.CTkButton(master=grammarFrame2,
                                text="PREV",
                                 width=120,
                                 height=32,
                                 bg_color="#008ECC",
                                 corner_radius=0,
                                  text_color="white",
                                  text_font="Consolas",
                                  command=lambda:switchPage(grammarFrame2,grammarPage)
                                 )
    nextBtn=customtkinter.CTkButton(master=grammarFrame2,
                                text="NEXT",
                                 width=120,
                                 height=32,
                                 bg_color="#008ECC",
                                 corner_radius=0,
                                  text_color="white",
                                  text_font="Consolas",
                                command=lambda:switchPage(grammarFrame2,grammarPage3)
                                 )
    
    # prevBtn.place(relx=0.6, rely=0.6, anchor=tkinter.SW )
    # nextBtn.place(relx=0.88, rely=1, anchor=tkinter.SE )
    prevBtn.pack(padx=10, pady=10)
    nextBtn.pack(padx=15, pady=15)



        
    grammarFrame2.pack(pady=20)

def grammarPage3():
    grammarFrame3=tkinter.Frame(content,bg="#EDEDED")
    
    #Label adjectives
    adj=tkinter.Label(grammarFrame3,
                      text="Adverbs",
                      font=("Helvetica",30),
                      fg="#008ECC",
                      bg="#EDEDED")
    adj.pack()
    #first paragraph
    firstParaText = ("We can use adverbs to describe how somebody does something.\n"
                    "I speak English well.\nHe plays hockey badly.\nWe try to do our homework correctly.")
    firstPara = tkinter.Text(grammarFrame3,
                             wrap=tkinter.WORD,  # Wrap text by word
                             font=("Helvetica", 15),
                             fg="black",
                             bd=0,
                             height=6,  # Adjust the height as needed
                             width=40,
                             bg="#EDEDED")  # Adjust the width as needed
    firstPara.pack()
    firstPara.insert(tkinter.END, firstParaText)
    firstPara.tag_configure("bold", font=("Helvetica", 15, "bold"))
    for word in ["well", "badly", "correctly"]:
        start = "1.0"
        while start:
            start = firstPara.search(word, start, stopindex=tkinter.END)
            if start:
                end = f"{start}+{len(word)}c"
                firstPara.tag_add("bold", start, end)
                start = end

    #How to use label
    useAdj=tkinter.Label(grammarFrame3,
                      text="How to use them",
                      font=("Helvetica",30),
                      fg="#008ECC",
                      bg="#EDEDED")
    useAdj.pack()
    #Second paragraph
    secondtParaText = ("To make adverbs, we normally add ly to the adjective. Sometimes the spelling is different.\n"
                    "She ran quickly.\nThe children are playing happily.\nI dance terribly.\n"
                    "Some adverbs don't have ly.\n"
                    "I don't write Italian well.\nDo you work hard?")
    secondPara = tkinter.Text(grammarFrame3,
                             wrap=tkinter.WORD,  # Wrap text by word
                             font=("Helvetica", 15),
                             fg="black",
                             bd=0,
                             height=8,  # Adjust the height as needed
                             width=40,
                             bg="#EDEDED")  # Adjust the width as needed
    secondPara.pack()
    secondPara.insert(tkinter.END, secondtParaText)
    secondPara.tag_configure("bold", font=("Helvetica", 15, "bold"))
    for words in ["ly", "well", "hard"]:
        start = "1.0"
        while start:
            start = secondPara.search(words, start, stopindex=tkinter.END)
            if start:
                end = f"{start}+{len(words)}c"
                secondPara.tag_add("bold", start, end)
                start = end
    # let's practise label
    prevBtn=customtkinter.CTkButton(master=grammarFrame3,
                                text="PREV",
                                 width=120,
                                 height=32,
                                 bg_color="#008ECC",
                                 corner_radius=0,
                                  text_color="white",
                                  text_font="Consolas",
                                  command=lambda:switchPage(grammarFrame3,grammarPage2)
                                 )
    nextBtn=customtkinter.CTkButton(master=grammarFrame3,
                                text="NEXT",
                                 width=120,
                                 height=32,
                                 bg_color="#008ECC",
                                 corner_radius=0,
                                  text_color="white",
                                  text_font="Consolas",
                                command=lambda:switchPage(grammarFrame3,grammarPage4)
                                 )
    prevBtn.place(relx=0.88, rely=0.9, anchor=tkinter.S )
    nextBtn.place(relx=0.88, rely=1, anchor=tkinter.S )
 

    grammarFrame3.pack(pady=20)
    
def grammarPage4():
    grammarFrame4=tkinter.Frame(content)
    paragraph = "The boy is__1__careless.\nThe winds are__2_strong.\nThe naughty boy is__3__annoying."

    correct_answers = {
        "1": "too",
        "2": "very",
        "3": "so"
    }

    paragraph_label = tkinter.Label(grammarFrame4, text=paragraph, wraplength=300,font=("Helvetica", 10) )
    paragraph_label.pack(padx=10, pady=10)

    user_answers = {}
    for blank_number in correct_answers.keys():
        label = tkinter.Label(grammarFrame4, text=f"Blank {blank_number}:")
        label.pack()
        entry = tkinter.Entry(grammarFrame4)
        entry.pack()
        user_answers[blank_number] = entry

    def check_answers():
        correct = True
        for blank_number, entry in user_answers.items():
            user_answer = entry.get()
            if user_answer.lower() != correct_answers[blank_number]:
                correct = False
                break
        if correct:
            result = "All answers are correct!"
        else:
            result = "Some answers are incorrect. Please try again."
        messagebox.showinfo("Result", result)
    answer_label = tkinter.Label(grammarFrame4, text="Choose from this list : too-very-so", wraplength=300,font=("Helvetica", 10) )
    answer_label.pack(padx=10, pady=10)
    check_button = tkinter.Button(grammarFrame4, text="Check Result", command=check_answers)
    check_button.pack(pady=10)

    prevBtn=customtkinter.CTkButton(master=grammarFrame4,
                                text="PREV",
                                 width=120,
                                 height=32,
                                 bg_color="#008ECC",
                                 corner_radius=0,
                                  text_color="white",
                                  text_font="Consolas",
                                  command=lambda:switchPage(grammarFrame4,grammarPage3)
                                 )
 
   
    prevBtn.pack(padx=10, pady=10)




        
    grammarFrame4.pack(pady=20)

def pronunciationPage():
    prFrame = tkinter.Frame(content)
    video_path = "ABC Alphabet Pronunciation - English Educational Videos _ Little Smart Planet.mp4"
    instance = vlc.Instance("--no-xlib")
    player = instance.media_player_new()

    # Set the media and play the video
    media = instance.media_new(video_path)
    player.set_media(media)

    # Create a Canvas to display the video
    canvas = tkinter.Canvas(content, width=600, height=480)
    canvas.pack()

    # Embed the player into the Canvas
    player.set_hwnd(canvas.winfo_id())
    player.play()
  
    

def switchPage(frame,page):
    frame.destroy()
    page()


def hideIndicators():
    readingIndicator.config(bg="#008ECC")
    grammarIndicator.config(bg="#008ECC")
    pronunciationIndicator.config(bg="#008ECC")

def delete_pages():
    for frame in content.winfo_children():
        frame.destroy()

    
def indicate(lb , page):
    hideIndicators()
    lb.config(bg="white")
    delete_pages()
    page()


readingIndicator=tkinter.Label(menu,text="",background="#008ECC")
readingIndicator.place(x=0,y=100,width=5,height=40)

grammarIndicator=tkinter.Label(menu,text="",background="#008ECC")
grammarIndicator.place(x=0,y=150,width=5,height=40)


pronunciationIndicator=tkinter.Label(menu,text="",background="#008ECC")
pronunciationIndicator.place(x=0,y=200,width=5,height=40)



ReadingBtn=tkinter.Button(master=menu,
                          text="READING",
                          font="bold",
                          fg="white",
                          bd=0,
                          padx=0,
                          activebackground="white",
                          activeforeground="#008ECC",
                          bg="#008ECC",
                          command=lambda:indicate(readingIndicator,readingPage)
                          )

grammarBtn=tkinter.Button(menu,
                          text="GRAMMAR",
                          font="bold",
                          fg="white",
                          bd=0,
                          activebackground="white",
                          activeforeground="#008ECC",
                          bg="#008ECC",
                          command=lambda:indicate(grammarIndicator,grammarPage)
                        
                        
                          
                          )


pronunciationBtn=tkinter.Button(menu,
                          text="PRONUNCIATION",
                          font="bold",
                          fg="white",
                          bd=0,
                          activebackground="white",
                          activeforeground="#008ECC",
                          bg="#008ECC",
                          command=lambda:indicate(pronunciationIndicator,pronunciationPage)
                         
                          
                          
                          )
exitIcon=tkinter.PhotoImage(file="back.png")
resizeIcon=exitIcon.subsample(10, 10)   
exitBtn=tkinter.Button(menu,
                       text="EXIT",
                       font="bold",
                       compound="left",
                       image=resizeIcon,
                       
                       fg="white",
                       bd=0,
                       activebackground="white",
                       activeforeground="#008ECC",
                       bg="#008ECC",
                       command=lambda:exit()

                        )
ReadingBtn.place(x=50,y=100)
grammarBtn.place(x=45,y=150)
pronunciationBtn.place(x=18,y=200)
exitBtn.place(x=50,y=250)




root_tk.mainloop()