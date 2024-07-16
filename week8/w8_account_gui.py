from tkinter import *
from tkinter import filedialog
from w8_account import Account
import csv
from tkinter import messagebox as msb
class AccountGUI:
    def __init__(self):
        self.create_window()
        self.create_widgets()

    def create_window(self):
        self.window = Tk()
        self.window.title("TPBank Account Manager")
        self.window.geometry("500x300")

    def load_accounts(self):
        self.accounts = []
        file_name = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
        
        with open(file_name) as file:
            reader = csv.reader(file)
            # skip the header
            next(reader)
            for row in reader:
                try:
                    acc = Account(row[0], row[1], float(row[2]))
                    self.accounts.append(acc)
                except ValueError as e:
                    msb.showerror("Error", str(e))
                except Exception as e:
                    msb.showerror("Error", 'Unknown error')
                    return
        # insert the account names into the listbox
        for acc in self.accounts:
            self.lst_accounts.insert(END, acc.name)

    def list_accounts_selected(self, event):
        # get the index of the selected item
        index = self.lst_accounts.curselection()[0]
        # get the account object
        acc = self.accounts[index]
        # display the account details
        self.display_text(self.txt_id, acc.id)
        self.display_text(self.txt_name, acc.name)
        self.display_text(self.txt_balance, acc.balance)
    
    def display_text(self, widget, value):
        widget.config(state=NORMAL)
        widget.delete(0, END)
        widget.insert(0, value)
        widget.config(state='readonly')

    def search_accounts(self, event):
        name = self.txt_search.get()
        found = False
        for i in range(len(self.accounts)):
            if name.lower() in self.accounts[i].name.lower():
                # clear the current selection of listbox
                self.lst_accounts.selection_clear(0, END)
                # select the item at index i
                self.lst_accounts.select_set(i)
                self.lst_accounts.activate(i)
                # call the list_accounts_selected method to display the account details
                self.list_accounts_selected(None)
                found = True
                break
        if not found:
            msb.showinfo("Search", "No account found")

    def create_widgets(self):
        self.lbl_bank = Label(self.window, text="TPBank Account Manager")
        self.lbl_bank.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

        self.btn_load = Button(self.window, text="Load accounts", command=self.load_accounts)
        self.btn_load.grid(row=1, column=0, sticky=W, padx=5, pady=5)

        self.lst_accounts = Listbox(self.window, width=20, height=10, selectmode=SINGLE, exportselection=False)
        self.lst_accounts.grid(row=2, column=0, rowspan=4, sticky=W, padx=5, pady=5)
        # bind the listbox to the event handler list_accounts_selected
        self.lst_accounts.bind("<<ListboxSelect>>", self.list_accounts_selected)

        self.lbl_search = Label(self.window, text="Search:")
        self.lbl_search.grid(row=1, column=1, sticky=E, padx=5, pady=5)

        self.txt_search = Entry(self.window, width=20)
        self.txt_search.grid(row=1, column=2, sticky=W, padx=5, pady=5, columnspan=3)
        self.txt_search.bind("<Return>", self.search_accounts)

        self.lbl_id = Label(self.window, text="ID:")
        self.lbl_id.grid(row=2, column=1, sticky=E, padx=5, pady=5)

        self.txt_id = Entry(self.window, width=20, state="readonly")
        self.txt_id.grid(row=2, column=2, sticky=W, padx=5, pady=5, columnspan=3)

        self.lbl_name = Label(self.window, text="Name:")
        self.lbl_name.grid(row=3, column=1, sticky=E, padx=5, pady=5)

        self.txt_name = Entry(self.window, width=20, state='readonly')
        self.txt_name.grid(row=3, column=2, sticky=W, padx=5, pady=5, columnspan=3)

        self.lbl_balance = Label(self.window, text="Balance:")
        self.lbl_balance.grid(row=4, column=1, sticky=E, padx=5, pady=5)

        self.txt_balance = Entry(self.window, width=20, state='readonly')
        self.txt_balance.grid(row=4, column=2, sticky=W, padx=5, pady=5, columnspan=3)

        self.txt_amount = Entry(self.window, width=8)
        self.txt_amount.grid(row=5, column=2, sticky=W, padx=5, pady=5)

        self.btn_withdraw = Button(self.window, text="-", command=self.withdraw)
        self.btn_withdraw.grid(row=5, column=3, sticky=W, padx=5, pady=5)

        self.btn_deposit = Button(self.window, text="+", command=self.deposit)
        self.btn_deposit.grid(row=5, column=4, sticky=W, padx=5, pady=5)

        self.btn_exit = Button(self.window, text="Exit", command=self.quit)
        self.btn_exit.grid(row=6, column=3, sticky=E, padx=5, pady=5, columnspan=2)

    def deposit(self):
        # get amount from the entry widget
        amount = float(self.txt_amount.get())
        # get selected account
        index = self.lst_accounts.curselection()[0]
        acc = self.accounts[index]
        # deposit the amount
        try:
            acc.deposit(amount)
            # show new balance
            self.display_text(self.txt_balance, acc.balance)
        except ValueError as e:
            msb.showerror("Error", str(e))
        except Exception as e:
            msb.showerror("Error", 'Unknown error')
            return

    def withdraw(self):
        # get amount from the entry widget
        amount = float(self.txt_amount.get())
        # get selected account
        index = self.lst_accounts.curselection()[0]
        acc = self.accounts[index]
        # withdraw the amount
        try:
            acc.withdraw(amount)
            # show new balance
            self.display_text(self.txt_balance, acc.balance)
        except ValueError as e:
            msb.showerror("Error", str(e))
        except Exception as e:
            msb.showerror("Error", 'Unknown error')
            return

    def quit(self):
        exit(0)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    bank = AccountGUI()
    bank.run()