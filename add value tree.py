def camelcase(s):
    count = 0
    #word = []
    for i in range(0, len(s)):
        if s[0].isupper():
            return False
        elif s[i].islower():
        #if s[i].lower in s:
            #print(s[i].lower)
           print(s[i],end='')
        elif s[i].isupper() and s[i+1].islower():
            print(s[i]+s[i+1],end='')
            #return True
    count +=1


    return  count

print(camelcase('helloRamHowAreYou'))



#helloRamHowAreYou