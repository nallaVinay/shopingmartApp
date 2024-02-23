class ShoppingItem(object):
    def __init__(self, prod, qty):
        self.product = prod
        self.quantity = qty


class ShoppingCart(object):
    def __init__(self):
        self.items = []  # in the beginning shopping cart is empty

    def add_item(self, product, qty):
        sitem = ShoppingItem(product, qty)
        self.items.append(sitem)

    def remove_item(self, pid):  # remove item from cart
        item_to_remove = None
        for item in self.items:
            if item.product.product_id == pid:
                item_to_remove = item
        if item_to_remove != None:
            self.items.remove(item_to_remove)

    def compute_total(self):  # total price of items in shopping cart
        total = 0
        for item in self.items:
            total = total + item.product.price * item.quantity
        return total

    def apply_discount(self, total):
        if 100 < total < 500:
            total = total - (total * 5 / 100)
        elif 500 < total < 1000:
            total = total - (total * 10 / 100)
        else:
            total = total - (total * 15 / 100)

        return total

    def show_cart(self):
            for item in self.items:
                print('\t\t' + item.product.__str__().replace('\n', '') + '\tqty=' +
                      str(item.quantity))

    def Delete_cart(self):
          self.items.clear()
          print("cart as been deleted  ")