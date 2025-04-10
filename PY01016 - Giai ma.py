t = int(input())
while t:
    encode = input()
    decode = ""
    for i in range(0, len(encode), 2):
        decode += encode[i] * int(encode[i+1])
    
    print(decode)
    t -= 1
