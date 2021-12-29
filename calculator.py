import tkinter as tk #This line imports the Tkinter module into your program's namespace, but renames it as tk.
import math

class Application(tk.Frame): # Your application class must inherit from Tkinter's Frame class

    def __init__(self, master=None):
        tk.Frame.__init__(self, master) # Your application class must inherit from Tkinter's Frame class

        self.prevOperand = ''
        self.currentOperand = '0'
        self.operator_selected = ''
        
        self.display_num = tk.StringVar()
        self.display_num.set('0')
        
        # Background color of app
        self.config(bg='#ff0000')
        self.grid( 
            sticky=tk.N+tk.S+tk.E+tk.W, #Makes widgets stretch with resize
            )# Necessary to make the application actually appear on the screen. 
        self.createWidgets()

    def number_display(self, number):
        # function to update display value
        self.display_num.set(number)
    
    def compute(self, prevOperand, currentOperand, operator):
        # function to compute value

        if prevOperand.find('.') > -1:
            prevOperand = float(prevOperand)
        else:
            prevOperand = int(prevOperand)

        if currentOperand.find('.') > -1:
            currentOperand = float(currentOperand)
        else:
            currentOperand = int(currentOperand)

        total = 0

        if operator == '+':
            total = prevOperand + currentOperand
        elif operator == '-':
            total = prevOperand - currentOperand
        elif operator == '*':
            total = prevOperand * currentOperand
        elif operator == '/':
            total = prevOperand / currentOperand
        elif operator == '**':
            total = pow(prevOperand,currentOperand)

        self.prevOperand = ''
        self.currentOperand = str(total)
        self.operator = ''
        self.number_display(total)

    def clear(self):
        # function to clear all values and 
        self.prevOperand = ''
        self.currentOperand = '0'
        self.display_num.set('0')
        self.number_display('0')

    def decimal(self):
        # function to add decimal place
        if self.currentOperand.find('.') == -1:
            self.currentOperand = self.currentOperand + '.'
        else:  
            return

        self.number_display(self.currentOperand)

    def number(self, number_pressed):
        # function to add number to current value
        if self.currentOperand == '0':
            self.currentOperand = number_pressed
        else:
            self.currentOperand = self.currentOperand + number_pressed

        self.number_display(self.currentOperand)
        

    def operator_select(self, operator_pressed):
        # function for selection of operator
        self.operator = operator_pressed
        self.prevOperand = self.currentOperand
        self.currentOperand = '0'
        self.number_display(self.currentOperand)

    def percent(self):
        self.currentOperand = str(float(self.currentOperand) * 1.00)
        self.number_display(self.currentOperand)

    def sqrt(self):
        # function for square rooting number
        total = math.sqrt(float(self.currentOperand))
        self.prevOperand = ''
        self.currentOperand = str(total)
        self.number_display(total)

    def delete(self):
        # function to delete last number from currentOperand
        self.currentOperand = self.currentOperand[:-1]
        if len(self.currentOperand) < 1:
            self.currentOperand = '0'

        self.number_display(self.currentOperand)

    def equal(self):
        # function to total values
        # if no prevOperand... return
        if self.prevOperand == '':
            return
        else:
            self.compute(self.prevOperand, self.currentOperand, self.operator)

    def store_memory(self):
        # Stores current operand into memory
        self.clear_memory
        file = open('memory.txt','a')
        file.write(self.currentOperand)
        self.clear
        file.close()
    
    def retreive_memory(self):
        # Retrieves operand value in memory
        file = open('memory.txt','rt')
        memory = file.readline()
        self.currentOperand = memory
        self.number_display(memory)

    def clear_memory(self):
        # clears operand stored in memory
        file = open('memory.txt','w')
        file.write("")
        file.close()
        self.currentOperand = '0'
        self.number_display('0')

    def createWidgets(self):
        # test=tk.StringVar() # create a StringVar to be displayed on button
        # test.set('Quit')    # set the value of the StringVar

        top=self.winfo_toplevel() 
        # The “top levelwindow” is the outermostwindowon the screen. However, this window is not your
        # Application window—it is the parent of the Application instance. To get the top-level window
        # all the .winfo_toplevel() method on anywidget in your application; see Section 26, “Universal
        # widget methods” (p. 97).
        # top.geometry('320x360-300+50') # location and size of application
        top.config(bg='#ff0000') # color 

        self.columnconfigure(0,minsize=80,weight=1)
        self.columnconfigure(1,minsize=80,weight=1)
        self.columnconfigure(2,minsize=80,weight=1)
        self.columnconfigure(3,minsize=80,weight=1)
        
        self.rowconfigure(0,minsize=60,weight=1)
        self.rowconfigure(1,minsize=60,weight=1)
        self.rowconfigure(2,minsize=60,weight=1)
        self.rowconfigure(3,minsize=60,weight=1)
        self.rowconfigure(4,minsize=60,weight=1)
        self.rowconfigure(5,minsize=60,weight=1)
        self.rowconfigure(6,minsize=60,weight=1)
        self.rowconfigure(7,minsize=60,weight=1)

        # ROW 1 - DISPLAY

        self.display = tk.Label(
            self,
            textvariable=self.display_num,
            anchor=tk.SE,
            font=('Times',36),
            fg='#000000',
            bg='#ff0000'
        )

        style=tk.Button(      
            self,
            name='button',      
            bg='#000000', # background color of button
            fg='#ff0000', # foreground color of button ie text
            activebackground='#ff0000', #background color when pressed
            activeforeground='#000000', #foreground color when pressed
            bd=1, # default is 2 . borderwidth is also variation of same option
            font=('Times',24,'italic'),
            )

        # ROW 2
        self.blank = tk.Button(self, style,
            text='',    # text of button
        )
        self.memory_store = tk.Button( self, style,
            text='MS',    # text of button
            command = self.store_memory, # action to perform when clicked
        )
        self.memory_retrieve = tk.Button( self, style,
            text='MR',    # text of button
            command = self.retreive_memory, # action to perform when clicked
        )
        self.memory_clear = tk.Button( self, style,
            text='MC',    # text of button
            command = self.clear_memory, # action to perform when clicked
        )
        # ROW 3
        self.percent = tk.Button(self, style,
            text='%',    # text of button
            command = self.percent, # action to perform when clicked
        )
        self.expo = tk.Button( self, style,
            text='x²',    # text of button
            command = lambda m='**' : self.operator_select(m), # action to perform when clicked
        )
        self.sqrt = tk.Button( self, style,
            text='√',    # text of button
            command = self.sqrt, # action to perform when clicked
        )
        self.delete = tk.Button( self, style,
            text='del',    # text of button
            command = self.delete, # action to perform when clicked
        )

        # ROW 4
        self.seven = tk.Button( self, style,
            text='7',    # text of button
            command = lambda m='7' : self.number(m) # action to perform when clicked
        )
        self.eight = tk.Button( self, style,
            text='8',    # text of button
            command = lambda m='8' : self.number(m), # action to perform when clicked
        )
        self.nine = tk.Button( self, style,
            text='9',    # text of button
            command = lambda m='9' : self.number(m), # action to perform when clicked
        )
        self.multiply = tk.Button( self, style,
            text='x',    # text of button
            command = lambda m='*' : self.operator_select(m), # action to perform when clicked
        )

        # ROW 5
        self.four = tk.Button( self, style,
            text='4',    # text of button
            command = lambda m='4' : self.number(m), # action to perform when clicked
        )
        self.five = tk.Button( self, style,
            text='5',    # text of button
            command = lambda m='5' : self.number(m), # action to perform when clicked
        )
        self.six = tk.Button( self, style,
            text='6',    # text of button
            command = lambda m='6' : self.number(m), # action to perform when clicked
        )
        self.minus = tk.Button( self, style,
            text='-',    # text of button
            command = lambda m='-' : self.operator_select(m), # action to perform when clicked
        )

        # ROW 6
        self.one = tk.Button( self, style,
            text='1',    # text of button
            command = lambda m='1' : self.number(m), # action to perform when clicked
        )
        self.two = tk.Button( self, style,
            text='2',    # text of button
            command = lambda m='2' : self.number(m) # action to perform when clicked
        )
        self.three = tk.Button( self, style,
            text='3',    # text of button
            command = lambda m='3' : self.number(m), # action to perform when clicked
        )
        self.plus = tk.Button( self,style,
            text='+',    # text of button
            command = lambda m='+' : self.operator_select(m), # action to perform when clicked
        )

        # ROW 7
        self.clear = tk.Button( self, style,
            text='CE',    # text of button
            command = self.clear, # action to perform when clicked
        )
        self.zero = tk.Button( self, style,
            text='0',    # text of button
            command = lambda m='0' : self.number(m), # action to perform when clicked
        )
        self.period = tk.Button( self, style,
            text='.',    # text of button
            command = lambda m='.' : self.decimal(), # action to perform when clicked
        )
        self.equal = tk.Button( self, style,
            text='=',    # text of button
            command = self.equal, # action to perform when clicked
        )
# ROW 1 - DISPLAY
        self.display.grid(row=0, column=0, rowspan=2, columnspan=4, sticky=tk.N+tk.S+tk.E+tk.W)

# ROW 2
        self.blank.grid(row=2, column=0, sticky=tk.N+tk.S+tk.E+tk.W) #Makes column 0 of the Application widget's grid stretchable
        self.memory_store.grid(row=2, column=1, sticky=tk.N+tk.S+tk.E+tk.W) #Makes column 0 of the Application widget's grid stretchable
        self.memory_retrieve.grid(row=2, column=2, sticky=tk.N+tk.S+tk.E+tk.W) #Makes column 0 of the Application widget's grid stretchable
        self.memory_clear.grid(row=2, column=3, sticky=tk.N+tk.S+tk.E+tk.W) #Makes column 0 of the Application widget's grid stretchable
# ROW 3
        self.percent.grid(row=3, column=0, sticky=tk.N+tk.S+tk.E+tk.W) #Makes column 0 of the Application widget's grid stretchable
        self.expo.grid(row=3, column=1, sticky=tk.N+tk.S+tk.E+tk.W) #Makes column 0 of the Application widget's grid stretchable
        self.sqrt.grid(row=3, column=2, sticky=tk.N+tk.S+tk.E+tk.W) #Makes column 0 of the Application widget's grid stretchable
        self.delete.grid(row=3, column=3, sticky=tk.N+tk.S+tk.E+tk.W) #Makes column 0 of the Application widget's grid stretchable
# ROW 4
        self.seven.grid(row=4, column=0, sticky=tk.N+tk.S+tk.E+tk.W) #Makes column 0 of the Application widget's grid stretchable
        self.eight.grid(row=4, column=1, sticky=tk.N+tk.S+tk.E+tk.W) #Makes column 0 of the Application widget's grid stretchable
        self.nine.grid(row=4, column=2, sticky=tk.N+tk.S+tk.E+tk.W) #Makes column 0 of the Application widget's grid stretchable
        self.multiply.grid(row=4, column=3, sticky=tk.N+tk.S+tk.E+tk.W) #Makes column 0 of the Application widget's grid stretchable
# ROW 5
        self.four.grid(row=5, column=0, sticky=tk.N+tk.S+tk.E+tk.W) #Makes column 0 of the Application widget's grid stretchable
        self.five.grid(row=5, column=1, sticky=tk.N+tk.S+tk.E+tk.W) #Makes column 0 of the Application widget's grid stretchable
        self.six.grid(row=5, column=2, sticky=tk.N+tk.S+tk.E+tk.W) #Makes column 0 of the Application widget's grid stretchable
        self.minus.grid(row=5, column=3, sticky=tk.N+tk.S+tk.E+tk.W) #Makes column 0 of the Application widget's grid stretchable
# ROW 6
        self.one.grid(row=6, column=0, sticky=tk.N+tk.S+tk.E+tk.W) #Makes column 0 of the Application widget's grid stretchable
        self.two.grid(row=6, column=1, sticky=tk.N+tk.S+tk.E+tk.W) #Makes column 0 of the Application widget's grid stretchable
        self.three.grid(row=6, column=2, sticky=tk.N+tk.S+tk.E+tk.W) #Makes column 0 of the Application widget's grid stretchable
        self.plus.grid(row=6, column=3, sticky=tk.N+tk.S+tk.E+tk.W) #Makes column 0 of the Application widget's grid stretchable
# ROW 7
        self.clear.grid(row=7, column=0, sticky=tk.N+tk.S+tk.E+tk.W) #Makes column 0 of the Application widget's grid stretchable
        self.zero.grid(row=7, column=1, sticky=tk.N+tk.S+tk.E+tk.W) #Makes column 0 of the Application widget's grid stretchable
        self.period.grid(row=7, column=2, sticky=tk.N+tk.S+tk.E+tk.W) #Makes column 0 of the Application widget's grid stretchable
        self.equal.grid(row=7, column=3, sticky=tk.N+tk.S+tk.E+tk.W) #Makes column 0 of the Application widget's grid stretchable


app = Application() #The main program starts here by instantiating the Application class.
app.master.title('Python UI Project')  #The main program starts here by instantiating the Application class.
app.mainloop() #The main program starts here by instantiating the Application class.