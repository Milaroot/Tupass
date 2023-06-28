from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showinfo
from generator import *
from os import chdir


#This class is used to handle various functions of buttons
class butten_function:
    def __init__(self) -> None:
        self.KEYWORDS_ARR = []
        self.COMBINATIONS_ARR = []
        self.OPT_ARR = [] 
        self.SAVE_PATH = ""
        self.UPPER_BOOL = FALSE
    
    def set_upper_state(self) -> None:
        self.UPPER_BOOL = not(self.UPPER_BOOL) 
    
    def choose_directory(self) -> None:
        self.SAVE_PATH = askdirectory()
        
    def result_print(self) -> None:
        chdir(self.SAVE_PATH)
        with open("result.txt", "w") as ofile:
            ofile.write("========================================================\n")
            ofile.write(f"Keywords: {self.KEYWORDS_ARR}\n")
            ofile.write("========================================================\n\n")
            
            for opt in self.OPT_ARR:
                opt = "".join(list(opt))
                ofile.write(opt + "\n")
        showinfo(title="Tupass", message="success")    

    def start_button(self) -> None:
        self.KEYWORDS_ARR = keyword_text.get('1.0', END).split()
        
        if self.UPPER_BOOL == 1:
            self.KEYWORDS_ARR = upper_keywords(self.KEYWORDS_ARR)
        
        self.COMBINATIONS_ARR = combinations_keywords(self.KEYWORDS_ARR)
        self.OPT_ARR = permutations_keywords(self.COMBINATIONS_ARR)
        
        #save result
        self.result_print()
        
        
        
#used to generate the GUI 
if __name__ == "__main__":
    
    window = Tk() 
    window.title("Tupass 2.0")
    window.minsize(width=500, height=500)
    window.resizable(width=False, height=False)
    main_bf = butten_function()



    main_title = Label(text="Tupass",
                    font=("Arial", 21, "bold"),
                    padx=5,
                    pady=5,
                    fg="black")
    main_title.pack()

    title_version = Label(text="version 2.0",
                        font=("Arial", 8, "bold"),
                        padx=5,
                        pady=2,
                        fg="black")
    title_version.pack()

    keyword_title = Label(text="Keywords",
                        font=("Arial", 14, "bold"),
                        padx=5,
                        pady=10,
                        fg="black")
    keyword_title.pack()

    keyword_text = Text(height=10,
                        width=30,
                        font=("Arial", 10 ),
                        bg="gray",
                        fg="black",
                        state=NORMAL)
    keyword_text.insert(END, "keyword 1...\nkeyword 2...")
    keyword_text.pack()

    setting_title = Label(text="Settings",
                        font=("Arial", 14, "bold"),
                        padx=5,
                        pady=10,
                        fg="black")
    setting_title.pack()

    ask_dir_button = Button(text="Choose Directory",
                        font=("Arial", 10),
                        padx=5,
                        pady=5,
                        bg="black",
                        fg="gray",
                        command=main_bf.choose_directory)
    ask_dir_button.pack()
    
    upper_butten = Checkbutton(text="Add all uppercase and first letter capitalized",
                               pady=10,
                               command=main_bf.set_upper_state)
    upper_butten.pack()

    start_button = Button(text="Generate",
                        font=("Arial", 14),
                        padx=5,
                        pady=10,
                        bg="black",
                        fg="gray",
                        command=main_bf.start_button)
    start_button.pack()



    window.iconbitmap("./icon/main.ico")
    window.mainloop()

