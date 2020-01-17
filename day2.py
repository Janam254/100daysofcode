"""Create an if statement that prints the string “That’s too many”
if the variable ninjas contains a number that’s less than 50, prints
“It’ll be a struggle, but I can take ’em” if it’s less than 30, and
prints “I can fight those ninjas!” if it’s less than 10 """

#I indented with tabs
ninja = 5
if ninja > 50:
    print(''' "That's too many" ''')
elif ninja < 30:
    print(''' "It'll be a struggle, but i can take 'em"''')
elif ninja < 10:
    print(''' “I can fight those ninjas!” ''')