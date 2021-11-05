import tkinter as tk

commands = {}

def parsetool():
    try:
        fin = open("tool.py","r")
    except:
        print("Tool File Open Error")
        quit()
    finally:
        line = fin.readline()
        while line:
            if "@common.cli.command()" in line:
                line = fin.readline()
                options = []
                while "@click.option" in line:
                    options.append(line.split("\"")[1])
                    line = fin.readline()
                if "def " in line:
                    commands[line.split(" ")[1].split("(")[0]] = options
            line = fin.readline()
        fin.close()
        print (commands)

def submitcommand():
    print("Submit Clicked")

def changeoptions(var, index, mode):
    print("Option Change")
    print(window.getvar(var))

def drawwin():
    parsetool()
    window = tk.Tk()
    window.iconbitmap("icon.ico")
    window.title("Translation Tool EZUI")
    
    topframe = tk.Frame(master=window, width=50).pack(side=tk.TOP)
    frame1 = tk.Frame(master=topframe, width=25).pack(side=tk.LEFT, fill=tk.BOTH)
    label = tk.Label(master = frame1,
        text="Pick an operation and any flags you may want",
        fg="black",
        bg="white",
        height=25
    ).pack(side=tk.LEFT, fill=tk.BOTH)
    frame2 = tk.Frame(master=topframe, width=25).pack(side=tk.LEFT, fill=tk.BOTH)
    v = tk.StringVar()
    x = 0
    optionmenu = tk.OptionMenu(frame2, v, *list(commands)).pack(fill=tk.BOTH)
    bottomframe = tk.Frame(master=window, width=50).pack(side=tk.TOP,fill=tk.BOTH)
    submit = tk.Button(bottomframe,width=50,text="Submit", command=submitcommand).pack(fill=tk.BOTH)
    

    v.trace("w", changeoptions)
    
    window.mainloop()



    
if __name__ == "__main__":
    drawwin()
