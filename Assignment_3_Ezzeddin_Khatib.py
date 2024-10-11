def count_digits(n):
    if n == 0:
        return 0
    else:
        return 1 + count_digits(n // 10)

def find_max(lst, n):
    if n == 1:
        return lst[0]
    else:
        return max(lst[n-1], find_max(lst, n-1))

def count_tags(html, tag):
    open_tag = f"<{tag}>"
    close_tag = f"</{tag}>"
    if open_tag not in html:
        return 0
    else:
        open_index = html.find(open_tag)
        close_index = html.find(close_tag, open_index) + len(close_tag)
        return 1 + count_tags(html[close_index:], tag)

while True:
        print("1. Count Digits")
        print("2. Find Max")
        print("3. Count Tags")
        print("4. Exit")
        choice = input("Enter a choice: ")

        if choice == "1":
            number = int(input("Enter an integer: "))
            print(f"Number of digits: {count_digits(abs(number))}")
        
        elif choice == "2":
            lst = list(map(int, input("Enter a list of integers (comma-separated): ").split(',')))
            if lst:
                print(f"Maximum value: {find_max(lst, len(lst))}")
            else:
                print("List is empty.")
        
        elif choice == "3":
            html_code = """<html>
<head>
<title>My Website</title>
</head>
<body>
<h1>Welcome to my website!</h1>
<p>Here you'll find information about me and my hobbies</p>
<h2>Hobbies</h2>
<ul>
<li>Playing guitar</li>
<li>Reading books</li>
<li>Traveling</li>
<li>Writing cool h1 tags</li>
</ul>
</body>
</html>"""
            tag = input("Enter the HTML tag to count: ")
            print(f"Occurrences of '{tag}' tag: {count_tags(html_code, tag)}")
        
        elif choice == "4":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Try again.")