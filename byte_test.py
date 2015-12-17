byte_numbers = []
for i in ['0','1','2','3','4','5','6','7','8','9',',']:
    byte_numbers.append(ord(i))

    
def get_input(stuff):
    converted_input = []
    input_stuff = ""
    i = 0
    while (i < len(stuff)) :
        if(stuff[i] in byte_numbers):
            if stuff[i] != ord(','):
                input_stuff += str(stuff[i]-ord('0'))
            else:
                pass
        i += 1
    converted_input.append(input_stuff)
            
    print(converted_input)

print(byte_numbers)
get_input(b'00001,2342,354896345987346932463536')
