# always use space instead of tabs for indentation
# in general 2 or 4 spaces are used, but every multiplication of the first used spaces is valid
# vscode with the right python extensions will autodetect when indentation is increased and use standard 4 spaces
# use this to your advantage: when you expect an indentation and vscode does not automatically insert it,
# that means you have a syntax error (maybe missing ':')

# a block is defined by it's intendation, hence a block ends, when the indentation ends
if True:
    # start of the if block
    a = 3
    some_func()
    # last line part of the if block
# outside the if block
a = 5

# same for loops and functions
for a in range(0,10):
    c = a * 2
    some_func(c)
    for b in range(a, c):
        x = a + b
        y = a**2 + a/b
        print(x,y)

def some_func(val = 0):
    a = 3
    for i in [0,5,9,8]:
        I = 'Select {}'.format(i)
        print(I)
        return a