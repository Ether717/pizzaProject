from menu_class import menu_list

# providing a daily summary of the quantities sold for each pizza variety

class Summary():
    """" """
    
    # constructor
    def __init__(self,menu_list, order_receipt_list):
        
        # both are lists with objects inside to call methods
        self.menu_list = menu_list
        self.order_receipt_list = order_receipt_list