
#IMPORTANT
#Riley,Is a virtual assistant
#   Copyright (C) 2021  Dexter
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 3 of the License, or
#   (at your option) any later version.
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software Foundation,
#   Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA
#   This is free software, and you are welcome to redistribute it







#imports
import json
import pickle






#defs

def write():
    while True:
        print("'done'to exit")
        name = input("what do you call the person:>> ")
        email = input("their gmail id:>> ")
        password = input("their google account password:>> ")
        a = name
        b = email
        c = password
        if "done" in name:
            break
        elif "done" in email:
            break
        elif "done" in password:
            break
        with open('a', 'ab') as handle:
            pickle.dump(a, handle, protocol=pickle.HIGHEST_PROTOCOL)
        with open('b', 'ab') as handle:
            pickle.dump(b, handle, protocol=pickle.HIGHEST_PROTOCOL)
        with open('c', 'ab') as handle:
            pickle.dump(c, handle, protocol=pickle.HIGHEST_PROTOCOL)


def mydata():
    
    lis = ["name" , "songs" , "band" , "wakeup" , "sleep" , "email" , "hobby" ,"youtube" , "password"]
    print("note that the time is 24 hour format")
    name = input("what should i call you?>> ")

    songs = input("what kind of songs do you like?>> ")
    band = input("what is your favorite band? >> ")
    your_email = input("your gmail id >>")
    your_password = input("google account password>> ")
    hobbies = input("what are your hobbies>> ")
    yt_channels = input("what is the channel you watch the most(only one)>> ")
    wakeup = input("what time do you generally wake up>> ")
    sleep_time = input("what time do you usually sleep?>> ")
    info = [name , songs , band , wakeup , sleep_time,your_email ,hobbies , yt_channels,your_password]
    
    with open('lis', 'ab') as handle:
        pickle.dump(lis, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('info', 'ab') as handle:
        pickle.dump(info, handle, protocol=pickle.HIGHEST_PROTOCOL)

def my_email():
    email = input("whats your email id?>>")
    pswd  = input("whatsa your password?>>>")
    
    with open('my_email', 'ab') as handle:
        pickle.dump(email, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('my_email_password', 'ab') as handle:
        pickle.dump(pswd, handle, protocol=pickle.HIGHEST_PROTOCOL)

def my_friends():
    
    na_me= input("what do you call the person:>> ")
    email_id = input("their gmail id:>> ")
    
    a = na_me
    b = email_id
    

    with open('na_me', 'ab') as handle:
        pickle.dump(a, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('email_id', 'ab') as handle:
        pickle.dump(b, handle, protocol=pickle.HIGHEST_PROTOCOL)
        
def dump_routine():
    time_ = input("time: ")
    activity_ = input("what do you do?:>> ")


    routine = {time_ : activity_}
    print(routine)
    while True:
        time_ = input("time: ")
        activity_ = input("what do you do?:>> ")
        if "done" in time_ or "done" in activity_:
            break
        else:
            routine.update({time_ : activity_})
            print(routine)
    with open('routine', 'ab') as handle:
        pickle.dump(routine, handle, protocol=pickle.HIGHEST_PROTOCOL)
        
print("enter done to save and exit or ctrl+c to discard and exit")
while True:
    inp = input("1;to tell me about yourself,2;to register devices,3;to gimme your email creds,4;tell me your routine,5;tell me about your friends")
    if inp == "1" or inp ==1:
        mydata()
    elif inp =="2" or inp==2:
        write()
    elif inp == "3" or inp ==3:
        my_email()
    elif inp == "4" or inp ==4:
        dump_routine()
    elif inp == "5" or inp ==5:
        my_friends()
        
    if inp == "done":
        print("changes made")
        print("bye")
    
