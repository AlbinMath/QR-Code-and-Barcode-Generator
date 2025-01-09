from tkinter import *  
from tkinter import messagebox, filedialog  
import os  
import qrcode  
from barcode import Code128 
from barcode.writer import ImageWriter 
 
win = Tk()
win.title('QR Code and Barcode Generator')
win.geometry('700x850') 
win.config(bg='DarkTurquoise')

def browse_directory():
    folder_selected = filedialog.askdirectory() 
    if folder_selected:
        loc.delete(0, END) 
        loc.insert(0, folder_selected)
          
def clear_fields():
    text.delete(0, END)
    loc.delete(0, END)
    name.delete(0, END)
    size.delete(0, END)
    
def generateCode():
    try:
        folder_path = loc.get().strip()
        file_name = name.get().strip()
        if not folder_path or not file_name: 
            raise ValueError("Both the location and filename are required.")
        fileDir = os.path.join(folder_path, file_name + ".png")
        if code_type.get() == "QR Code":
            qr = qrcode.QRCode(version=1, box_size=int(size.get()) if size.get().isdigit() else 10, border=5 )
            qr.add_data(text.get())
            qr.make(fit=True) 
            img = qr.make_image(fill_color="black", back_color="white")
            img.save(fileDir)
            messagebox.showinfo("QR Code Generator", f"QR Code saved successfully at {fileDir}!") 
        elif code_type.get() == "Barcode": 
            code = Code128(text.get(), writer=ImageWriter()) 
            code.save(fileDir)
            messagebox.showinfo("Barcode Generator", f"Barcode saved successfully at {fileDir}!") 
    except Exception as e:
        messagebox.showerror("Error", str(e))
        
headingFrame = Frame(win, bg="azure", bd=5)
headingFrame.place(relx=0.15, rely=0.03, relwidth=0.7, relheight=0.1)
headingLabel = Label(headingFrame, text="Generate QR Code or Barcode", bg='azure', font=('Times', 20, 'bold'))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
code_type = StringVar()
code_type.set("")

Frame1 = Frame(win, bg="DarkTurquoise") 
Frame1.place(relx=0.1, rely=0.15, relwidth=0.8, relheight=0.1)
label1 = Label(Frame1, text="Choose code Type:", bg="DarkTurquoise", fg='azure', font=('FiraMono', 14, 'bold'))
label1.place(relx=0.05, rely=0.2, relheight=0.6)
barcode_option = OptionMenu(Frame1, code_type, "QR Code", "Barcode")
barcode_option.config(font=('FiraMono', 12)) 
barcode_option.place(relx=0.6, rely=0.2, relwidth=0.35, relheight=0.6) 

Frame2 = Frame(win, bg="DarkTurquoise") 
Frame2.place(relx=0.1, rely=0.27, relwidth=0.8, relheight=0.15)
label2 = Label(Frame2, text="Enter the text/URL:", bg="DarkTurquoise", fg='azure', font=('FiraMono', 14, 'bold'))
label2.place(relx=0.05, rely=0.15, relheight=0.3)
text = Entry(Frame2, font=('FiraMono', 14))
text.place(relx=0.05, rely=0.5, relwidth=0.9, relheight=0.4)

Frame3 = Frame(win, bg="DarkTurquoise")
Frame3.place(relx=0.1, rely=0.45, relwidth=0.8, relheight=0.15)
label3 = Label(Frame3, text="Select location to save:", bg="DarkTurquoise", fg='azure', font=('FiraMono', 14, 'bold'))
label3.place(relx=0.05, rely=0.15, relheight=0.3)
loc = Entry(Frame3, font=('FiraMono', 14))
loc.place(relx=0.05, rely=0.5, relwidth=0.7, relheight=0.4)

browseButton = Button(Frame3, text="Browse", command=browse_directory, font=('FiraMono', 12))
browseButton.place(relx=0.78, rely=0.5, relwidth=0.15, relheight=0.4)

Frame4 = Frame(win, bg="DarkTurquoise")
Frame4.place(relx=0.1, rely=0.62, relwidth=0.8, relheight=0.12)
label4 = Label(Frame4, text="Enter the name of the file:", bg="DarkTurquoise", fg='azure', font=('FiraMono', 14, 'bold'))
label4.place(relx=0.05, rely=0.2, relheight=0.3)
name = Entry(Frame4, font=('FiraMono', 14))
name.place(relx=0.05, rely=0.6, relwidth=0.9, relheight=0.4)

Frame5 = Frame(win, bg="DarkTurquoise")
Frame5.place(relx=0.1, rely=0.75, relwidth=0.8, relheight=0.12)
label5 = Label(Frame5, text="Enter the size (1 to 40):", bg="DarkTurquoise", fg='azure', font=('FiraMono', 14, 'bold'))
label5.place(relx=0.05, rely=0.2, relheight=0.3)
size = Entry(Frame5, font=('FiraMono', 14))
size.place(relx=0.05, rely=0.6, relwidth=0.9, relheight=0.4)

buttonGenerate = Button(win, text="Generate", font=('FiraMono', 15), command=generateCode)
buttonGenerate.place(relx=0.2, rely=0.9, relwidth=0.25, relheight=0.05)

buttonClear = Button(win, text="Clear All", font=('FiraMono', 15), command=clear_fields)
buttonClear.place(relx=0.55, rely=0.9, relwidth=0.25, relheight=0.05)

win.mainloop() 