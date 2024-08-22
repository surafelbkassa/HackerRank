if __name__ == '__main__':
    N = int(input())
    arr=[]
    for i in range(N):
        cmd=map(str,input().split())
        cmd_List=list(cmd)
        if cmd_List[0]=="insert":
            arr.insert(int(cmd_List[1]),int(cmd_List[2]))
        elif cmd_List[0]=="print":
            print(arr)
        elif cmd_List[0]=="remove":
            arr.remove(int(cmd_List[1]))
        elif cmd_List[0]=="append":
            arr.append(int(cmd_List[1]))
        elif cmd_List[0]=="sort":
            arr.sort()
        elif cmd_List[0]=="pop":
            arr.pop()
        elif cmd_List[0]=="reverse":
            arr.reverse()
    
        
        