from taipy.gui import Gui, notify
from time import strftime

# Function to get the current time
def get_current_time():
    return strftime('%I:%M:%S %p')

# Variable to hold the current time
current_time = get_current_time()

# Function to update the time
def update_time(state):
    state.current_time = get_current_time()
    notify(state, "info", f"Time updated: {state.current_time}")

# Create the page content
page = """
### Current Time
<|{current_time}|text|class_name=time-display|>

<|Update Time|button|on_action=update_time|class_name=update-button|>
"""



gui = Gui(page=page)
#gui.css = css
gui.run(debug=True)
    

