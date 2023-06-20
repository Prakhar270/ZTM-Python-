#f = open("test.txt","r")
#print(f.read(50))
#print(f.name)
#print(f.mode)
#content = f.readlines()
#print(content)
#for lines in f:
    #print(lines, end = " ")
f=open("test.txt",'r')
read=f.readlines()
f.close()
idi=[]
for ln in read:
    if ln.startswith("T"):
        idi.append(ln)
print(idi)

print([ (a,b) for a in range(3) for b in range(a) ])
