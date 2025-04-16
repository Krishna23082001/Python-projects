from tkinter import Tk, Button
import os

def restart():
    os.system("shutdown /r /t 1")
def restarttime():
    os.system("shutdowm /r /t 20")
def logout():
    os.system("shutdowm -1")
def shutdown():
    os.system("shutdowm /s /t 1")
st=Tk()
st.title("Shutdown App")
st.geometry("500x500")
st.config(bg="light blue")

r_button = Button(st, text="Restart", font=("Time New Roman",30,"bold"), relief="raise", cursor="plus", command= restart)
r_button.place(x=160, y=20, height=50, width=150)

rt_button = Button(st, text="Restart With Time", font=("Time New Roman",30,"bold"), relief="raise", cursor="plus", command= restarttime)
rt_button.place(x=70, y=100, height=50, width=350)

log_button = Button(st, text="Log Out", font=("Time New Roman",30,"bold"), relief="raise", cursor="plus", command= logout)
log_button.place(x=150, y=200, height=50, width=180)

s_button = Button(st, text="Shutdown", font=("Time New Roman",30,"bold"), relief="raise", cursor="plus", command= shutdown)
s_button.place(x=150, y=300, height=50, width=200)




st.mainloop()