
import sys

# f=open("dd.txt","r")
# f=sys.stdin

reg={"000":0,"001":0,"010":0,"011":0,"100":0,"101":0,"110":0,"111":"0000000000000000"}
def binaryconvert(a):
    b=str(bin(int(a)))
    no='0'*(10-len(b))+b[2:]
    return no


def inttobinary(a,l):
    b=bin(a)[2:]
    b='0'*(l-len(b))+b
    return b

def execute(inst,pc):
    opcode=inst[:5]
    #addition
    if(opcode=="10000"):
        a=inst[7:10]
        b=inst[10:13]
        c=inst[13:16]
        reg[a]=reg[b]+reg[c]
        pc+=1
        reg['111']='0000000000000000'
        if (reg[a]>65535):
            reg['111']='0'*12+'1000'
            reg[a]=reg[a]%65536
    #SUBTRACTION
    elif(opcode=="10001"):
        a=inst[7:10]
        b=inst[10:13]
        c=inst[13:16]
        reg[a]=reg[b]-reg[c]
        pc+=1
        reg['111']='0000000000000000'
        if (reg[a]>65535):
            reg['111']='0'*12+'1000'
            reg[a]=reg[a]%65536
    #move immediate
    elif(opcode=="10010"):
        a=inst[5:8]
        b=inst[8:16]
        reg[a]=int(b,2)
        pc+=1
        reg['111']='0000000000000000'
        if (reg[a]>65535):
            reg['111']='0'*12+'1000'
            reg[a]=reg[a]%65536
    #move register
    elif(opcode=="10011"):
        a=inst[10:13]
        b=inst[13:16]
        reg[b]=reg[a]
        pc+=1
        reg['111']='0000000000000000'
        if (reg[a]>65535):
            reg['111']='0'*12+'1000'
            reg[a]=reg[a]%65536
    #load
    if(opcode=="10100"):
        a=inst[5:8]
        b=int(inst[8:16],2)
        reg[a]=int(mem[b],2)
        pc+=1
        reg['111']='0000000000000000'
        if (reg[a]>65535):
            reg['111']='0'*12+'1000'
            reg[a]=reg[a]%65536
    #store
    if(opcode=="10101"):
        a=inst[5:8]
        b=int(inst[8:16],2)
        mem[b]=inttobinary(reg[a],16)
        pc+=1
        reg['111']='0000000000000000'
        if (reg[a]>65535):
            reg['111']='0'*12+'1000'
            reg[a]=reg[a]%65536
    #multiply
    if(opcode=="10110"):
        a=inst[7:10]
        b=inst[10:13]
        c=inst[13:16]
        reg[a]=reg[b]*reg[c]
        pc+=1
        reg['111']='0000000000000000'
        if (reg[a]>65535):
            reg['111']='0'*12+'1000'
            reg[a]=reg[a]%65536
    #divide
    if(opcode=="10111"):
        b=inst[10:13]
        c=inst[13:16]
        reg["000"]=reg[b]/reg[c]
        reg["001"]=reg[b]%reg[c]
        pc+=1
        reg['111']='0000000000000000'
        if (reg[a]>65535):
            reg['111']='0'*12+'1000'
            reg[a]=reg[a]%65536
    #right shift
    if(opcode=="11000"):
        a=inst[5:8]
        b=inst[8:16]
        reg[a]=reg[a]>>int(b,2)
        pc+=1
        reg['111']='0000000000000000'
        if (reg[a]>65535):
            reg['111']='0'*12+'1000'
            reg[a]=reg[a]%65536
    #left shift
    if(opcode=="11001"):
        a=inst[5:8]
        b=inst[8:16]
        reg[a]=reg[a]<<int(b,2)
        pc+=1
        reg['111']='0000000000000000'
        if (reg[a]>65535):
            reg['111']='0'*12+'1000'
            reg[a]=reg[a]%65536
    #ex or
    if(opcode=="11010"):
        a=inst[7:10]
        b=inst[10:13]
        c=inst[13:16]
        reg[c]=reg[a]^reg[b]
        pc+=1
        reg['111']='0000000000000000'
        if (reg[a]>65535):
            reg['111']='0'*12+'1000'
            reg[a]=reg[a]%65536
    #or
    if(opcode=="11011"):
        a=inst[7:10]
        b=inst[10:13]
        c=inst[13:16]
        reg[a]=reg[b]|reg[c]
        pc+=1
        reg['111']='0000000000000000'
        if (reg[a]>65535):
            reg['111']='0'*12+'1000'
            reg[a]=reg[a]%65536
    #and
    if(opcode=="11100"):
        a=inst[7:10]
        b=inst[10:13]
        c=inst[13:16]
        reg[a]=reg[b]&reg[c]
        pc+=1
        reg['111']='0000000000000000'
        if (reg[a]>65535):
            reg['111']='0'*12+'1000'
            reg[a]=reg[a]%65536
    #invert
    if(opcode=="11101"):
        b=inst[10:13]
        c=inst[13:16] 
        reg[c]=~reg[b]
        pc+=1
        reg['111']='0000000000000000'
        if (reg[c]>65535):
            reg['111']='0'*12+'1000'
            reg[c]=reg[c]%65536
    #compare
    if(opcode=="11110"):
        a=inst[10:13]
        b=inst[13:16]
        if(reg[a]==reg[b]):
            reg['111']='0000000000000001'
        if(reg[a]>reg[b]):
            reg['111']='0000000000000010'
        if(reg[a]<reg[b]):
            reg['111']='0000000000000100'
        pc+=1
    #unconditional jump
    if(opcode=="11111"):
        a=inst[8:16]
        pc=int(a,2)
        reg['111']='0000000000000000'
    #jump if less than
    if(opcode=="01100"):
        a=inst[8:16]
        if(reg["111"][13]=='1'):
            pc=int(a,2)
        else:
            pc+=1
        reg['111']='0000000000000000'
    #jump if greater than
    if(opcode=="01101"):
        a=inst[8:16]
        if(reg["111"][14]=='1'):
            pc=int(a,2)
        else:
            pc+=1
        reg['111']='0000000000000000'
    #jump if equal
    if(opcode=="01111"):
        a=inst[8:16]
        if(reg["111"][15]=='1'):
            pc=int(a,2)
        else:
            pc+=1
        reg['111']='0000000000000000'
    #hlt
    if(opcode=="01010"):
        pc+=1
        reg['111']='0000000000000000'

    
    
    if(opcode=="01010"):
        return True,pc
    else:
        return False,pc


mem=[]
code=[]
a=sys.stdin.read()
# a=f.read()
a=a.split('\n')
for line in a:
    if(len(line)>0):
        mem.append(line)

# mem[-1]=mem[-1]+'0'
# print(len(mem))
while(len(mem)<=255):
    mem.append('0000000000000000')
# print(mem)
pc=0
halt=False
while(not halt):
    Instruction=mem[pc]
    print(inttobinary(pc,8),end=" ")
    halt,pc=execute(Instruction,pc)
    # print(inttobinary(pc-1,8),end=" ")
    for i in reg:
        if(i=='111'):
            no=reg[i]
        else:
            no=inttobinary(reg[i],16)
        print(no,end=" ")
    print()
# print(len(mem))
for line in mem:
    if(len(line)!=0):
        print(line)
# f.close()