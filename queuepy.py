queue=[]

def enQ():
    queue.append(input('Enter new string:').strip())

def deQ():
    if len(queue)==0:
        print('Cannot pop from an empty queue!')
    else:
        print('remove[%s]'%queue.pop(0))

def viewQ():
    print(queue)

cmds={'e':enQ,'d':deQ,'v':viewQ}

def showmenu():
    pr="""
(E)nqueue
(D)equeue
(V)iew
(Q)uit
Enter choice:"""
    while True:
        while True:
            try:
                choice=input(pr).strip()[0].lower()
            except (EOFError,KeyboardInterrupt,IndexError):
                choice='q'

            print('\nYou picked:[%s]'%choice)
            if choice not in 'devq':
                print('Invalid option,try agagin')
            else:
                break
        if choice=='q':
            break
        cmds[choice]()

if __name__=='__main__':
    showmenu()
            
