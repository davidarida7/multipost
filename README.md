# MultiPost
MultiPost is a small Python application that allows you to send multiple users the same message individually on Facebook Messenger.

## Setup
On whatever directory you choose on your local machine to clone this repository, execute the following command in a terminal. **__(Note: The command below assumes you have pip installed.)__**
```sh
sudo pip install fbchat
```
This makes use of the Python wrapper from [this repository](https://github.com/carpedm20/fbchat).
Afterward, create two local files in the same directory, "username.txt" and "password.txt", with "username.txt" containing the email you use to login to Faceebok and "password.txt" containing your Facebook password.

## Execution
To run the program, just execute the following command in a terminal in the directory where you cloned the Git repository. **__(Note: The command below assumes you have Python installed.)__**
```sh
python ./fb_messenger.py
```
Then, just follow the prompts.