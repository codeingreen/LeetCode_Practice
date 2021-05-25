class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        d = {'0': 0, '1': 1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        
        def convert_to_integer(num):
            
            number = 0
            sign = 1
            
            for n in num:
                
                if n == '-':
                    sign = -1
                    continue
                    
                number = number * 10 + d[n]
                
            return sign * number
        
        
        num1 = convert_to_integer(num1)
        num2 = convert_to_integer(num2)
        
        result = num1 * num2 
        
        print(result)
        
        return str(result)
        
            
            
        
