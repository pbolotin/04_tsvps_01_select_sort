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
        result = [(itr, item) for itr, item in enumerate(f)]
        return result
    except Exception:
        eprint("Fatal error with code 0001")
        exit()
        
def selection_sort_enum_list_and_comment_steps(enum_list, order="a"):
    for step in range(1, len(enum_list)):
        eprint(f"Step {step}: search value less than first in the right part")
        left_idx = step - 1
        for right_idx in range(left_idx + 1, len(enum_list)):
            if order == "a":
                if enum_list[left_idx][1] > enum_list[right_idx][1]:
                    eprint(f"SWAP:{enum_list[left_idx][0]},{enum_list[right_idx][0]}")
                    swap = enum_list[left_idx]
                    enum_list[left_idx] = enum_list[right_idx]
                    enum_list[right_idx] = swap
            else:
                if enum_list[left_idx][1] < enum_list[right_idx][1]:
                    eprint(f"SWAP:{enum_list[left_idx][0]},{enum_list[right_idx][0]}")
                    swap = enum_list[left_idx]
                    enum_list[left_idx] = enum_list[right_idx]
                    enum_list[right_idx] = swap

if __name__ == "__main__":
    eprint("01_selectsort")
    if not arguments_validation():
        print_help()
        exit()
    if not check_file(sys.argv[1]):
        print_help()
        exit()
    
    enm_lst = read_file_into_enum_list(sys.argv[1])
    eprint(enm_lst)
    selection_sort_enum_list_and_comment_steps(enm_lst)
    eprint(enm_lst)