# FetchKeyWord_Data
Here we generate random account headers received from databases or data profiles to obtain login information . 
###
#This function receives a file, selects one of them, and displays one result from one of the two files
```py
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

```
# Result
```shell
Username :  MERCER
Password :  6969
```
#
