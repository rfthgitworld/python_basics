

 
   
def collatz (number):
 
    if number % 2 == 0:
        number = number // 2
        print (number)
        return number
        
    elif number % 2 == 1:
        number = 3 * number + 1
        print (number)
        return number
    
number = int(input("Enter a number: "))

while number != 1:
    number =  collatz(number)
       
       
