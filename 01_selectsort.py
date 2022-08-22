import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def print_help():
    eprint("This is a help message")
    eprint("Use program with just one argument: filename to sort")
    eprint("Example:")
    eprint("01_selectsort.py sort_this_file.txt > out.txt")
    eprint("It will sort content of file sort_this_file.txt and place result in the out.txt")
    eprint("So... Good Luck!")

def arguments_validation():
    if len(sys.argv) != 2:
        return False
    else:
        return True
        
def check_file(filename_to_check):
    try:
        f = open(filename_to_check, "r")
        f.close()
        return True
    except:
        return False
        
def read_file_into_enum_list(filename):
    try:
        f = open(filename, "r")
        result = [(itr, item.rstrip('\n')) for itr, item in enumerate(f)]
        return result
    except OSError:
        eprint("Fatal error with code 0001")
        exit()

def show_input(enum_list):
    eprint("Input:")
    [eprint(f"[{n}]:{s}") for n, s in enum_list]
        
def selection_sort_enum_list_and_comment_steps(enum_list, order="a"):
    for step in range(1, len(enum_list)):
        left_idx = step - 1
        eprint(f"Step {step}: try to swap between rightest value in the left part and min(max) value in the right part")
        eprint([t[0] for t in enum_list[:left_idx+1]],"|",[t[0] for t in enum_list[left_idx+1:]])
        swap_candidate = left_idx
        for right_idx in range(left_idx + 1, len(enum_list)):
            if order == "a" and enum_list[swap_candidate][1] > enum_list[right_idx][1]:
                eprint(f"SWAP CANDIDATE:{left_idx}:{enum_list[left_idx][0]},{right_idx}:{enum_list[right_idx][0]}")
                swap_candidate = right_idx
            elif order != "a" and enum_list[swap_candidate][1] < enum_list[right_idx][1]:
                eprint(f"SWAP CANDIDATE:{left_idx}:{enum_list[left_idx][0]},{right_idx}:{enum_list[right_idx][0]}")
                swap_candidate = right_idx
                
        if swap_candidate != left_idx:
            eprint(f"SWAP {left_idx}:{enum_list[left_idx][0]}, {swap_candidate}:{enum_list[swap_candidate][0]}")
            swap = enum_list[left_idx]
            enum_list[left_idx] = enum_list[swap_candidate]
            enum_list[swap_candidate] = swap
            
        eprint()
            
    eprint("RESULT:", [t[0] for t in enum_list])

def output_result(enum_list):
    for n, s in enum_list:
        if sys.stdout.isatty():
            eprint(f"[{n}]:", end="", flush=True)
        print(s, flush=True)
    
if __name__ == "__main__":
    eprint("01_selectsort")
    if not arguments_validation():
        print_help()
        exit()
    if not check_file(sys.argv[1]):
        print_help()
        exit()
    
    enm_lst = read_file_into_enum_list(sys.argv[1])
    show_input(enm_lst)
    selection_sort_enum_list_and_comment_steps(enm_lst)
    output_result(enm_lst)