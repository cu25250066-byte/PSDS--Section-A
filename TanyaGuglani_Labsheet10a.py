n = int(input())
nums = list(map(int, input().split()))

count = {}
answer = 0

for num in nums:
    digit_sum = sum(map(int, str(num)))

    if digit_sum in count:
        answer += count[digit_sum]

    count[digit_sum] = count.get(digit_sum, 0) + 1

print(answer)
