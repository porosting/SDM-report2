#!/usr/bin/python3

import re
                
def calc(A,B):
        if isinstance(A, int) and isinstance(B, int):
                a=A
                b=B
                if 1 <= a and 1<=b and a<=999 and b<=999:
                        valid=True
                else:
                        valid=False
        else:
                valid=False
        if valid:
                ans=a*b
                return ans
        else:
                return -1

def main ():
	matchstring = ''
	while matchstring != 'end':
                A = input ('input A: ')
                B = input ('input B: ')
                print ('input A * input B = ', calc(A,B))

if __name__ == '__main__':
	main()