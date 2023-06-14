# import requests
#
# USERS = 1
# COMMENTS = 2
#
#
# def request_key(item_type):
#     if not(item_type == USERS or item_type == COMMENTS):
#         raise Exception("Wrong input")
#     if item_type == USERS:
#         requested = 'users'
#     else:
#         requested = 'posts'
#
#     # Send a GET request to the API endpoint for users
#     users_response = requests.get(f'https://jsonplaceholder.typicode.com/{requested}')
#
#     # Check if the request was successful (status code 200)
#     if users_response.status_code == 200:
#         # Parse the users_response as JSON
#         users = users_response.json()
#
#         # Iterate over the users and print their names
#         for user in users:
#             print(user['name'])
#     else:
#         print('Failed to retrieve users. Status code:', users_response.status_code)
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     request_key(1)
#
import requests
import tkinter as tk

USER = 'userId'
POST = 'postId'
bullet_point = '\u2022'

user_id = {}
post_id = {}


def get_list(item_type, id, list_box):
    # Send a GET request to the items (todos or comments) endpoint for the specified user ID
    if item_type == USER:
        response = requests.get(f'https://jsonplaceholder.typicode.com/todos?{USER}={id}')
    elif item_type == POST:
        response = requests.get(f'https://jsonplaceholder.typicode.com/comments?{POST}={id}')
    else:
        raise Exception('wrong input in get_list')

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the users_response as JSON
        todos = response.json()

        # Clear the previous todos (if any)
        list_box.delete(0, tk.END)

        # Add the todos to the listbox
        for todo in todos:
            list_box.insert(tk.END, f'{bullet_point} {todo["title"]}')
    else:
        print('Failed to retrieve items for ID', id)


def listbox_clicked(event, listbox_activated, listbox_write_to):
    # Get the selected user from the listbox
    selected_user = listbox_activated.get(tk.ACTIVE).replace(bullet_point,'').strip()
    id = user_id[selected_user]

    # Call the get_todos function with the selected user's ID
    get_list(USER, id, listbox_write_to)


def create_toolbox(window, item_type, side):
    # Send a GET request to the items endpoint
    items_listbox = None
    items_response = []
    param = ''
    if item_type == USER:
        param = 'name'
        items_response = requests.get('https://jsonplaceholder.typicode.com/users')
    elif item_type == POST:
        param = 'title'
        items_response = requests.get('https://jsonplaceholder.typicode.com/posts')

    # Create a frame for the listbox
    frame = tk.Frame(window)
    frame.pack(side=side)

    # Create a listbox to display the items
    items_listbox = tk.Listbox(frame)
    items_listbox.pack(side=tk.TOP)

    # Check if the request was successful (status code 200)
    if items_response.status_code == 200:
        # Parse the users_response as JSON
        items = items_response.json()

        # Populate the listbox with the users
        for item in items:
            items_listbox.insert(tk.END, f"{bullet_point} {item[param]}")
            user_id[item[param]] = item['id']

        # Create a listbox to display the todos
        info_listbox = tk.Listbox(frame)
        info_listbox.pack(side=tk.BOTTOM)

        # Bind the user_clicked function to the listbox selection event
        items_listbox.bind('<<ListboxSelect>>', lambda event: listbox_clicked(event, items_listbox, info_listbox))

    return frame


if __name__ == '__main__':
    ""
    window = tk.Tk()
    users_frame = create_toolbox(window, USER, tk.LEFT)
    posts_frame = create_toolbox(window, POST, tk.RIGHT)

    users_frame.pack()
    posts_frame.pack()

    # Run the main window's event loop
    window.mainloop()