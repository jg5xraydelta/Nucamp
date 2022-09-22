""" string[a:b:c] -> If a is less than b, the c should be blank or positive.
If a is such that the char is to the left of b ( or @ b) AND c is negative, then an empty string is returned.  
If a is such that the char is to the right of b AND c is negative, then all char from a to b-excluded is returned.
Whatever is located at b is never included."""

stringy = 'abcdefghijklmnop'

print("\nstringy =", stringy, "has a length of 16.\n")

print("stringy[16] returns ", 'IndexError: string index out of range\n')

print("stringy[-1] =", stringy[-1], '# prints the last char\n')

print("stringy[:-1] =", stringy[:-1], '# prints up to the next-to-last char\n')

print("stringy[::-1] =", stringy[::-1], '# prints the string in reverse\n')

print("stringy[-2] =", stringy[-2], '# prints the next-to-last char\n')

print("stringy[:-2] =", stringy[:-2], '# prints up to the 2nd-to-last char\n')

print("stringy[::-2] =", stringy[::-2],
      '# prints the string in reverse by 2 starting with the last char\n')

print("stringy[-1:-1] =", stringy[-1:-1], '# prints nothing\n')

print("stringy[-1:any negative integer] =",
      stringy[-1:-5], '# prints nothing\n')

print("stringy[-1::-2] =", stringy[-1::-2],
      '# prints the string in reverse by 2 starting with the last char\n')

print("stringy[-2::-3] =", stringy[-2::-3],
      '# prints the string in reverse by 3 starting with the next-to-last char\n')

print("stringy[-17] returns", 'IndexError: string index out of range\n')

print("stringy[:-36:-3] =", stringy[:-36:-3],
      '# prints the last char and then every 3rd char\n')

print("stringy[:-36:-4] =", stringy[:-36:-4],
      '# prints the last char and then every 4th char\n')

print("stringy[:-36:-15] =", stringy[:-36:-15],
      '# prints the last char and then every 15th char\n')

print("stringy[-5:-1:-1] =", stringy[-5:-1:-1], '# prints nothing\n')
