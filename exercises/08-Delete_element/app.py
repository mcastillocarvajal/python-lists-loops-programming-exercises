people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:
def deletePerson(person_name):
    #Your code go here:
    arr = []
    for a in people:
        if a != person_name:
            arr.append(a)
    return arr
    
print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))