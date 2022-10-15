import sys

# fix for string command line is to add an additional '' around the string ""
var=eval(sys.argv[1])
t=type(var)
print 'The command line object:{v}\n object type:{s}'.format(v=var,s=t)

