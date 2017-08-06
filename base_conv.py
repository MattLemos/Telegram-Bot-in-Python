def binToDec(num):
	word = str(num)
	tam = len(word)-1
	j = 0
	total = 0
	while(tam >= 0):
		if(word[tam] == '1'):
			total += 2**j
		tam -= 1
		j += 1
	return total

def decToBase(num,base):
	t = []
	aux = []
	i = 0
	while(num > 0):
		atual = str(num%base)
		t.append(atual)
		num = int(num/base)
	tam = len(t)-1
	while(tam >= 0):
		aux.append(t[tam])
		tam -= 1
	new_aux = ''.join(aux)
	return new_aux

def main(opt, num, base):
	if(opt == 'bin'):
		val = binToDec(num)
		nv = decToBase(val,base)
		base = str(base)
		val = str(val)
		nv = str(nv)
		answer = 'Base 10: '+val+'\n'+'Base '+base+' : '+nv

	else:
		nv = decToBase(num,base)
		nv = str(nv)
		base = str(base)
		answer = 'Base '+base+' : '+nv
	return answer
