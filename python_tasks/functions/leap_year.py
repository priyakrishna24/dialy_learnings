def leapyear(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                print("Leap year")
            else:
                print('not')
        else:
            print("leap year")
    else:
        print("Not leap year")

leapyear(2030)