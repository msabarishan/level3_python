remove()
discard()
append()
insert()
pop()
reverse()

Eg:
if __name__ == '__main__':
    N = int(input())
o_lst=[]  
for i in range(N):
    var=input()
    lst=var.split()
    
    cmd=lst[0]
    if cmd =='insert':
        o_lst.insert(int(lst[1]),int(lst[2]))
    elif cmd=='print':
        print(o_lst)
    elif cmd=='remove':
        o_lst.remove(int(lst[1]))
    elif cmd=='append':
        o_lst.append(int(lst[1]))
    elif cmd=='sort':
        o_lst=sorted(o_lst)
    elif cmd=='pop':
        o_lst.pop()
    else:
        o_lst.reverse()
            
