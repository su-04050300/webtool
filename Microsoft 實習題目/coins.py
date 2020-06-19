def count(a = []):
    con_sum=0
    a=list(map(int, a))#轉整數
    coin_num = a[0]
    a.pop(0)
    total = a[0]
    a.pop(0)
    a=sorted(a ,reverse=True)
        #print(a)
    for i in a:
        #print("i=",i)
        if total%i != i:
        #print("total%i != i")
            con_sum += total//i
            total = total%i
        #print("con_sum=",con_sum)
    #print("total=",total)
    if total!=0:
        return -1
    else:
        return con_sum  


def input_num():
    rows = int(input())
    List = [] # 宣告一個一維串列
    b=[]
    for i in range(0 ,rows):
        for j in range(0,2): 
            a = input()
            b += a.split()
        List.append(b)
        b = []
    return List

if __name__ == '__main__':
    List = input_num()
    for i in range(len(List)):
        print(count(List[i]))
       