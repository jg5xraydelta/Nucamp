class Queue:
    def __init__(self) -> None:
        self.items = []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.size() == 0:
            return None
        return self.items.pop(0)

    def show_queue(self):
        print(self.items)


class IceCreamShop:
    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()

    def take_order(self, customer, flavor, scoops):
        if flavor not in self.flavors:
            print("Sorry, we don't have that flavor.")
            return

        if scoops not in [1,2,3]:
            print("Please choose either 1, 2, or 3 scoops.")
            return

        print("Order created!")
        order = {"customer": customer, "flavor": flavor, "scoops":
                 scoops}
        self.orders.enqueue(order)

    def show_all_orders(self):
        print("\nAll Pending Ice Cream Orders:")
        for order in self.orders.items:
            print("Customer:", order['customer'], "--Flavor:", order["flavor"], "--Scoops:", order["scoops"])

    def next_order(self):
        print("\nNext Order Up!")
        order = self.orders.dequeue()
        print("Customer:", order['customer'], "--Flavor:", order["flavor"], "--Scoops:", order["scoops"])


shop = IceCreamShop(['rocky road', 'mint chip', 'pistachio'])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()
