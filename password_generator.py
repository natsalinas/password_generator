import random 
import PySimpleGUI as pg 

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*(),'

def generate_password(length):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    
    return passwords

# Set a theme
pg.theme("BluePurple")

# Display generated password in Text box
output = pg.Text()

# Create Layout 
layout = [
    [output],
    [pg.Slider(range=(8,32), default_value=12, expand_x=True, enable_events=True, orientation='horizontal')],
    [pg.Button("Generate"), pg.Button("Cancel")]
]

# Create Window 
window =  pg.Window("Password Generator", layout)

# Event Loop 
while True:
    event, values = window.read()
    print(event, values)
    new_password = generate_password(int(values[0]))
    output.update(value=new_password)
    if event == "Cancel" or event == pg.WIN_CLOSED:
        break 

# Close Window 
window.close()


 