import time

def sing_verse(num):
	if num > 0:

	    print(num, "bottles of beer on the wall")
	    print(num, "bottles of beer")
	    print("Take one down, pass it around", num-1 ,"bottles of beer on the wall\n")
	    # print(num - 1, "bottles of beer on the wall\n")
	    time.sleep(7)

	    num=num-1
	    sing_verse(num)
	else:
		return

sing_verse(997)


# num = -5
# if num>0:
# 	print("true")
# else:
#  print("less than 0")