#Task 6b New Words
'''
Task 6b New Words - Part2 (4marks)

Add to the code from part 1 to create another new word. 
The new word should replace 'o' in the word with a 'y'. 
Use a for loop to print out each letter of this new word on a new line. 
Then print this new word on 1 line at the end.

For example:
=========================
Say: typo
New word!
t
y
p
y
y
y
y
y
y
typyyyyyy!
========================= 

'''
def main():
    x="Task6b"
    #===============================
    # Write your code here
    message = input("Say: ")
    words = message.split()
    last_word = words[-1]
    emphasised_word = last_word + last_word[-1] *5 +"!"
    words[-1] = emphasised_word
    new_word = last_word.replace('o','y')
    print("New word!")
    for letter in new_word:
        print(letter)
    new_word_emphasised = new_word + new_word[-1] * 5 +"!"
    print(new_word_emphasised)
    

    # End of your code here
    #===============================

if __name__ == '__main__':
    main()
