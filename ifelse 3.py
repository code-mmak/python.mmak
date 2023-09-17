is_vacation = input("are you on a vacation?")
is_weekday = input("is it a weekday")
if is_vacation == "yes" or is_weekday != "yes":
    print("you can sleep in late")
else:
    print("you can not sleep late")