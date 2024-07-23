import csv
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from w9_base_gui import BaseGUI
from w9_item import Item

class StoreGUI(BaseGUI):
    def __init__(self):
        super().__init__("Sport Store", "450x300")
        self.__items = []
    
    # Override _create_widgets method to create widgets for the store
    def _create_widgets(self):
        self.__create_listbox()
        self.__create_entries()
        self.__create_buttons()

    def __create_listbox(self):
        self.__listbox = Listbox(self._window, width=20, height=10, 
                                selectmode="SINGLE", exportselection=False)
        self.__listbox.grid(row=0, column=0, columnspan=2, rowspan=4, padx=5, pady=5)
        self.__listbox.bind("<<ListboxSelect>>", self.__on_select)
    
    def __on_select(self, event):
        # get selected index
        seleted_index = self.__listbox.curselection()[0]
        # get the selected item
        item = self.__items[seleted_index]
        # display the item's information
        self.__update_entry(self.__txt_id, item.item_id)
        self.__update_entry(self.__txt_name, item.name)
        self.__update_entry(self.__txt_brand, item.brand)
        self.__update_entry(self.__txt_price, item.price)
    
    def __update_entry(self, entry, value):
        entry.delete(0, END)
        entry.insert(0, value)

    def __create_entries(self):
        lbl_id = Label(self._window, text="ID:")
        lbl_id.grid(row=0, column=2, padx=5, pady=5)
        self.__txt_id = Entry(self._window)
        self.__txt_id.grid(row=0, column=3, padx=5, pady=5, columnspan=3)

        lbl_name = Label(self._window, text="Name:")
        lbl_name.grid(row=1, column=2, padx=5, pady=5)
        self.__txt_name = Entry(self._window)
        self.__txt_name.grid(row=1, column=3, padx=5, pady=5, columnspan=3)

        lbl_brand = Label(self._window, text="Brand:")
        lbl_brand.grid(row=2, column=2, padx=5, pady=5)
        self.__txt_brand = Entry(self._window)
        self.__txt_brand.grid(row=2, column=3, padx=5, pady=5, columnspan=3)

        lbl_price = Label(self._window, text="Price:")
        lbl_price.grid(row=3, column=2, padx=5, pady=5)
        self.__txt_price = Entry(self._window)
        self.__txt_price.grid(row=3, column=3, padx=5, pady=5, columnspan=3)

    def __create_buttons(self):
        self.__btn_load = Button(self._window, text="Load", command=self.__load)
        self.__btn_load.grid(row=4, column=0, padx=5, pady=5)

        self.__btn_save = Button(self._window, text="Save", command=self.__save)
        self.__btn_save.grid(row=4, column=1, padx=5, pady=5)

        self.__btn_add = Button(self._window, text="Add", command=self.__add)
        self.__btn_add.grid(row=4, column=3, padx=5, pady=5)

        self.__btn_edit = Button(self._window, text="Edit", command=self.__edit)
        self.__btn_edit.grid(row=4, column=4, padx=5, pady=5)

        self.__btn_delete = Button(self._window, text="Delete", command=self.__delete)
        self.__btn_delete.grid(row=4, column=5, padx=5, pady=5)
    
    def __load(self):
        file_name = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
        # clear the listbox
        self.__listbox.delete(0, END)
        # clear the items list
        self.__items.clear()
        # read the file
        with open(file_name, "r") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                item = Item(row[0], row[1], row[2], row[3])
                self.__items.append(item)
                self.__listbox.insert(END, item.name)
        messagebox.showinfo("Information", "Items are loaded successfully.")

    def __save(self):
        # open file to save
        file_name = filedialog.asksaveasfilename(filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
        
        with open(file_name, 'w') as f:
            # write header
            f.write('ID,Item Name,Brand,Price\n')
            for item in self.__items:
                f.write(f'{item.item_id},{item.name},{item.brand},{item.price}\n')

        messagebox.showinfo("Information", "Items are saved successfully.")

    def __add(self):
        # get the item information from the entries
        item_id = int(self.__txt_id.get())  # should validate item_id
        name = self.__txt_name.get()
        brand = self.__txt_brand.get()
        price = float(self.__txt_price.get())
        # create item object and add it to the list
        item = Item(item_id, name, brand, price)
        self.__items.append(item)
        # add the item name to the listbox
        self.__listbox.insert(END, item.name)

        messagebox.showinfo("Information", "Item is added successfully.")

    def __edit(self):
        # get the item information from the entries
        name = self.__txt_name.get()
        brand = self.__txt_brand.get()
        price = float(self.__txt_price.get())

        # get selected index
        selected_index = self.__listbox.curselection()[0]
        # get the selected item
        item = self.__items[selected_index]
        # update the item's information
        item.name = name
        item.brand = brand
        item.price = price
        # update the listbox
        self.__listbox.delete(selected_index)
        self.__listbox.insert(selected_index, item.name)

        messagebox.showinfo("Information", "Item is updated successfully.")

    def __delete(self):
        # get selected index
        selected_index = self.__listbox.curselection()[0]
        # delete the item from the list
        self.__items.pop(selected_index)
        # delete the item from the listbox
        self.__listbox.delete(selected_index)
        # clear the entries
        self.__txt_id.delete(0, END)
        self.__txt_name.delete(0, END)
        self.__txt_brand.delete(0, END)
        self.__txt_price.delete(0, END)

        messagebox.showinfo("Information", "Item is deleted successfully.")

if __name__ == "__main__":
    store_gui = StoreGUI()
    store_gui.run()