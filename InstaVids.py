import os
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox



#to set the old stored session to session textbox
def getUserSession():
    # file path for a textfile that stores and retreives user's SessionID
    myFilePath = os.getcwd() + "/assets/mySessionID.txt"
    isExist = os.path.exists(myFilePath)

    if isExist:
        fRead = open(myFilePath)
        entrySession.delete(0,END)
        entrySession.insert(0,fRead.readline())
        fRead.close()
    else:
        return




# when url button clicked, show messagebox
def btnURL():
    messagebox.showinfo('Instagram URL', "Paste Here The Reel/IGTV Video URL... Get The Full URL Using The 'Copy Link' Button")

# when session button clicked, show messagebox
def btnSession():
    messagebox.showinfo('Instagram Session ID', "Find The SessionID From The Browser, Login To Your Account First Then Access Inspect(DevTools) -> Application -> Session Storage -> 'SessionID': 'xxxxxxxxxxx-xxxxxx' " )

# when folder button clicked, show gui dialog to select folder and insert folder path to the folder textbox
def btnFolder():
    path = fd.askdirectory()
    print("Folder Selected : ",path)
    entryFolder.delete(0,END)
    entryFolder.insert(0,path)

# when downlaod button clicked
def btnDownload():
    print("Download Started")

    myFilePath = os.getcwd() + "/assets/mySessionID.txt"
    

    # check if user didnt enter any text
    if entrySession.get() == "" or entryFolder.get() == "" or entryURL.get() == "":
        messagebox.showwarning('Warning', 'Textbox is Empty!')
    else:
        # make text file that stores the user's SessionID
        fNew = open(myFilePath,"w")
        fNew.write(entrySession.get())
        fNew.close()  
    




window = Tk() # start GUI window

window.title("InstaVids")

# main canvas
window.geometry("1000x600")
window.configure(bg = "#fcfcfc")
canvas = Canvas(
    window,
    bg = "#fcfcfc",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

# background image and texts
imageAndTexts_img = PhotoImage(file = f"assets/imageandtexts.png")
background = canvas.create_image(
    396.5, 300.0,
    image=imageAndTexts_img)

# the url text box
entryURL_img = PhotoImage(file = f"assets/textbox.png")
entryURL_bg = canvas.create_image(
    681.0, 167.5,
    image = entryURL_img)

entryURL = Entry(
    bd = 0,
    bg = "#f1f5ff",
    highlightthickness = 0)

entryURL.place(
    x = 490.0, y = 137,
    width = 382.0,
    height = 59)

# the url button next to the textbox
urlIcon = PhotoImage(file = f"assets/url.png")
bURL = Button(
    image = urlIcon,
    borderwidth = 0,
    highlightthickness = 0,
    command = btnURL,
    relief = "flat")

bURL.place(
    x = 894, y = 137,
    width = 55,
    height = 61)

# the Folder textbox
entryFolder_img = PhotoImage(file = f"assets/textbox.png")
entryFolder_bg = canvas.create_image(
    681.0, 274.5,
    image = entryFolder_img)

entryFolder = Entry(
    bd = 0,
    bg = "#f1f5ff",
    highlightthickness = 0)

entryFolder.place(
    x = 490.0, y = 244,
    width = 382.0,
    height = 59)

# the Folder button next to the textbox
folderIcon = PhotoImage(file = f"assets/folder.png")
bFolder = Button(
    image = folderIcon,
    borderwidth = 0,
    highlightthickness = 0,
    command = btnFolder,
    relief = "flat")

bFolder.place(
    x = 894, y = 244,
    width = 55,
    height = 61)

# the Session textbox
entrySession_img = PhotoImage(file = f"assets/textbox.png")
entrySession_bg = canvas.create_image(
    681.0, 381.5,
    image = entrySession_img)

entrySession = Entry(
    bd = 0,
    bg = "#f1f5ff",
    highlightthickness = 0)

entrySession.place(
    x = 490.0, y = 351,
    width = 382.0,
    height = 59)

# the Session button next to the textbox
infoIcon = PhotoImage(file = f"assets/info.png")
bSession = Button(
    image = infoIcon,
    borderwidth = 0,
    highlightthickness = 0,
    command = btnSession,
    relief = "flat")

bSession.place(
    x = 894, y = 351,
    width = 55,
    height = 61)


    # call the getUserSession function to set the old session to textbox
getUserSession()

# the download button next at the bottom
downloadIcon = PhotoImage(file = f"assets/download.png")
bDownload = Button(
    image = downloadIcon,
    borderwidth = 0,
    highlightthickness = 0,
    command = btnDownload,
    relief = "flat")

bDownload.place(
    x = 626, y = 452,
    width = 180,
    height = 55)

window.resizable(False, False)
window.mainloop() # END GUI window

