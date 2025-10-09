#Task 4b King Letter
'''
Task 4b King Letter (2marks)

Add to the code from part 1 to change the output when a number is 
greater than 100 to show for example:

=========================
How old are you? 111
You already got your letter 11 years ago
========================= 

'''
def main():
    x="Task4b"
    #===============================
    # Write your code here
    age = int(input("How old are you? "))
    print("=========================")
    if age < 100:
        print("Years untill your letter...")
        print(100-age)
    elif age == 100:
        print("You got your letter this year!")
    else:
        print(f"You already got your letter {age-100} years ago")
    print("=========================")
    # End of your code here
    #===============================

if __name__ == '__main__':
    main()
