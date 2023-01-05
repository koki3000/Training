menu_dict = {
    '1':['soup', 8.2],
    '2':['chips', 7],
    '3':['pizza', 30],
}

if __name__ == '__main__':
    print('Menu')
    for pos in menu_dict:
        print(f'{pos} - {menu_dict[pos][0]} - {menu_dict[pos][1]} zl')
    print('0 - nothing else')
    order = []
    sum = 0
    while True:
        try:
            pos = input('Which dish do you want to order? ')
            if pos == '0':
                break
            else:
                order.append(menu_dict[pos])
                sum += menu_dict[pos][1]
        except:
            print('please input number from menu')
    
    print('Your order:')
    for pos in order:
        print(f'{pos[0]} - {pos[1]} zl')
    print(f'Total {sum} zl')