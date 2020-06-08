__author__ = 'joel'
from ExpStack import ExpStack


#whether a char is a number
def is_number(char):
    return ("0" == char or "1" == char or "2" == char or "3" == char or
            "4" == char or "5" == char or "6" == char or "7" == char or
            "8" == char or "9" == char)


#whether a char is dot
def is_dot(char):
    return "." == char


#whether a char is calculator operation
def is_calculator_option(char):
    return ("+" == char or "-" == char or "*" == char or "/" == char
            or "(" == char or ")" == char or "^" == char)


#get calculator string
def get_calculator_str():
    return raw_input("Please input calculator string(no '=') end with '-1':\n")


#whether a string consists of numbers
def is_number_str(m_str):
    for n in m_str:
        if (not is_number(n)) and (not is_dot(n)):
            return False
    return True


#filter blanks from a string
def str_trim(src_str):
    ret_str = ""
    for c in src_str:
        if " " != c:
            ret_str += c
    return ret_str


#filter useless characters from a string
def str_filter(src_str):
    ret_str = ""
    for c in src_str:
        if is_number(c) or is_calculator_option(c) or is_dot(c):
            ret_str += c
    return ret_str


#print elements in the stack
def print_calculator_stack(stack):
    print "---stack content---"
    print stack.get_data()
    print


#compare operators, return an integer
#1: higher priority; 0:lower priority; -1:wrong operator; 2:same priority
def compare_operator(op1, op2):
    if "^" == op1:
        if "^" == op2:
            return 2
        elif "+" == op2 or "-" == op2 or "*" == op2 or "/" == op2:
            return 1
        else:
            return -1
    elif "*" == op1 or "/" == op1:
        if "^" == op2:
            return 0
        elif "*" == op2 or "/" == op2:
            return 2
        elif "+" == op2 or "-" == op2:
            return 1
        else:
            return -1
    elif "+" == op1 or "-" == op1:
        if "^" == op2 or "*" == op2 or "/" == op2:
            return 0
        elif "+" == op2 or "-" == op2:
            return 2
        else:
            return -1
    else:
        return -1


#get all elements from calculator string and return a stack
def get_calculator_stack(cal_str):
    exp_stack = ExpStack.ExpStack()
    ele = ""              # one element, a number or operator
    get_a_number = False  # whether get a number
    #if calculator string start with "-(", push 0 in the bottom of the stack
    if len(cal_str) > 2 and "-" == cal_str[0] and "(" == cal_str[1]:
        exp_stack.push("0")
    for tem_char in cal_str:
        if (((not get_a_number) and "-" == tem_char) or
                (not is_calculator_option(tem_char))):  # is a number
            ele += tem_char
            get_a_number = True
        else:  # is a operator
            if "" != ele:
                exp_stack.push(ele)
                ele = ""
            exp_stack.push(tem_char)
            if ")" != tem_char:  # is )
                get_a_number = False
            else:  # is (
                get_a_number = True
    if len(ele) != 0:
        exp_stack.push(ele)
    return exp_stack


#turn prefix stack into suffix stack
def prefix_to_suffix(prefix_stack):
    data = prefix_stack.get_data()
    suffix_stack = ExpStack.ExpStack()
    tem_stack = ExpStack.ExpStack()
    get_a_number = False
    get_a_operator = False
    for ele in data:
        if is_number_str(ele):  # is number, put it into suffix
            get_a_operator = False
            if get_a_number:
                suffix_stack.push(ele)
                suffix_stack.push("*")
            else:
                suffix_stack.push(ele)
                get_a_number = True
        elif "(" == ele:  # is (, push elements into stack
            tem_stack.push(ele)
        elif ")" == ele:  # is ),
            while "(" != tem_stack.get_top():
                suffix_stack.push(tem_stack.get_top())
                tem_stack.pop()
                if tem_stack.is_empty():
                    print "Brackets not match!"
                    return None
            if "(" == tem_stack.get_top():
                tem_stack.pop()
        elif is_calculator_option(ele):  # is operator
            get_a_number = False
            if get_a_operator:  # no numbers between 2 operators
                print "Wrong Exps."
                return None
            else:
                get_a_operator = True
            while ((not tem_stack.is_empty())
                   and "(" != tem_stack.get_top()
                   and compare_operator(tem_stack.get_top(), ele) > 0):
                suffix_stack.push(tem_stack.get_top())
                tem_stack.pop()
            tem_stack.push(ele)
    while not tem_stack.is_empty():
        if "(" == tem_stack.get_top():
            print "Brackets not match!"
            return None
        suffix_stack.push(tem_stack.get_top())
        tem_stack.pop()
    return suffix_stack


#calculate from stack, return result string
def calculate_from_stack(suffix_stack):
    error_str = "Error"
    nan_str = "NaN"
    if None == suffix_stack:
        print "stack is empty!"
        return error_str
    data = suffix_stack.get_data()
    calculate_stack = ExpStack.ExpStack()
    for ele in data:
        if is_number_str(ele):
            calculate_stack.push(ele)
        elif is_calculator_option(ele):
            if calculate_stack.size() < 2:
                print "Wrong suffix exps."
                print_calculator_stack(suffix_stack)
                return error_str
            try:
                num1 = float(calculate_stack.get_top())
                calculate_stack.pop()
                num2 = float(calculate_stack.get_top())
                calculate_stack.pop()
                if "+" == ele:
                    calculate_stack.push(num1+num2)
                elif "-" == ele:
                    calculate_stack.push(num2-num1)
                elif "*" == ele:
                    calculate_stack.push(num2*num1)
                elif "/" == ele:
                    calculate_stack.push(num2/num1)
                elif "^" == ele:
                    calculate_stack.push(num2**num1)
                else:
                    print "Unknown calculator operator", ele
                    return error_str
            except TypeError, e:
                print "type error:", e
                return error_str
            except ValueError, e:
                print "value error:", e
                return error_str
            except ZeroDivisionError, e:
                print "divide zero error:", e
                return nan_str
    if 1 == calculate_stack.size():
        return str(calculate_stack.get_top())
    else:
        print "Unknown error, calculate stack:"
        print_calculator_stack(calculate_stack)
        return error_str