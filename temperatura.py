op = int(input(" c = "))

if op == 1:
   tk = float(input("b = "))
   temperatura_kelvin_p_Celsius = tk - 273.15
   print(round(temperatura_kelvin_p_Celsius), "°C.")
elif op == 2:
    tc = float(input(" k = "))
    temperatura_Celsius_p_kelvin = tc + 273.15
    print(round(temperatura_Celsius_p_kelvin), "°K.")
elif op == 3:
    tf = float(input(" F = "))
    temp_Fahrenheit_p_C = (tf-32) * 5/9
    print(round(temp_Fahrenheit_p_C), "°C.")
elif op == 4:
    tcf = float(input(" Cf = "))
    tempcf = (tcf * 9/5 ) + 32
    print(round(tempcf), " °F.")
elif op == 5:
    tkf = float(input(" Kf = "))
    tempkf = (tkf-273.15) * 9/5 + 32
    print(round(tempkff), "°F.")
elif op == 6:
    tfk = float(input(" Fk = "))
    tempfk = (tfk-32) * 5/9 + 273.15 
    print(round(tempfk), " °K.")
