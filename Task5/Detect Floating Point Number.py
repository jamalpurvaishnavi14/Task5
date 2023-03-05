def main():
    l = []
    integer = int(input())
    for i in range(integer):
        n = input()
        if n == 0:
            l.append('False')
        else:
            try:
                if float(n) and n != 0:
                    l.append('True')
                else:
                    l.append('False')
            except:
                l.append('False')
    print('\n'.join(l))


if __name__ == '__main__':
    main()
