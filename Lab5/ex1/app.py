from utils import process_item as f


flag = True
while flag:
    x = input()
    if str(x) == 'q':
        flag = False
    else:
        print("Result :")
        print(f(int(x)))    