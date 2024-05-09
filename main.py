import tkinter as tk
from tkinter import font
import variables


def execute(event=None, result_box_counter=0):
    def command_list(userCommand):

        def help_me():
            help_text = ""
            for internalCommand in variables.defaultCommandList:
                help_text += internalCommand + "\n"
            help_text += "\n"
            for internalCommand in variables.userCommandList:
                help_text += internalCommand + "\n"
            return help_text

        def a1():
            return "a1"

        if userCommand == "h":
            return help_me()
        elif userCommand == 'c':
            return "clear"
        elif userCommand == 'e':
            return "exit"
        elif userCommand == '1':
            return a1()
        else:
            return variables.defaultUnknownCommandLine1 + userCommand + variables.defaultUnknownCommandLine2
        # return command_list_result

    #
    try:
        command = commandBox.get("1.0", "end-1c").strip()
        commandBox.delete("1.0", tk.END)
        result = str(command_list(command))

        if result == "clear":
            resultsBox.delete("1.0", tk.END)
        elif result == "exit":
            window.destroy()
        else:
            current_content = resultsBox.get("1.0", tk.END).splitlines()
            if len(current_content) >= int(variables.resultBoxLength * variables.windowSizeConverter):
                resultsBox.delete("1.0", "2.0")
            else:
                resultsBox.insert(tk.END, result)
                resultsBox.insert(tk.END, '\n')
                resultsBox.see(tk.END)
    #
    except Exception as e:
        result = str(e)
        resultsBox.insert(tk.END, result)
        resultsBox.insert(tk.END, '\n')
        resultsBox.see(tk.END)


def window_geometry():
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()

    windowWidth = int(screenWidth * variables.windowSizeConverter)
    windowHeight = int(screenHeight * variables.windowSizeConverter)

    center_x = int(screenWidth / 2 - windowWidth / 2)
    center_y = int(screenHeight / 2 - windowHeight / 2)

    return window.geometry(f'{windowWidth}x{windowHeight}+{center_x}+{center_y}')


window = tk.Tk()
window.title("GUI frame Tkinter")
window_geometry()
window.configure(bg=variables.windowBackGroundColor)
default_font = font.Font(family="Source Code Pro", size=variables.fontSize)
window.option_add("*Font", default_font)

labelCommand = tk.Label(window,
                        text="Access terminal",
                        bg=variables.boxBackGroundColor,
                        fg=variables.boxTextColor)

labelCommand.place(x=int(variables.labelCommandBoxPlaceX * variables.windowSizeConverter),
                   width=int(variables.labelCommandBoxWidth * variables.windowSizeConverter),
                   y=int(variables.labelCommandBoxPlaceY * variables.windowSizeConverter),
                   height=int(variables.labelCommandBoxHeight * variables.windowSizeConverter))

labelResults = tk.Label(window,
                        text="Output data",
                        bg=variables.boxBackGroundColor,
                        fg=variables.boxTextColor)

labelResults.place(x=int((variables.commandBoxPlaceX + variables.commandBoxWidth + variables.commandAndResultsBoxOffset)
                         * variables.windowSizeConverter),
                   width=int(variables.labelCommandBoxWidth * variables.windowSizeConverter),
                   y=int(variables.labelCommandBoxPlaceY * variables.windowSizeConverter),
                   height=int(variables.labelCommandBoxHeight * variables.windowSizeConverter))

commandBox = tk.Text(window,
                     bg=variables.boxBackGroundColor,
                     fg=variables.boxTextColor)

commandBox.place(x=int(variables.commandBoxPlaceX * variables.windowSizeConverter),
                 width=int(variables.commandBoxWidth * variables.windowSizeConverter),
                 y=int((variables.labelCommandBoxPlaceY + variables.labelCommandBoxHeight +
                        variables.commandAndResultsBoxOffset) * variables.windowSizeConverter),
                 height=int(variables.commandBoxHeight * variables.windowSizeConverter))

commandBox.bind('<Return>', execute)

resultsBox = tk.Text(window,
                     bg=variables.boxBackGroundColor,
                     fg=variables.boxTextColor)

resultsBox.place(x=int((variables.commandBoxPlaceX + variables.commandBoxWidth +
                        variables.commandAndResultsBoxOffset) * variables.windowSizeConverter),
                 width=int(variables.resultsBoxWidth * variables.windowSizeConverter),
                 y=int((variables.labelResultsBoxPlaceY + variables.labelResultsBoxHeight +
                       variables.commandAndResultsBoxOffset) * variables.windowSizeConverter),
                 height=int(variables.resultsBoxHeight * variables.windowSizeConverter))

window.mainloop()
