n:int = int(input("You're working in Zn with n (prime number) being : "))
operation:str = str(input("And the operation is ('x | +') : "))

def main():
    if operation == '+':     
        for number in range(n-1):
            print(summation(number), end=" - Card : ")
            print(len(summation(number)))
            
    
    elif operation == 'x':
        for number in range(n-2):
            print(product(number + 1), end=" - Card : ")
            print(len(product(number)))
    
    
def summation(number:int):
    if number > 0 :
        group:list = [0, number]
        sum_all:int = number
        while ((sum_all + number) % n != 1):
            group.append((sum_all + number)%n)
            sum_all = ( sum_all + number ) % n
            
    else : 
        group:list = [0]            
    return group
    
def product(number:int):
    if number > 1 :
        group:list = [1, number]
        sum_all:int = number
        while ((sum_all * number) % n != 1):
            group.append((sum_all * number) % n)
            sum_all = ( sum_all * number ) % n
    
    else :
        group:list = [1]
    
    return group        
    
    
if __name__ == "__main__":
    main()
    