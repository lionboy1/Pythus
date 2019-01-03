from tkinter import *
import backend # import the backend script to work with the front end script


def view_command():
    list1.delete(0, END)#This will prevent duplicate data when the button is pressed multiple times. On a new press, all data will be deleted from index 0 to the END of the list before repopulating the view.
    for row in backend.view():
        list1.insert(END, row)#new entries are appended at the end of the list. Rows are returned from the backend.py script

def search_command():
    list1.delete(0,END)
    for row in backend.search(client_text.get(), email_text.get(), phone_text.get(), address_text.get()):# Grab data from entry boxes in the GUI this time since this is where data is displayed
        list1.insert(END, row)

def add_command():
    backend.insert(client_text.get(), email_text.get(), phone_text.get(), address_text.get())
    list1.delete(0, END)
    list1.insert(END, (client_text.get(), email_text.get(), phone_text.get(), address_text.get()))#inseert as a tuple to have entries return on a single line.

def delete_command(id):
    backend.delete()

#Event handler for listbox selection. event is a parameter that gets called when the listbox is selected, which executed the get_selected_row function.
def get_selected_row(event):
    try:
        global selected_tuple# Global variable to be accessed by other functions (i.e delete() and update())
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        e1.delete(0, END)# clear prevously populated data from index 0 to END before populating box with new selected data
        e1.insert(END,selected_tuple[1])#Client
        e2.delete(0, END)
        e2.insert(END,selected_tuple[2])#Author
        e3.delete(0, END)
        e3.insert(END,selected_tuple[3])#Phone
        e4.delete(0, END)
        e4.insert(END,selected_tuple[4])#Address
    except IndexError:
        pass



def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0], client_text.get(), email_text.get(), phone_text.get(), address_text.get())#Index number doesn't get deleted/updated but everything else can be.







window = Tk()
window.wm_title("Client Database")

l1 = Label(window, text="Client:")# Labels for entry boxes
l1.grid(row=0, column=0)

l2 = Label(window, text="Email:")
l2.grid(row=0, column=2)

l3 = Label(window, text="Phone:")
l3.grid(row=1, column=0)

l4 = Label(window, text="Physical Address")
l4.grid(row=1, column=2)

client_text = StringVar()# StringVar() takes text input
e1 = Entry(window, textvariable = client_text)# Entry boxes for user data input
e1.grid(row=0, column=1)

email_text = StringVar()
e2 = Entry(window, textvariable = email_text)
e2.grid(row=0, column=3)

phone_text = StringVar()
e3 = Entry(window, textvariable = phone_text)
e3.grid(row=1, column=1)

address_text = StringVar()
e4 = Entry(window, textvariable = address_text)
e4.grid(row=1, column=3)

list1 = Listbox(window, height=6, width=35)#listbox to view selections
list1.grid(row=2, column=0, rowspan=6, columnspan=2) #spans are for stretching the Listbox

sb1 = Scrollbar(window)#position the scroll bar
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand = sb1.set)#set scroll to vertical
sb1.configure(command=list1.yview)
#Bind click events to the list box to populate boxes when an item is selected from the list.
list1.bind('<<ListboxSelect>>', get_selected_row)

#Set up buttons
b1= Button(window, text="View all", width=12, command=view_command)# view_command is passed as a parameter and NOT a function to prevent automatic execution when the program runs
b1.grid(row=2, column=3)

b2= Button(window, text="Search entry", width=12, command=search_command)
b2.grid(row=3, column=3)

b3= Button(window, text="Add entry", width=12, command=add_command)
b3.grid(row=4, column=3)

b4= Button(window, text="Update selected", width=12, command=update_command)
b4.grid(row=5, column=3)

b5= Button(window, text="Delete selected", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6= Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()
