from tkinter import *
from tkinter import messagebox,filedialog,ttk
import os


root = Tk()
root.geometry("200x200")
root.resizable(0,0)
root.title("ArviS | MKV To MP4 Converter")

#ARKAPLAN FOTO CANVAS
img = PhotoImage(file="icon.png")
width, height = img.width(), img.height()
canvas = Canvas(root, width=width, height=height)
canvas.place(x=0,y=0)
canvas.create_image((0, 0), image=img, anchor="nw")

def convert():
    mkvfile = filedialog.askopenfilename()
    mkvfilepath = mkvfile.replace("/","\\")
    mp4file = filedialog.asksaveasfilename(initialdir="/",title="Kaydedilecek Dizini Seç Ve Dosyayı Adlandırın (Default Olarak MP4 Kaydedilir)",defaultextension=".mp4")
    #mp4filepath = mp4file.replace("/","\\")
    #exactmp4 = mp4filepath+"\\"+"out.mp4"
    
    os.system(f"ffmpeg -i {mkvfilepath} -codec copy {mp4file}")
    messagebox.showinfo("İşlem Başarılı",f"MKV Dosyası Başarıyla Dönüştürüldü \n {mp4file}")
    


#CONVERT BUTON
ttk.Button(root,text="MP4'e Çevir",command=convert).pack(side=TOP,padx=50,pady=50)










root.mainloop()
