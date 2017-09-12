from fbchat import Client
from fbchat.models import *

username_file = open("username.txt", "r")
username = username_file.read()
username_file.close()
password_file = open("password.txt", "r")
password = password_file.read()
password_file.close()
client = Client(username, password)
user_input = raw_input('What are the names of the users on Facebook Messenger you would like to send messages to? Write their full names, separated by commas.\n')
user_list = user_input.split(", ")
user_id_array = []
for name in user_list:
	user_id_array.append(client.searchForUsers(name)[0].uid)
message = raw_input('Please input the message you would like to send.\n')
for identity in user_id_array:
	client.sendMessage(message, thread_id=identity, thread_type=ThreadType.USER)
client.logout()