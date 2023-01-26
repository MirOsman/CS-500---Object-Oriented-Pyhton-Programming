def main():
    data = input("Enter numbers: ").split()
    numbers = [float(x) for x in data]

    total = 0
    count = 0
    for grade in numbers:
        total += grade
        count += 1
    mean = total / count

    print("The mean is", mean)

    total = 0
    count = 0
    for grade in numbers:
        total += (grade - mean) ** 2
        count += 1
    standard_deviation = (total / (count - 1)) ** 0.5

    print("The standard deviation is", standard_deviation)

if __name__=="__main__":
    main()
