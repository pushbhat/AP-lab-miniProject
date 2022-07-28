import tkinter as tk
from tkinter import PhotoImage, StringVar, Tk, ttk
from tkinter import filedialog as fd
from tkinter.constants import HORIZONTAL
from tkinter.messagebox import showinfo
from tkinter.messagebox import showerror
from tkinter.ttk import *
from PIL import ImageTk, Image
import time
#backend
from moviepy.editor import VideoFileClip
from moviepy.editor import AudioFileClip

def vidtovid(file,toformat):
    vid=VideoFileClip(file)
    v=vid.size  
    vid.write_videofile(file[:-3]+toformat)
    print("done")
def vidtoaud(file,toformat):
    vid=VideoFileClip(file)
   # if vid.audio==True:
    aud=vid.audio
    aud.write_audiofile(file[:-3]+toformat)
  #  else: print("no  audio")
def audtoaud(file,toformat):
    aud=AudioFileClip(file)
    aud.write_audiofile(file[:-3]+toformat)
    print("done")
    
    
def convertable(fr,to):
    #vid to vid
    if fr in["mp4","mkv","wmv","avi"] and to in ["mp4","mkv","wmv","avi"]:
        return "vv"
    #vid to aud
    if fr in["mp4","mkv","wmv","avi"] and to in ["mp3"]:
        return "va"
    #aud to aud
    if fr in["mp3","aac","wmv"]and to in ["mp3"]:
        return "aa"
    
def printhis(item):
     print(type(item))  
def convert(file,to):
    toform=to
    curform=file.split(".")[1]
    conversion=convertable(curform,toform)
    print("toform"+toform)
    print("curform"+curform)

    print(conversion)
    if conversion=="av":
        print("non convertable")
    else:
          print("converting "+file)
          if conversion=="vv":
              vidtovid(file,to)
          elif conversion=="va":
              vidtoaud(file,to)
          else:
              audtoaud(file,to)
              
              
#-----gui--------          
# create the root window
root = Tk()
root.title('Tkinter File Dialog')
root.resizable(True, True)
root.geometry("500x500")
root.config(bg="grey")



#r"C:\Users\nrdc2\Downloads\
    #r"C:\Users\nrdc2\Downloads\
imgname = ImageTk.PhotoImage(Image.open("converter.jpg" ))
imgname1= ImageTk.PhotoImage(Image.open("re.jpg"))

my_label=Label(root, image=imgname)
my_label.grid(row=0,column=0,padx='10', pady='50',rowspan='5')
my_label1=Label(root, image=imgname1)
my_label1.place(x=10,y=0,relwidth=1,relheight=1)
my_label1.grid(row=0,column=5,padx='50', pady='50',rowspan='5')

def Convert():
     for i in root.filename:
     
       fr=i.split(("/"))[-1].split('.')[1]
       if fr  in["mp3","aac"] and clicked.get() in ["mp4","mkv","wmv","avi"]:
           
           showerror(
            title='error',
            message="cannot convert from audio to video"
            )
           continue
       
       tlabel=tk.Label(root,text="converting "+i.split(("/"))[-1]+" to "+clicked.get())
       tlabel.grid(row='6',column=2)
       tlabel.config(font=("Courier", 10))
       root.update_idletasks()
           
       convert(i,clicked.get())
       dlabel=tk.Label(root,text="last task: converted "+i.split(("/"))[-1]+" to "+clicked.get())
       dlabel.grid(row='8',column=2,pady=5)
       dlabel.config(font=("Courier", 20))
      
       root.update_idletasks()
       
#selecting files       
def select_files():
    global files
    filetypes = (
        ('wmv files', '*.wmv'),
        ('AAC files', '*.aac'),
        ('MKV files', '*.mkv'),
        ('All files', '*.*')
    )

    root.filename = fd.askopenfilenames(
        title='Open files',
        initialdir='E:\sem 5\AP_LAB\mini_project',
        filetypes=filetypes)
    printhis(root.filename)
    files=""
    for i in root.filename:
        files=files+i+"\n"
    slabel=tk.Label(root,text="setected files\n "+files).grid(row='4',column='2')

#buttons in root
# open button
open_button = ttk.Button(
    root,
    text='Select Files',
    command=select_files,
    width='50'
)
convert_button = ttk.Button(
    root,
    text='Convert',
    command=Convert,
    width='50'
)
#slabel=tk.Label(root,text=str(files)).pack()
options = [
	"mp4","mp3"
]	
clicked = tk.StringVar()
clicked.set(options[0])
drop =tk.OptionMenu(root, clicked, *options)

#put on root
open_button.grid(row='0',column='2',pady='50')
drop.grid(row='3',column='2',pady='50')
convert_button.grid(row='5',column='2',pady='50')

root.mainloop()
