swimTime = float(input("Enter your swim time: "))
if swimTime < 55.0:
    print("Participant qualifies for gold category. ")
elif swimTime > 55.0 and swimTime <= 60.0:
    print("Participant qualifies for silver category. ")
elif swimTime > 60.0 and swimTime < 65.0:
    print("Participant qualifies for bronze category. ")
else:
    print("Participant does not qualify. ")