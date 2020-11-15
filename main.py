import tkinter as tk
import os


#TKINTER_PROGRAMME_STARTS
temp = "" 
def main():
    root = tk.Tk()
    root.geometry("500x200")
    root.title("Magic Calculator")
    
 

    #this function is used to get the data from the button and insert into the Entry_input text
    def get_data(a):
        global temp
        temp = temp + str(a)
        # text_input.set(temp)  # will put the entered values from button as display in Entry_input
        Entry_input.insert(tk.END, temp) #inserts the value into entry_input
        temp=""

    # def collect_data():
    #     data=Entry_input.get() #gets the input from the '=' sign 
    #     Entry_input_1.delete(0,tk.END) #deletes the entry_input_1 column while the programme starts
    #     try:
    #         Entry_input_1.insert(0,'123456789')
    #     except:
    #         Entry_input_1.insert(0,'sorry error occured')

    def change_dropdown(*args):
        drop_var=tkvar.get() #gets the input from drop doen menu to entry_input_1 when the '=' sign is pressed 
        Entry_input_1.delete(0,tk.END) #clears the entry_input_1 if data aready exists
        Entry_input_1.insert(0,drop_var) #inserts the data of drop down into the entry_input_1
        tkvar.set("NA") # reset the drop down menu to NA so output is not visible
    
    #this function clears only one element from the Entry_input field
    def clear_one():
        txt=""
        txt=Entry_input.get()[:-1] # considers all elements except the last
        Entry_input.delete(0,tk.END) #deletes all the elements in the list 
        c=Entry_input.insert(0,txt) # then paste the coppied txt  variable in the entry field

    #this function clears all element from the Entry_input field
    def clear_all():
        Entry_input.delete(0,tk.END) #clears all the elements from the 


    #creating top frame
    topFrame=tk.Frame(root)
    topFrame.grid(row=0,column=0)

    #creating bottom frame
    bottomFrame=tk.Frame(root)
    bottomFrame.grid(row=1,column=0)

    #creating first input entry button
    Entry_input=tk.Entry(topFrame,bg='pink')
    Entry_input.grid(row=1,column=1)

    #creating secong output entry button
    Entry_input_1=tk.Entry(topFrame,bg='yellow')
    Entry_input_1.grid(row=2,column=1)

    label_1 = tk.Label(topFrame,text="output")
    label_1.grid(row=2,column=0)

    # Create a Tkinter variable
    tkvar = tk.StringVar(root)

    #options for drop down menu 
    options = ["123456","123","NA","4563"]

    tkvar.set("NA") # setting the default value for the drop down bar

    #setting up the drop down
    popupMenu = tk.OptionMenu(bottomFrame, tkvar, *options)

    #change the drop down button (menu) colour
    popupMenu.config(bg="black")

    #change the dropdown options colour
    popupMenu["menu"].config(bg="green")

    #settig up the position for the drop down
    popupMenu.grid(row = 4, column =2)

    #statement to link the function change)drpdown to the drop down funtionality
    # tkvar.trace('w', change_dropdown)

    #creating button_1
    button_1=tk.Button(bottomFrame,text="1",width=10,command=lambda: get_data('1'),fg='red')
    button_1.grid(row=0,column=0)

    #creating button_2
    button_2=tk.Button(bottomFrame,text="2",width=10,command=lambda: get_data('2'),fg='green')
    button_2.grid(row=0,column=1)

    #creating button_3
    button_3=tk.Button(bottomFrame,text="3",width=10,command=lambda: get_data('3'),fg='orange')
    button_3.grid(row=0,column=2)

    #creating button_4
    button_4=tk.Button(bottomFrame,text="4",width=10,command=lambda: get_data('4'),fg='brown')
    button_4.grid(row=0,column=3)

    #creating button_5
    button_5=tk.Button(bottomFrame,text="5",width=10,command=lambda: get_data('5'),fg='medium violet red')
    button_5.grid(row=0,column=4)

    #creating button_6
    button_6=tk.Button(bottomFrame,text="6",width=10,command=lambda: get_data('6'),fg='black')
    button_6.grid(row=1,column=0)

    #creating button_7
    button_7=tk.Button(bottomFrame,text="7",width=10,command=lambda: get_data('7'),fg='violet')
    button_7.grid(row=1,column=1)

    #creating button_8
    button_8=tk.Button(bottomFrame,text="8",width=10,command=lambda: get_data('8'),fg='green')
    button_8.grid(row=1,column=2)

    #creating button_9
    button_9=tk.Button(bottomFrame,text="9",width=10,command=lambda: get_data('9'),fg='medium spring green')
    button_9.grid(row=1,column=3)

    #creating button_10
    button_10=tk.Button(bottomFrame,text="0",width=10,command=lambda: get_data('0'),fg='brown')
    button_10.grid(row=1,column=4)

    #creating button_11
    button_11=tk.Button(bottomFrame,text="+",width=10,command=lambda: get_data('+'),fg='DeepPink4')
    button_11.grid(row=2,column=0)

    #creating button_12
    button_12=tk.Button(bottomFrame,text="-",width=10,command=lambda: get_data('-'),fg='black')
    button_12.grid(row=2,column=1)

    #creating button_13
    button_13=tk.Button(bottomFrame,text="/",width=10,command=lambda: get_data('/'),fg='violet')
    button_13.grid(row=2,column=2)

    #creating button_14
    button_14=tk.Button(bottomFrame,text="*",width=10,command=lambda: get_data('*'),fg='green')
    button_14.grid(row=2,column=3)

    #creating button_15
    button_15=tk.Button(bottomFrame,text="=",width=10,command=lambda: change_dropdown(),fg='red')
    button_15.grid(row=2,column=4)

    #creating button_16
    button_16=tk.Button(bottomFrame,text="(",width=10,command=lambda: get_data('('),fg='red')
    button_16.grid(row=3,column=1)

    #creating button_17
    button_17=tk.Button(bottomFrame,text=")",width=10,command=lambda: get_data(')'),fg='red')
    button_17.grid(row=3,column=2)

    #creating button_18 for clearing one element 
    button_18=tk.Button(bottomFrame,text="<=]",width=10,command=lambda: clear_one(),fg='blue')
    button_18.grid(row=3,column=3)

    #creating button_19 for clearing all elements in Entry_input text field 
    button_19=tk.Button(bottomFrame,text="[x]",width=10,command=lambda: clear_all(),fg='green')
    button_19.grid(row=3,column=4)

    button_20=tk.Button(bottomFrame,text="^",width=10,command=lambda: get_data('^'),fg='green')
    button_20.grid(row=3,column=0)

    #main loop ends here 
    root.mainloop()

if __name__ == "__main__":
    main()