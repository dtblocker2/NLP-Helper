import time
import os
#------------------------------------------------

def space():
    return print("=======================================\n")
#------------------------------------------------

print("system intialising please wait........")
time.sleep(5)

pwd = int(input("\nplease enter your password: "))
if pwd == 12345:
    print("you have sucessfully gained access to the system")
    time.sleep(5)
    space()
    while True:
        user_name = input("mind telling me your name: ")
        if user_name == "skip":
            user_name = "Dhruva Kumar"
            age = 18
            gender = "male"
        while True:
            age = int(input("and age? "))
            if age > 100:
                print("please enter a valid age")
            elif age < 8:
                print("you are too young to make account")
            else:
                break
        while True:
            gender = input("and gender: ")
            a = 0
            gender_normalised = gender.lower()
            valid_genders = ["male", "female", "man", "woman"]
            for item in valid_genders:
                if gender_normalised == item:
                    a += 1
            if a > 0:
                break
            else:
                print("please enter a valid gender. we don't love rainbows")
        confirmation_of_details = input("do you want to confirm your details: ")
        if confirmation_of_details == "no":
            print("ok change it")
        else:
            print("details changed successfully")
            space()
            print("user details preview: \nname:", user_name, "\nage:", age, "\ngender:", gender)
            time.sleep(5)
            break
elif pwd == 1122:
    print("initialising special access to the creator")
    time.sleep(3)
    user_name = "dhruva majoka"
    age = 18
    gender = "male"
    space()
    print("user details preview: \nname:", user_name, "\nage:", age, "\ngender:", gender)
    time.sleep(5)
elif pwd == 1196:
    space()
    print("Work: dk30nov2005@gmail.com \npwd: 34sw_CjFE_iexF5 \n \nMS Office: dhruvamajoka@hotmail.com \npwd: dhruva@123 \nPIN: 1122 \n \nLinkedIn: dhruvamajoka@hotmail.com \npwd:J3udK:UfTUX!3pi \n \nVidhya Laxmi Portal: sureshkumar15ju@gmail.com \npwd: Suresh@57k \n \nDiscord: dk30nov2005@gmail.com \npwd: w224RD}X$E;p")
    space()
    print("exiting in 20 sec")
    time.sleep(20)
else:
    print("wrong password exiting....")
    time.sleep(5)
    quit()
#----------------------------------------------------

space()
print("You whats up", user_name, "i am J.A.R.V.I.S. prototype. i was made by dhruva majoka, a high school passout as a time pass.")
time.sleep(6)
print("my version is 0.2(previous version before me wasn't even able to run). \nmy creator knows very little about coding like he doesn't even know how to store data in file so that if i take your username now and never forget it later when reopened.")
time.sleep(6)
print("but thats not the problem atleast my creator is trying to learn some coding to make me")
time.sleep(5)
print("as i've mentioned earlier that my creator doesn't know much about coding also he isn't so smart to think of things that i can do, so i've limited my power so for now i will be able to do limited and random tasks. :O)")
time.sleep(10)

while True:
    print("what do you want me to do: \n0. to exit \n1. set up timer \n2. create a test file")

#------------------------------------------------
    response_1 = int(input("\nenter serial number of task: "))

#-----------------------------------------------
    if response_1 == 0:
        print("exiting")
        time.sleep(5)
        quit()

#-------------------------------------------------
    if response_1 == 1:
        i = int(input("enter time in seconds: "))
        def countdown(seconds):
            while seconds > 0:
                print("time remaining:", seconds, end='\r')
                time.sleep(1)
                seconds -= 1
        countdown(i)
        space()
        time.sleep(5)

#----------------------------------------------------
    if response_1 == 2:
        x = 0
        while True:
            x = str(x)
            file_path = "test_" + x +  ".py"
            if not os.path.isfile(file_path):
                with open(file_path, 'w') as file:
                    file.write("#this is new python file")
                break
            else:
                x = int(x)
                x += 1

        x = str(x)
        print("test_" + x + " created succesfully")
        space()
        time.sleep(5)