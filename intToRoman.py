## Reverse of the other problem, where we now take integer and convert it to Roman numeral.
## For example: if one enters '249', the output should be 'CCXLIV'

class RomanNumeral:
    def integerToRoman(self, num: int) -> str: 
        kv_pair = {
            1000: 'M',
            900: 'DM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }
        
        val = (
            1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1
        )
        
        result = str()
        
        for i in val: 
            result += (num//i)*kv_pair[i]
            num %= i 
            
        return result 