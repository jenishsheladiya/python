# print all the elements in a list using recursion

list = [1, 4, 9, 16, 25, 36, 49, 64, 74, 84, 100]

def cal_ele(list , idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    cal_ele(list, idx+1)

cal_ele(list)