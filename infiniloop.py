# i understand why it is an infinite loop but don't know how to make it stop looping unsure what i am not grasping

def powers(v):
  while v % 2 < 0:
# added break here
    v = v / 2
  if v == 1:
    return True
  return False
  

print(powers(0))
print(powers(1))
print(powers(8))
print(powers(9))
