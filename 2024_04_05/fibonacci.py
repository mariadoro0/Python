def fibonacci():
    fibo=[0,1]
    for i in range (1,25):
        fibo.append(fibo[i]+fibo[i-1])
    fibo.remove(0)
    return fibo
def main():
    print(fibonacci())

main()