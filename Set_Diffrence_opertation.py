# Enter your code here. Read input from STDIN. Print output to STDOUT
def Diffrence():
    English=int(input())
    English_Set=set(input().split())
    French=int(input())
    French_Set=set(input().split())
    print(len(English_Set.difference(French_Set)))
Diffrence()