num = int(input())
nums = [int(i) for i in input().split()]

def fib_to_n(n, nums):
    fk1 = 0
    fk2 = 0
    fk3 = 0
    itog = 0
    dict={0:0}
    for j in range(1, n):

        if j<=2:
            itog = j
        else:
            if j==3:
                itog = 2
                fk1, fk2, fk3  = itog, 2, 1
            else:
                itog = fk1 + fk3
                fk1, fk2, fk3 = itog, fk1, fk2
        if nums.count(j)!=0:
            dict.update({j:itog})
    return dict


fib_seq = fib_to_n(int(sorted(set(nums))[-1])+1, nums)
for gg in range(len(nums)):
    print(fib_seq.get(nums[gg]), end = ' ')



















