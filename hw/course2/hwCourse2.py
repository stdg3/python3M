equalSymbolCounts = 50
# Создать лист из 6 любых чисел. Отсортировать его по возрастанию
nonSortList = [1,5,6,7,6,9]
minVal = nonSortList[0]
maxVal = nonSortList[0]

k=int(	)
""" min max from lis
for x in nonSortList:
	if minVal>x :
		minVal = x

for x in nonSortList:
	if maxVal<x:
		maxVal = x
"""
for x in range(0, len(nonSortList)):
	for j in range(x, len(nonSortList)):
		if nonSortList[x] > nonSortList[j]:
			k = nonSortList[x]
			nonSortList[x] = nonSortList[j]
			nonSortList[j] = k

print("min sorted:",nonSortList)

for x in range(0,len(nonSortList)):
	for j in range(x,len(nonSortList)):
		if nonSortList[x] < nonSortList[j]:
			k = nonSortList[x]
			nonSortList[x] = nonSortList[j]
			nonSortList[j] = k
print("max sorted:",nonSortList)

print("=" * equalSymbolCounts)

# same operation by func
nonSortList.sort()
print("min sort by func:",nonSortList)
nonSortList.sort(reverse=True)
print("max sort by func:",nonSortList)

print("=" * equalSymbolCounts)

# Создать словарь из 5 пар: int -> str, например {6: '6'}, вывести его в консоль попарно
myDic = {1: "x1", 2: "x2", 3: "x3", 4: "x4", 5: "x5"}
for keys, values in myDic.items():
	print("key {key} = {value}".format(
		key=keys, 
		value=values
		))
	pass

print("=" * equalSymbolCounts)
#Создать лист из 3 слов: ['Earth', 'Russia', 'Moscow'], соеденить все слова в единую строку,
#чтобы получилось: 'Earth -> Russia -> Moscow'

wList = ["Earth", "Russia", "Moscow"]
answ = ""
for x in range(0, len(wList)):
	if x < len(wList)-1 :
		answ = answ + wList[x] + " -> "
	else :
		answ += wList[x]
print(answ)

print("=" * equalSymbolCounts)

# Создать tuple из 10 любых дробных чисел, найти максимальное и минимальное значение в нем

tuple1 = (6.06, 4.15, 4.41, 2.87, 1.001, 9.98, 6.66, 5.4, 45.0, 12.7,)
minVal=tuple1[0]
maxVal = tuple1[0]
for x in tuple1:
	if minVal > float(x): 
		minVal = x
	elif maxVal < float(x):
		maxVal = x
print(minVal, maxVal)

print("=" * equalSymbolCounts)

# Взять строку '/bin:/usr/bin:/usr/local/bin' и разбить ее в список по символу ':'
myDir = "/bin:/usr/bin:/usr/local/bin"
directories = list()
cell = str()
for x in myDir:
	if not x == ":":
		cell += x
	elif x == ":":
		directories.append(cell)
		cell = ""
directories.append(cell)
print(directories)
# Пройти по всем числам от 1 до 100, написать в консоль, какие из них делятся на 7, а какие - нет
seven = list()
for x in range(0,100):
	if x % 7 == 0 and not x == 0:
		seven.append(x)
print(seven)

print("=" * equalSymbolCounts)

#Создать список с тремя значениями 'to-delete' и нескольми любыми другими, 
#удалить из него все значения 'to-delete'

listToDel = ["to-delete1", "to-delete2", "to-delete3"]

# by-index
popped = listToDel.pop(0)
print("pop val =", popped)

# by value
listToDel.remove("to-delete3")

# by del
del listToDel[0]
print("list: ",listToDel)

print("=" * equalSymbolCounts, 
	"\n" 
	+ "=" * equalSymbolCounts)

quiz = {
	"What is name this language?": "python",
	"5 + 3 =": "8",
	"What is the OS on your PC?": "casablanca"
	}
correctAnswCounter = 0
for x in quiz:
	qAnser = input(x)
	if qAnser.lower() == quiz[x] or qAnser.upper() == quiz[x]:
		correctAnswCounter +=1
print("Your score", correctAnswCounter)
