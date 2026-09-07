
# Str and repr are the same except str is meant to be readable and repr is used for debugging (more precise)

s = 'Hello, world.'
print str(s)
print str(4.0/2.0)

print repr(s)
print repr(4.0/2.0)

x = 10 * 3.256
y = 200 * 2.53

print str(x/y)
print repr(x/y)

print repr((x, y, ('spam', 'eggs')))
