from Product import Product


class MyStore(object):
    def __init__(self):
        self.plist = []  # store contains list of products

    def read_products_from_file(self, file_name):
        lines = open(file_name)
        plist = []  # product list
        for line in lines:
            parts = line.split(',')  # split line into parts
            pr = Product(int(parts[0]), parts[1], float(parts[2]), parts[3])
            self.plist.append(pr)

    def show_products(self):
        print('\n')
        for pr in self.plist:
            print(pr, end='')  # end='' suppresses newline after each print

    def get_product(self, pid):
        for pr in self.plist:
            if pr.product_id == pid:
                return pr

        return None
