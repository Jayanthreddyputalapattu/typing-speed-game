import random

words = ['mango','apple',"thumb",'village','door','toor','jayanth','gayathri','television','mobile','laptop','speed fan','people','good','super','bye','hi','bad','chrome','google','yahoo','firefox','safari','super bad','come','here','there','lego','best','waste','chennai','delhi capitals','mumbai indians','india','indian cricket','royals','hyderabad','putalapattu','gujart lions','pune warriors','gujart sigh','australia','new zeland','china','Umerica','United kingdom','United States','bangladesh','nepal ']


def time():
    global timeleft,score,miss
    if(timeleft >= 11):
        pass
    else:
        TimeLabelCount.configure(fg='red')
    if(timeleft>0):
        timeleft -= 1
        TimeLabelCount.configure(text=timeleft)
        TimeLabelCount.after(1000,time)
    else:
        GamePlayDetailLabel.configure(text='Hit = {} | Miss = {} | Total Score = {}'.format(score,miss,score-miss))
        rr = messagebox.askretrycancel("Nofitication","For Play Again Hit Retry")
        if(rr == True):
            score = 0
            timeleft = 120
            miss=0
            TimeLabelCount.configure(text=score)
            TimeLabelCount.configure(fg='blue')
            scoreLabelCount.configure(text=score)
        if(rr == False):
            exit()

def Labelslider():
    global count,sliderWords
    text = 'Welcome to Typing Speed Increaser Game'
    if(count >= len(text)):
        count = 0
        sliderWords = ''
    sliderWords += text[count]
    count += 1
    fontLabel.configure(text=sliderWords)
    fontLabel.after(150,Labelslider)



def startGame(event):
    global score,miss
    if(timeleft == 120):
        time()
    GamePlayDetailLabel.configure(text='')
    if(wordEntry.get() == wordLabel['text']):
        score += 1
        scoreLabelCount.configure(text=score)
    else:
        miss += 1
        print("Miss",miss)
    random.shuffle(words)
    wordLabel.configure(text=words[0])
    wordEntry.delete(0,END)
from tkinter import *
from tkinter import messagebox


root = Tk()
root.geometry("980x680+400+100")
root.configure(bg='powder blue')
root.title("Typing speed Increaser Game")


score = 0
timeleft = 120
count = 0
sliderWords = ''
miss = 0

fontLabel = Label(root,text='',font=("airal",25,'italic bold'),
                  bg='powder blue',fg='red',width=40)
fontLabel.place(x=10,y=10)
Labelslider()


random.shuffle(words)
wordLabel = Label(root,text=words[0],font=('airal',40,'italic bold'),bg="powder blue",justify="center")
wordLabel.place(x=350,y=200)


scoreLabel = Label(root,text='Your Score : ',font=("airal",25,'italic bold'),bg='powder blue',fg='blue')
scoreLabel.place(x=10,y=100)

scoreLabelCount = Label(root,text=score ,font=("airal",25,'italic bold'),bg='powder blue',fg='blue')
scoreLabelCount.place(x=80,y=180)

TimerLabel = Label(root,text="Time Left : ",font=("airal",25,'italic bold'),bg='powder blue',fg='blue')
TimerLabel.place(x=600,y=100)

TimeLabelCount = Label(root,text=timeleft ,font=("airal",25,'italic bold'),bg='powder blue',fg='blue')
TimeLabelCount.place(x=680,y=180)



GamePlayDetailLabel = Label(root,text="Type a Word and Hit Enter",font=("airal",30,"italic bold"),bg='powder blue',fg="dark grey")
GamePlayDetailLabel.place(x=150,y=450)



wordEntry = Entry(root,font=("airal",25,"italic bold"),bd=10,justify="center")
wordEntry.place(x=250,y=300)
wordEntry.focus_set()

root.bind('<Return>',startGame)
root.mainloop()