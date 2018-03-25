'''
You are the head of a firm and you have to assign jobs to people. You have N persons working under you and you have N jobs that are to be done by these persons. Each person has to do exactly one job and each job has to be done by exactly one person. Each person has his own capability (in terms of time taken) to do any particular job. Your task is to assign the jobs to the persons in such a way that the total time taken is minimum. A job can be assigned to only one person and a person can do only one job.

'''
#code
def encodeSet(people, jobs):
    return ''.join(list(map(lambda x: str(x), people))) + ' ' + ''.join(list(map(lambda x: str(x), jobs)))

def jobAssign(people, jobs, peopleJob, memo):
    checkSet = encodeSet(people, jobs)
    if memo.get(checkSet, None) is not None: return memo[checkSet]
    if len(people) == 1:
        memo[checkSet] = jobs[0]
        return jobs[0]
    elif len(people) == 2:
        #This should be the base case
        #The Idea is simple choose the job assignment wit the least cost
        person1Cost = [peopleJob[people[0]][jobs[0]], peopleJob[people[0]][jobs[1]]]
        person2Cost = [peopleJob[people[1]][jobs[0]], peopleJob[people[1]][jobs[1]]]
        memo[checkSet] = min(person1Cost[0] + person2Cost[1], person1Cost[1] + person2Cost[0])
        return memo[checkSet]
    else:
        best = float('inf')
        for i, p in enumerate(people):
            for j, jo in enumerate(jobs):
                jobCost = peopleJob[p][jo]
                jobCost += jobAssign(people[:i] + people[i+1:]
                                    ,jobs[:j] + jobs[j+1:] 
                                    ,peopleJob, memo)
                best = min(best, jobCost)
        memo[checkSet] = best
        return memo[checkSet]


tests = int(input())
for t in range(tests):
    n = int(input())
    people, jobs = list(range(n)), list(range(n))
    inSt = input().split()
    arr = []
    for i in range(n):
        arr.append(list(map(lambda x: int(x), inSt[i*n: (i+1)*n])))
    memo = {}
    print (jobAssign(people, jobs, arr, memo))
