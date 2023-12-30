letter = ['hello','question','word','yatch','zebra','monkey','pig','joyful','explore','vehicle']

set_ = set()
set_full = set(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])


for i in letter:
    for j in i:
        set_.add(j)

print(set_full - set_)

#list_ = list(set_)
#list_ .sort()
#print(list_)
