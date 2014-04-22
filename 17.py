one_to_nine = ["one","two","three","four","five","six","seven","eight","nine"]

def generate_num_list(num):

    num_str = ""
    
    for i in range(num):
        num_str += one_to_nine[i]

print generate_num_list(5)

