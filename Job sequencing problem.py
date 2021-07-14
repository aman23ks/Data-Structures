class Jobs:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit


def JobScheduling(Jobs, n):
    arr = []
    check = [False]*n
    print(check)
    total = 0
    jobs_done = 0
    for i in range(n):
        arr.append([Jobs[i].profit, Jobs[i].deadline])

    arr.sort(reverse=True)

    for i in range(n):
        for j in range(min(arr[i][1]-1, n), -1, -1):
            print(check)
            if check[j] == False:
                print(check)
                check[j] = True
                total += arr[i][0]
                jobs_done += 1
                break

    return jobs_done, total


job1 = Jobs(1, 2, 100)
job2 = Jobs(2, 1, 19)
job3 = Jobs(3, 2, 27)
job4 = Jobs(4, 1, 25)
job5 = Jobs(5, 1, 15)
Job = [job1, job2, job3, job4, job5]
print(JobScheduling(Job, len(Job)))
