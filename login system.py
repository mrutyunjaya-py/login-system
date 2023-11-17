from tkinter import *
from tkinter import messagebox

def login():
    user=username.get()
    code=password.get()
    if user=="Bapun" and code=="1234":
        root=Toplevel(a)
        root.title("Bill")
        root.geometry("1280x720+150+80")
        root.configure(bg="#d7dae2")
        root.resizable(False,False)

        # Bill calculation code
        def calculate_bill():
            try:
                # Get the quantity and price entered by the user for each item
                quantity = int(quantity_entry.get())
                price = float(price_entry.get())

                # Calculate the total amount for the item
                total_amount = quantity * price

                # Display the total amount in the result label
                result_label.config(text=f'Total Bill: ${total_amount:.2f}')

            except ValueError:
                messagebox.showerror("Error", "Please enter valid numeric values.")

        # GUI components for bill calculation
        bill_frame = Frame(root, bg="#d7dae2")
        bill_frame.pack(padx=20, pady=20)

        Label(bill_frame, text="Item Quantity:", font=("arial", 16), bg="#d7dae2").grid(row=0, column=0, padx=10,
                                                                                        pady=10)
        quantity_entry = Entry(bill_frame, width=12, bd=2, font=("arial", 16))
        quantity_entry.grid(row=0, column=1, padx=10, pady=10)

        Label(bill_frame, text="Item Price:", font=("arial", 16), bg="#d7dae2").grid(row=1, column=0, padx=10, pady=10)
        price_entry = Entry(bill_frame, width=12, bd=2, font=("arial", 16))
        price_entry.grid(row=1, column=1, padx=10, pady=10)

        calculate_button = Button(bill_frame, text="Calculate", command=calculate_bill, font=("arial", 16))
        calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

        result_label = Label(bill_frame, text="", font=("arial", 16), bg="#d7dae2")
        result_label.grid(row=3, column=0, columnspan=2)

        #end of code

    #all alerts, when someone try to enter wrong username and password
    elif user=="" and code=="":
        messagebox.showerror("Invalid", "please enter valid username and password")

    elif user=="":
        messagebox.showerror("Invalid", "username is required")

    elif code=="":
        messagebox.showerror("Invalid", "The password is required")

    elif user!="Bapun" and code!="1234":
        messagebox.showerror("Invalid", "please enter valid username and password")

    elif user!="Bapun":
        messagebox.showerror("Invalid", "plesae enter valid username")

    elif code!="1234":
        messagebox.showerror("Invalid", "please enter valid password")


def main_screen():
    global a
    global username
    global password

    a=Tk()
    a.geometry("1280x720+150+80")
    a.configure(bg="#d7dae2")

    #icon
    image_icon=PhotoImage(file="C:/Users/mruty/Downloads/login.png")
    a.iconphoto(False,image_icon)
    a.title("login system")

    lblTittle=Label(a,text="Login System", font=("arial",50,'bold'),fg="black",bg="#d7dae2")
    lblTittle.pack(pady=50)

    bordercolor=Frame(a,bg="black",width=800,height=400)
    bordercolor.pack()

    mainframe=Frame(bordercolor,bg="#d7dae2",width=800,height=400)
    mainframe.pack(padx=20,pady=20)

    Label(mainframe, text="username", font=("arial", 30, "bold"), bg="#d7dae2").place(x=100, y=50)
    Label(mainframe, text="password", font=("arial", 30, "bold"), bg="#d7dae2").place(x=100, y=150)

    username=StringVar()
    password=StringVar()

    entry_username=Entry(mainframe,textvariable=username,width=12,bd=2,font=("arial",30))
    entry_username.place(x=400,y=50)
    entry_password=Entry(mainframe,textvariable=password,width=12,bd=2,font=("arial",30),show="*")
    entry_password.place(x=400,y=150)

    #reset will reset the input you have given in yhe entry box
    def reset():
        entry_username.delete(0,END)
        entry_password.delete(0,END)

    Button(mainframe,text="Login",height="2",width=23,bg="#ed3833",fg="white",bd=2,command=login).place(x=100,y=250)
    Button(mainframe, text="Reset", height="2", width=23, bg="#1089ff", fg="white", bd=2,command=reset).place(x=300, y=250)
    Button(mainframe, text="Exit", height="2", width=23, bg="#00bd56", fg="white", bd=2,command=a.destroy).place(x=500, y=250)
    #destroy will exit the tkinter window
    a.mainloop()
main_screen()
