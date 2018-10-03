from functions import *


user_type, time_stamp, username = login()
if user_type == 'bootcamper':
    show_scores(username)
    logout()
elif user_type == 'lfa':
    while True:
        action = select_action()
        perform_action(action)
elif user_type == 'lf':
    show_all_scores()
    logout()

