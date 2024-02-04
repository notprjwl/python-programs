# You're trying to automate your alarm clock by writing a function for it. 
# You're given a day of the week encoded as 1=Mon, 2=Tue, ... 6=Sat, 7=Sun, and whether you are on vacation as a boolean value (A Boolean object is either True or False). Based on the day and whether you're on vacation, write a function that returns a time in the form of a string indicating when the alarm clock should ring. 
# When not on vacation, on weekdays, the alarm should ring at '7:00' and on the weekends

# if vacation:
# weekdays - 1-5 ; 10:00 AM
# weekends  - 6-7 ; "OFF"

# if not vacation:
# weekdays - 1-5 ; 7:00 AM
# weekends - 6-7 ; 10:00 AM


def automate_alarm(day, vacation):
    weekdays = [1, 2, 3, 4, 5]
    weekends = [6, 7]
    
    if (day in weekdays) and (vacation == True):
        return "10:00 AM"
    elif (day in weekends) and (vacation == True):
        return "OFF"  
    elif (day in weekdays) and (vacation == False):
        return "7:00 AM"
    elif (day in weekends) and (vacation == False):
        return "10:00 AM" 
    else:
        return "enter a number between 1-7 and a boolean value"
    
        
day = int(input())
vacation = (input("are you on a vacation(True/False): ").capitalize()=="True")  
print(automate_alarm(day, vacation))