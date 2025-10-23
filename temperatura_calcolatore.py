#temperatura_calcolatore
tempC=float(input("inserisci una tmperatura in gradi Celsius: "))
tempK=tempC+273.15
tempF=(9/5*tempC)+32
if tempC>-273.15:
    print("temperatura in Kelvin:",tempK,"K")
    print("temperatura in Fahreneit",tempF,"F")
else:
    print("valore della variabile non corretto")
        
