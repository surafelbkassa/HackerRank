# Enter your code here. Read input from STDIN. Print output to STDOUT
def Union():
    English=int(input())
    English_List=set(input().split())
    French=int(input())
    French_List=set(input().split())
    print(len(English_List.union(French_List)))
Union()