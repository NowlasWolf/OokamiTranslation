import tkinter as tk
import os

def parsetool(tn):
    commands = {}
    try:
        fin = open(tn,"r")
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
        return commands


class EZUI:

    def submitcommand(self):
        print("Submit Clicked")
        endstring = ""
        for i, x in enumerate(self.optionselected):
            if x.get() == 1:
                endstring = endstring + " " + self.commands[self.v.get()][i]
        endstring = self.v.get() + endstring
        print("executing: " + endstring)
        os.system("cmd /k tool.exe " + endstring)

    def changeoptions(self,*args):
        self.optionselected = []
        print("Option Changed to " + self.v.get())
        for i in self.optionselects:
            i.destroy()
        self.optionselects = []
        count = 1
        for i in self.commands[self.v.get()]:
            newvar = tk.IntVar()
            newcb = tk.Checkbutton(self.window, text=i, variable=newvar)
            newcb.grid(row=count, column=1)
            self.optionselects.append(newcb)
            self.optionselected.append(newvar)
            count += 1
            
        self.submit.grid(row=count,columnspan=2)
        self.label.grid(row=0, column=0, padx=0, rowspan=(count-1>0 or 1))
    
    def __init__(self,toolname):
        self.window = tk.Tk()
        self.window.iconbitmap("icon.ico")
        self.window.title("Translation Tool EZUI")
        

        self.label = tk.Label(self.window,
        text="Pick an operation and any flags you may want",
        fg="black",
        bg="white",
        width=25,
        height=5,
        wraplength=100,
        justify = tk.CENTER
        )
        self.label.grid(row=0, column=0, padx=0, rowspan=2)
        self.submit = tk.Button(self.window,width=50,text="Submit", command=self.submitcommand)
        self.submit.grid(row=2,columnspan=2)
        
        self.commands = parsetool(toolname)
        self.v = tk.StringVar()
        self.v.set(list(self.commands)[0])
        self.v.trace("w", self.changeoptions)
        self.commandmenu = tk.OptionMenu(self.window, self.v,*list(self.commands)).grid(row=0, column=1)

        self.optionselected = []
        self.optionselects = []
        self.changeoptions()
        
        
        self.window.mainloop()
        
    
    
if __name__ == "__main__":
    thewin = EZUI("tool.py")
