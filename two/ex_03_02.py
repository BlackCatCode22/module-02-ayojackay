hours = input('Enter hours: \n')
rate = input('Enter Rate: \n')
try:
    fhours = float(hours)
    frate = float(rate)
except:
    print('Please choose numeric values.')
    quit()

if fhours > 40:
    reg = fhours * frate
    otp = (fhours - 40.00) * (frate * 0.5)
    pay = reg + otp
else:
    pay = fhours * frate
print(pay)
