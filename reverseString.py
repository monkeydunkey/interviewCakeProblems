def splitReverse(st):
    st = st.strip()
    i, j = 0, len(st) - 1
    insertPos = 0
    outList = []
    while i < j:
        while st[j] == " " and j >= 0: j-=1
        s1 = ""
        while st[j] != " "  and j >= 0: 
            s1 = st[j] + s1
            j -=1
        
        while st[i] == " " and i < len(st): i+=1
        s2 = ""
        while st[i] != " "  and i < len(st): 
            s2 += st[i]
            i += 1
        
        outList.insert(insertPos, s1)  
        if i <= j:
            outList.insert(insertPos+1, s2)
        insertPos += 1
    return ' '.join(outList)


print splitReverse("Hello     world I am")
