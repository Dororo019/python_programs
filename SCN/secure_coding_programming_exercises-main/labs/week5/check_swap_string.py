# def swap_string(string):
    # Swap adjacent characters
    # swapped_string = ''.join([string[i+1] + string[i] for i in range(0, len(string)-1, 2)])
    # Add space after each pair
    # spaced_string = ' '.join([swapped_string[i:i+2] for i in range(0, len(swapped_string), 2)])
    # Add space if no swapping partner is present
    # if len(string) % 2 != 0:
        # spaced_string += ' ' + string[-1]
    # return spaced_string






    
    # let's swap 2 letters from the characters
def swap_string(string):
    # Swap adjacent characters
    swapped_string = ''.join([string[i+1] + string[i] for i in range(0, len(string)-1,2)])
    # Add space after each pair
    spaced_string = ' '.join([swapped_string[i:i+2] for i in range(0, len(swapped_string),2)])
    # Add space if no swapping partner is present
    if len(string) % 2 != 0:
        spaced_string += '  '+ string[-1]
    return spaced_string


            
print(swap_string("Quirk"))
    