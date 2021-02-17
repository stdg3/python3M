# Basic try/except
try:
	print(1 / 0)
except:
	print("0!!!")

try:
	print(1 / 0)
except Exception: #"hata" yakalar
	print("0 division")

try:
	print(1 / 0)
except ZeroDivisionError: # hata türü 0'a bölme ise alt satıra geçer 
#bilmediği hata tipi olursa prog yine çatlar
	print("/0")

try:
	1 / int(input("x: "))
except ZeroDivisionError:
	print("/0!!!")
except TypeError:
	print("Wrong input type")
except ValueError:
	print("Bad input")


try:
	print(1 /0)
except ZeroDivisionError as e:
	# e değişken adı sadece hatanın mesajını almak için
	print("Exception! Stop it!")
	print(e)

# Mismatced exception will be not captured
try:
	d = {"key": 23}
	#print(d["doesNotExist"])
except ZeroDivisionError:
	print ("this won't be called")

try:
	d = {"key": 23}
	print(d["doesNotExist"])
except KeyError as e:
	print("got it", e)

l = [1, 2]
try:
	l[9]
except IndexError as e:
	print("Hey! Out of range!")

# Raising exception ekrana fırlatma
#raise typeOfExcept("yourMessage")
#mesela autent olmayan kullanıcı girmaye çalışır sisteme >> hatafırlat
try:	
	raise IndexError("Hi! index err")
except IndexError as e:
	print(e)

try:
	raise ValueError("Hi! F1")
except ValueError as e:
	print(e)
#try / except / else

try:
	print("fine")
except KeyError:
	print("nope")
else:
	print("else cacuse")

# try / except/ finally
try:
	print(1 / 0)
except ZeroDivisionError:
	print("0/!")
finally:
	print("I will be called in the end!")

# all together
try:
	print("try")
except ValueError:
	pass # You should never pass no exception!
else:
	print("else")
finally:
	print("finally")

try:
	raise ValueError("zıııı")
finally:
	print("FFFFFFinally") #