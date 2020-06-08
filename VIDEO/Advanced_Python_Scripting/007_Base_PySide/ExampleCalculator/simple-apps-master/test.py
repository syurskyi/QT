import string

def main():
    a = raw_input("add a string, no num: ")
    try:
        if not a.isalpha():
            raise NameError
    except NameError:
        print 'NameError: add nonum string\n'
    else:
        print 'gg\n'
    print a.upper()

if __name__ == '__main__':
    main()
