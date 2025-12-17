def openfile():
    #filedialog returns string
    #initialdir sets the initial directory
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\Kaan\\Desktop\\tk\\GUI",
                                          title="Open the file calmly",
                                          filetypes=(("text files","*.txt"),
                                          ("all files","*.*"))) 

    myfile = open(filepath,"r")
    print(myfile.read())
    myfile.close()