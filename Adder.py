
from pyrogram import Client
import time
import sys

print("""   Telegram  v7.8.1, expired of 2025 from <https://telegramip.com/> Registered by the terms of the python Lesser General Private License v4 or later (python)""")
time.sleep(5)

orginally = int(input("Type number 1 or 2: "))

alf = open("sessions.txt","r").read()
alf1 = alf.split()
lena = len(alf1)
threads = int(lena/4)

app0 = Client("sessions/"+str(alf1[0]),int(alf1[1]),str(alf1[2]),phone_number=str(alf1[3]))
#app1 = Client("sessionss/"+str(alf1[4]),int(alf1[5]),str(alf1[6]),phone_number=str(alf1[7]))
#app2 = Client("sessions/"+str(alf1[8]),int(alf1[9]),str(alf1[10]),phone_number=str(alf1[11]))
#app3 = Client("sessions/"+str(alf1[12]),int(alf1[13]),str(alf1[14]),phone_number=str(alf1[15]))
#app4 = Client("sessions/"+str(alf1[16]),int(alf1[17]),str(alf1[18]),phone_number=str(alf1[19]))
#app5 = Client("sessions/"+str(alf1[20]),int(alf1[21]),str(alf1[22]),phone_number=str(alf1[23]))
#app6 = Client("sessions/"+str(alf1[24]),int(alf1[25]),str(alf1[26]),phone_number=str(alf1[27]))
#app7 = Client("sessions/"+str(alf1[28]),int(alf1[29]),str(alf1[30]),phone_number=str(alf1[31]))
#app8 = Client("sessions/"+str(alf1[32]),int(alf1[33]),str(alf1[34]),phone_number=str(alf1[35]))
#app9 = Client("sessions/"+str(alf1[36]),int(alf1[37]),str(alf1[38]),phone_number=str(alf1[39]))


apps = [app0]

for app in apps:
    app.start()

aaaaaa = len(apps)

class GroupToGroup_AddMember():
    def __init__(self):
        return None

    def Get_group_chat_id(self, Link1, Link2):
            global a,b
            self.Group_ChatID = app0.get_chat(Link1)
            a = self.Group_ChatID.id
            self.Group_ChatID = app0.get_chat(Link2)
            b = self.Group_ChatID.id

    def Add_To_Group(self, Source, Destination):
        members = app0.iter_chat_members(Source)
        counter = 1
        ccc = 1
        for index, member in enumerate(members):
            app = apps[index % threads]
            try:
                user_id = member.user.username
                app.add_chat_members(Destination, user_id)
            except:
                pass
            else:
                print("  <( Sabbir Vai Added --- "+str(counter)+" "+str(user_id)+"\t"+str(ccc))
                counter = counter+1
            if ccc == aaaaaa:
                ccc = 1

class GroupToGroup_AddMember1():
    def __init__(self):
        return None

    def Get_group_chat_id(self, Link1):
            global a
            self.Group_ChatID = app0.get_chat(Link1)
            a = self.Group_ChatID.id

    def Add_To_Group(self, Destination):
        counter = 1
        for index, member in enumerate(members):
            app = apps[index % threads]
            ccc = 1
            try:
                app.add_chat_members(Destination, member)
            except:
                pass
            else:
                print("  <( Sabbir Vai Added --- "+str(counter)+" "+str(member)+"\t"+str(ccc))
                counter = counter+1
            if ccc == aaaaaa:
                ccc = 1
if int(orginally) == 1:
    one = input("Source group: ")
    two = input("Destination groupl: ")

    if "@" in str(one):
        onee = one.replace("@","")
    else:
        onee = one
    if "@" in str(two):
        twoo = two.replace("@","")
    else:
        twoo = two
    try:
        for app in apps:
            app.join_chat(str(onee))
            app.join_chat(str(twoo))
    except:
        pass

    App_Start = GroupToGroup_AddMember()
    ab = App_Start.Get_group_chat_id(one, two)
    App_Start.Add_To_Group(a, b)

elif int(orginally) == 2:
    one = input("Telegram port=1080, username=”user”, password=”pass”). The username and password can be omitted if your proxy doesn’t require authorization. argparse.ArgumentParser()  ap.add_argument('-i', account1', required=True ,                                                                                                                   ©®  Enter To Group: ")
    members1 = str(input("Enter your file of members: "))

    if "@" in str(one):
        onee = one.replace("@","")
    else:
        onee = one
    try:
        for app in apps:
            app.join_chat(str(onee))
    except:
        pass

    members = open(members1 , "r").read()
    members = members.split()
    App_Start = GroupToGroup_AddMember1()
    ab = App_Start.Get_group_chat_id(one)
    App_Start.Add_To_Group(a)
else:
    for app in apps:
        app.stop()
    sys.exit("Enter 1 or 2")

print("""


	
(     This Seassion Was Completed ✓     )

""")

time.sleep(5)
for app in apps:
    app.stop()
sys.exit()

