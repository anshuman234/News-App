import io
import webbrowser
import requests
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk,Image

class News_app:
    def __init__(self):
        # FETCH DATA
        # api key  -- 646cdd6f8be14aab8f85ba7bf657811e

        self.data = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=646cdd6f8be14aab8f85ba7bf657811e').json()
        self.load_gui()
        self.load_news_item(0)



    def load_gui(self):
        self.root = Tk()
        self.root.geometry('400x400')
        self.root.resizable(0,0)
        self.root.configure(background='black')

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()


    def load_news_item(self, index):
        self.clear()
        
        # try:

        #     img_url =self.data['articles'][index]['urlToImage']
        #     raw_data = urlopen(img_url).read()
        #     img = Image.open(io.Bytes10(raw_data)).resize((350,250))
        #     photo = ImageTk.PhotoImage(img)

        # except:
        #     img_url = 'https://static.vecteezy.com/system/resources/thumbnails/004/141/669/small/no-photo-or-blank-image-icon-loading-images-or-missing-image-mark-image-not-available-or-image-coming-soon-sign-simple-nature-silhouette-in-frame-isolated-illustration-vector.jpg'
        #     raw_data = urlopen(img_url).read()
        #     img = Image.open(io.Bytes10(raw_data)).resize((350,250))
        #     photo = ImageTk.PhotoImage(img)


        # label = Label(self.root,image=photo)  
        # label.pack()

        heading = Label(self.root,text=self.data['articles'][index]['title'],bg='black', fg='white', wraplength=350,justify='center')
        heading.pack(pady=(10,20))
        heading.config(font=('verdana',15))


        details = Label(self.root,text=self.data['articles'][index]['description'],bg='black', fg='white', wraplength=350,justify='center')
        details.pack(pady=(2,20))
        details.config(font=('verdana',12))

        frame = Frame(self.root,bg='black')
        frame.pack(expand=True, fill=BOTH)

        if index !=0:
            
            prev = Button(frame,text='Prev',width=18, height=3, command= lambda :self.load_news_item(index-1))
            prev.pack(side=LEFT)

        if index != len(self.data['articles'])-1:

            next = Button(frame,text='Next',width=18, height=3, command= lambda :self.load_news_item(index+1))
            next.pack(side=RIGHT)
            read = Button(frame,text='Read More',width=18, height=3, command=lambda :self.open_link(self.data['articles'][index]['url']))
            read.pack(side=LEFT)

            

        if index == len(self.data['articles'])-1:
            
            read = Button(frame,text='Read More',width=18, height=3, command=lambda :self.open_link(self.data['articles'][index]['url']))
            read.pack(side=RIGHT)


        self.root.mainloop()

    def open_link(self,url):
        webbrowser.open(url)

obj = News_app()
