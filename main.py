# import requests
#
# USERS = 1
# COMMENTS = 2
#
#
# def request_key(key):
#     if not(key == USERS or key == COMMENTS):
#         raise Exception("Wrong input")
#     if key == USERS:
#         requested = 'users'
#     else:
#         requested = 'posts'
#
#     # Send a GET request to the API endpoint for users
#     response = requests.get(f'https://jsonplaceholder.typicode.com/{requested}')
#
#     # Check if the request was successful (status code 200)
#     if response.status_code == 200:
#         # Parse the response as JSON
#         users = response.json()
#
#         # Iterate over the users and print their names
#         for user in users:
#             print(user['name'])
#     else:
#         print('Failed to retrieve users. Status code:', response.status_code)
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     request_key(1)
#
import requests
import tkinter as tk


def get_todos(user_id):
    # Send a GET request to the todos endpoint for the specified user ID
    response = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={user_id}')

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the response as JSON
        todos = response.json()

        # Clear the previous todos (if any)
        todos_listbox.delete(0, tk.END)

        # Add the todos to the listbox
        for todo in todos:
            todos_listbox.insert(tk.END, todo['title'])
    else:
        print('Failed to retrieve todos for user ID', user_id)


def user_clicked(event):
    # Get the selected user from the listbox
    selected_user = users_listbox.get(tk.ACTIVE)
    user_id = int(selected_user.split(':')[0])

    # Call the get_todos function with the selected user's ID
    get_todos(user_id)


# Send a GET request to the users endpoint
response = requests.get('https://jsonplaceholder.typicode.com/users')

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the response as JSON
    users = response.json()

    # Create the main window
    window = tk.Tk()

    # Create a listbox to display the users
    users_listbox = tk.Listbox(window)
    users_listbox.pack(side=tk.TOP)

    # Populate the listbox with the users
    for user in users:
        users_listbox.insert(tk.END, f"{user['name']}")

    # Create a listbox to display the todos
    todos_listbox = tk.Listbox(window)
    todos_listbox.pack(side=tk.BOTTOM)

    # Bind the user_clicked function to the listbox selection event
    users_listbox.bind('<<ListboxSelect>>', user_clicked)

    # Run the main window's event loop
    window.mainloop()

else:
    print('Failed to retrieve users. Status code:', response.status_code)
