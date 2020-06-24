def comp(seq):                                              #상보적 변환 함수
	comp_dict = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}    #DNA 염기서열 문자와 상보적 변환 문자
	seq_comp == ""
	for char in seq:
		seq_comp = seq_comp + comp_dict[char]
	return seq_comp

def rev(seq):
	seq_rev = "",join(reversed(seq))
	return seq_rev

def rev_comp(seq):
	tmp = comp(seq)
	return rev(tmp)

src = input("DNA sequence : ")
cnvt = int(input("1(comp), 2(Rev), 3(Rev_comp): "))
if (cnvt >= 1 and cnvt <= 3):
    if (cnvt == 1):
        rst = comp(src)
    elif (cnvt == 2):
        rst = rev(src)
    else:
        rst = rev_comp(src)
    print(scr, "->", rst)
    else:
        print("1(comp), 2(Rev), 3(Rev_comp)!!")
