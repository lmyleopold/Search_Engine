import argparse

# the parameter from the command line
parser = argparse.ArgumentParser()
parser.add_argument('--read', type = str, help='read a file')
args = parser.parse_args()

#after command line, used for input, can be supplement of argsparse
search = input('search > ')

print('\n')
print('answer >', 1)
for i in range(10):
    print('        ', i)