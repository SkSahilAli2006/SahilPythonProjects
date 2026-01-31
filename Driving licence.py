#Driving Licence - Test Programm
while True:
    try:
        name = input("Enter candidate name: ").upper()
        age = int(input("Enter Candidate Age: "))

        if age >= 18 and age <= 100:
            print("You Are Eligible For DL-Test")
            print("Your Test Will be conducted on car Track. Go There!")


            while True:

                test = input("DL-Test -> Pass OR Fail: ").lower()

                if test == "pass":
                    print(name,"Passed Test - You Will Receive Your DL after a few days")
                    break
                elif test == "fail":
                    print(name,"Failed Test - Try Again After a Week")
                    break
                else:
                    print("Invalid Input (Choose - Pass/Fail)")

            break
        else:
            print("You Are Not Eligible For DL-Test")
            break
    except ValueError:
        print("Invalid Age! Please Enter a valid Integer number.")