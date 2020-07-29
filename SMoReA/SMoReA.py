from bs4 import BeautifulSoup 
import requests
import tkinter
from tkinter import *
import random
from tkinter import messagebox
from PIL import *



#Functionsssssssssssssss

def NoSelect():
    messagebox.showerror("Error", "Please select an emotion!!")


def Error():
    home.destroy()
    
def ShowChoice():
    print(v.get())
    
def ExitApplication():
    MsgBox = messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
       home.destroy()    


def Result():
    ResultWindow=Toplevel()
	
	
	
    ImgList=[
	"ResultImg (1).gif",
	"ResultImg (2).gif",
	"ResultImg (3).gif",
	"ResultImg (4).gif",
	"ResultImg (5).gif",
	"ResultImg (6).gif",
	"ResultImg (7).gif",
	"ResultImg (8).gif",
	"ResultImg (9).gif",
	"ResultImg (10).gif",
	"ResultImg (11).gif",
	"ResultImg (12).gif",
	"ResultImg (13).gif",
	"ResultImg (14).gif",
	"ResultImg (15).gif",
	"ResultImg (16).gif",
	"ResultImg (17).gif",
	"ResultImg (18).gif",
	"ResultImg (19).gif",
	"ResultImg (20).gif"
	
    ]
	
    a=random.choice(ImgList)
    BackImg = PhotoImage(file=a)
	
	
    r=Label(ResultWindow, 
         justify = CENTER,
          compound = CENTER,
            image=BackImg,
        padx = 20)
    
    r.image=BackImg
    r.pack()

    
    global MainText
    MainText=list()
    
    for t in range(5):
        x=int(v.get())	
        if(x == 0): 
                urlhere = 'https://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter, asc'
            
        elif(x == 1): 
                urlhere = 'https://www.imdb.com/search/title?genres=musical&title_type=feature&sort=moviemeter, asc'
            
        elif(x== 2): 
                urlhere = 'https://www.imdb.com/search/title?genres=family&title_type=feature&sort=moviemeter, asc'
            
        elif(x== 3): 
                urlhere = 'https://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'
            
        elif(x== 4): 
                urlhere = 'https://www.imdb.com/search/title?genres=sport&title_type=feature&sort=moviemeter, asc'
            
        elif(x== 5): 
                urlhere = 'https://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'
            
        elif(x== 6): 
                urlhere = 'https://www.imdb.com/search/title?genres=western&title_type=feature&sort=moviemeter, asc'

        elif(x== 7): 
                urlhere = 'https://www.imdb.com/search/title?genres=film_noir&title_type=feature&sort=moviemeter, asc'
        
    


        page=requests.get(urlhere)
        soup=BeautifulSoup(page.content, 'html.parser')

        text1=soup.find_all('h3',class_='lister-item-header')[t].get_text()
        text2="Category: " +soup.find_all('span',class_='genre')[t].get_text()
        text4="Runtime: "+soup.find_all('span',class_='runtime')[t].get_text()


        
        
        MainText.append(text1+"\n"+text2)
        

		

    frameR =Frame(ResultWindow,
                highlightbackground="gray",
                  bd=0,
                 )
    frameR.place(x=90,y=100)
    
    
    ResultBlock1 = Label(frameR, 
                   text=MainText[0], 
                   fg="black",
                   #bg="#"+("%06x"%random.randint(0,16777215)),
                   font=("Freestyle Script", 18),
	    	   bg="gray"
					
                           )
    ResultBlock1.pack(side=LEFT,padx=0)


    ResultBlock2 = Label(frameR, 
                   text=MainText[1], 
                   fg="gray",
                   #bg="#"+("%06x"%random.randint(0,16777215)),
                   font=("Freestyle Script", 18),
	    	   bg="black"
					
                           )
    ResultBlock2.pack(side=LEFT,padx=0)
    

    ResultBlock3 = Label(frameR, 
                   text=MainText[2], 
                   fg="black",
                   #bg="#"+("%06x"%random.randint(0,16777215)),
                   font=("Freestyle Script", 18),
	    	   bg="gray"
					
                           )
    ResultBlock3.pack(side=LEFT,padx=0)

    ResultBlock4 = Label(frameR, 
                   text=MainText[3], 
                   fg="gray",
                   #bg="#"+("%06x"%random.randint(0,16777215)),
                   font=("Freestyle Script", 18),
	    	   bg="black"
					
                           )
    ResultBlock4.pack(side=LEFT,padx=0)

		
		
    
    Back =Button(ResultWindow, 
                   text="Go back", 
                   fg="white",
                   bg="RoyalBlue1",
                   font=("Jokerman", 16),
                  cursor="circle",
                 relief=RAISED,
                   command=ResultWindow.destroy)
    Back.place(x=10,y=10)
    

    

    
def Emotion():
    
    global v
    v=IntVar()
    EmotionWindow=Toplevel()
	
    v.set(1)
    
    Emolist = [
    ("Sad"),
    ("Disgust"),
    ("Anger"),
    ("Anticipation"),
    ("Fear"),
    ("Enjoyment"),
    ("Trust"),
    ("Surprise")
    ]
    
    length=int(len(Emolist))

    Label(EmotionWindow, 
         text="""Choose your emotion:""",
         justify =CENTER,
		 
         padx = 20).pack()

    colors = ["coral", "cyan", "azure2", "khaki1", "maroon1", "plum1", "gold","SlateBlue1","HotPink1"]


    for val in range(length):
        Radiobutton(EmotionWindow, 
                  text=Emolist[val],
		bg=colors[int(val)],
	         activeforeground="yellow",
                    activebackground="red",
                  indicatoron=0,
                    bd=4,
                  padx=16,
                   pady=5,
		     width=20,
                    cursor="target",
                    value=val,
                  variable=v,
		    font=("Forte", 24),
                    relief=RAISED
                  ).pack()
        
              
    frame1 =Frame(EmotionWindow,
                highlightbackground="gray",
                 bd= 6,
                 )
    frame1.pack()
    
  
	
    Back =Button(frame1, 
                   text="Go back", 
                   fg="white",
                   bg="RoyalBlue1",
                   font=("Jokerman", 16),
                 cursor="circle",
                 relief=RAISED,
                   command=EmotionWindow.destroy)
    Back.pack(side=LEFT,padx=12)

    slogan = Button(frame1,
                   text="RECOMMEND MOVIES",
                   fg="white",
                   bg="green",
                   font=("Jokerman", 16),
                    cursor="circle",
                   command=Result)
    slogan.pack(side=LEFT)



#Tkinter codeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
try:
    home=Tk()
    home.title("SMoReA")
    logo = PhotoImage(file="img2.gif")
    w = Label(home, 
             compound = CENTER, 
             image=logo).pack(side="right")
			 
			 
    Start=Button(home, 
                   text="Let's Get Started",
                   fg="white", bg="RoyalBlue1",
                    #activeforeground="green", activebackground="red",
    			command=Emotion,
                 cursor="circle",
                   font=("Jokerman", 18)
                          )
    Start.place(x=520,y=470)

    QuitButton = Button(home, 
                   text="Quit",
                   fg="white", bg="Red",
                    #activeforeground="green", activebackground="red",
                   font=("Jokerman", 14),
                    cursor="circle",
                   command=ExitApplication
                           )
    QuitButton.place(x=10,y=480)

    home.mainloop()

except Exception:
    messagebox.showerror("Error", "Something's wrong!!\n Check your internet connection and try again")
    Error()
