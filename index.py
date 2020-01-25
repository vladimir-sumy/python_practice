#using type()
a=44 #int class
b=33.2 #float class
print(a, type(a))
print(b, type(b))

#using id()
c = 3
r = 3
print( c, id(c))
print(r, id(r))

#strings
h = 'Hello '
w = 'world! '
phrase = h + w
print(phrase * 4)
print( phrase, type(phrase))

print(a, b, c, r, h, w, phrase)