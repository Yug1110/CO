import sys
A={"add":"10000","sub":"10001","mul":"10110","xor":"11010","or":"11011","and":"11100"}
B={"mov":"10010","rs":"11000","ls":"11001"}
C={"mov":"10011","div":"10111","cmp":"11110","not":"11101"}
D={"ld":"10100","st":"10101"}
F={"hlt":"01010"}
E={"jmp":"11111","jlt":"01100","jgt":"01101","je":"01111"}


REG={"R0":"000","R1":"001","R2":"010","R3":"011","R4":"100","R5":"101","R6":"110","FLAGS":"111"}
# f=open("x.txt","r")
a= sys.stdin.read()
# a=f.read()
l=a.split("\n")
l1=[]
l_var=[]
l_labels={}
l_ans=[]
ans=""
count=0
l_var1=[]
j=1
x=[]
p=0
st=0
for i in l:
    x=i.split()
    # print(x)
    l1.append(x)
    # print(l1)
    if len(x)==0:
        count+=1
    elif x[0]=="var":
        if(len(x)==2):
            l_var.append(x[1])
    elif x[0][-1]==":":
        l_labels[x[0]]=st+1
        if len(x)==3:
            if(x[1]=="var"):
                l_var.append(x[2])
    elif x[0]!="var":
        count +=1
    st +=1

# print(l1)
    
for i in l1:
    if(i==[]):
        continue
    cmd=i[0]
    ans=""
    if i[0]=="var":
        if len(i)!=2:
            print(f"General Syntax Error in {j}")
            p=1
            break
        l_var1.append(i[1])

    elif i[0][-1]==":":
        if(len(i)==1):
            print(f"General Syntax Error in {j}")
            p=1
            break
        k=i[1:]
        cmd=k[0]
        if(cmd=="mov" and i[2][0]=="$"):
            if(len(i)!=3):
                print(f"General syntax error in {j}")
                p=1
                break
            if(i[2][0]!="$"):
                print(f"Typos in instruction name or register name in {j}")
                p=1
                break   
            try:
                x=int(i[2][1:])
            except:
                print(f"General syntax error in {j}")
                p=1
                break
            if(i[1] not in REG.keys() ):
                print(f"General syntax error in {j}")
                p=1
                break
            if(i[1]=="FLAGS"):
                print(f"Illegal use of FLAGS in {j}")
                p=1
                break
            w=int(i[2][1:])
            if(w>255 and w<0):
                print(f"No not in range in {j}")
                p=1
                break
            binary=str(bin(int(i[2][1:])))
            binary=binary[2:]
            if (len(binary)>8 or binary[0]==1):
                print(f"Illegal use of immediate values in {j}")
                p=1
                break
            ans=ans+B[i[0]]
            ans=ans+REG[i[1]]
            while(len(binary)<8):
                binary="0"+binary
            ans=ans+binary
            l_ans.append(ans)

        elif (cmd=="mov"):
            if(len(i)!=3):
                print(f"General syntax error in {j}")
                p=1
                break
            if(i[1] not in REG.keys() or i[2] not in REG.keys()):
                print(f"Typos in instruction name or register name in {j}")
                p=1
                break
            if(i[1]=="FLAGS" or i[2]=="FLAGS"):
                print(f"Illegal use of FLags in {j}")
                p=1
                break
            ans=ans+C[i[0]]
            ans=ans+"00000"
            ans=ans+REG[i[1]]+REG[i[2]]
            l_ans.append(ans)


        elif cmd in A.keys():
            if (len(k)!=4):
                print(f"General syntax error in {j}")
                p=1
                break
            ans=ans+A[cmd]
            ans=ans+"00"
            if(k[1] not in REG.keys() or k[2] not in REG.keys() or k[3] not in REG.keys()):
                print(f"Typos in instruction name or register name in {j}")
                p=1
                break
            if(k[1]=="FLAGS" or k[2]=="FLAGS" or k[3]=="FLAGS"):
                print(f"Typos in instruction name or register name in {j}")
                p=1
                break
            ans=ans+REG[k[1]]+REG[k[2]]+REG[k[3]]
            l_ans.append(ans)



        elif cmd in B.keys():
            if(len(k)!=3):
                print(f"General syntax error in {j}")
                p=1
                break
            if(k[2][0]!="$"):
                print(f"Typos in instruction name or register name in {j}")
                p=1
                break   
            try:
                x=int(k[2][1:])
            except:
                print(f"General syntax error in {j}")
                p=1
                break
            if(k[1] not in REG.keys() ):
                print(f"General syntax error in {j}")
                p=1
                break
            if(k[1]=="FLAGS"):
                print(f"Illegal use of FLAGS in {j}")
                p=1
                break
            w=int(k[2][1:])
            if(w>255 and w<0):
                print(f"No not in range in {j}")
                p=1
                break
            binary=str(bin(int(k[2][1:])))
            binary=binary[2:]
            if (len(binary)>8 or binary[0]==1):
                print(f"Illegal use of immediate values in {j}")
                p=1
                break
            ans=ans+B[k[0]]
            ans=ans+REG[k[1]]
            while(len(binary)<8):
                binary="0"+binary
            ans=ans+binary
            l_ans.append(ans)



        elif cmd in C.keys():
            if(len(k)!=3):
                print(f"General syntax error in {j}")
                p=1
                break
            if(k[1] not in REG.keys() or k[2] not in REG.keys()):
                print(f"Typos in instruction name or register name in {j}")
                p=1
                break
            if(k[1]=="FLAGS" or k[2]=="FLAGS"):
                print(f"Illegal use of FLags in {j}")
                p=1
                break
            ans=ans+C[k[0]]
            ans=ans+"00000"
            ans=ans+REG[k[1]]+REG[k[2]]
            l_ans.append(ans)



        elif cmd in D.keys():
            if(len(k)!=3):
                print(f"General Syntax Error in {j}")
                p=1
                break
            if(k[1] not in REG.keys()):
                print(f"Typos in register name in {j}")
                p=1
                break
            if(k[1]=="FLAGS"):
                print(f"Illegal use of FLags in {j}")
                p=1
                break
            if(k[2] not in l_var1 and k[2] in l_labels.keys()):
                print(f"Misuse of labels as variables")
                p=1
                break

            if(k[2] not in l_var1):
                print(f"Variables not declared in beginning in {j}")
                p=1
                break

            ans=ans+D[k[0]]
            ans=ans+REG[k[1]]
            index=l_var.index(k[2])
            index=count+index
            binary=str(bin(int(index)))
            binary=binary[2:]
            while(len(binary)<8):
                binary="0"+binary
            ans=ans+binary
            l_ans.append(ans)

    
        elif cmd in E.keys():
            if(len(k)!=2):
                print(f"General syntax error in {j}")
                p=1
                break
            if(k[1] not in E.keys() and k[1] in l_var1):
                print(f"Misuse of variables as labels in {j}")
                p=1
                break
            if((k[1]+":") not in l_labels.keys()):
                print(k)
                print(f"Use of Undefined labels in {j}")
                p=1
                break
        
            ans=ans+E[k[0]]+"000"
            val=l_labels[k[1]+":"]
            binary=str(bin(int(val)))
            binary=binary[2:]
            while(len(binary)<8):
                binary="0"+binary
            ans=ans+binary
            l_ans.append(ans)

        elif cmd in F.keys():
            ans=ans+F[cmd]+"00000000000"
            l_ans.append(ans)
            break
    
    elif(cmd=="mov" and i[2][0]=="$"):
        if(len(i)!=3):
            print(f"General syntax error in {j}")
            p=1
            break
        if(i[2][0]!="$"):
            print(f"Typos in instruction name or register name in {j}")
            p=1
            break   
        try:
            x=int(i[2][1:])
        except:
            print(f"General syntax error in {j}")
            p=1
            break
        if(i[1] not in REG.keys() ):
            print(f"General syntax error in {j}")
            p=1
            break
        if(i[1]=="FLAGS"):
            print(f"Illegal use of FLAGS in {j}")
            p=1
            break
        w=int(i[2][1:])
        # print(w)
        if(w>255 or w<0):
            print(f"No not in range in line {j}")
            p=1
            break
        binary=str(bin(int(i[2][1:])))
        binary=binary[2:]
        if (len(binary)>8 or binary[0]==1):
            print(f"Illegal use of immediate values in {j}")
            p=1
            break
        ans=ans+B[i[0]]
        ans=ans+REG[i[1]]
        while(len(binary)<8):
            binary="0"+binary
        ans=ans+binary
        l_ans.append(ans)

    elif (cmd=="mov"):
        if(len(i)!=3):
            print(f"General syntax error in {j}")
            p=1
            break
        if(i[1] not in REG.keys() or i[2] not in REG.keys()):
            print(f"Typos in instruction name or register name in {j}")
            p=1
            break
        if(i[1]=="FLAGS" or i[2]=="FLAGS"):
            print(f"Illegal use of FLags in {j}")
            p=1
            break
        ans=ans+C[i[0]]
        ans=ans+"00000"
        ans=ans+REG[i[1]]+REG[i[2]]
        l_ans.append(ans)

        


    elif cmd in A.keys():
        if (len(i)!=4):
            print(f"General syntax error in {j}")
            p=1
            break
        ans=ans+A[cmd]
        ans=ans+"00"
        if(i[1] not in REG.keys() or i[2] not in REG.keys() or i[3] not in REG.keys()):
            print(f"Typos in instruction name or register name in {j}")
            p=1
            break
        if(i[1]=="FLAGS" or i[2]=="FLAGS" or i[3]=="FLAGS"):
            print(f"Typos in instruction name or register name in {j}")
            p=1
            break
        ans=ans+REG[i[1]]+REG[i[2]]+REG[i[3]]
        l_ans.append(ans)



    elif cmd in B.keys():
        if(len(i)!=3):
            print(f"General syntax error in {j}")
            p=1
            break
        if(i[2][0]!="$"):
            print(f"Typos in instruction name or register name in {j}")
            p=1
            break   
        try:
            x=int(i[2][1:])
        except:
            print(f"General syntax error in {j}")
            p=1
            break
        if(i[1] not in REG.keys() ):
            print(f"General syntax error in {j}")
            p=1
            break
        if(i[1]=="FLAGS"):
            print(f"Illegal use of FLAGS in {j}")
            p=1
            break
        w=int(i[2][1:])
        if(w>255 or w<0):
            print(f"No. not in range in {j}")
            p=1
            break
        binary=str(bin(int(i[2][1:])))
        binary=binary[2:]
        if (len(binary)>8 or binary[0]==1):
            print(f"Illegal use of immediate values in {j}")
            p=1
            break
        ans=ans+B[i[0]]
        ans=ans+REG[i[1]]
        while(len(binary)<8):
            binary="0"+binary
        ans=ans+binary
        l_ans.append(ans)



    elif cmd in C.keys():
        if(len(i)!=3):
            print(f"General syntax error in {j}")
            p=1
            break
        if(i[1] not in REG.keys() or i[2] not in REG.keys()):
            print(f"Typos in instruction name or register name in {j}")
            p=1
            break
        if(i[1]=="FLAGS" or i[2]=="FLAGS"):
            print(f"Illegal use of FLags in {j}")
            p=1
            break
        ans=ans+C[i[0]]
        ans=ans+"00000"
        ans=ans+REG[i[1]]+REG[i[2]]
        l_ans.append(ans)



    elif cmd in D.keys():
        if(len(i)!=3):
            print(f"General Syntax Error in {j}")
            p=1
            break
        if(i[1] not in REG.keys()):
            print(f"Typos in register name in {j}")
            p=1
            break
        if(i[1]=="FLAGS"):
            print(f"Illegal use of FLags in {j}")
            p=1
            break
        if(i[2] not in l_var1 and i[2] in l_labels.keys()):
            print(f"Misuse of labels as variables")
            p=1
            break

        if(i[2] not in l_var1):
            print(f"Variables not declared in beginning in {j}")
            p=1
            break

        ans=ans+D[i[0]]
        ans=ans+REG[i[1]]
        index=l_var.index(i[2])
        index=count+index
        binary=str(bin(int(index)))
        binary=binary[2:]
        while(len(binary)<8):
            binary="0"+binary
        ans=ans+binary
        l_ans.append(ans)

    
    elif cmd in E.keys():
        if(len(i)!=2):
            print(f"General syntax error in {j}")
            p=1
            break
        if(i[1] not in E.keys() and i[1] in l_var1):
            print(f"Misuse of variables as labels in {j}")
            p=1
            break
        if(i[1] not in E.keys()):
            print(f"Use of Undefined labels")
            p=1
            break
        
        ans=ans+E[i[0]]+"000"
        val=l_labels[i[2]]
        binary=str(int(bin(val)))
        binary=binary[2:]
        while(len(binary)<8):
            binary="0"+binary
        ans=ans+binary
        l_ans.append(ans)

    elif cmd in F.keys():
        ans=ans+F[cmd]+"00000000000"
        l_ans.append(ans)
        break

#ERROR HANDLING
    else:
        print(f"Typos in instruction name or register name in {j}")
        p=1
    j=j+1
try:
    index=l.index("hlt")
except:
    index=-1

if(l.count("hlt")>1):
    print("More than required hlt commands")
    p=1
    

check=0
if index==-1:
    p=1
    print("Missing hlt instruction")
    check =1

if check==0:
    for i in range(index+1,len(l1)):
        if(l1[i]!=[]):
            p=1
            print("hlt is not last instruction")
            break
    
if p==0:
    for i in l_ans:
        print(i)