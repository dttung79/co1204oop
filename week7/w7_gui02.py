from tkinter import *

class MacbookStore:
    def __init__(self):
        self.window = self.create_window()
        self.create_widgets()

    def run(self):
        self.window.mainloop()

    
    def create_window(self):
        window = Tk()
        window.geometry("300x300")
        window.title("Macbook Store")
        return window
    
    def create_widgets(self):
        self.lbl_store = Label(self.window, text="Macbook Store")
        self.lbl_store.grid(row=0, column=0)

        self.macbook_price = IntVar()
        self.macbook_price.set(2000)
        self.rd_pro13 = Radiobutton(self.window, text="Macbook Pro 13-inch ($2000)", 
                                    value=2000, variable=self.macbook_price, 
                                    command=self.calculate_price)     
        self.rd_pro13.grid(row=1, column=0)

        self.rd_air13 = Radiobutton(self.window, text="Macbook Air 13-inch ($1500)",
                                    value=1500, variable=self.macbook_price,
                                    command=self.calculate_price)
        self.rd_air13.grid(row=2, column=0, sticky=W)

        self.rd_pro15 = Radiobutton(self.window, text="Macbook Pro 15-inch ($3000)",
                                    value=3000, variable=self.macbook_price,
                                    command=self.calculate_price)
        
        self.rd_pro15.grid(row=3, column=0, sticky=W)

        self.lbl_option = Label(self.window, text="Choose an option")
        self.lbl_option.grid(row=4, column=0, sticky=W)

        self.cover_var = BooleanVar()
        self.chk_cover = Checkbutton(self.window, text="Cover ($10)", variable=self.cover_var,
                                     command=self.calculate_price)
        self.chk_cover.grid(row=5, column=0, sticky=W)

        self.case_var = BooleanVar()
        self.chk_case = Checkbutton(self.window, text="Briefcase ($25)", variable=self.case_var,
                                    command=self.calculate_price)
        self.chk_case.grid(row=6, column=0, sticky=W)

        self.lbl_price = Label(self.window, text="Price:")
        self.lbl_price.grid(row=7, column=0, sticky=W)

        self.price_var = IntVar()
        self.price_var.set(2000)
        self.txt_price = Entry(self.window, width=20, textvariable=self.price_var)
        self.txt_price.grid(row=8, column=0, sticky=W)

    def calculate_price(self):
        price = self.macbook_price.get()    # price is set to the value of the selected macbook

        if self.cover_var.get():    # if user selected the cover, add $10 to the price
            price += 10
        if self.case_var.get():     # if user selected the case, add $25 to the price
            price += 25
        # set the price to the price_var, which will update the text in the Entry widget
        self.price_var.set(price)

if __name__ == '__main__':
    store = MacbookStore()
    store.run()