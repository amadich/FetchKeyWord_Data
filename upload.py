from pickle import*
from random import*
def get_user():
    
    
    x = randint(0,1)
    k = randint(1,999)
    if x == 0:
        fb = open("keyword/user_boys.txt","r")
        user = fb.readlines()
        username = user[k]
        fb.close()
        
    elif x == 1:
        fg = open("keyword/user_girls.txt","r")
        user = fg.readlines()
        username = user[k]
        fg.close()
    return username
        
def get_pwd():
    t = randint(1,498)
    fp = open("keyword/pwd.txt","r")
    pwd = fp.readlines()
    password = pwd[t]
    return password
username = get_user()
password = get_pwd()

print("Username : ",username, "\nPassword : ", password )
f = open("0x001.dat","ab")
d = {}
d["username"] = username
d["password"] = password
dump(d,f)
f.close()