from tkinter import *
from tkinter import ttk as ttk
from PIL import Image, ImageTk  
from tkinter import messagebox as mb
from model import datum
from controller import ACTION_
from login import wrong_contact
import webbrowser

url = "https://github.com/Cha-Euy-Sung/traveling_communities"

def openweb():
    webbrowser.open(url,new=1)


def search_area_window(id_):
    new_frame = Tk() 
    new_frame.geometry('200x130') 
    new_frame.title("지역명 입력")

    space=Label(new_frame,bg="white",fg='blue', text="| 관심지역 검색 |",width=200, height= 3)
    space.pack(side=TOP,anchor='center')
    input_text = StringVar(new_frame) 
    
    entry1 = ttk.Entry(new_frame, textvariable = input_text, justify = CENTER) 

    entry1.focus_force() 
    entry1.pack(side = TOP, ipadx = 30, ipady = 6) 
    
    save = ttk.Button(new_frame, text = '살펴보기', command = lambda : new_frame.destroy()) 
    save.pack(side = TOP, pady = 10) 
    new_frame.mainloop()
    view_byarea(id_,input_text.get())


def search_club_window(id_):
    new_frame = Tk() 
    new_frame.geometry('200x130') 
    new_frame.title("커뮤니티명 입력")

    space1=Label(new_frame,bg="white",fg='blue', text=":: 이름의 일부로도 검색가능 ::",width=200, height= 2)
    space1.pack(side=TOP,anchor='center')
    input_text = StringVar(new_frame) 
    
    entry1 = ttk.Entry(new_frame, textvariable = input_text, justify = CENTER) 

    entry1.focus_force() 
    entry1.pack(side = TOP, ipadx = 30, ipady = 6) 
    
    save = ttk.Button(new_frame, text = '살펴보기', command = lambda : new_frame.destroy()) 
    save.pack(side = TOP, pady = 10) 
    new_frame.mainloop()
    view_byname(id_,input_text.get())


def view_byarea(id_,area_):
    global tree
    root = Tk()
    root.title("활동지역 검색결과")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = 730
    height = 320
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
    root.resizable(0, 0)
    space=Frame(root, width=700, height=15)
    space.pack(side=TOP,anchor='center')
    Body = Frame(root, width=650, height=300, bd=8)
    Body.pack(side=LEFT)
    Button_Group=Frame(root, width=700, height=200)
    Button_Group.pack(side=LEFT,anchor='nw')
    Buttons = Frame(Button_Group, width=200, height=100)
    Buttons.pack(side=BOTTOM,anchor='center')
    btn_register = Button(Buttons, width=15, text="가입하기",command=lambda:joining_club(id_, selected_club))
    btn_register.pack(ipadx=3,ipady=3,anchor='s')
    btn_register2 = Button(Buttons, width=15, text="탈퇴하기",command=lambda:leaving_club(id_, selected_club))
    btn_register2.pack(ipadx=3,ipady=3,anchor='s')
    btn_register3 = Button(Buttons, width=15, text="나가기",command=lambda:root.destroy())
    btn_register3.pack(ipadx=3,ipady=3,anchor='s')

    scrollbary = Scrollbar(Body, orient=VERTICAL)
    scrollbarx = Scrollbar(Body, orient=HORIZONTAL)
    tree = ttk.Treeview(Body, columns=("clubName", "own","area", "content"), selectmode="extended", height=300, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('clubName', text="커뮤니티", anchor=W)
    tree.heading('own', text="모임장", anchor=W)
    tree.heading('area', text="모임지역", anchor=W)
    tree.heading('content', text="한줄공지", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=150)
    tree.column('#2', stretch=NO, minwidth=0, width=100)
    tree.column('#3', stretch=NO, minwidth=0, width=50)
    tree.column('#3', stretch=NO, minwidth=0, width=100)
    tree.bind('<ButtonRelease-1>', selectItem)
    tree.pack()
    populate_area(tree,area_)
    root.mainloop()
    main_GUI(id_)


def view_byname(id_,clubName_):
    global tree
    root = Tk()
    root.title("커뮤니티명 검색결과")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = 730
    height = 320
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
    root.resizable(0, 0)
    space=Frame(root, width=700, height=15)
    space.pack(side=TOP,anchor='center')
    Body = Frame(root, width=650, height=300, bd=8)
    Body.pack(side=LEFT)
    Button_Group=Frame(root, width=700, height=200)
    Button_Group.pack(side=LEFT,anchor='nw')
    Buttons = Frame(Button_Group, width=200, height=100)
    Buttons.pack(side=BOTTOM,anchor='center')
    btn_register = Button(Buttons, width=15, text="가입하기",command=lambda:joining_club(id_, selected_club))
    btn_register.pack(ipadx=3,ipady=3,anchor='s')
    btn_register2 = Button(Buttons, width=15, text="탈퇴하기",command=lambda:leaving_club(id_, selected_club))
    btn_register2.pack(ipadx=3,ipady=3,anchor='s')
    btn_register3 = Button(Buttons, width=15, text="나가기",command=lambda:root.destroy())
    btn_register3.pack(ipadx=3,ipady=3,anchor='s')

    scrollbary = Scrollbar(Body, orient=VERTICAL)
    scrollbarx = Scrollbar(Body, orient=HORIZONTAL)
    tree = ttk.Treeview(Body, columns=("clubName", "own","area", "content"), selectmode="extended", height=300, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('clubName', text="커뮤니티", anchor=W)
    tree.heading('own', text="모임장", anchor=W)
    tree.heading('area', text="모임지역", anchor=W)
    tree.heading('content', text="한줄공지", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=150)
    tree.column('#2', stretch=NO, minwidth=0, width=100)
    tree.column('#3', stretch=NO, minwidth=0, width=50)
    tree.column('#3', stretch=NO, minwidth=0, width=100)
    tree.bind('<ButtonRelease-1>', selectItem)
    tree.pack()
    populate_club(tree,clubName_)
    root.mainloop()
    main_GUI(id_)



def selectItem(a):
    global selected_club
    try:
        curItem = tree.focus()
        item = tree.item(curItem)
        selected_club = item["values"][0]
    except IndexError:
        pass
    finally:
        pass

def joining_club(id_, selected_club):
    result = datum().join_club(id_,selected_club)
    join_club_message(result)

def leaving_club(id_, selected_club):
    print("leaving club clicked")
    result = datum().remove_member(id_,selected_club)
    print("result passed")
    leave_club_message(result)
    


def view_allcommunities(id_):
    global tree
    root = Tk()
    root.title("커뮤니티 목록보기")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = 730
    height = 320
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
    root.resizable(0, 0)
    space=Frame(root, width=700, height=15)
    space.pack(side=TOP,anchor='center')
    Body = Frame(root, width=650, height=300, bd=8)
    Body.pack(side=LEFT)
    Button_Group=Frame(root, width=700, height=200)
    Button_Group.pack(side=LEFT,anchor='nw')
    Buttons = Frame(Button_Group, width=200, height=100)
    Buttons.pack(side=BOTTOM,anchor='center')
    btn_register = Button(Buttons, width=15, text="가입하기",command=lambda:joining_club(id_, selected_club))
    btn_register.pack(ipadx=3,ipady=3,anchor='s')
    btn_register2 = Button(Buttons, width=15, text="탈퇴하기",command=lambda:leaving_club(id_, selected_club))
    btn_register2.pack(ipadx=3,ipady=3,anchor='s')
    btn_register3 = Button(Buttons, width=15, text="나가기",command=lambda:root.destroy())
    btn_register3.pack(ipadx=3,ipady=3,anchor='s')

    scrollbary = Scrollbar(Body, orient=VERTICAL)
    scrollbarx = Scrollbar(Body, orient=HORIZONTAL)
    tree = ttk.Treeview(Body, columns=("clubName", "own","area", "content"), selectmode="extended", height=300, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('clubName', text="커뮤니티", anchor=W)
    tree.heading('own', text="모임장", anchor=W)
    tree.heading('area', text="모임지역", anchor=W)
    tree.heading('content', text="한줄공지", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=150)
    tree.column('#2', stretch=NO, minwidth=0, width=100)
    tree.column('#3', stretch=NO, minwidth=0, width=50)
    tree.column('#3', stretch=NO, minwidth=0, width=100)
    tree.bind('<ButtonRelease-1>', selectItem)
    tree.pack()
    populateView(tree)
    root.mainloop()

def view_users(id_):
    global tree
    root = Tk()
    root.title("내정보보기")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = 730
    height = 320
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
    root.resizable(0, 0)
    space=Frame(root, width=700, height=15)
    space.pack(side=TOP,anchor='center')
    Body = Frame(root, width=650, height=300, bd=8)
    Body.pack(side=LEFT)
    Button_Group=Frame(root, width=700, height=200)
    Button_Group.pack(side=LEFT,anchor='nw')
    Buttons = Frame(Button_Group, width=200, height=100)
    Buttons.pack(side=BOTTOM,anchor='center')
    btn_register = Button(Buttons, width=15, text="수정하기",command=lambda:moveto_user_update(root,id_))
    btn_register.pack(ipadx=3,ipady=3,anchor='s')
    btn_register2 = Button(Buttons, width=15, text="나가기",command=lambda:root.destroy())
    btn_register2.pack(ipadx=3,ipady=3,anchor='s')

    scrollbary = Scrollbar(Body, orient=VERTICAL)
    scrollbarx = Scrollbar(Body, orient=HORIZONTAL)
    tree = ttk.Treeview(Body, columns=("name", "gender","area", "contact"), selectmode="extended", height=300, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('name', text="이름", anchor=W)
    tree.heading('gender', text="성별", anchor=W)
    tree.heading('area', text="거주지역", anchor=W)
    tree.heading('contact', text="연락처", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=150)
    tree.column('#2', stretch=NO, minwidth=0, width=100)
    tree.column('#3', stretch=NO, minwidth=0, width=50)
    tree.column('#3', stretch=NO, minwidth=0, width=100)
    tree.bind('<ButtonRelease-1>', selectItem)
    tree.pack()
    populateView_user(tree,id_)
    root.mainloop()
    main_GUI(id_)

def view_members(id_):
    global tree
    root = Tk()
    root.title("멤버 정보보기")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = 730
    height = 320
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
    root.resizable(0, 0)
    space=Frame(root, width=700, height=15)
    space.pack(side=TOP,anchor='center')
    Body = Frame(root, width=650, height=300, bd=8)
    Body.pack(side=LEFT)
    Button_Group=Frame(root, width=700, height=200)
    Button_Group.pack(side=LEFT,anchor='nw')
    Buttons = Frame(Button_Group, width=200, height=100)
    Buttons.pack(side=BOTTOM,anchor='center')
    btn_register = Button(Buttons, width=15, text="저장하기",command=lambda:ACTION_().save_contact(id_))
    btn_register.pack(ipadx=3,ipady=3,anchor='s')
    btn_register2 = Button(Buttons, width=15, text="나가기",command=lambda:root.destroy())
    btn_register2.pack(ipadx=3,ipady=3,anchor='s')

   
    scrollbary = Scrollbar(Body, orient=VERTICAL)
    scrollbarx = Scrollbar(Body, orient=HORIZONTAL)
    tree = ttk.Treeview(Body, columns=("name", "gender","area", "contact"), selectmode="extended", height=300, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('name', text="이름", anchor=W)
    tree.heading('gender', text="성별", anchor=W)
    tree.heading('area', text="거주지역", anchor=W)
    tree.heading('contact', text="연락처", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=150)
    tree.column('#2', stretch=NO, minwidth=0, width=100)
    tree.column('#3', stretch=NO, minwidth=0, width=50)
    tree.column('#3', stretch=NO, minwidth=0, width=100)
    tree.bind('<ButtonRelease-1>', selectItem)
    tree.pack()
    populateView_members(tree,id_)
    root.mainloop()
    main_GUI(id_)



def populateView(tree):
    tree.delete(*tree.get_children())
    fetch = datum().get_clubList()
    for data in fetch:
        tree.insert('', 'end', values=(data["clubName"], data["owner"], data["area"],data["content"]))


def populateView_joined(tree,id_):
    tree.delete(*tree.get_children())
    fetch = datum().get_clubList_joined(id_)
    for data in fetch:
        tree.insert('', 'end', values=(data["clubName"], data["owner"], data["area"],data["content"]))


def populateView_members(tree,id_):
    tree.delete(*tree.get_children())
    fetch = datum().get_members_joined(id_)
    if fetch == False:
        new_message= Tk()
        new_message.withdraw()
        mb.showinfo("Message", "당신은 모임장이 아닙니다.")
        new_message.destroy()
    else:
        for data in fetch:
            tree.insert('', 'end', values=(data["name"], data["gender"], data["area"],data["contact"]))


def populateView_user(tree,id_):
    tree.delete(*tree.get_children())
    fetch = [datum().get_user(id_)]
    for data in fetch:
        tree.insert('', 'end', values=(data["name"], data["gender"], data["area"],data["contact"]))


def populate_area(tree,area_):
    tree.delete(*tree.get_children())
    fetch = datum().get_Areas(area_)
    print(fetch)
    for data in fetch:
        tree.insert('', 'end', values=(data["clubName"], data["owner"], data["area"],data["content"]))



def populate_club(tree,clubName_):
    tree.delete(*tree.get_children())
    fetch = datum().get_clubs(clubName_)
    print(fetch)
    for data in fetch:
        tree.insert('', 'end', values=(data["clubName"], data["owner"], data["area"],data["content"]))


def switch_frame(frame):
    frame.tkraise()


def del_club(id_):
    new_frame = Tk()
    new_frame.withdraw()
    result = datum().delete_club(id_)
    if result == 2:
        mb.showinfo("Message", "커뮤니티가 '삭제'되었습니다.")
    elif result ==3:
        mb.showinfo("Message", "남아있는 멤버가 있을 시, 삭제가 불가능 합니다.")
    else:
        mb.showinfo("Message", "소유한 커뮤니티가 없습니다.")
    new_frame.destroy()


def join_club_message(result):
    new_message= Tk()
    new_message.withdraw()
    if result == True:
        mb.showinfo("Message", "커뮤니티에 가입되었습니다.")
    else:
        mb.showinfo("Message", "이미 가입한 커뮤니티 입니다.")
    new_message.destroy()
 
def leave_club_message(result):
    new_message= Tk()
    new_message.withdraw()
    if result == True:
        mb.showinfo("Message", "정상적으로 '탈퇴'되었습니다.")
    else:
        mb.showinfo("Message", "가입되지 않았거나 모임장은 탈퇴할 수 없습니다.")
    new_message.destroy()


def register_club(values):
    new_frame = Tk()
    new_frame.withdraw()
    id_ = values[0]
    clubName = values[1]
    content = values[2]
    area = values[3]
    result = datum().add_club(id_, clubName, content, area)
    if result == 2:
        mb.showinfo("Message", "정상적으로 등록되었습니다.")
    elif result == 0:
        mb.showinfo("Message", "이미 등록된 커뮤니티입니다.")
    else:
        mb.showinfo("Message", "이미 소유한 커뮤니티가 있습니다.")
    new_frame.destroy()

def updating_club(values):
    print('updating...')
    id_ = values[0]
    content= values[1]
    area = values[2]
    datum().update_club(id_, content, area)
    return None

def updating_user(values):
    print('updating...')
    id_ = values[0]
    contact = values[1]
    gender= values[2]
    area = values[3]
    datum().update_user(id_, contact, gender,area)
    return None

def closed_(window):
    window.destroy()



def register_window(id_):
    new_frame = Tk()
    screen_width = new_frame.winfo_screenwidth()
    screen_height = new_frame.winfo_screenheight()
    x = (screen_width/2) - (700/2)
    y = (screen_height/2) - (350/2)
    new_frame.title("")
    new_frame.geometry('700x370+%d+%d'%(x,y-150))
    new_frame.configure(bg="white") 


    title = Label(new_frame,bg="white",fg='red', text="| 커뮤니티 생성 |",width=20,font=("bold", 20))
    title.place(x=0,y=23)

    fullname = Label(new_frame , bg="white",fg='black',text="* 커뮤니티 이름 : ",width=20,font=("bold", 10))
    fullname.place(x=30,y=100)
    clubname = StringVar(new_frame)
    name_entry = Entry(new_frame ,textvariable=clubname)
    name_entry.place(x=180,y=100)

    content = Label(new_frame ,bg="white",fg='black', text="* 한줄소개 :",width=20,font=("bold", 10))
    content.place(x=10,y=140)
    myContent =StringVar(new_frame )
    content_entry = Entry(new_frame ,textvariable=myContent, width = 50 )
    content_entry.place(x=180,y=140)

    area = Label(new_frame ,bg="white",fg='black', text="* 모임지역 :",width=20,font=("bold", 10))
    area.place(x=10,y=180)

    list1 = ['서울','인천','경기','강원','충남','충북','전북','전남','경북','경남','제주']
    c=StringVar(new_frame)
    droplist=OptionMenu(new_frame, c, *list1)
    droplist.config(width=25)
    c.set('어디든지') 
    droplist.place(x=178,y=180)
    
    Button(new_frame , text='등록',width=20,bg='brown',fg='white', command=lambda:closed_(new_frame)).place(x=260,y=260)
    #Button(new_frame , text='종료',width=20,bg='brown',fg='white', command=lambda:closed_(new_frame)).place(x=420,y=260)
    new_frame.mainloop()
    values = (id_, clubname.get(), myContent.get(),  c.get())
    register_club(values)
    main_GUI(id_)
    

def check_ownership(id_,func):
    ownership = datum().get_clubName(id_)
    if ownership == None:
        new_frame = Tk()
        new_frame.withdraw()
        mb.showinfo("Message", "당신은 모임장이 아닙니다.")
        new_frame.destroy()
        main_GUI(id_)
    else:
        func(id_)


def moveto_register(root,id_):
    root.destroy()
    register_window(id_)

def moveto_update(root,id_):
    root.destroy()
    check_ownership(id_,update_window)

def moveto_user_update(root,id_):
    root.destroy()
    update_window_user(id_)

def moveto_members(root,id_):
    root.destroy()
    check_ownership(id_,view_members)

def moveto_users(root,id_):
    root.destroy()
    view_users(id_)

def moveto_viewArea(root,id_):
    root.destroy()
    search_area_window(id_)


def moveto_viewClub(root,id_):
    root.destroy()
    search_club_window(id_)


def del_club(id_):
    new_frame = Tk()
    new_frame.withdraw()
    result = datum().delete_club(id_)
    if result == 2:
        mb.showinfo("Message", "커뮤니티가 '삭제'되었습니다.")
    elif result ==3:
        mb.showinfo("Message", "남아있는 멤버가 있을 시, 삭제가 불가능 합니다.")
    else:
        mb.showinfo("Message", "소유한 커뮤니티가 없습니다.")
    new_frame.destroy()


def update_window_user(id_):
    user_name = datum().get_userName(id_)
    id_ = id_
    while True:
        root = Tk()
        root.geometry('500x500')
        root.title(":: 정보수정 ::")
        root.configure(bg='white')
        title = Label(root,bg="white",fg='red', text="| 내 정보 |",width=20,font=("bold", 20))
        title.place(x=80,y=53)

        fullname = Label(root, bg="white",fg='black',text="* 이  름 :",width=20,font=("bold", 10))
        fullname.place(x=100,y=130)
        myname = StringVar(root)
        myname.set(user_name)
        name_entry = Entry(root,textvariable=myname, state='disabled')
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
        
        if ACTION_().check_contact(myContact.get()) == True:
            values=(id_, myContact.get(),var.get(), c.get())
            updating_user(values)
            break  
        else:
            wrong_contact()   
    main_GUI(id_)

def update_window(id_):
    content_ = datum().get_Content(id_)
    new_frame = Tk()
    screen_width = new_frame.winfo_screenwidth()
    screen_height = new_frame.winfo_screenheight()
    x = (screen_width/2) - (500/2)
    y = (screen_height/2) - (250/2)
    new_frame.title("")
    new_frame.geometry('500x250+%d+%d'%(x,y-150))
    new_frame.configure(bg="white") 
    title = Label(new_frame,bg="white",fg='red', text="커뮤니티 정보" ,width=20,font=("bold", 20))
    title.place(x=0,y=23)
    content = Label(new_frame ,bg="white",fg='black', text="* 공지사항 :",width=20,font=("bold", 10))
    content.place(x=10,y=80)
    myContent =StringVar(new_frame )
    myContent.set(content_)
    content_entry = Entry(new_frame ,textvariable=myContent, width = 30 )
    content_entry.place(x=180,y=80)

    area = Label(new_frame ,bg="white",fg='black', text="* 모임지역 :",width=20,font=("bold", 10))
    area.place(x=10,y=120)

    list1 = ['서울','인천','경기','강원','충남','충북','전북','전남','경북','경남','제주']
    c=StringVar(new_frame)
    c.set("어디든지") 
    droplist=OptionMenu(new_frame, c, *list1)
    droplist.config(width=25)
    droplist.place(x=178,y=120)
    Button(new_frame , text='수정하기',width=20,bg='brown',fg='white', command=lambda:closed_(new_frame)).place(x=260,y=200)
    new_frame.mainloop()
    values = (id_, myContent.get(),  c.get())
    updating_club(values)
    main_GUI(id_)


def view_joined_communities(id_):
    global tree
    root = Tk()
    root.title("커뮤니티 목록보기")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = 730
    height = 320
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
    root.resizable(0, 0)
    space=Frame(root, width=700, height=15)
    space.pack(side=TOP,anchor='center')
    Body = Frame(root, width=650, height=300, bd=8)
    Body.pack(side=LEFT)
    Button_Group=Frame(root, width=700, height=200)
    Button_Group.pack(side=LEFT,anchor='nw')
    Buttons = Frame(Button_Group, width=200, height=100)
    Buttons.pack(side=BOTTOM,anchor='center')
    btn_register2 = Button(Buttons, width=15, text="탈퇴하기",command=lambda:leaving_club(id_, selected_club))
    btn_register2.pack(ipadx=3,ipady=3,anchor='s')
    btn_register3 = Button(Buttons, width=15, text="나가기",command=lambda:root.destroy())
    btn_register3.pack(ipadx=3,ipady=3,anchor='s')
    scrollbary = Scrollbar(Body, orient=VERTICAL)
    scrollbarx = Scrollbar(Body, orient=HORIZONTAL)
    tree = ttk.Treeview(Body, columns=("clubName", "own","area", "content"), selectmode="extended", height=300, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('clubName', text="커뮤니티", anchor=W)
    tree.heading('own', text="모임장", anchor=W)
    tree.heading('area', text="모임지역", anchor=W)
    tree.heading('content', text="한줄공지", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=150)
    tree.column('#2', stretch=NO, minwidth=0, width=100)
    tree.column('#3', stretch=NO, minwidth=0, width=50)
    tree.column('#3', stretch=NO, minwidth=0, width=100)
    tree.bind('<ButtonRelease-1>', selectItem)
    tree.pack()
    populateView_joined(tree,id_)
    root.mainloop()


def notbuilt_message():
    new_frame = Tk()
    new_frame.withdraw()
    mb.showinfo("Message", "게시판 기능은 아직입니다 ㅠㅠ")
    new_frame.destroy()


def log_out(root):
    global run
    root.destroy()
    run = 1
    return run

def exiting(root):
    global run
    root.destroy()
    run = 2
    return run

def main_GUI(id_):
    root = Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (700/2)
    y = (screen_height/2) - (350/2)
    root.geometry('700x350+%d+%d'%(x,y-150))
    root.title(':: Traveling Community Manager ::') 
    root.protocol("WM_DELETE_WINDOW", lambda:quit())
    background_image = PhotoImage(file=r'./img/mainpage.png') # check image_location and file name 
    background_label = Label(root,background='white',image=background_image)
    background_label.place(relwidth=1,relheight=1)  
    # Creating Menubar 
    menubar = Menu(root) 
    # Adding Account Menu 
    account = Menu(menubar, tearoff = 0) 
    menubar.add_cascade(label ='메인메뉴', menu = account) 
    account.add_command(label ='내정보보기', command = lambda:moveto_users(root,id_))
    account.add_separator() 
    account.add_command(label ='로그아웃', command = lambda:log_out(root))
    account.add_command(label ='종료하기', command = lambda:exiting(root))
    
    # Adding Menu and commands 
    club = Menu(menubar, tearoff = 0) 
    menubar.add_cascade(label ='커뮤니티', menu = club) 
    club.add_command(label ='만들기', command = lambda: moveto_register(root,id_)) 
    club.add_command(label ='지우기', command = lambda: del_club(id_)) 
    club.add_separator() 
    club.add_command(label ='내용수정', command = lambda: moveto_update(root,id_))
    club.add_command(label ='멤버정보', command = lambda:moveto_members(root,id_))
    club.add_separator() 
    club.add_command(label ='게시판생성', command = lambda:notbuilt_message())

    # Adding Edit Menu and commands 
    view = Menu(menubar, tearoff = 0) 
    menubar.add_cascade(label ='목록보기', menu = view) 
    view.add_command(label ='모든 커뮤니티', command = lambda:view_allcommunities(id_))
    view.add_command(label ='가입한 커뮤니티', command = lambda:view_joined_communities(id_)) 
  
    # Adding Search Menu 
    search_ = Menu(menubar, tearoff = 0) 
    menubar.add_cascade(label ='찾아보기', menu = search_) 
    search_.add_command(label ='커뮤니티명', command = lambda:moveto_viewClub(root,id_)) 
    search_.add_command(label ='활동지역', command = lambda:moveto_viewArea(root,id_)) 
   


    # Adding Help Menu 
    help_ = Menu(menubar, tearoff = 0) 
    menubar.add_cascade(label ='도움말', menu = help_) 
    help_.add_command(label ='github', command = lambda:openweb()) 

    
    # display Menu 
    root.config(menu = menubar,bg='white') 

    root.mainloop() 
    # exception 
    try:
        return run 
    except NameError:
        pass
  

#main_GUI("brcha")