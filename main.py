rate = int(input("Enter your hourly rate: "))
try:
    int(rate)
except:
    print ("invalid input")
otrate = rate * 1.5
hours = int(input("Enter hours worked this week: "))
otpay = (hours - 40) * otrate



total = str(40 * rate)
totalWithOT = str(40 * rate + otpay)
yearly = str(2080 * rate)
yearlyWithOT = str((otpay * 52) + (rate * 2080))

if hours <= 40:
    print ("Your Weekly gross pay is $" + total)
    print("Without any overtime you will gross $" + yearly + " in a year")

elif hours > 40:
    totalWithOT = str((rate * 40) + (otpay))
    print ("Your weekly gross pay is $" + totalWithOT)
    print("With current overtime you will gross $" + yearlyWithOT + " in a year")


