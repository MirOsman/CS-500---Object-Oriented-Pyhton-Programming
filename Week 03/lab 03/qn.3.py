def Left_triangle(rows):
    print()
    l = 1
    while l <= rows:
        m = l
        while m < rows:
            # display space
            print(' ', end=' ')
            m += 1
        n = 1
        while n <= l:
            print('*', end=' ')
            n += 1
        print()
        l += 1

    l = rows
    while l >= 1:
        m = l
        while m <= rows:
            print(' ', end=' ')
            m += 1
        n = 1
        while n < l:
            print('*', end=' ')
            n += 1
        print('')
        l -= 1
rows = int(input("Enter maximum stars: "))
Left_triangle(rows)

