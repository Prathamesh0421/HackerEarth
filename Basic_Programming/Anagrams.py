testcase = int(input())
 
def charCount(string1,string2):
    dict1 = {}
    dict2 ={}
    for letter in string1:
        if letter in dict1.keys():
            dict1[letter] = dict1[letter] + 1
        else:
            dict1[letter] = 1
 
    for letter in string2:
        if letter in dict2:
            dict2[letter] += 1
        else:
            dict2[letter] = 1
    return (dict1,dict2)
 
 
def deletion(x, y):
    count = 0
    while x != y:
        if x > y:
            x = x - 1
        else:
            x = x + 1
        count = count + 1
 
    return count
 
 
def count_deletion(dict1,dict2):
    tot_count = 0
    for x in dict1:
        if x in dict2:
            count = deletion(dict1[x],dict2[x])
            if dict1[x] > dict2[x]:
                dict1[x] = dict1[x] - count
            else:
                dict2[x] = dict2[x] - count
        else:
            count = deletion(dict1[x],0)
        tot_count = tot_count + count
 
    for x in dict2:
        if x in dict1:
            count = deletion(dict2[x],dict1[x])
        else:
            count = deletion(dict2[x],0)
        tot_count = tot_count + count
 
    return tot_count
 
for i in range(testcase):
    string1 = input()
    string2 = input()
    dict1,dict2 = charCount(string1,string2)
    total_deletion = count_deletion(dict1,dict2)
    print(total_deletion)