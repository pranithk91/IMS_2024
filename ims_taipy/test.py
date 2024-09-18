import taipy as tp
#$from taipy import Config, Scheduler
from taipy.gui import Gui, navigate, notify
import taipy.gui.builder as tgb
from time import strftime
import datetime

def on_menu(state, action, info):
    page = info["args"][0]
    navigate(state, to=page)

userInput = ""
medName = ""
medicineDeliveryDets= []
dDate = ""
medQty = ""
newPrice = ""
table_entry = ""

# Define the page layout
"""def get_time():
    string = strftime('%I:%M:%S %p')
    self.timeLabel.configure(text=string)
    self.timeLabel.after(1000, get_time)
get_time()"""

def get_current_time():
    return strftime('%I:%M:%S %p')

# Variable to hold the current time
current_time = get_current_time()

# Function to update the time
def update_time(state):
    state.current_time = get_current_time()
    notify(state, "info", f"Time updated: {state.current_time}")

#Scheduler.every(10).minutes.do(tp.create_scenario, update_time)
# Add a navbar to switch from one page to the other
with tgb.Page() as root_page:
    def get_time(state):
        string = strftime('%I:%M:%S %p')
        
    with tgb.layout(columns = "1fr 200px" ):
        tgb.text("### Title Here - This is gonna be shown in all Pages", mode="md")
        tgb.text("### {current_time}", class_name='time_display', mode = 'md')
    tgb.menu(label="Menu", 
             lov=[('page1', 'Medicine Deliveries'), ('page2', 'Page 2')], 
             on_action=on_menu)

def button_pressed(state):
    # Create a dictionary with the current input values
    global table_entry
    delivery = {
        "date": state.dDate,
        "name": state.medName,
        "quantity": state.medQty,
        "price": state.newPrice
    }
    
    # Add the dictionary to the deliveries list
    state.medicineDeliveryDets.append(delivery)
    table_entry = medicineDeliveryDets[0].values()
    # Clear the input fields
    state.dDate = ""
    state.medName = ""
    state.medQty = ""
    state.newPrice = ""
    
    #table1.reload()
    #table1.rebuild()
    # Notify the user
    
    notify(state, "info", "Delivery added successfully!")
    print(f"User input stored: {medicineDeliveryDets[0].values()}")

with tgb.Page() as MedicineDeliveriesPage:
    with tgb.layout(columns="4*1"):
        with tgb.part():
            tgb.text("Delivery Date", mode='md')
            tgb.input(label="date", value="{dDate}")
        with tgb.part():
            tgb.text("Medicine Name", mode='md')
            tgb.input(label="name", value="{medName}")

    #with tgb.layout(columns="1fr 1fr"):
        with tgb.part():
            tgb.text("Quantity", mode="md")
            tgb.input(label="qty", value="{medQty}")
        with tgb.part():
            tgb.text("New Price", mode="md")
            tgb.input(label="price", value="{newPrice}")

    with tgb.layout(columns="500px"):
        with tgb.part():
            tgb.button("Submit", on_action=button_pressed, class_name="submit_button")
    # Display the list of deliveries
    tgb.table("{table_entry}", rebuild=True)

css= """
.time-display {
    font-size: 8em;
    font-weight: bold;
    text-align: center;
    color-primary: #089404
}
.submit_button {
    text_align: left;
    color-background-light: #089404;
    color-background-dark: #089404
}
"""

#Last submitted value: <|{user_input}|>
#, mode="md")
    
with tgb.Page() as page_2:
    tgb.text("## This is page 2", mode="md")

pages = {
    "/": root_page,
    "page1": MedicineDeliveriesPage,
    "page2": page_2
}

gui = Gui(pages=pages, css_file=css).run(debug=True, port=5008)



