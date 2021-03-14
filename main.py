# Function to show numer
zero = "###\n# #\n# #\n# #\n###\n"
one = " # \n # \n # \n # \n # \n"
two = "###\n  #\n###\n#  \n###\n"
three="###\n  #\n###\n  #\n###\n"
four = "# #\n# #\n###\n  #\n  #\n"
five = "###\n#  \n###\n  #\n###\n"
six = "###\n#  \n###\n# #\n###\n"
seven = "###\n  #\n  #\n  #\n  #\n"
eight = "###\n# #\n###\n# #\n###\n"
nine = "###\n# #\n###\n  #\n###\n"


def led_number(n):
    n = str(n)
    led_string =""
    for element in n:
        if element == "1":
            led_string = led_string + one
        elif element == "2":
            led_string = led_string + two
        elif element == "3":
            led_string = led_string + three
        elif element == "4":
            led_string = led_string + four
        elif element == "5":
            led_string = led_string + five
        elif element == "6":
            led_string = led_string + six
        elif element == "7":
            led_string = led_string + seven
        elif element == "8":
            led_string = led_string + eight
        elif element == "9":
            led_string = led_string + nine
        elif element == "0":
            led_string = led_string + zero
        
    return led_string
    
# Main code.

n = int(input("Please chose a number: "))
print(led_number(n), end= "")
