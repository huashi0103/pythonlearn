#!/usr/bin/env python

db={}

def newuser():
    prompt='login desired:'
    while True:
        name=input(prompt)
        if name in db.keys():
            prompt='name taken,try another:'
            continue
        else:
            break
    pwd=input('passwd:')
    db[name]=pwd


def olduser():
    name=input('login:')
    pwd=input('passwd:')
    passwd=db.get(name)
    if passwd==pwd:
        print('welcome back %s'%name)
    else:
        print('login incorrect')


def showmenu():
    prompt="""
(N)ew User Login
(E)xisting User Login
(Q)uit
Example 7.1 Dictionary Example (userpw.py)(continued)
Enter choice:"""
    done=False
    while not done:
        chosen=False
        while not chosen:
            try:
                choice=input(prompt).strip()[0].lower()
            except(EOFError,KeyboardInterrupt):
                choice='q'
            print('\n You picked:[%s]'%choice)
            if choice not in 'neq':
                print('invalid option,try again')
            else:
                chosen=True
                done=True
    newuser()
    olduser()


if __name__=="__main__":
    showmenu()
    
