one_to_nine = [
"","one","two","three","four","five","six","seven","eight","nine"
]

ten_to_nineteen = [
'ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen'
]

tens = [
'','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety'
]

hundreds = [
'onehundred','twohundred','threehundred','fourhundred','fivehundred','sixhundred','sevenhundred','eighthundred','ninehundred'
]

def count_to_nine(num):
    num_str = ''
    for i in range(num+1): #Adjust for blank
        num_str += one_to_nine[i]
    return num_str

def count_to_nineteen(num):
    num_str = count_to_nine(9)
    for i in range(num%10):
        num_str += ten_to_nineteen[i]
    return num_str

def count_to_99(num):
    num_str = count_to_nineteen(19)
    for i in range(1,num/10-1): # Adjust for blank, only do complete tens
        for j in range(10):
            num_str += tens[i]+one_to_nine[j]
    for i in range(num%10+1):   # Adjust for blank, complete incomplete ten
        num_str += tens[num/10-1]+one_to_nine[i]
    return num_str

def count_to_999(num):
    num_str = count_to_99(99)
    return None

def generate_num_list(num):

    num_str = ""
    
    if num < 10:
        num_str += count_to_nine(num)
    elif 10 <= num < 20:
        num_str += count_to_nineteen(num)
    elif 20 <= num < 100:
        num_str += count_to_99(num)
        
    return num_str

print len(generate_num_list(99))

# This problem is tedious and not instructive
