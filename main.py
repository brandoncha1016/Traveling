from tkinter import *
from tkinter import messagebox as mb
from domain import userEntity
from model import datum
import pymysql.cursors
from login import Login
import view


def main():
    # 로그인 절차 
    while(True):
        window = Tk()
        app = Login(window, "SK Travel Community 로그인")
        window.mainloop()
        login = app.result()
        if login[0]==True:
            id_ = login[1]
            run = view.main_GUI(id_)
            print(run)
            if run == 2:
                quit()
            elif run == 1:
                id_ = None
                break
    main()



if __name__ == "__main__":
    main()
        
