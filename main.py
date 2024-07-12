from ui_class import UiMenu
from menu_class import MenuItem
from menu_class import menu_list
from process_order_class import ProcessOrder


def main():
    process_menu = ProcessOrder(menu_list)
    ui_menu = UiMenu(menu_list)


if __name__ == "__main__":
    main()
