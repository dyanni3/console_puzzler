import numpy as np
import sys
import pandas #pointless

def swap(i1, i2, arr):
    save = arr[i1[0], i1[1]]
    arr[i1[0],i1[1]] = arr[i2[0],i2[1]]
    arr[i2[0],i2[1]] = save
    return(arr)

def move(dir_, a):
    zpos = np.where(a==0)
    i1 = (zpos[0][0],zpos[1][0])
    i2 = list(i1)
    if dir_ == 'd':
        i2[0]+=1
    if dir_ == 'r':
        i2[1] += 1
    if dir_ == 'l':
        i2[1] -= 1
    if dir_ == 'u':
        i2[0] -= 1
    i2 = tuple(i2)
    return(swap(i1, i2, a))

def pprint(a):
    for row in a:
        print(' '+str(row).replace('[','').replace(']','').replace('0',' '), flush=True)

def play(a):
    while(True):
        
        pprint(a)
        sys.stdout.flush()
        dir_ = input()
        d = 'f'
        if dir_ == 'w':
            d = 'u'
        if dir_ == 's':
            d = 'd'
        if dir_ == 'd':
            d = 'r'
        if dir_ == 'a':
            d = 'l'
        if dir_ == 'q':
            break
        try:
            move(d, a)
        except:
            print('illegal')

def make_board():
	while(True):
		try:
			m = int(input("number of rows: "))
			break
		except:
			print("please enter integer")
	while(True):
		try:
			n = int(input("number of cols: "))
			break
		except:
			print("please enter integer")
	a = np.arange(m*n)
	np.random.shuffle(a)
	a = a.reshape(m,n)
	return(a)

if __name__ == '__main__':
	a = make_board()
	pprint(a)
	print("press q to quit")
	print("use w,a,s,d to move the empty space around")
	play(a)