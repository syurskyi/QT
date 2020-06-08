__author__ = 'Joel'
from ExpStack import ExpStack
from Calculator import CalTools


########### several test function ############
def test_stack():
    my_stack = ExpStack.ExpStack()
    print my_stack.is_empty()
    my_stack.push("1")
    my_stack.push(2)
    my_stack.push(3.14)
    print my_stack.is_empty()
    print my_stack.get_data()
    print my_stack.size()
    CalTools.print_calculator_stack(my_stack)


def test_is_num():
    num = ["1", "2", 1., '0']
    i = 0
    while i < len(num):
        if CalTools.is_number(num[i]):
            print num[i], " is number"
        else:
            print num[i], "is not number"
        i += 1
########### END ############


def main():
    if __name__ == "__main__":
        cal_str = CalTools.get_calculator_str()
        cal_str = CalTools.str_filter(cal_str)  # filter string
        # main loop
        while "-1" != cal_str:
            prefix_stack = CalTools.get_calculator_stack(cal_str)
            print "cal str:", cal_str
            print "prefix stack:"
            CalTools.print_calculator_stack(prefix_stack)
            # make prefix to suffix
            suffix_stack = CalTools.prefix_to_suffix(prefix_stack)
            print "suffix stack:"
            CalTools.print_calculator_stack(suffix_stack)
            # calculate suffix
            print "---calculator result---"
            print CalTools.calculate_from_stack(suffix_stack)

            cal_str = CalTools.get_calculator_str()
            cal_str = CalTools.str_filter(cal_str)  # filter string
        print "bye~"
    else:
        print __name__


#the main!
main()
