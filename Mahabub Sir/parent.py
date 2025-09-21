def parent (x,y):
    return (x,y) in [("john","mary"),("mary","joe")]

def grandparent (x,z):
    for y in ["mary","joe"]:
        if parent(x,y) and parent(y,z):
            return True
    return False

print("parent(john,mary)",parent("john","mary"))
print("parent(mary,joe)",parent("mary","joe"))
print("grandparent(john,joe)",grandparent("john","joe"))
