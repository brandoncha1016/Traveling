from tkinter import *
from tkinter import messagebox as mb
from model import datum 
from PIL import Image, ImageTk  
import pymysql.cursors
from domain import  userEntity
from controller import ACTION_

class Login:

    def __init__(self, window, titles):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width/2) - (400/2)
        y = (screen_height/2) - (140/2)
         
        self.window = window
        self.window.title(titles)
        self.window.protocol("WM_DELETE_WINDOW", lambda:quit())
        self.window.geometry("400x140+%d+%d"%(x,y-100)) 
        #self.window.resizable(False, False)
        self.component()
        self.input_id.focus_set()
 

    def component(self):
        # logo image
        global logo_image
        logo_image = PhotoImage(file=r'./img/skinfosec.png') # check image_location and file name 
        image_label = Label(self.window, background="white", image=logo_image)
        image_label.pack(fill=BOTH, expand=YES,side="left")

        frame_ = Frame(self.window, bd=10)
        frame_.pack(fill=BOTH, expand=YES,side="left")
         
        frame_data = Frame(frame_, bd=5)
        frame_data.pack(fill=BOTH, expand=YES)
         

        # atur input username
        Label(frame_data, text='아이디:').grid(row=0, column=1, sticky=W)
        self.input_id = Entry(frame_data)
        self.input_id.grid(row=0, column=2)


        # atur input password
        Label(frame_data, text='비밀번호:').grid(row=1, column=1, sticky=W)
        self.input_pwd = Entry(frame_data, show='*')
        self.input_pwd.grid(row=1, column=2)
  
        # check -> show password 
        self.check_ = IntVar() 
         
        self.show_pwd = Checkbutton(frame_data, text='비밀번호표시', variable=self.check_, command=self.see_pwd)
        self.show_pwd.grid(row=2, column=2, sticky=E)
         
        # button on frame
        frame_button = Frame(frame_, bd=5)
        frame_button.pack(fill=BOTH, expand=YES)
         
        # atur tombol login
        self.btnLogin = Button(frame_button, text='접속하기', command=self.prossess_login)
        self.btnLogin.pack(side=LEFT, fill=BOTH, expand=YES)
 
         
        self.btnRegister = Button(frame_button, text='등록하기', command=self.register_user)
        self.btnRegister.pack(side=LEFT, fill=BOTH, expand=YES)
         
        # 편의성을 위해 키보드와 버튼(함수) 연결
        self.window.bind('<Return>',self.prossess_login)
        self.window.bind('<Escape>',self.closed)
        self.window.bind('<Control-s>',self.register_user)

        

    def prossess_login(self, event=None):
        # retrieve input data from the user
        global nmUser
        global regi
        regi = False
        nmUser = self.input_id.get()
        passUser = self.input_pwd.get()
        

        if nmUser=='':
            mb.showwarning('Warnning', '아이디를 입력하십시오.', parent=self.window)
            self.process_ = False
            self.input_id.focus_set()
        elif passUser=='':
            mb.showwarning('Warnning', '비밀번호를 입력하십시오', parent=self.window)
            self.process_ = False
            self.input_pwd.focus_set()
        
        elif datum().login(nmUser,passUser):
            mb.showinfo("Login", "인증에 성공하였습니다.", parent=self.window)
            self.process_ = True
            regi = True
            self.closed()
        else:
            mb.showwarning('Warnning', '아이디 혹은 비밀번호가 잘못되었습니다.', parent=self.window)
            self.process_ = False
            self.delete_()
             

    def see_pwd(self, event=None):
        check_value = self.check_.get()
         
        if check_value== 1:
            self.input_pwd['show'] = ''
        else:
            self.input_pwd['show'] = '*'
         
    def closed(self, event=None):
        self.delete_()
        self.window.destroy()
         
    def delete_(self, event=None):
        self.input_id.delete(0, END)
        self.input_pwd.delete(0, END)
        self.input_id.focus_set()        
         
    
    def register_user(self,event=None):
        global nmUser
        global regi
        regi = False
        nmUser = self.input_id.get()
        passUser = self.input_pwd.get()
       
        if nmUser=='':
            mb.showwarning('Warnning', '아이디를 입력하십시오.', parent=self.window)
            self.process_ = False
            self.input_id.focus_set()
        
        elif passUser=='':
            mb.showwarning('Warnning', '비밀번호를 입력하십시오', parent=self.window)
            self.process_ = False
            self.input_pwd.focus_set()


        elif datum().get_id(nmUser)!=True:
            mb.showinfo("Login", "이미 등록된 계정입니다.", parent=self.window)
            self.process_ = False
            self.delete_()
        else:
            try:
                self.window.destroy()
                user_info = user_registration()
                print("user_info",user_info)
                user_entity = userEntity(nmUser,passUser,user_info[0], user_info[1], user_info[2],user_info[3])
                print("entity",user_entity)
                regi = True
                datum().insert_userInfo(user_entity)
            finally:
                pass

        

    def result(self):
        a = [regi, nmUser]
        try:
            return a
        except AttributeError:
             return [False,None]
        except NameError:
            return [False,None]
        except TypeError:
            return [False,None]
        finally:
            pass
      
  
        
    def get_info(self,new_window,values):
        print("values in get_info function :", values)
        new_window.destroy()
        return values
    
  
  
def user_registration(): 
    while(True):
        root = Tk()
        root.geometry('500x500')
        root.title(":: 회원가입 ::")
        root.configure(bg='white')
        title = Label(root,bg="white",fg='red', text="| 멤버십 등록 |",width=20,font=("bold", 20))
        title.place(x=80,y=53)
        root.protocol("WM_DELETE_WINDOW", lambda: root.destroy())

        fullname = Label(root, bg="white",fg='black',text="* 이  름 :",width=20,font=("bold", 10))
        fullname.place(x=100,y=130)
        myname = StringVar(root)
        name_entry = Entry(root,textvariable=myname)
        name_entry.place(x=240,y=130)
        
        contact = Label(root,bg="white",fg='black', text="* 연락처 :",width=20,font=("bold", 10))
        contact.place(x=100,y=180)
        myContact =StringVar(root)
        contact_entry = Entry(root,textvariable=myContact)
        contact_entry.place(x=240,y=180)

        gender= Label(root,bg="white", fg='black',text="* 성  별 :",width=20,font=("bold", 10))
        gender.place(x=100,y=230)
        var = IntVar(root)
        Radiobutton(root,bg="white", text="남자",padx = 5, variable=var, value=1).place(x=235,y=230)
        Radiobutton(root,bg="white", text="여자",padx = 20, variable=var, value=2).place(x=290,y=230)
        
        area = Label(root,bg="white",fg='black', text="* 거주지역 :",width=20,font=("bold", 10))
        area.place(x=100,y=280)

        list1 = ['서울','인천','경기','강원','충남','충북','전북','전남','경북','경남','제주'];
        c=StringVar(root)
        droplist=OptionMenu(root,c, *list1)
        droplist.config(width=15)
        c.set('지역선택') 
        droplist.place(x=240,y=275)
        
        Button(root, text='Submit',width=20,bg='brown',fg='white', command=lambda:root.destroy()).place(x=180,y=380)
        root.mainloop()
        res= ACTION_().check_contact(myContact.get())
        if res == True:
            correct()
            return (myname.get(), myContact.get(), var.get(), c.get())
        elif res == False:
            wrong_contact()
        else:
            pass
   

def wrong_contact():
    new_message= Tk()
    new_message.withdraw()
    mb.showinfo("잘못된 연락처 양식 ", "예시) '000-0000-0000' 형식으로 입력하여 주십시오. ")
    new_message.destroy()



def correct():
    new_message= Tk()
    new_message.withdraw()
    mb.showinfo("Message", "정상적으로 등록되었습니다.")
    new_message.destroy()

   
