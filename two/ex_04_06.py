def computepay(hours, rate):
    if hours > 40:
        reg = hours * rate
        otp = (hours - 40.00) * (rate * 0.5)
        pay = reg + otp
    else:
        pay = hours * rate
    return pay


hours = input('Enter hours: \n')
rate = input('Enter Rate: \n')
fhours = float(hours)
frate = float(rate)

xp = computepay(fhours, frate)
print("Pay:", xp)
