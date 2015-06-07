def delete(s):
    if s==1:
        return True
    for i in range(2,s):
         if s%i == 0:
             return True
    return False

print (filter(delete,range(1,101)))
