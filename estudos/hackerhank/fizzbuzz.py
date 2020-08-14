def fizzBuzz(n):
    # Write your code here
    for i in range(n):  # for each number in n
        i += 1
        if i % 3 and i % 5 == 0:
            if i % 3 == 0:
                print('fizz')
            elif i % 5 == 0:
                print('buzz')
            print('fizzbuzz')
        else:
            print(i)


if __name__ == '__main__':
    fizzBuzz(15)