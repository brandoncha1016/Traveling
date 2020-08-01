from model import datum
from tkinter import *
from tkinter import ttk as ttk
from PIL import Image, ImageTk  
from tkinter import messagebox as mb
import csv 
import re

class ACTION_:

    def check_contact(self,contact):
        print(contact)
        if contact == "":
            return 2
        else:
            return bool(re.match('(\d{2,3})-(\d{3,4})-(\d{4})', contact))

    def check_ownership(self,id_,func):
        new_frame = Tk()
        new_frame.withdraw()
        ownership = datum().get_clubName(id_)
        if ownership == None:
            mb.showinfo("Message", "당신은 모임장이 아닙니다.")
            new_frame.destroy()
        else:
            func(id_)
            new_frame.destroy()

    def moveto_register(self,root,id_):
        root.destroy()
        view.register_window(id_)

    def moveto_update(self,root,id_):
        root.destroy()
        self.check_ownership(id_,view.update_window)

    def moveto_members(self,root,id_):
        root.destroy()
        self.check_ownership(id_,view.view_members)

        
    def del_club(self,id_):
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

    def return_value(self,root,value):
        print(value)
        root.destroy()
        return value

    def save_contact(self,id_):
        data_list=list()
        fetch = datum().get_members_joined(id_)
        
        for data in fetch:
            data_list.append([data["name"], data["gender"], data["area"],data["contact"]])
        print(data_list)
        with open("member_contact.csv", "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames = ["이름", "성별", "지역","연락처"])
            writer.writeheader()
            writer = csv.writer(f)
            writer.writerows(data_list)
      
    def disable_event(self):
        pass
