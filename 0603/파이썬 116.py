curt=input("현재 시각 : ")

if curt[3:]=="00" :


chr = input("한 문자 입력 : ")

if chr.isIower():
    print(chr.upper())
elif 'A' <= chr <= 'Z' :      #elif chr >= 'A' and chr <= 'Z'
    print(chr.lower())
else:
    print(chr)
