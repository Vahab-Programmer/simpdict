from itertools import permutations,combinations,product
from math import factorial
def aps(data:str)->list[str]:
    output=list()
    for i in range(len(data)):
        output.append(data[i:])
        if data[:i]:output.append(data[:i])
    output.extend(data.strip())
    output=list(set(output))
    return output
def apc(data:str)->list[str]:
    output=[]
    cases=([i.upper(),i.lower()] for i in data)
    for i in product(*cases):
        output.append("".join(i))
    return output
def cts(data:list[str])->list[str]:
    output=[]
    for i in data:
        if i !="":output.append(i)
    return output
def capp(data:list[list[str]])->int:
    nec=[col for col in data if len([x for x in col if x.strip()!=""])>0]
    total=0
    n=len(nec)
    for r in range(1,n+1):
        for cols in combinations(nec,r):
            count=1
            for col in cols:
                count*=len([x for x in col if x.strip()!=""])
            total+=factorial(r)*count
    return total
def generate_cases(*data)->str:
    for i in product(*data):
        if len(cts(i))==0:continue
        for x in permutations(cts(i)):
            yield "".join(x)
def main()->None:
    collection=[]
    first=input("First Name:")
    last=input("Last Name:")
    year=input("Year Of Birth:")
    mon=input("Month Of Birth:")
    day=input("Day Of Birth:")
    phone=input("Phone Number:")
    nation=input("National Code:")
    word=input("Enter Word(s) To Include (Seperator Is Space):")
    number=input("Enter Number(s) To Include (Seperator Is Space):")
    char=input("Enter Character(s) To Include:")
    if first:
        tmp=[""]
        for i in apc(first):
            tmp.extend(aps(i))
        collection.append(tmp)
    if last:
        tmp=[""]
        for i in apc(last):
            tmp.extend(aps(i))
        collection.append(tmp)
    if phone:
        tmp=[""]
        tmp.extend(aps(phone))
        collection.append(tmp)
    if nation:
        tmp=["",nation]
        collection.append(tmp)
    if word:
        tmp=[""]
        word=list(set(word.split(" ")))
        for i in word:
            for x in apc(i):
                tmp.extend(aps(x))
        collection.append(tmp)
    if number:
        tmp = [""]
        numbers=list(set(number.split(" ")))
        for i in numbers:
            tmp.extend(aps(i))
        collection.append(tmp)
    if char:
        tmp=[""]
        tmp.extend(list(set(char.strip())))
        collection.append(tmp)
    if year:
        collection.append(["",year])
    if mon:
        collection.append(["",mon])
    if day:
        collection.append(["",day])
    coa=capp(collection)
    pc=0
    with open("Dictionary.txt","tw") as file:
        for out in generate_cases(*collection):
            pc+=1
            print("\rTotal:{} || Generated:{} || Remaining:{}".format(coa,pc,coa-pc),end="")
            file.write(out+"\n")
    print("\n\rAll Password Generated SuccessFully")
main()