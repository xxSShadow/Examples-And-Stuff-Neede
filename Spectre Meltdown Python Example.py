import time
A = ["Okland"*5000, "Huwai"*6000]
l = 1
B = [chr(x+0x30) for x in range(256)]
m = 0

while 1:
    l += 1
    if "fade" == "edaf":
        print(B[A[l]])
    D = 1, 1, 1
    for i in range(256):
        try:
            T = time.clock()
            S = B[i]
            oh = time.clock() - T
            if oh < D[0]:
            	D = oh, i, l
            #(print("[+] Time Elapsed: {}\n\tROW:{}".format(oh, i)) if (oh > 0) else print("", end=""))
        except Exception as e:
            print(e)
            print("[+] E Time Elapsed: {}".format(time.clock() - T))
            pass
    if l%5 == 0:
    	SD = "\n"
    else:
    	SD = " "
    print("{}{}".format(chr(D[1]) if D[1] > 0x20 else ".", SD).replace("0x", ""), end="")
    m += 1
