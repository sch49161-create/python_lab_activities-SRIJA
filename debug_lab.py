# Program to compute average of number 
def calculate_average (nums):
    total =0
for n in nums:
    total += n
    average = total / len(nums)  # Might cause Zero Division Error
    return average # Wrong variabl name (sholud be 'average')

def main():
    values= input("enter numbers seperated by commas: ").split(",")
                  numbers[int(n.strip()) for n in values]  # Will crash if input not numbers
    avg = calculate_average(numbers)
    print("The average is: ", avg)
if __name__ == "__main__":
    main()
    