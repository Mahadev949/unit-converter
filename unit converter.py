import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import customtkinter as ctk
from decimal import Decimal
import os
import sys


def resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        # Running as a bundled .exe
        return os.path.join(sys._MEIPASS, relative_path)
    else:
        # Running as a script (not bundled)
        return os.path.join(os.path.abspath("."), relative_path)

converter_info=""
input_value=""
def disablewid():
    calframe.pack_forget()
    frame2.pack_forget()
    frame3.pack(side="left",expand=True,fill=tk.BOTH)
    labell.config(text="")
    #frame4.pack(side="left",expand=True,fill=tk.BOTH)

def enablewid():
    
    frame3.pack_forget()
    #frame4.pack_forget()
    calframe.pack(pady=150)
    frame1.pack(fill="both")    
    frame2.pack(expand=True,pady=2)
    
#----------------------------
length_unit=["Meter","Kilometer","Centimeter","Millimeter","Mile","Yard","Foot","Inch","Decimeter","Micrometer","Nanometer","Picometer","Nautical mile","Furlong","Fathom","Li","Zhang","Chi","cun","Fen","Lil","Hao","Parsec","Lunar distance","Astronomical unit","Light year"]
length_unit.sort()
weight_unit=["Kilogram","Gram","Ton","Pound","Ounce","Milligram","Microgram","Quintal","Carat","Grain","Long ton","Short ton","UK hundredweight","US hundredweight","Stone","Dram",'Dan','Jin','Qian','Liang','Jin(Taiwan)']
weight_unit.sort()
temperature_unit=["Celsius","Fahrenheit","Kelvin",'Rankine','Reaumur']
temperature_unit.sort()
Time_unit=["Second","Minute","Hour","Day","Week","Month","Year","Millisecond","Microsecond","Picosecond"]
Time_unit.sort()
speed_unit=["Meter per Second","Kilometer per Hour","Mile per Hour","Foot per Second","Light speed","Foot per hour","Mach","Kilometer per second","Knot","Inch per second","Meter per hour","Mile per second"]
speed_unit.sort()
volume_unit = ["Liter", "Milliliter", "Gallon", "Quart", "Pint", "Cup", "Cubic Meter","Cubic decimeter", "Cubic kilometer", "Cubic mile", "Cubic yard", "Cubic foot", "Cubic inch", "Cubic centimeter", "Cubic millimeter", "Cubic micrometer", "Cubic nanometer", "Cubic picometer",  "Barrel", "Cord", "Deciliter", "Centiliter", "Hectoliter", "Microliter", "Nanoliter", "Picoliter", "Femtoliter", "Attoliter", "Zeptoliter", "Yoctoliter", "Decaliter"]
volume_unit.sort()
area_unit = ["Square Meter", "Square Kilometer", "Square Mile", "Square Yard", "Square Foot", "Acre", "Hectare", "Square Inch", "Square Centimeter", "Square Millimeter", "Square Micrometer", "Square Nanometer", "Square Picometer", "Are", "Barn","yottameter square"]
area_unit.sort()
 
energy_units = ['Kilowatt-hour', 'Watt-hour', 'Joule', 'Kilojoule', 'Megajoule', 'Electronvolt', 'British Thermal Unit', 'Therm', 'Gigajoule', 'Microjoule', 'KiloWatt', 'Volt-ampere-hour', 'Ampere-hour', 'Femtowatt-hour', 'Megawatt-hour', "Gigawatt hour", "Terawatt hour", "Petawatt hour", "Exawatt hour", "Zettawatt hour", "Yottawatt hour", "Ronnawatt hour", "Quettawatt hour", "Brontawatt hour", "Geptawatt hour"]
energy_units.sort()
storage_units = ['Bit', 'Byte', 'Kilobit', 'Kilobyte', 'Megabit', 'Megabyte', 'Gigabit', 'Gigabyte', 'Terabit', 'Terabyte', 'Petabit', 'Petabyte', 'Exabit', 'Exabyte', 'Zettabit', 'Zettabyte', 'Yottabit', 'Yottabyte', 'Kibibit', 'Kibibyte', 'Mebibit', 'Mebibyte', 'Gibibit', 'Gibibyte', 'Tebibit', 'Tebibyte', 'Pebibit', 'Pebibyte', 'Exbibit', 'Exbibyte', 'Zebibit', 'Zebibyte', 'Yobibit', 'Yobibyte', 'Megabit per second', 'Megabit per hour', 'Kilobit per second', 'Kilobit per hour', 'Gigabit per second', 'Gigabit per hour', 'Terabit per second', 'Terabit per hour', 'Bit per second', 'Byte per second', 'Bit per hour', 'Byte per hour', 'Megabyte per second', 'Megabyte per hour', 'Kilobyte per second', 'Kilobyte per hour', 'Gigabyte per second', 'Gigabyte per hour', 'Terabyte per second', 'Terabyte per hour']
storage_units.sort()

#---------------------------
#convert to requred units ------------------------------------------
def convert_required_unit(unit):
    global converter_info
    output_type=combobox2.get()
    foutput=0.0

    if converter_info in "length":

        if output_type in "Meter":foutput=(unit)

        elif output_type == "Centimeter":foutput=unit*100

        elif output_type=="Astronomical unit":foutput=(unit/ 1.4960e+11)
				
        elif output_type=="Chi":foutput=(unit / 0.3333)
		
        elif output_type=="Decimeter":foutput=(unit*10)
		
        elif output_type=="Fathom":foutput=(unit/ 1.8288)
		
        elif output_type=="Fen":foutput=(unit/ 0.00333)
		
        elif output_type=="Foot":foutput=(unit* 3.28084)
		
        elif output_type=="Furlong":foutput=(unit / 201.168)
		
        elif output_type=="Hao":foutput=(unit / 0.000033)
		
        elif output_type=="Inch":foutput=(unit* 39.3701)
		
        elif output_type=="Kilometer":foutput=(unit/ 1000)
		
        elif output_type=="Li":foutput=(unit/500)
		
        elif output_type=="Light year":foutput=(unit/ 9.4607e+15)
		
        elif output_type=="Lil":foutput=(unit/ 0.00033)
		
        elif output_type=="Lunar distance":foutput=(unit/ 384400000)
				
        elif output_type=="Micrometer":foutput=(unit* 1e+6)
		
        elif output_type=="Mile":foutput=(unit/ 1609.344)
		
        elif output_type=="Millimeter":foutput=(unit*1000)
		
        elif output_type=="Nanometer":foutput=(unit* 1e+9)
		
        elif output_type=="Nautical mile":foutput=(unit/ 1852)
		
        elif output_type=="Parsec":foutput=(unit/ 3.0857e+16)
		
        elif output_type=="Picometer":foutput=(unit* 1e+12)
		
        elif output_type=="Yard":foutput=(unit* 1.09361)
		
        elif output_type=="Zhang":foutput=(unit/ 3.3333)
		
        elif output_type=="cun":foutput=(unit/ 0.03333)
    elif converter_info =="weight":
        
        if output_type == "Carat":
            foutput=(unit / 0.2)  
    
        elif output_type == "Dan":
            foutput=(unit / 50000) 
    
        elif output_type == "Dram":
            foutput=(unit / 1.77185) 
    
        elif output_type == "Grain":
            foutput=(unit / 0.0647989)  
    
        elif output_type == "Gram":
            foutput=(unit)  
        elif output_type == "Jin":
            foutput=(unit / 500)  

        elif output_type == "Jin(Taiwan)":
            foutput=(unit / 600)  
    
        elif output_type == "Kilogram":
            foutput=(unit / 1000) 
    
        elif output_type == "Liang":
            foutput=(unit / 50)  
    
        elif output_type == "Long ton":
            foutput=(unit / 1_016_046.9088)  
    
        elif output_type == "Microgram":
            foutput=(unit * 1_000_000)  
    
        elif output_type == "Milligram":
            foutput=(unit * 1000)  
        elif output_type == "Ounce":
            foutput=(unit / 28.3495) 
    
        elif output_type == "Pound":
            foutput=(unit / 453.592)  
    
        elif output_type == "Qian":
            foutput=(unit / 50) 
    
        elif output_type == "Quintal":
            foutput=(unit / 100000)  
    
        elif output_type == "Short ton":
            foutput=(unit / 907_184.74)  
    
        elif output_type == "Stone":
            foutput=(unit / 6350.29)  
    
        elif output_type == "Ton":
            foutput=(unit / 1_000_000)  
    
        elif output_type == "UK hundredweight":
            foutput=(unit / 50_802.3)  
    
        elif output_type == "US hundredweight":
            foutput=(unit / 45_359.2) 
    elif converter_info == "temperature":
        if output_type=="Celsius":foutput=(unit)
		
        elif output_type=="Fahrenheit":foutput=((unit*1.8)+32)
		
        elif output_type=="Kelvin":foutput=(unit+273.15)
		
        elif output_type=="Rankine":foutput=((unit+273.15)*1.8)
		
        elif output_type=="Reaumur":foutput=(unit*0.8)
    elif converter_info=="time":
        if output_type=="Day":foutput=(unit/(86400 * 1e12))
		
        elif output_type=="Hour":foutput=(unit/(3600 * 1e12))
		
        elif output_type=="Microsecond":foutput=(unit/(1e6))
		
        elif output_type=="Millisecond":foutput=(unit/1e9)
		
        elif output_type=="Minute":foutput=(unit/(60 * 1e12))
		
        elif output_type=="Month":foutput=(unit/(30 * 86400 * 1e12))
		
        elif output_type=="Picosecond":foutput=(unit)
		
        elif output_type=="Second":foutput=(unit/1e12)
		
        elif output_type=="Week":foutput=(unit/( 604800 * 1e12))
		
        elif output_type=="Year":foutput=(unit/(365 * 86400 * 1e12))
    elif converter_info=="speed":
        
        if output_type=="Foot per Second":foutput=(unit)
        
        elif output_type=="Foot per hour":foutput=(unit*3600)

        elif output_type=="Inch per second":foutput=(unit*12)
		
        elif output_type=="Kilometer per Hour":foutput=(unit*1.09728)
		
        elif output_type=="Kilometer per second":foutput=(unit*0.0003048)
		
        elif output_type=="Knot":foutput=(unit*0.592484)
		
        elif output_type=="Light speed":foutput=(unit*1.0167*(10**(-9)))
		
        elif output_type=="Mach":foutput=(unit*0.00089408)
		
        elif output_type=="Meter per Second":foutput=(unit*0.3048)
		
        elif output_type=="Meter per hour":foutput=(unit*1097.28)
		
        elif output_type=="Mile per Hour":foutput=(unit*0.681818)
		
        elif output_type=="Mile per second":foutput=(unit*0.000189394)

    elif converter_info=="volume":
    

        if output_type == "Acre-foot":foutput = (unit) / (1.233 * 10**9)




        elif output_type == "Attoliter":foutput = (unit) * 10**15

        elif output_type == "Barrel":foutput = (unit) / 163700
        
        elif output_type == "Centiliter":foutput = (unit) / 10

        elif output_type == "Cord":foutput = (unit) / 3624556.42

        elif output_type == "Cubic Meter":foutput = (unit) / 1000000

        elif output_type == "Cubic centimeter":foutput = (unit)

        elif output_type == "Cubic decimeter":foutput = (unit) / 1000

        elif output_type == "Cubic foot":foutput = (unit) / 28316.8466

        elif output_type == "Cubic inch":foutput = (unit) / 16.387064

        elif output_type == "Cubic kilometer":foutput = (unit) / (10**15)

        elif output_type == "Cubic micrometer":foutput = (unit) * 10**12

        elif output_type == "Cubic mile":foutput = (unit) / (4.16818 * 10**15)

        elif output_type == "Cubic millimeter":foutput = (unit) * 1000

        elif output_type == "Cubic nanometer":foutput = (unit) * 10**21

        elif output_type == "Cubic picometer":foutput = (unit) * 10**30

        elif output_type == "Cubic yard":foutput = (unit) / 764554.858

        elif output_type == "Cup":foutput = (unit) / 236.6

        elif output_type == "Decaliter":foutput = (unit) / 10000

        elif output_type == "Deciliter":foutput = (unit) / 100

        elif output_type == "Femtoliter":foutput = (unit) * 10**15

        elif output_type == "Gallon":foutput = (unit) / 3785.41

        elif output_type == "Hectoliter":foutput = (unit) / 100000

        elif output_type == "Liter":foutput = (unit) / 1000

        elif output_type == "Microliter":foutput = (unit) * 1000

        elif output_type == "Milliliter":foutput = (unit)

        elif output_type == "Nanoliter":foutput = (unit) * 10**6

        elif output_type == "Picoliter":foutput = (unit) * 10**9

        elif output_type == "Pint":foutput = (unit) / 473.176

        elif output_type == "Quart":foutput = (unit) / 946.353

        elif output_type == "Yoctoliter":foutput = (unit) * 10**21

        elif output_type == "Zeptoliter":foutput = (unit) * 10**18
    elif converter_info=="area":
        if output_type == "Square Meter":foutput = (unit)

        elif output_type == "Square Kilometer":foutput = (unit * 1e-6)

        elif output_type == "Square Mile":foutput = (unit * 3.861021585e-7)

        elif output_type == "Square Yard":foutput = (unit * 1.195990046)

        elif output_type == "Square Foot":foutput = (unit * 10.763910417)

        elif output_type == "Acre":foutput = (unit * 0.000247105381467)

        elif output_type == "Hectare":foutput = (unit * 0.0001)

        elif output_type == "Square Inch":foutput = (unit * 1550.0031)

        elif output_type == "Square Centimeter":foutput = (unit * 10000)

        elif output_type == "Square Millimeter":foutput = (unit * 1e6)

        elif output_type == "Square Micrometer":foutput = (unit * 1e12)

        elif output_type == "Square Nanometer":foutput = (unit * 1e18)

        elif output_type == "Square Picometer":foutput = (unit * 1e24)

        elif output_type == "Are":foutput = (unit * 0.01)

        elif output_type == "Barn":foutput = (unit * 1e28)

        elif output_type == "yottameter square":foutput = (unit * 1e-24)
        if abs(foutput - round(foutput)) < 1e-9:
            foutput = round(foutput)
    elif converter_info=="energy":
        if output_type == "Kilowatt-hour":foutput = (unit / 3600000)

        elif output_type == "Watt-hour":foutput = (unit / 3600)

        elif output_type == "Joule":foutput = (unit)

        elif output_type == "Kilojoule":foutput = (unit / 1000)

        elif output_type == "Megajoule":foutput = (unit / 1000000)

        elif output_type == "Electronvolt":foutput = (unit / 1.602176634e-19)

        elif output_type == "British Thermal Unit":foutput = (unit / 1055.056)

        elif output_type == "Therm":foutput = (unit / 105506000)

        elif output_type == "Gigajoule":foutput = (unit / 1000000000)

        elif output_type == "Microjoule":foutput = (unit / 0.000001)

        elif output_type == "KiloWatt":foutput = (unit / 1000)

        elif output_type == "Volt-ampere-hour":foutput = (unit / 3600)

        elif output_type == "Ampere-hour":foutput = (unit / 3600)

        elif output_type == "Femtowatt-hour":foutput = (unit / 3.6e-15)

        elif output_type == "Megawatt-hour":foutput = (unit / 3600000000)
        elif output_type == "Gigawatt hour":foutput = (unit / 3600000000000)
        elif output_type == "Terawatt hour":foutput = (unit / 3600000000000000)
        elif output_type == "Petawatt hour":foutput = (unit / 3600000000000000000)
        elif output_type == "Exawatt hour":foutput = (unit / 3600000000000000000000)
        elif output_type == "Zettawatt hour":foutput = (unit / 3600000000000000000000000)
        elif output_type == "Yottawatt hour":foutput = (unit / 3600000000000000000000000000)
        elif output_type == "Ronnawatt hour":foutput = (unit / 3600000000000000000000000000000)
        elif output_type == "Quettawatt hour":foutput = (unit / 3600 * 10**30)
        elif output_type == "Brontawatt hour":foutput = (unit / 3600 * 10**33)
        elif output_type == "Geptawatt hour":foutput = (unit / 3600 * 10**36)

    elif converter_info=="storage":
        if output_type == "Bit":
            foutput = (unit * 8)  
        elif output_type == "Byte":
            foutput = unit  
        elif output_type == "Kilobit":
            foutput = (unit * 8) / 1000  
        elif output_type == "Kilobyte":
            foutput = unit / 1000  
        elif output_type == "Megabit":
            foutput = (unit * 8) / 1000000  
        elif output_type == "Megabyte":
            foutput = unit / 1000000 
        elif output_type == "Gigabit":
            foutput = (unit * 8) / 1000000000 
        elif output_type == "Gigabyte":
            foutput = unit / 1000000000  
        elif output_type == "Terabit":
            foutput = (unit * 8) / 1000000000000  
        elif output_type == "Terabyte":
            foutput = unit / 1000000000000  
        elif output_type == "Petabit":
            foutput = (unit * 8) / 1000000000000000  
        elif output_type == "Petabyte":
            foutput = unit / 1000000000000000  
        elif output_type == "Exabit":
            foutput = (unit * 8) / 1000000000000000000  
        elif output_type == "Exabyte":
            foutput = unit / 1000000000000000000  
        elif output_type == "Zettabit":
            foutput = (unit * 8) / 1000000000000000000000  
        elif output_type == "Zettabyte":
            foutput = unit / 1000000000000000000000  
        elif output_type == "Yottabit":
            foutput = (unit * 8) / 1000000000000000000000000  
        elif output_type == "Yottabyte":
            foutput = unit / 1000000000000000000000000  
        elif output_type == "Kibibit":
            foutput = (unit * 8) / 1024  
        elif output_type == "Kibibyte":
            foutput = unit / 1024  
        elif output_type == "Mebibit":
            foutput = (unit * 8) / 1048576 
        elif output_type == "Mebibyte":
            foutput = unit / 1048576  
        elif output_type == "Gibibit":
            foutput = (unit * 8) / 1073741824  
        elif output_type == "Gibibyte":
            foutput = unit / 1073741824  
        elif output_type == "Tebibit":
            foutput = (unit * 8) / 1099511627776  
        elif output_type == "Tebibyte":
            foutput = unit / 1099511627776  
        elif output_type == "Pebibit":
            foutput = (unit * 8) / 1125899906842624 
        elif output_type == "Pebibyte":
            foutput = unit / 1125899906842624 
        elif output_type == "Exbibit":
            foutput = (unit * 8) / 1152921504606846976  
        elif output_type == "Exbibyte":
            foutput = unit / 1152921504606846976  
        elif output_type == "Zebibit":
            foutput = (unit * 8) / 1180591620717411303424 
        elif output_type == "Zebibyte":
            foutput = unit / 1180591620717411303424  
        elif output_type == "Yobibit":
            foutput = (unit * 8) / 1208925819614629174706176  
        elif output_type == "Yobibyte":
            foutput = unit / 1208925819614629174706176 
        elif output_type == "Megabit per second":
            foutput = (unit * 8) / 1000000  
        elif output_type == "Megabit per hour":
            foutput = (unit * 8) / 1000000 * 3600  
        elif output_type == "Kilobit per second":
            foutput = (unit * 8) / 1000  
        elif output_type == "Kilobit per hour":
            foutput = (unit * 8) / 1000 * 3600 
        elif output_type == "Gigabit per second":
            foutput = (unit * 8) / 1000000000  
        elif output_type == "Gigabit per hour":
            foutput = (unit * 8) / 1000000000 * 3600  
        elif output_type == "Terabit per second":
            foutput = (unit * 8) / 1000000000000 
        elif output_type == "Terabit per hour":
            foutput = (unit * 8) / 1000000000000 * 3600  
        elif output_type == "Bit per second":
            foutput = (unit * 8)  
        elif output_type == "Byte per second":
            foutput = unit  
        elif output_type == "Bit per hour":
            foutput = (unit * 8) * 3600  
        elif output_type == "Byte per hour":
            foutput = unit * 3600  
        elif output_type == "Megabyte per second":
            foutput = unit / 1000000
        elif output_type == "Megabyte per hour":
            foutput = unit / 1000000 * 3600
        elif output_type == "Kilobyte per second":
            foutput = unit / 1000
        elif output_type == "Kilobyte per hour":
            foutput = unit / 1000 * 3600
        elif output_type == "Gigabyte per second":
            foutput = unit / 1000000000
        elif output_type == "Gigabyte per hour":
            foutput = unit / 1000000000 * 3600
        elif output_type == "Terabyte per second":
            foutput = unit / 1000000000000
        elif output_type == "Terabyte per hour":
            foutput = unit / 100000
            
        
    
    vachindra=int(float(foutput)) if float(foutput).is_integer() else float(foutput)

    ttext2.set(vachindra)
    vachindra = str(Decimal(vachindra).normalize())
    if (len(str(vachindra))>25):
        labell.config(text="The value is too large\n"+str(vachindra))
    else:
        labell.config(text="")
    
# conversion units--------------------------------------------------------------------------
def convert_units(*args):
    try:
        global converter_info,input_entry,input_type,output_type,input_value,cbi
        input_value = ttext1.get()
        input_type = combobox1.get()
        output_type=combobox2.get()


        if not input_value.strip():
            foutput=("")
            return

        if converter_info == "length":
            if input_type=="Meter":
                convert_required_unit(float(input_value))
            elif input_type=="Kilometer":
                convert_required_unit(float(input_value)*1000)
            elif input_type=="Centimeter":
                convert_required_unit(float(input_value)/100)
            elif input_type=="Millimeter":
                convert_required_unit(float(input_value)/1000)
            elif input_type=="Mile":
                convert_required_unit(float(input_value)*1609.344)
            elif input_type=="Yard":
                convert_required_unit(float(input_value)/1.0936133)
            elif input_type=="Astronomical unit":convert_required_unit(float(input_value)*149600000000)
			
            elif input_type=="Chi":convert_required_unit(float(input_value)*0.333333333333)
			
            elif input_type=="Decimeter":convert_required_unit(float(input_value)*0.1)
			
            elif input_type=="Fathom":convert_required_unit(float(input_value)*1.8288)
			
            elif input_type=="Fen":convert_required_unit(float(input_value)*0.003333)
			
            elif input_type=="Foot":convert_required_unit(float(input_value)*0.3048)
			
            elif input_type=="Furlong":convert_required_unit(float(input_value)*201.168)
            
            elif input_type=="Hao":convert_required_unit(float(input_value)*0.0328084)
			
            elif input_type=="Inch":convert_required_unit(float(input_value)*0.0254)
						
            elif input_type=="Li":convert_required_unit(float(input_value)*500)
			
            elif input_type=="Light year":convert_required_unit(float(input_value)*9460700000000000)
			
            elif input_type=="Lil":convert_required_unit(float(input_value)*0.001)
			
            elif input_type=="Lunar distance":convert_required_unit(float(input_value)*384400000)
			
            elif input_type=="Micrometer":convert_required_unit(float(input_value)*0.000001)
			
            elif input_type=="Nanometer":convert_required_unit(float(input_value)*0.000000001)
			
            elif input_type=="Nautical mile":convert_required_unit(float(input_value)*1852)
			
            elif input_type=="Parsec":convert_required_unit(float(input_value)*3.086e16)
			
            elif input_type=="Picometer":convert_required_unit(float(input_value)*0.000000000001)
			
            elif input_type=="Yard":convert_required_unit(float(input_value)*0.9144)
			
            elif input_type=="Zhang":convert_required_unit(float(input_value)*3.33333)
			
            elif input_type=="cun":convert_required_unit(float(input_value)* 0.0333)

        elif converter_info=="weight":

            if input_type=="Carat":convert_required_unit(float(input_value)*0.2)
			
            elif input_type=="Dan":convert_required_unit(float(input_value)*50000)
			
            elif input_type=="Dram":convert_required_unit(float(input_value)*1.77185)   
			
            elif input_type=="Grain":convert_required_unit(float(input_value)*0.0647989)
			
            elif input_type=="Gram":convert_required_unit(float(input_value))
			
            elif input_type=="Jin":convert_required_unit(float(input_value)*500)
			
            elif input_type=="Jin(Taiwan)":convert_required_unit(float(input_value)*600)
			
            elif input_type=="Kilogram":convert_required_unit(float(input_value)*1000)
			
            elif input_type=="Liang":convert_required_unit(float(input_value)*50)
			
            elif input_type=="Long ton":convert_required_unit(float(input_value)*1016046.9088)
			
            elif input_type=="Microgram":convert_required_unit(float(input_value)*0.000001)
			
            elif input_type=="Milligram":convert_required_unit(float(input_value)*0.001)
			
            elif input_type=="Ounce":convert_required_unit(float(input_value)*28.3495)
			
            elif input_type=="Pound":convert_required_unit(float(input_value)*453.592)
			
            elif input_type=="Qian":convert_required_unit(float(input_value)*50)
			
            elif input_type=="Quintal":convert_required_unit(float(input_value)*100000)
			
            elif input_type=="Short ton":convert_required_unit(float(input_value)*907184.74)
			
            elif input_type=="Stone":convert_required_unit(float(input_value)*6350.29)
			
            elif input_type=="Ton":convert_required_unit(float(input_value)*1000000)
			
            elif input_type=="UK hundredweight":convert_required_unit(float(input_value)*50802.3)
			
            elif input_type=="US hundredweight":convert_required_unit(float(input_value)*45359.2)

        elif converter_info=="temperature":

            if input_type=="Celsius":convert_required_unit(float(input_value))
			
            elif input_type=="Fahrenheit":convert_required_unit((float(input_value)-32)/1.8)
			
            elif input_type=="Kelvin":convert_required_unit(float(input_value)-273.15)
			
            elif input_type=="Rankine":convert_required_unit((float(input_value)-491.67)/1.8)
			
            elif input_type=="Reaumur":convert_required_unit(float(input_value)/0.8)

        elif converter_info=="time":

            if input_type=="Day":convert_required_unit(float(input_value)*86400 * 1e12)
			
            elif input_type=="Hour":convert_required_unit(float(input_value)*3600 * 1e12)
			
            elif input_type=="Microsecond":convert_required_unit(float(input_value)*1e6)
			
            elif input_type=="Millisecond":convert_required_unit(float(input_value)*1e9)
			
            elif input_type=="Minute":convert_required_unit(float(input_value)*60 * 1e12)
			
            elif input_type=="Month":convert_required_unit(float(input_value)*30* 86400 * 1e12)
			
            elif input_type=="Picosecond":convert_required_unit(float(input_value))
			
            elif input_type=="Second":convert_required_unit(float(input_value)*1e12)
			
            elif input_type=="Week":convert_required_unit(float(input_value)*604800 * 1e12)

            elif input_type=="Year" and output_type == "Month":
                output_entry.configure(state="normal")
                ttext2.set(int(input_value)*12)
                output_entry.configure(state="readonly")
			
            elif input_type=="Year":convert_required_unit(float(input_value)*365* 86400 * 1e12)     

        elif converter_info=="speed":

            if input_type=="Foot per Second":convert_required_unit(float(input_value))
			
            elif input_type=="Foot per hour":convert_required_unit(float(input_value)*0.000277778)
			
            elif input_type=="Inch per second":convert_required_unit(float(input_value)*0.0833333)
			
            elif input_type=="Kilometer per Hour":convert_required_unit(float(input_value)*0.911344)
			
            elif input_type=="Kilometer per second":convert_required_unit(float(input_value)*3280.84)
			
            elif input_type=="Knot":convert_required_unit(float(input_value)*1.68781)
			
            elif input_type=="Light speed":convert_required_unit(float(input_value)*983571056)
			
            elif input_type=="Mach":convert_required_unit(float(input_value)*1116.47)
			
            elif input_type=="Meter per Second":convert_required_unit(float(input_value)*3.28084)
			
            elif input_type=="Meter per hour":convert_required_unit(float(input_value)*0.000911344)
			
            elif input_type=="Mile per Hour":convert_required_unit(float(input_value)*1.46667)
			
            elif input_type=="Mile per second":convert_required_unit(float(input_value)*5280)

        elif converter_info=="volume":


            if input_type=="Acre-foot":convert_required_unit(float(input_value)*1.233*(10**9))
			
            elif input_type=="Attoliter":convert_required_unit(float(input_value)*10**-15)
			
            elif input_type=="Barrel":convert_required_unit(float(input_value)*119240.471)
			
            elif input_type=="Centiliter":convert_required_unit(float(input_value)*10)
			
            elif input_type=="Cord":convert_required_unit(float(input_value)*3624556.42)
			
            elif input_type=="Cubic Meter":convert_required_unit(float(input_value)*1000000)
			
            elif input_type=="Cubic centimeter":convert_required_unit(float(input_value))
			
            elif input_type=="Cubic decimeter":convert_required_unit(float(input_value)*1000)
			
            elif input_type=="Cubic foot":convert_required_unit(float(input_value)*28316.8466)
			
            elif input_type=="Cubic inch":convert_required_unit(float(input_value)*16.387064)
			
            elif input_type=="Cubic kilometer":convert_required_unit(float(input_value)*1*10**15)
			
            elif input_type=="Cubic micrometer":convert_required_unit(float(input_value)*1*10**-12)
			
            elif input_type=="Cubic mile":convert_required_unit(float(input_value)*4.16818*10**15)
			
            elif input_type=="Cubic millimeter":convert_required_unit(float(input_value)*0.001)
			
            elif input_type=="Cubic nanometer":convert_required_unit(float(input_value)*1*10**-21)
			
            elif input_type=="Cubic picometer":convert_required_unit(float(input_value)*1*10**-30)
			
            elif input_type=="Cubic yard":convert_required_unit(float(input_value)*764554.858)
			
            elif input_type=="Cup":convert_required_unit(float(input_value)*236.6)
			
            elif input_type=="Decaliter":convert_required_unit(float(input_value)*10000)
			
            elif input_type=="Deciliter":convert_required_unit(float(input_value)*100)
			
            elif input_type=="Femtoliter":convert_required_unit(float(input_value)*10**-12)
			
            elif input_type=="Gallon":convert_required_unit(float(input_value)*3785.41)
			
            elif input_type=="Hectoliter":convert_required_unit(float(input_value)*100000)
			
            elif input_type=="Liter":convert_required_unit(float(input_value)*1000)
			
            elif input_type=="Microliter":convert_required_unit(float(input_value)*0.001)
			
            elif input_type=="Milliliter":convert_required_unit(float(input_value))
			
            elif input_type=="Nanoliter":convert_required_unit(float(input_value)*10**-6)
			
            elif input_type=="Picoliter":convert_required_unit(float(input_value)*10**-9)
			
            elif input_type=="Pint":convert_required_unit(float(input_value)*473.176)
			
            elif input_type=="Quart":convert_required_unit(float(input_value)*946.353)
			
            elif input_type=="Yoctoliter":convert_required_unit(float(input_value)*10**-21)
			
            elif input_type=="Zeptoliter":convert_required_unit(float(input_value)*10**-18)

        elif converter_info=="area":
            if input_type=="Square Meter":convert_required_unit(float(input_value))
            
            elif input_type=="Square Kilometer":convert_required_unit(float(input_value)*1000000)
            
            elif input_type=="Square Mile":convert_required_unit(float(input_value)*2589988.110336)
            
            elif input_type=="Square Yard":convert_required_unit(float(input_value)*0.83612736)
            
            elif input_type=="Square Foot":convert_required_unit(float(input_value)*0.09290304)
            
            elif input_type=="Acre":convert_required_unit(float(input_value)*4046.8564224)
            
            elif input_type=="Hectare":convert_required_unit(float(input_value)*10000)
            
            elif input_type=="Square Inch":convert_required_unit(float(input_value)*0.00064516)
            
            elif input_type=="Square Centimeter":convert_required_unit(float(input_value)*0.0001)
            
            elif input_type=="Square Millimeter":convert_required_unit(float(input_value)*0.000001)
            
            elif input_type=="Square Micrometer":convert_required_unit(float(input_value)*1e-12)
            
            elif input_type=="Square Nanometer":convert_required_unit(float(input_value)*1e-18)
            
            elif input_type=="Square Picometer":convert_required_unit(float(input_value)*1e-24)
            
            elif input_type=="Are":convert_required_unit(float(input_value)*100)
            
            elif input_type=="Barn":convert_required_unit(float(input_value)*1e-28)
            
            elif input_type=="yottameter square":convert_required_unit(float(input_value)*1e24)
        elif converter_info=="energy":
            if input_type=="Kilowatt-hour":convert_required_unit(float(input_value)*3600000)
            
            elif input_type=="Watt-hour":convert_required_unit(float(input_value)*3600)
            
            elif input_type=="Joule":convert_required_unit(float(input_value))
            
            elif input_type=="Kilojoule":convert_required_unit(float(input_value)*1000)
            
            elif input_type=="Megajoule":convert_required_unit(float(input_value)*1000000)
            
            elif input_type=="Electronvolt":convert_required_unit(float(input_value)*1.602176634e-19)
            
            elif input_type=="British Thermal Unit":convert_required_unit(float(input_value)*1055.056)
            
            elif input_type=="Therm":convert_required_unit(float(input_value)*105506000)
            
            elif input_type=="Gigajoule":convert_required_unit(float(input_value)*1000000000)
            
            elif input_type=="Microjoule":convert_required_unit(float(input_value)*0.000001)
            
            elif input_type=="KiloWatt":convert_required_unit(float(input_value)*1000)
            
            elif input_type=="Volt-ampere-hour":convert_required_unit(float(input_value)*3600)
            
            elif input_type=="Ampere-hour":convert_required_unit(float(input_value)*3600)
            
            elif input_type=="Femtowatt-hour":convert_required_unit(float(input_value)*3.6e-15)
            
            elif input_type=="Megawatt-hour":convert_required_unit(float(input_value)*3600000000)
            elif input_type=="Gigawatt hour":convert_required_unit(float(input_value)*3600000000000)
            elif input_type=="Terawatt hour":convert_required_unit(float(input_value)*3600000000000000)
            elif input_type=="Petawatt hour":convert_required_unit(float(input_value)*3600000000000000000)
            elif input_type=="Exawatt hour":convert_required_unit(float(input_value)*3600000000000000000000)
            elif input_type=="Zettawatt hour":convert_required_unit(float(input_value)*3600000000000000000000000)
            elif input_type=="Yottawatt hour":convert_required_unit(float(input_value)*3600000000000000000000000000)
            elif input_type=="Ronnawatt hour":convert_required_unit(float(input_value)*3600000000000000000000000000000)
            elif input_type=="Quettawatt hour":convert_required_unit(float(input_value)*3600*10**30)
            elif input_type=="Brontawatt hour":convert_required_unit(float(input_value)*3600*10**33)
            elif input_type=="Geptawatt hour":convert_required_unit(float(input_value)*3600*10**36)

        elif converter_info=="storage":
            if input_type == "Bit":
                convert_required_unit(float(input_value) / 8)  
            elif input_type == "Byte":
                convert_required_unit(float(input_value) * 1)
            elif input_type == "Kilobit":
                convert_required_unit(float(input_value) * 1000 / 8)  
            elif input_type == "Kilobyte":
                convert_required_unit(float(input_value) * 1000)
            elif input_type == "Megabit":
                convert_required_unit(float(input_value) * 1000000 / 8) 
            elif input_type == "Megabyte":
                convert_required_unit(float(input_value) * 1000000)
            elif input_type == "Gigabit":
                convert_required_unit(float(input_value) * 1000000000 / 8)  
            elif input_type == "Gigabyte":
                convert_required_unit(float(input_value) * 1000000000)
            elif input_type == "Terabit":
                convert_required_unit(float(input_value) * 1000000000000 / 8)
            elif input_type == "Terabyte":
                convert_required_unit(float(input_value) * 1000000000000)
            elif input_type == "Petabit":
                convert_required_unit(float(input_value) * 1000000000000000 / 8)
            elif input_type == "Petabyte":
                convert_required_unit(float(input_value) * 1000000000000000)
            elif input_type == "Exabit":
                convert_required_unit(float(input_value) * 1000000000000000000 / 8)
            elif input_type == "Exabyte":
                convert_required_unit(float(input_value) * 1000000000000000000)
            elif input_type == "Zettabit":
                convert_required_unit(float(input_value) * 1000000000000000000000 / 8)  
            elif input_type == "Zettabyte":
                convert_required_unit(float(input_value) * 1000000000000000000000)
            elif input_type == "Yottabit":
                convert_required_unit(float(input_value) * 1000000000000000000000000 / 8) 
            elif input_type == "Yottabyte":
                convert_required_unit(float(input_value) * 1000000000000000000000000)
            elif input_type == "Kibibit":
                convert_required_unit(float(input_value) * 1024 / 8) 
            elif input_type == "Kibibyte":
                convert_required_unit(float(input_value) * 1024)
            elif input_type == "Mebibit":
                convert_required_unit(float(input_value) * 1048576 / 8) 
            elif input_type == "Mebibyte":
                convert_required_unit(float(input_value) * 1048576)
            elif input_type == "Gibibit":
                convert_required_unit(float(input_value) * 1073741824 / 8) 
            elif input_type == "Gibibyte":
                convert_required_unit(float(input_value) * 1073741824)
            elif input_type == "Tebibit":
                convert_required_unit(float(input_value) * 1099511627776 / 8) 
            elif input_type == "Tebibyte":
                convert_required_unit(float(input_value) * 1099511627776)
            elif input_type == "Pebibit":
                convert_required_unit(float(input_value) * 1125899906842624 / 8) 
            elif input_type == "Pebibyte":
                convert_required_unit(float(input_value) * 1125899906842624)
            elif input_type == "Exbibit":
                convert_required_unit(float(input_value) * 1152921504606846976 / 8)
            elif input_type == "Exbibyte":
                convert_required_unit(float(input_value) * 1152921504606846976)
            elif input_type == "Zebibit":
                convert_required_unit(float(input_value) * 1180591620717411303424 / 8) 
            elif input_type == "Zebibyte":
                convert_required_unit(float(input_value) * 1180591620717411303424)
            elif input_type == "Yobibit":
                convert_required_unit(float(input_value) * 1208925819614629174706176 / 8) 
            elif input_type == "Yobibyte":
                convert_required_unit(float(input_value) * 1208925819614629174706176)
            elif input_type == "Megabit per second":
                convert_required_unit(float(input_value) * 1000000 / 8) 
            elif input_type == "Megabit per hour":
                convert_required_unit(float(input_value) * 1000000 / 8 / 3600) 
            elif input_type == "Kilobit per second":
                convert_required_unit(float(input_value) * 1000 / 8)  
            elif input_type == "Kilobit per hour":
                convert_required_unit(float(input_value) * 1000 / 8 / 3600)  
            elif input_type == "Gigabit per second":
                convert_required_unit(float(input_value) * 1000000000 / 8)  
            elif input_type == "Gigabit per hour":
                convert_required_unit(float(input_value) * 1000000000 / 8 / 3600)  
            elif input_type == "Terabit per second":
                convert_required_unit(float(input_value) * 1000000000000 / 8)  
            elif input_type == "Terabit per hour":
                convert_required_unit(float(input_value) * 1000000000000 / 8 / 3600)
            elif input_type == "Bit per second":
                convert_required_unit(float(input_value) / 8)  
            elif input_type == "Byte per second":
                convert_required_unit(float(input_value) * 1)  
            elif input_type == "Bit per hour":
                convert_required_unit(float(input_value) / 8 / 3600)  
            elif input_type == "Byte per hour":
                convert_required_unit(float(input_value) * 1 / 3600)  
            elif input_type=="Gigabyte per second":
                convert_required_unit(float(input_value)*1000000000)
            elif input_type=="Gigabyte per hour":
                convert_required_unit(float(input_value)*1000000000/3600)
            elif input_type=="Megabyte per second":
                convert_required_unit(float(input_value)*1000000)
            elif input_type=="Megabyte per hour":
                convert_required_unit(float(input_value)*1000000/3600)
            elif input_type=="Kilobyte per second":
                convert_required_unit(float(input_value)*1000)
            elif input_type=="Kilobyte per hour":
                convert_required_unit(float(input_value)*1000/3600)
            elif input_type=="Terabyte per second":
                convert_required_unit(float(input_value)*1000000000000)
            elif input_type=="Terabyte per hour":
                convert_required_unit(float(input_value)*1000000000000/3600)
            elif input_type=="Petabyte per second":
                convert_required_unit(float(input_value)*1000000000000000)
            elif input_type=="Petabyte per hour":
                convert_required_unit(float(input_value)*1000000000000000/3600)
            elif input_type=="Exabyte per second":
                convert_required_unit(float(input_value)*1000000000000000000)
            elif input_type=="Exabyte per hour":
                convert_required_unit(float(input_value)*1000000000000000000/3600)
            elif input_type=="Zettabyte per second":
                convert_required_unit(float(input_value)*1000000000000000000000)
            elif input_type=="Zettabyte per hour":
                convert_required_unit(float(input_value)*1000000000000000000000/3600)
            elif input_type=="Yottabyte per second":
                convert_required_unit(float(input_value)*1000000000000000000000000)
            elif input_type=="Yottabyte per hour":
                convert_required_unit(float(input_value)*1000000000000000000000000/3600)
            elif input_type=="Ronnabyte per second":
                convert_required_unit(float(input_value)*1000000000000000000000000000)
            elif input_type=="Ronnabyte per hour":
                convert_required_unit(float(input_value)*1000000000000000000000000000/3600)
            elif input_type=="Quettabyte per second":
                convert_required_unit(float(input_value)*1000000000000000000000000000000)      
    
    except ValueError:
        ttext2.set("Invalid input!")
    except Exception as e:
        print(f"Error: {str(e)}")
                 
    except TypeError:
        ttext2.insert(0, "Invalid input!")
       
    except Exception as e:
        print(f"Error: {str(e)}")


        
#def functions to put values--------------------------------
def length_unit_put():
    enablewid()
    global converter_info
    
    converter_info="length"
    combobox1['values']=length_unit
    combobox2['values']=length_unit
    combobox1.set(length_unit[0])
    combobox2.set(length_unit[0])
    convert_units()
    textreader()
    reseizer()
def weight_unitt():
    enablewid()
    global converter_info
    converter_info="weight"
    combobox1['values']=weight_unit
    combobox2['values']=weight_unit
    combobox1.set(weight_unit[0])
    combobox2.set(weight_unit[0])
    convert_units()
    textreader()
    reseizer()
def temperature_unitt():
    enablewid()
    global converter_info
    converter_info="temperature"

    combobox1['values']=temperature_unit
    combobox2['values']=temperature_unit
    combobox1.set(temperature_unit[0])
    combobox2.set(temperature_unit[0])
    convert_units()
    textreader()
    reseizer()
def area_unitt():
    global converter_info
    converter_info="area"
    enablewid()
    combobox1['values']=area_unit
    combobox2['values']=area_unit
    combobox1.set(area_unit[0])
    combobox2.set(area_unit[0])
    convert_units()
    textreader()
    reseizer()
def time_unitt():
    global converter_info

    enablewid()
    converter_info="time"
    combobox1['values']=Time_unit
    textreader()
    combobox2['values']=Time_unit
    combobox1.set(Time_unit[0])
    combobox2.set(Time_unit[0])
    convert_units()
    reseizer()
def volume_unitt():
    global converter_info
    enablewid()
    converter_info="volume"
    combobox1['values']=volume_unit
    combobox2['values']=volume_unit
    combobox1.set(volume_unit[0])
    combobox2.set(volume_unit[0])
    convert_units()
    textreader()
    reseizer()
def speed_unitt():
    global converter_info
    converter_info="speed"
    combobox1['values']=speed_unit
    combobox2['values']=speed_unit
    combobox1.set(speed_unit[0])
    combobox2.set(speed_unit[0])
    convert_units()
    textreader()
    enablewid()
    reseizer()
def energy_unitt():
    global converter_info
    converter_info="energy"
    combobox1['values']=energy_units
    combobox2['values']=energy_units
    combobox1.set(energy_units[0])
    combobox2.set(energy_units[0])
    textreader()
    enablewid()
    convert_units()
    reseizer()
def storage_unitt():
    global converter_info
    converter_info="storage"
    combobox1['values']=storage_units
    combobox2['values']=storage_units
    combobox1.set(storage_units[0])
    combobox2.set(storage_units[0])
    textreader()
    enablewid() 
    convert_units()
    reseizer()
def textreader():
    input_entry.configure(state="normal")

def reseizer():
    global converter_info
    photobt1.configure(border=1)
    photobt2.configure(border=1)
    photobt3.configure(border=1)
    photobt4.configure(border=1)
    photobt5.configure(border=1)
    photobt6.configure(border=1)
    photobt7.configure(border=1)
    photobt8.configure(border=1)
    photobt9.configure(border=1)

    if converter_info=="length":
        photobt1.configure(border=5,relief="solid")
    elif converter_info=="weight":
        photobt2.configure(border=5,relief="solid")
    elif converter_info=="temperature":
        photobt3.configure(border=5,relief="solid")
    elif converter_info=="area":
        photobt4.configure(border=5,relief="solid")
    elif converter_info=="time":
        photobt5.configure(border=5,relief="solid")
    elif converter_info=="volume":
        photobt6.configure(border=5,relief="solid")
    elif converter_info=="speed":
        photobt7.configure(border=5,relief="solid")
    elif converter_info=="energy":
        photobt8.configure(border=5,relief="solid")
    elif converter_info=="storage":
        photobt9.configure(border=5,relief="solid")

    
    

#--------------------------------------------------------------------------------------

gui = tk.Tk()
gui.title("Unit Converter")
#gui.geometry('1200x720')
gui.attributes('-fullscreen', True)
#gui.wm_state('zoomed')

gui.iconbitmap(resource_path("photoss/units.ico"))
gui.resizable(False, False)


menu=tk.Frame(gui)
menu.pack(side="top",fill="x")

bt1 = tk.Button(menu, text="X", command=gui.quit, font=("Arial",12, "bold"), bg="red", fg="white", relief="solid",border=0,width=4)
bt1.pack(side="right",padx=(0,2))


bt2=tk.Button(menu,text="←",command=disablewid, font=("Arial", 14), width=1, height=0,relief="flat",borderwidth=0,activebackground=gui["bg"], activeforeground="black",highlightthickness=0,padx=10)
bt2.pack(side="left",padx=(2,0))

# Create the frames
frame1 = tk.Frame(gui)
frame2 = tk.Frame(frame1)
frame2.pack(expand=True,pady=2)
frame1.pack(fill="both")

frame3=tk.Frame(frame1)
frame3.pack(side="left",expand=True,fill=tk.BOTH)


x=130
y=130
# Load the image and create a Tkinter-compatible photo image
image1 = Image.open(resource_path("photoss/length.jpg")).resize((x, y))

photo1 = ImageTk.PhotoImage(image1)

image2 = Image.open(resource_path("photoss/weight.jpg")).resize((x, y))
photo2 = ImageTk.PhotoImage(image2)

image3 = Image.open(resource_path("photoss/temperature.jpg")).resize((x, y)) 
photo3 = ImageTk.PhotoImage(image3)

image4 = Image.open(resource_path("photoss/area.jpg")).resize((x, y)) 
photo4 = ImageTk.PhotoImage(image4)

image5 = Image.open(resource_path("photoss/time.jpg")).resize((x, y)) 
photo5 = ImageTk.PhotoImage(image5)

image6 = Image.open(resource_path("photoss/volume.jpg")).resize((x, y)) 
photo6 = ImageTk.PhotoImage(image6)

image7 = Image.open(resource_path("photoss/speed.jpg")).resize((x, y)) 
photo7 = ImageTk.PhotoImage(image7)

image8 = Image.open(resource_path("photoss/current.jpg")).resize((x, y)) 
photo8 = ImageTk.PhotoImage(image8)

image9 = Image.open(resource_path("photoss/storage.jpg")).resize((x,y))
photo9 = ImageTk.PhotoImage(image9)

rows = 6 
columns = 3  
for i in range(rows):frame3.rowconfigure(i, weight=1)
for i in range(columns):frame3.columnconfigure(i, weight=1)

#assign all unit buttons in frame 3

photobt1 = tk.Button(frame3,image=photo1,command=length_unit_put,bg="black",border=1)
photobt1.grid(row=0, column=0,padx=10)
bttext=tk.Label(frame3,text="Length",font=("Arial",20))
bttext.grid(row=1,column=0,padx=10,pady=(3,40))

photobt2 = tk.Button(frame3,image=photo2,command=weight_unitt,bg="black",border=1)  
photobt2.grid(row=0, column=1,padx=10)
bttext=tk.Label(frame3,text="Weight",font=("Arial",20))
bttext.grid(row=1,column=1,padx=10,pady=(3,40))

photobt3 = tk.Button(frame3,image=photo3,command=temperature_unitt,bg="black",border=1)
photobt3.grid(row=0, column=2,padx=10)
bttext=tk.Label(frame3,text="Temperature",font=("Arial",20))
bttext.grid(row=1,column=2,padx=10,pady=(3,40))

photobt4 = tk.Button(frame3,image=photo4,command=area_unitt,bg="black",border=1)
photobt4.grid(row=2, column=0,padx=10)
bttext=tk.Label(frame3,text="Area",font=("Arial",20))
bttext.grid(row=3,column=0,padx=10,pady=(3,40))

photobt5 = tk.Button(frame3,image=photo5,command=time_unitt,bg="black",border=1)
photobt5.grid(row=2, column=1,padx=10)
bttext=tk.Label(frame3,text="Time",font=("Arial",20))
bttext.grid(row=3,column=1,padx=10,pady=(3,40))

photobt6 = tk.Button(frame3,image=photo6,command=volume_unitt,bg="black",border=1)
photobt6.grid(row=2, column=2,padx=10)
bttext=tk.Label(frame3,text="Volume",font=("Arial",20))
bttext.grid(row=3,column=2,padx=10,pady=(3,40))

photobt7 = tk.Button(frame3,image=photo7,command=speed_unitt,bg="black",border=1)
photobt7.grid(row=4, column=0,padx=10)
bttext=tk.Label(frame3,text="Speed",font=("Arial",20))
bttext.grid(row=5,column=0,padx=10,pady=(3,40))

photobt8 = tk.Button(frame3,image=photo8,command=energy_unitt,bg="black",border=1)
photobt8.grid(row=4, column=1,padx=10)
bttext=tk.Label(frame3,text="Energy",font=("Arial",20))
bttext.grid(row=5,column=1,padx=10,pady=(3,40))

photobt9 = tk.Button(frame3,image=photo9,command=storage_unitt,bg="black",border=1)
photobt9.grid(row=4, column=2,padx=10)
bttext=tk.Label(frame3,text="Storage",font=("Arial",20))
bttext.grid(row=5,column=2,padx=10,pady=(3,40))

# Assign photo to the button for frame 2
photobt1 = tk.Button(frame2,image=photo1,command=length_unit_put,bg="black",border=1)
bttxt=tk.Label(frame2,text="Length",font=("Arial",20)).grid(row=1,column=0,padx=10)
photobt1.grid(row=0, column=0,padx=10)

photobt2 = tk.Button(frame2,image=photo2,command=weight_unitt,bg="black",border=1)  
bttxt=tk.Label(frame2,text="Weight",font=("Arial",20)).grid(row=1,column=1,padx=10)
photobt2.grid(row=0, column=1,padx=10)

photobt3 = tk.Button(frame2,image=photo3,command=temperature_unitt,bg="black",border=1)
bttxt=tk.Label(frame2,text="Temperature",font=("Arial",14)).grid(row=1,column=2,padx=10)
photobt3.grid(row=0, column=2,padx=10)

photobt4 = tk.Button(frame2,image=photo4,command=area_unitt,bg="black",border=1)
bttxt=tk.Label(frame2,text="Area",font=("Arial",20)).grid(row=1,column=3,padx=10)
photobt4.grid(row=0, column=3,padx=10)

photobt5 = tk.Button(frame2,image=photo5,command=time_unitt,bg="black",border=1)
bttxt=tk.Label(frame2,text="Time",font=("Arial",20)).grid(row=1,column=4,padx=10)
photobt5.grid(row=0, column=4,padx=10)

photobt6 = tk.Button(frame2,image=photo6,command=volume_unitt,bg="black",border=1)
bttxt=tk.Label(frame2,text="Volume",font=("Arial",20)).grid(row=1,column=5,padx=10)
photobt6.grid(row=0, column=5,padx=10)

photobt7 = tk.Button(frame2,image=photo7,command=speed_unitt,bg="black",border=1)
bttxt=tk.Label(frame2,text="speed",font=("Arial",20)).grid(row=1,column=6,padx=10)
photobt7.grid(row=0, column=6,padx=10)

photobt8 = tk.Button(frame2,image=photo8,command=energy_unitt,bg="black",border=1)
bttxt=tk.Label(frame2,text="Energy",font=("Arial",20)).grid(row=1,column=7,padx=10)
photobt8.grid(row=0, column=7,padx=10)

photobt9 = tk.Button(frame2,image=photo9,command=storage_unitt,bg="black",border=1)
bttxt=tk.Label(frame2,text="storage",font=("Arial",20)).grid(row=1,column=8,padx=10)
photobt9.grid(row=0, column=8,padx=10)

# Keep a reference 
photobt1.image = photo1
photobt2.image = photo2
photobt3.image = photo3
photobt4.image = photo4
photobt5.image = photo5
photobt6.image = photo6
photobt7.image = photo7
photobt8.image = photo8


# length frame---------------------------------------------------
calframe=tk.Frame(gui)
calframe.pack(expand=True)

def converter_selector_text1(*args):
    
    convert_units()
    
def reverse_combo():
    b=combobox2.get()
    combobox2.set(combobox1.get())
    combobox1.set(b)
    converter_selector_text1()
def reverse_num():
    b=ttext1.get()
    ttext1.set(ttext2.get())
    ttext2.set(b)
    converter_selector_text1()

ttext1 = tk.StringVar()
ttext2 = tk.StringVar()

ttext1.trace("w", converter_selector_text1)

#----------------------------------------------------------------------------------------------------------------------------------
input_entry = ttk.Entry(calframe, textvariable=ttext1, font=("Arial", 16))
input_entry.grid(row=2,column=0,pady=10,padx=10)


reverse_button = tk.Button(calframe, text="↔", font=("Arial", 15), width=2, height=0,relief="flat",borderwidth=0,activebackground=gui["bg"] ,activeforeground="black",highlightthickness=0,command=reverse_combo)
reverse_button.grid(row=1,column=1)
reverse_button2 = tk.Button(calframe, text="↔", font=("Arial", 15), width=2, height=0,relief="flat",borderwidth=0,command=reverse_num)
reverse_button2.grid(row=2,column=1)

output_entry = ttk.Entry(calframe, textvariable=ttext2, font=("Arial", 16))
output_entry.grid(row=2,column=2,pady=10,padx=10)

combobox1=ttk.Combobox(calframe,state="readonly",font=("Arial",20))
combobox1.grid(row=1,column=0,pady=10,padx=100)

combobox2=ttk.Combobox(calframe,state="readonly",font=("Arial",20))
combobox2.grid(row=1,column=2,pady=10,padx=100)

labell=tk.Label(gui,text="",font=("Arial",20))
labell.pack(side="bottom",fill="x")
combobox1.bind("<<ComboboxSelected>>", converter_selector_text1)
combobox2.bind("<<ComboboxSelected>>", converter_selector_text1)
disablewid()
#---------------------------------------------------------------------
gui.mainloop()
