def read(file):
    x=0
    for line in open(file):
        if x>2:
            l = line.split()
            print(l)
            '''#print(l)
            data=l[-4:]
            #print(data)
            for i in data:
                if float(i)<-999:
                    print(line)'''
        x+=1





def main():
    read("data.txt")

main()