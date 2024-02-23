import sys
from ShoppingCart import ShoppingCart
from MyStore import MyStore
import re
import pickle


def main():
    fname = 'ProductsData.txt'
    store = MyStore()
    plist = store.read_products_from_file(fname)
    scart = ShoppingCart()  # empty shopping cart
    main_menu = '1: View Products' + '\n' + '2: Shop' + '\n' + \
                '3: Checkout' + '\n' + '4:Add a Product' + '\n' + '5.Delete a Product' + '\n' + '0: Exit'
    shopping_menu = '\t1: Add Product to Cart' + '\n\t' + '2: Remove Product FromCart' + '\n\t' + \
                    '3:show cart' + '\n\t' + '4:delet cart' + '\n\t' + '0:back main'
    menu_option = 1
    try:
        # cecks for picke file if exist other  wise create at close time of application
        p = open('dict.pickle', 'rb')
        LOADED_DICT = pickle.load(p)
        print('PRODUCTS IN PICKLE FILE::\n', LOADED_DICT['products'])
        print('YOUR PREVIOUS SAVED CART::\n', LOADED_DICT['saved_cart'])

    except Exception:
        print("YOU DON'T HAVE ANY SAVED CART STATUS ")
    count = 1
    while menu_option > 0:
        print('\n' + main_menu)
        menu_option = input('please enter an option: ')
        menu_option = int(menu_option)
        if count == 2:
            store.plist = []  # previous plist will be one and new plist will be updated
            store.read_products_from_file(fname)
        if menu_option == 0:
            print('quitting application..')
            pick = open('dict.pickle', "wb")
            l = store.plist
            s = []
            for items in scart.items:
                s.append(items.product.__str__().replace('\n', ' ').replace('\t', ' ') + 'qty=' +
                         str(items.quantity))
            dictionary = {'products': l, 'saved_cart': s}
            pickle.dump(dictionary, pick)
            pick.close()
            break  # exit main loop
        if menu_option == 1:
            store.show_products()
        if menu_option == 2:
            shopping_menu_option = 1
            while shopping_menu_option > 0:
                print('\n' + shopping_menu)
                soption = input('\tplease enter a shopping option: ')
                shopping_menu_option = int(soption)
                if shopping_menu_option == 1:  # add to cart
                    pid_qty = input('\tplease enter productid,qty to buy (ex:1001, 3): ')
                    if pid_qty.index(',') < 0:
                        print('invalid productid,qty specified..')
                    else:
                        parts = pid_qty.split(',')
                        pid = int(parts[0])
                        qty = int(parts[1])
                        pr = store.get_product(pid)
                        if pr is not None:
                            scart.add_item(pr, qty)
                if shopping_menu_option == 2:  # remove from cart
                    pid = input('\tplease enter productid to remove from cart: ')
                    scart.remove_item(int(pid))
                if shopping_menu_option == 3:  # view cart
                    scart.show_cart()
                if shopping_menu_option == 4:  # delet cart
                    scart.Delete_cart()

        if menu_option == 3:  # checkout
            total = scart.compute_total()
            total_after_discount = scart.apply_discount(total)
            print('\n------check ot info---------')
            print('Total Amount = ', total, ' Total Amount after discount = ', total_after_discount)
        if menu_option == 4:

            id = input('enter the id of product eg(1000):  ') + ','
            product_name = input('enter the product name:  ')
            value = input('enter price of product: ')
            cateory = input('enter  cateory eg(sports,food,electronics,etc): ')
            f = open('ProductsData.txt', 'r')
            l = f.readlines()
            f.close()
            string = ''.join(l)

            try:
                if re.search(id, string):
                    print('--------->plz enter a unique id<-------- \n'
                          'you have entered already  existed ID ')
                else:
                    id = id.replace(',', '')
                    if int(id) and float(value) and isinstance(product_name, str) and isinstance(cateory, str):
                        f = open('ProductsData.txt', 'a')
                        f.write('\n' + id + ',' + product_name + ',' + value + ',' + cateory)
                        print('add product is done.  ')
                        f.close()
                        if count == 2:
                            pass
                        else:
                            count += 1

            except Exception:
                print(
                    'plz make sure to enter id-->integer\tproduct-->string\t value as-->int or float \t category-->string ')
        if menu_option == 5:
            f = open('ProductsData.txt')

            lines = f.readlines()
            enter = input('enter the  id to remove:')
            for i in lines:
                if enter in i:
                    lines.remove(i)
                    print('product removed')

            f.close()
            f = open('ProductsData.txt', 'w')
            f.writelines(lines)
            f.close()
            if count == 2:
                pass
            else:
                count += 1


if __name__ == "__main__":
    sys.exit(int(main() or 0))
