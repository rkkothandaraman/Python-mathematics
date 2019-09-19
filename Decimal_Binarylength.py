def decimalToBinary(n):  
    return bin(n).replace("0b","")  
    
if __name__ == '__main__':
    N=int(input())
    M=str(decimalToBinary(N)) 
    print(len(M))
    
