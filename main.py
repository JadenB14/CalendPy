import dearpygui
import gui

# Define Objects
gui_obj = gui.Gui()

def main():
    print(dearpygui.__path__)
    gui_obj.context()

if __name__ == "__main__":
    main()
