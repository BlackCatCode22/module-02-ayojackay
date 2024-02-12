numOne = input("Give me three numbers. What's your first number?")
numTwo = input("Your second number?")
numThree = input("Your third and last number?")

numbers = [int(numOne), int(numTwo), int(numThree)]


def big(nums):
    if not nums:
        print("Hey, give me numbers!")
        return
    largest = max(nums)
    return largest


result = big(numbers)
print("Your biggest number is:", result)
