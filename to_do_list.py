def main():
    to_do_list = []
    item = input("Enter a to-do list item: ")
    while item:
        to_do_list.append(item)
        item = input("Enter a to-do list item: ")
    print_list(to_do_list)

def print_list(to_do_list):
    print("Here's your to-do list:")
    for i in range(len(to_do_list)):
        num = i + 1
        print(num, to_do_list[i])

if __name__ == "__main__":
    main()
