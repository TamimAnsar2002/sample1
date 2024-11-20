b=[3,4,2,1,6,12,16]
b.sort()

def binary(datas,start,last,target):
    if start <= last:
        mid=(start+last)//2
##        print(mid)
        if datas[mid]==target:
            return mid
        elif datas[mid]<target:
            return binary(datas,mid+1,last,target)
        else:
            return binary (datas,start,mid-1,target)
    else:
        return -1
t=int(input("target :"))
result=binary(b,0,len(b)-1,t)
if result>0:
    print(f"index :{result}")
else:
    print("target not in the list")
    