#################################################################################
#  Exercise 5 Until stop                                                        #
# Write a program that fulfills the specification:                              #
#   1. Create a while loop that runs forever                                    #
#   2. In each iteration, input a text                                          #
#   3. In each iteration, print a text "Enter stop to quit: "                   #
#   4. If the text equals stop, break the while loop                            #
#   5. If the text don't equals stop, print the text and the length of the text #
#################################################################################


while True:
    text = input("Enter a word: ").capitalize()
    if(text == "Stop"):
        break
    print("Enter STOP to quit!")
    print(f"The text you input is {text} and the lenght is {len(text)}")