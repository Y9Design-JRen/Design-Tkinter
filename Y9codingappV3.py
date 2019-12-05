# Prototype 1
# Translator App
# Y9 Coding
# Upper Canada College
# Jason Renaud

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Element Finder")
root.minsize(300, 300)
root.geometry("1000x700")

style = ttk.Style()
style.configure('TNotebook', tabposition='nw') 

# Create your variables to store data that is typed in by the user 
word1 = tk.StringVar()


# This is the command that does the actual translation

def pressBtn1():
    
    myText1 = str(word1.get())
    # right now it can only do lowercase words
    if myText1 == "H2o":
        result = str("Water")
        label3.config(text=result)
        print (myText1) 

    elif myText1 == "H":
        result = str("Hydrogen")
        label3.config(text=result)
        print (myText1) 

    elif myText1 == "He":
        result = str("Helium")
        label3.config(text=result)
        print (myText1)       
    
    elif myText1 == "Li":
        result = str("Lithium")
        label3.config(text=result)
        print (myText1)  
    
    elif myText1 == "Be":
        result = str("Beryllium")
        label3.config(text=result)
        print (myText1)  
    
    elif myText1 == "C":
        result = str("Carbon")
        label3.config(text=result)
        print (myText1)    
  
    elif myText1 == "B":
        result = str("Boron")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "N":
        result = str("Nitrogen")
        label3.config(text=result)
        print (myText1)  


    elif myText1 == "O":
        result = str("Oxygen")
        label3.config(text=result)
        print (myText1)  


    elif myText1 == "F":
        result = str("Fluorine")
        label3.config(text=result)
        print (myText1)  


    elif myText1 == "Ne":
        result = str("Neon")
        label3.config(text=result)
        print (myText1)  

    
    elif myText1 == "Na":
        result = str("Sodium")
        label3.config(text=result)
        print (myText1)  


    elif myText1 == "Mg":
        result = str("Magnesium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Al":
        result = str("Aluminium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Si":
        result = str("Silicone")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "P":
        result = str("Phosphorus")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "S":
        result = str("Sulfur")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Cl":
        result = str("Chlorine")
        label3.config(text=result)
        print (myText1)  


    elif myText1 == "Ar":
        result = str("Argon")
        label3.config(text=result)
        print (myText1)      

    elif myText1 == "K":
        result = str("Potassium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Ca":
        result = str("Calcium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Sc":
        result = str("Scandium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Ti":
        result = str("Titanium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "V":
        result = str("Vanadium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Cr":
        result = str("Chromium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Mn":
        result = str("Manganese")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Fe":
        result = str("Iron")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Co":
        result = str("Cobalt")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Ni":
        result = str("Nickel")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Cu":
        result = str("Copper")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Zn":
        result = str("Zinc")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Ga":
        result = str("Gallium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Ge":
        result = str("Germanium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "As":
        result = str("Arsenic")
        label3.config(text=result)
        print (myText1)  
    
    elif myText1 == "Se":
        result = str("Selenium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Br":
        result = str("Bromine")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Kr":
        result = str("Krypton")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Rb":
        result = str("Rubidium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Sr":
        result = str("Strontium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Y":
        result = str("Yttrium")
        label3.config(text=result)
        print (myText1)  


    elif myText1 == "Zr":
        result = str("Zirconium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Nb":
        result = str("Niobium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Mo":
        result = str("Molybdenum")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Tc":
        result = str("Technetium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Ru":
        result = str("Ruthenium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Rh":
        result = str("Rhodium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Pd":
        result = str("Palladium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Ag":
        result = str("Silver")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Cd":
        result = str("Cadmium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "In":
        result = str("Indium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Sn":
        result = str("Tin")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Sb":
        result = str("Antimony")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Te":
        result = str("Tellurium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "I":
        result = str("Iodine")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Xe":
        result = str("Xenon")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Cs":
        result = str("Caesium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Ba":
        result = str("Barium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Hf":
        result = str("Hafnium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Ta":
        result = str("Tantalum")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "W":
        result = str("Tungsten")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Re":
        result = str("Rhenium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Os":
        result = str("Osmium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Ir":
        result = str("Iridium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Pt":
        result = str("Platinum")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Au":
        result = str("Gold")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Hg":
        result = str("Mercury")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Tl":
        result = str("Thallium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Pb":
        result = str("Lead")
        label3.config(text=result)
        print (myText1)  
   
    elif myText1 == "Bi":
        result = str("Bismuth")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Po":
        result = str("Polonium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "At":
        result = str("Astatine")
        label3.config(text=result)
        print (myText1)  


    elif myText1 == "Rn":
        result = str("Radon")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Fr":
        result = str("Francium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Ra":
        result = str("Radium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Rf":
        result = str("Rutherfordium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Db":
        result = str("Dubnium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Sg":
        result = str("Seaborgium")
        label3.config(text=result)
        print (myText1)  


    elif myText1 == "Bh":
        result = str("Bohrium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Hs":
        result = str("Hassium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Mt":
        result = str("Meitnerium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Ds":
        result = str("Darmstadtium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Rg":
        result = str("Roentgenium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Cn":
        result = str("Copernicium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Nh":
        result = str("Nihonium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Fl":
        result = str("Flerovium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Mc":
        result = str("Moscovium")
        label3.config(text=result)
        print (myText1)  


    elif myText1 == "Lv":
        result = str("Livermorium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Ts":
        result = str("Tennessine")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Og":
        result = str("Oganesson")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "La":
        result = str("Lanthanum")
        label3.config(text=result)
        print (myText1)  


    elif myText1 == "Ce":
        result = str("Cerium")
        label3.config(text=result)
        print (myText1)  


    elif myText1 == "Pr":
        result = str("Praseodymium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Nd":
        result = str("Neodymium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Pm":
        result = str("Promethium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Sm":
        result = str("Samarium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Eu":
        result = str("Europium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Gd":
        result = str("Gadolinium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Tb":
        result = str("Terbium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Dy":
        result = str("Dysprosium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Ho":
        result = str("Holmium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Hg":
        result = str("Mercury")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Er":
        result = str("Erbium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Tm":
        result = str("Thulium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Yb":
        result = str("Ytterbium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Lu":
        result = str("Lutetium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Ac":
        result = str("Actinium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Th":
        result = str("Thorium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Pa":
        result = str("Protactinium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "U":
        result = str("Uranium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Np":
        result = str("Neptunium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Pu":
        result = str("Plutonium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Am":
        result = str("Americium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Cm":
        result = str("Curium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Bk":
        result = str("Berkelium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Cf":
        result = str("Californium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Es":
        result = str("Einsteinium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Fm":
        result = str("Fermium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Md":
        result = str("Mendelevium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "No":
        result = str("Nobelium")
        label3.config(text=result)
        print (myText1)  

    elif myText1 == "Lr":
        result = str("Lawrencium")
        label3.config(text=result)
        print (myText1)  

    else:
        result = str("This is not valid")
        label3.config(text=result)




planner = ttk.Notebook(root, width=1000, height=650)

# Create the frames of different colours that are 200*200 pixels in dimensions

######################################## Start Frame 1 ###################################

tab1 = tk.Frame(planner, bg='red', width=200, height=200)

# Here we create a label to tell the user of what to do
label1 = tk.Label(tab1, text="enter your Element")
label1.grid(row=0, column=2)
label1.configure(foreground="green")

# Here we create a label to tell the user what the answer is
label2 = tk.Label(tab1, text="Answer is:")
label2.grid(row=1, column=2)
label2.configure(foreground="green")

label3 = tk.Label(tab1, text = "???")
label3.grid (row = 5, column = 2)
label3.configure(foreground="green")

# Here we create a textbox for data entry
# "number1" will store this information that will be used by the "pressBtn1" helper function
entryNum1 = tk.Entry(tab1, textvariable=word1)
entryNum1.grid(row=2, column=2)

# Here we create a button
button1 = tk.Button(tab1, text="Translate", command = pressBtn1)
button1.grid(row=3, column=2)
button1.configure(foreground="green")


######################################## End Frame 1 ###################################

# These frames have not been implemented yet
tab2 = tk.Frame(planner, bg='red', width=200, height=200)


# Add the tabs/frames to the notebook object called "planner" 
# Referred to Stack Overflow for assistance

planner.add(tab1, text='Element Translator')
planner.add(tab2, text='Testing')


# Tabs will be added to the "top" of the "frame"
#planner.pack(side=tk.TOP)
planner.grid(row = 0, column = 0)

root.mainloop()



