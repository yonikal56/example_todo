from prettytable import PrettyTable

todo_list = []


def show_list():
    x = PrettyTable()
    x.field_names = ["TODO Item"]

    for item in todo_list:
        x.add_row([item])
    print(x)


print("To add a new item press A")
print("To delete an item press D")
print("To update an item press U")
print("To show all list press L")
print("To exit press E")

running = True

while running:
    user_input = input("Please enter your action ").lower()
    print(user_input)

    if user_input == "a":
        new_item = input("Please enter your TODO item ")

        if len(new_item) > 0 and type(new_item) is str:
            todo_list.append(new_item)
            show_list()
        else:
            print("Wrong value...")
        continue

    if user_input == "d":
        show_list()
        remove_item = input("Please enter your TODO to delete it ")

        if len(remove_item) > 0 and type(remove_item) is str:
            try:
                todo_list.remove(remove_item)
                show_list()
            except:
                print("Invalid value...")
         continue

    if user_input == "u":
        update_item = input("Enter your item to update it ")

        if len(update_item) > 0 and type(update_item) is str:
            try:
                item_idx = todo_list.index(update_item)
                if item_idx >= 0:
                    new_value = input("Enter your new value ")
                    todo_list[item_idx] = new_value
                    print("Your item was updated")
                    show_list()
                else:
                    print("The item is not found!")
            except:
                print("Invalid value...2")
        else:
            print("Invalid value...")
        continue

    if user_input == "l":
        show_list()
        continue

    if user_input == "e":
        running = False
        continue
        
    print("Invalid action, try again")
