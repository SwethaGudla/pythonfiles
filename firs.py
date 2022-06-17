import sys
import argparse
# msg="addition of two numbers"
# p = argparse.ArgumentParser(description=msg)
# print(msg)
print(sys.argv)
a=int(sys.argv[1])
b=int(sys.argv[2])
msg="addition of two numbers"
p = argparse.ArgumentParser(description=msg)
print(msg)
print(a+b)

# import argparse
# msg = 'hello'
# p=argparse.ArgumentParser(description=msg)
# print(msg)