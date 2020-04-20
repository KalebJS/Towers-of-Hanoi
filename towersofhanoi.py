# a KalebJS production!
# basically a recreation of towers of hanoi game using stacks in python 
# wow!

from stack import Stack

print("\nLet's play Towers of Hanoi!!")

# functions 
def get_input () :
    choices = [item.get_name()[0] for item in stacks] #creates list of first letters of each stack
    while True :
        for i in range(len(stacks)): #lists options
            name = stacks[i].get_name()
            letter = choices[i]
            print('Enter {} for {}'.format(letter, name))
        user_input = input().upper() 
        if (user_input in choices) : #ensures that user input is valid//if not reiterate loop
            for i in range(len(stacks)) :
                if user_input == choices[i] :
                    return stacks[i]
        else :
            continue

            



# initialization and setup

stacks = [] #these are the three poles. see image if unfamiliar
left_stack = Stack('Left')
middle_stack = Stack('Middle')
right_stack = Stack('Right')
stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)


#sets number of disks in game
num_disks = int(input("\nHow many disks do you want to play with?\n"))

while num_disks < 3 : #ensures that number of disks is greater than 3 so it will be fun
    num_disks = int(input("\nEnter a number greater than or equal to 3, please.\n")) 

for i in range(num_disks, 0 , -1) :
    stacks[0].push("Disk {}".format(i))

#the least number of moves you could complete this in
num_optimal_moves = 2 ** num_disks - 1

print('\nThe fastest you can solve this game is in {} moves'.format(num_optimal_moves))


# play the game

num_user_moves = 0

while not right_stack.get_size() == num_disks : #iterates the turn until the game is won!
    print('\n\n\n...Current Stacks...')
    for stack in stacks : #prints those dang stacks
        stack.print_items()
    while True : #ensures that a proper turn is taken
        print('\nWhich stack do you want to move from?\n')
        from_stack = get_input()
        if from_stack.is_empty() : #true means invalid
            print ('\n\nInvalid Move: stack is empty!')
            continue
        print('\nWhich stack do you want to move to?\n')
        to_stack = get_input()
        if to_stack.is_empty() or to_stack.peek() > from_stack.peek(): #true means continue
            disk = from_stack.peek()
            to_stack.push(disk)
            from_stack.pop()
            num_user_moves += 1
            break
        else :
            print ('\n\nInvalid Move: recipient stack\'s top disk is too small!')
            continue


else :
    print('You won in {} moves!'.format(num_user_moves))
    