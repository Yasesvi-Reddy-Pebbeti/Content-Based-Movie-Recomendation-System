'''
win1 = main page
win2 = register function
win3 = login function
window = movie recommendation system
'''
from tkinter import *
import registration
from tkinter import ttk
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import psycopg2
import movielistdata

def screen1():
    screen1 = Toplevel(win1)
    screen1.title("About the movie")
    tree = ttk.Treeview(screen1, column=("c1", "c2", "c3","c4"), show='headings')
    tree.column("#1", anchor=CENTER)
    tree.heading("#1", text="TITLE")
    tree.column("#2", anchor=CENTER)
    tree.heading("#2", text="CAST")
    tree.column("#3", anchor=CENTER)
    tree.heading("#3", text="DIRECTOR OF THE MOVIE")
    tree.column("#4", anchor=CENTER)
    tree.heading("#4", text="GENRE")
    tree.pack()
    itm = list1.get(list1.curselection())
    for row in movielistdata.search_movie_details(itm):
        tree.insert("",END, values=row)
    screen1.resizable(True,True)
    b2=Button(screen1, text="Close",command= screen1.destroy)
    b2.pack()

def insert_in_list1():
    movie_user_likes = entry_value.get()

    # Load the movie dataset with correct path
    df2 = pd.read_csv("data/movie_dataset.csv")

    # Check if movie title is in the dataset
    if movie_user_likes in df2['title'].values:
        list1.delete(0, END)

        def getIndex(title):
            return df2[df2.title == title].index[0]

        def getTitle(index):
            return df2.iloc[index]["title"]

        # Fill nulls in required features
        for feature in ['keywords', 'cast', 'director', 'genres']:
            df2[feature] = df2[feature].fillna('')

        # Combine features for vectorization
        df2['combined_features'] = df2['keywords'] + ' ' + df2['cast'] + ' ' + df2['director'] + ' ' + df2['genres']

        # Create similarity matrix
        cv = CountVectorizer()
        count_matrix = cv.fit_transform(df2['combined_features'])
        cosine_sim = cosine_similarity(count_matrix)

        # Get index of the searched movie
        movie_index = getIndex(movie_user_likes)

        # Get similar movies
        similar_movies = list(enumerate(cosine_sim[movie_index]))
        sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)

        i = 0
        for movie in sorted_similar_movies:
            movie_title = getTitle(movie[0])
            if movie_title != movie_user_likes:
                list1.insert(END, movie_title)
                i += 1
            if i >= 10:
                break
    else:
        list1.delete(0, END)
        list1.insert(END, "Searched movie not found")


def login_success():
    window= Toplevel(win1)
    window.wm_title("Movie Recommendation System")

    label1= Label(window, text="Enter title", width = 20)
    label1.grid(row=0, column=0)

    global entry_value,entry1
    entry_value= StringVar()
    entry1= Entry(window, textvariable=entry_value)
    entry1.grid(row=0,column=1)

    b1= Button(window, text="Recommended movies", width =20, command =insert_in_list1)
    b1.grid(row=0, column=2)

    l3=Label(window, text="")
    l3.grid(row=1,column=1)


    l1=Label(window, text="To know about the cast and crew of a movie click on the recommended list")
    l1.grid(row=2,column=1)

    l2=Label(window, text="")
    l2.grid(row=3,column=1)

    global list1
    list1= Listbox(window, height=10, width=100)
    list1.grid(row=4, column=1, rowspan=6, columnspan=2)

    sb1 = Scrollbar(window)
    sb1.grid(row=4, column=3, rowspan=6)

    list1.configure(yscrollcommand = sb1.set)
    sb1.configure(command = list1.yview)

    b3=Button(window, text="About movie",width=22,command= screen1)
    b3.grid(row=4,column=4)

    b6=Button(window, text="Logout ",width=22,command= window.destroy)
    b6.grid(row=5,column=4)

def closeFunction():
    win3.destroy()  
def user_login():
    uluser=le1.get()
    ulpassword=le2.get()
    le1.delete(0,END)
    le2.delete(0,END)
    if registration.verify(uluser,ulpassword):
        ull1=Label(win3,text ="Log-in successful",fg="green")
        ull1.pack()
        login_success()
        closeFunction()
    else:
        ull2=Label(win3,text ="Please verify your details",fg="green")
        ull2.pack()

    

def login():
    global win3
    win3= Toplevel(win1)
    win3.title("Login Page")
    win3.geometry("300x250")
    global userverify,passwordverify,le1,le2
    userverify=StringVar()
    passwordverify=StringVar()

    ll1=Label(win3,text="Please enter your login details")
    ll1.pack()
    ll2=Label(win3,text="")
    ll2.pack()
    ll3= Label(win3,text="Username")
    ll3.pack()
    le1=Entry(win3,textvariable=userverify)
    le1.pack()
    ll4= Label(win3, text="Password")
    ll4.pack()
    le2=Entry(win3,textvariable=passwordverify)
    le2.pack()
    ll5=Label(win3,text="")
    ll5.pack()
    lb1= Button(win3,text="Login", width=10, height=1, command=user_login)
    lb1.pack()


def user_registration():
    registration.insert_new_details(re1.get(), remail_entry.get(),re2.get())
    re1.delete(0,END)
    remail_entry.delete(0,END)
    re2.delete(0,END)
    url1=Label(win2,text ="Registration successful",fg="green")
    url1.pack()

def register():
    global win2
    win2= Toplevel(win1)
    win2.title("Registration page")
    win2.geometry("300x250")
    global username, password, re1,re2,remail_entry
    username = StringVar()
    password = StringVar()
    email = StringVar()

    rl1 = Label(win2,text= "please enter your details")
    rl1.pack()
    rl2= Label(win2, text="")
    rl2.pack()
    rl3= Label(win2, text="Username")
    rl3.pack()
    re1= Entry(win2,textvariable=username)
    re1.pack()
    remail= Label(win2, text="Email Id")
    remail.pack()
    remail_entry= Entry(win2,textvariable=email)
    remail_entry.pack()
    rl4= Label(win2, text="Password")
    rl4.pack()
    re2= Entry(win2,textvariable=password)
    re2.pack()
    rl5= Label(win2, text="")
    rl5.pack()
    rb1 = Button(win2, text ="Register", width = 10, height=1, command=user_registration)
    rb1.pack() 
    

win1 = Tk()
win1.title("Signup page")
win1.geometry("300x250")
l1= Label(win1, text ="")
l1.pack()
b1 = Button(win1, text ="Login", height=2,width=30,command=login)
b1.pack()
b2 = Button(win1, text ="Register", height=2,width=30,command=register)
b2.pack()
win1.mainloop()