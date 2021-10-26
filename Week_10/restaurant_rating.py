vote= [0,0,0,0,0]
n=0
while(True):
    print('1-Very poor 2-Poor 3-Average 4-Good 5-Very good -1: Exit')
    try:
        x=int(input("Enter your vote:"))
        if(x==-1):
            break
        else:
            try:
                vote[x-1]+= 1
                n+=1
            except IndexError:
                print('list index out of range. try again')

    except ValueError:
        print("invalid data type. enter integer only")
print('Very poor:{} Poor={} Average:{} Good:{} Very good:{}'.format(vote[0],
                vote[1],vote[2],vote[3],vote[4]))
if(n>0):
 ave=(vote[0]+vote[1]*2+vote[2]*3+vote[3]*4+vote[4]*5)/n
print('average={}'.format(ave))
