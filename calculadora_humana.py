import sys
import calculadora as calc
import datetime

N = int(sys.argv[1])

t1 = datetime.datetime.now()
err = 0
num = calc.random.randint(10,80)
for i in range(N):
	k=0
	if calc.check_div(num):
		op_num = range(4)
	else:
		op_num = range(3)
	op = calc.oper(num,calc.random.choice(op_num))
	while not calc.check(op.res):
		k += 1
		op = calc.oper(num,calc.random.choice(op_num))

	print("Question",i + 1,")   ",num,op.symb,op.b,"=")
	user_res = int(input())
	while op.res != user_res:
		#print(i,") ",num,op.symb,op.b,"=")
		user_res = int(input())
		err += 1

	num = op.res

T = datetime.datetime.now() - t1


print("Test finished")
print("=============")
print("Total time:",round(T.total_seconds(),1),"s =",round(T.total_seconds() / N,2),"s per question")
print("Total errors:",err)
