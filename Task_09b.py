#Task 9b Snail Cup
'''
Task 9b Snail Cup (4 marks)

Modify the code from Part a to print out the snails in alphabetical order on separate lines. 

It should ask for the name of a racer who's gone to sleep and REMOVE their name in the list. If 
that name isn't in the list, it should leave the list unmodified and print a message 
saying all the racers are still awake.

Here's an example of how your program should look:
=========================
And the line up is: Dash, Speedy, Lighting, Flash, Sonic
Who's gone to sleep? Dash
Remaining racers:
Flash
Lighting
Sonic
Speedy
========================= 

'''



def main():
    x="Task9b"
    #===============================
    # Write your code here
    racers = {"Dash","Speedy","Lightning","Flash", "Sonic" }
    asleep_racer = input("Who's gone to sleep? ")
    asleep_racer_lower = asleep_racer_lower()
    updated_racers = {racer for racer in racers if racer.lower() != asleep_racer_lower}
    if len (updated_racers) == len(racers):
        print("All the racers are still awake.")
    else:
        updated_racers.sort()
        print("Remaining racers:")
        for racer in updated_racers:
            print(racer)

    # End of your code here
    #===============================

if __name__ == '__main__':
    main()
