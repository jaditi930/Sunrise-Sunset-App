from main  import get_data_and_format,get_lat_and_long
from tkinter import *

def zipcode_entry():
    clear_frame(f1)
    Label(f1,text="Enter Zipcode:").place(relx=0.4,rely=0.3)
    Entry(f1,textvariable=ZipcodeVal).place(relx=0.4,rely=0.4)
    Button(f1,text="Fetch",command=submit_zipcode,bg="light green")\
    .place(relx=0.4,rely=0.6)

def lat_and_long_entry():
    clear_frame(f1)
    Label(f1,text="Enter latitude:").place(relx=0.4,rely=0.3)
    Entry(f1,textvariable=LatitudeVal).place(relx=0.4,rely=0.4)
    Label(f1,text="Enter longitude:").place(relx=0.4,rely=0.5)
    Entry(f1,textvariable=LongitudeVal).place(relx=0.4,rely=0.6)
    Button(f1,text="Fetch",command=submit_lat_and_long,bg="light green")\
    .place(relx=0.4,rely=0.8)

def clear_frame(frame):
   for widgets in frame.winfo_children():
      widgets.destroy()

def show(data):
    clear_frame(f1)
    option_menu.destroy()
    user_choice.place_forget()
    if len(data)<1:
        Label(f1,text="Invalid Entry !!Please try again",font="Helventica 30 bold")\
        .place(relx=0.2,rely=0.2)
    elif data['status']!='ok':
        Label(f1,text="Sorry,we could n't fetch the data !Please try again!!",font="Helventica 30 bold")\
        .place(relx=0.2,rely=0.2)
    else:
        Label(f1,text=f"Sunrise Time : {data['rise']}",bg="orange",font="Helventica 30 bold")\
            .place(relx=0.2,rely=0.2)
        Label(f1,text=f"Sunset Time : {data['set']}",bg="orange",font="Helventica 30 bold")\
            .place(relx=0.2,rely=0.4)

def submit_zipcode():
    zip=ZipcodeVal.get()
    output=get_lat_and_long(zip)
    show(output)

def submit_lat_and_long():
    la=LatitudeVal.get()
    lo=LongitudeVal.get()
    output=get_data_and_format(la,lo)
    show(output)

def myfunc(e):
    if e==option_list[0]:
        lat_and_long_entry()
    else:
        zipcode_entry()

window=Tk()
window.geometry("644x434")
window.maxsize(644,434)
window.title("Sunrise Sunset App")

f1=Frame()
f1.option_add("*Label.Font", "Helventica 15 bold")
f1.option_add("*Button.Font", "Helventica 15 bold")
f1.option_add("*Entry.Font", "Helventica 10 bold")

text=Label(text="Sunset Sunrise App",bg="yellow",fg="red",font="Helventica 30 bold")
text.pack(fill="x")
user_choice=Label(text="Enter manually:",font="Helventica 15 bold")
user_choice.place(relx=0.2,rely=0.2)
ChoiceVal=StringVar()
ChoiceVal.set("Choose an option")
option_list=["Latitude and Longitude","Zipcode Only"]
option_menu=OptionMenu(window,ChoiceVal,*option_list,command=myfunc)
option_menu.place(relx=0.5,rely=0.2)
f1.pack(fill="both",expand=True)

LatitudeVal=StringVar()
LongitudeVal=StringVar()
ZipcodeVal=StringVar()
window.mainloop()