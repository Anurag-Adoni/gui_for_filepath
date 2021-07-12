import PySimpleGUI as sg
import os
import sys

''' copy and paste this code to input filepath with Gui'''

#setting up the gui
sg.theme("DarkTeal2")
layout = [[sg.T("")], [sg.Text("Choose the file : "),sg.Input(), sg.FileBrowse(key="-IN-")], [sg.Button("Submit")]]
window = sg.Window('Path Finder', layout, size=(600, 150))
#reading the file path and the buttons 
try:
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Exit":
            sys.exit()
            
        elif event == "Submit":
            fpath = values["-IN-"]
            window.close()
            break

except (FileNotFoundError, IOError):
    sg.popup("file not found please try again")
    print("error")
'''
if the file path is not working convert it to a rawstring by placing "r" in front of
the file path (ex: r'C:/users/myfile.txt')
'''
print("fpath is :",fpath)
abs_path = os.path.abspath(fpath)
print("absolute path is :" ,abs_path)
raw_path = r"abs_path"
