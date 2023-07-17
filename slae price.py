Friday = input("Is it friday? I will give you an extra 10 percent off as well")
tag = int(input("Enter your tag price, I will give up a coupon that is 10 percent off:"))
Step1 = tag*10
Step2 = Step1/100
FinalPriceNotFriday = tag - Step2

if Friday == 'Yes':
    
    Step1Friday = FinalPriceNotFriday*10
    Step2Friday = Step1Friday/100
    FinalPrice = FinalPriceNotFriday - Step2Friday


    print("This is your final price to pay:", FinalPrice)

else:
    print("This is your final price to pay:", FinalPriceNotFriday)