pocket = ['paper', 'handphone']
card = True
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    if card:
        print("택시를 타고 가라")
    else: 
        print("걸어가라")

pocket = ['paper', 'cellphone']
card = False
if 'money' in pocket:
    print("택시를 타고 가라")
elif card:
    print("택시를 타고 가라")
else:
    print("걸어가라")

score = 70
if score<=60:
    print("success")
elif score>70:
    print("success")
else:
    print("fail") 