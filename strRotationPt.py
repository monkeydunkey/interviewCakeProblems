'''
Find the rotation point of a an array i.e. where 2 sorted list are joined together
both the sorted list should have the same ordering
'''

def findRotPoint(li):
    if len(li) < 2:
        #there is nothing to return
        return -1
    fi_ele = li[0]
    low_pt = 0
    hi_pt = len(li) - 1
    while hi_pt >= low_pt:
        #print hi_pt, low_pt
        mid_pt = (hi_pt + low_pt)//2
        if mid_pt != 0 and mid_pt != len(li) - 1:
            if li[mid_pt] < li[mid_pt + 1] and li[mid_pt] < li[mid_pt - 1]:
                #this is the rotation point
                return mid_pt
            else:
                if li[mid_pt] > li[0]:
                    #the rotation point is still to the right
                    low_pt = mid_pt + 1
                elif li[mid_pt] < li[0]:
                    #the rotation point is to the left now
                    hi_pt = mid_pt - 1
                else:
                    #this condition should not arrive
                    print 'This condition should not arrive', mid_pt, hi_pt, low_pt
        else:
            if mid_pt == len(li) - 1 and li[0] > li[-1]:
                return len(li) - 1
            else:
                # this case should not arrive as this means that there is no turning pt
                print 'this case should not arrive as this means that there is no turning pt'
                return -1

    return -1


if __name__ == '__main__':
    print findRotPoint(['ptolemaic', 'retrograde', 'supplant', 'undulate', 'xenoepist', 'yyy', 'zzz', 'asymptote', 'babka', 'banoffee', 'engender', 'karpatka', 'othellolagkage'])

