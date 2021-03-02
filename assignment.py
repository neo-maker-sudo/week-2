def calculate(min, max):
    # 請用你的程式補完這個函式的區塊
    sum = 0
    for n in range(min, max+1):
        sum += n
    print(sum)


calculate(1, 3)  # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8)  # 你的程式要能夠計算 4+5+6+7+8，最後印出 30


def avg(data):
    # 請用你的程式補完這個函式的區塊
    count = data["count"]
    employees = data["employees"]
    sum = 0
    for n in employees:
        sum += n["salary"]
    result = sum / len(employees)
    print(result)

avg({
    "count": 3,
    "employees": [
        {
            "name": "John",
            "salary": 30000
        },
        {
            "name": "Bob",
            "salary": 60000
        },
        {
            "name": "Jenny",
            "salary": 50000
        }
    ]
})  # 呼叫 avg 函式


def maxProduct(nums):
    # 請用你的程式補完這個函式的區塊
    num = 0
    maxNumber = 0
    for i, a in zip(nums, range(0, len(nums))):
        for j, b in zip(nums, range(0, len(nums))):
            if a != b:
                num = i*j
                if maxNumber < num:
                    maxNumber = num
                elif num < 0 and maxNumber == 0:
                    maxNumber = num
    print(maxNumber)

maxProduct([5, 20, 2, 6])  # 得到 120 因為 20 和 6 相乘得到最大值
maxProduct([10, -20, 0, 3])  # 得到 30 因為 10 和 3 相乘得到最大值

def towSum(nums, target):
    # your code here
    arr = []
    for x in nums:
        for y in nums:
            if x + y == target:
                arr.append(nums.index(x))
                arr.append(nums.index(y))
                return arr


result = towSum([2, 11, 7, 15], 9)
print(result)  # show [0, 2] because nums[0]+nums[2] is 9


def maxZeros(nums):
    # 請用你的程式補完這個函式的區塊
    maxNumber = 0
    num = 0
    for n in nums:
        if n >= 0:
            maxNumber += 1
            if num < maxNumber and n == 0:
                num = maxNumber
            if n == 1:
                maxNumber = 0
    print(num)


maxZeros([0, 1, 0, 0])  # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0])  # 得到 4
maxZeros([1, 1, 1, 1, 1])  # 得到 0


