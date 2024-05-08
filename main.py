import tkinter as tk
import variables


def execute(event=None, result_box_counter=0):
    def command_list(userCommand):

        def help_me():
            pass

        def a1():
            return "a1 ok"

        def a2():
            return "a2 ok"

        if userCommand == "a1":
            return a1()
        elif userCommand == 'a2':
            return a2()
        elif userCommand == 'h':
            return help_me()
        else:
            return variables.defaultUnknownCommandLine1 + userCommand + variables.defaultUnknownCommandLine2
        # return command_list_result

    try:
        command = commandBox.get("1.0", "end-1c").strip()
        commandBox.delete("1.0", tk.END)

        if command:
            result = command_list(command)
            current_content = resultsBox.get("1.0", tk.END).splitlines()

            if len(current_content) >= int(variables.resultBoxLength * variables.windowSizeConverter + 1):
                # resultsBox.insert(tk.END, str(resultsBox.place))
                resultsBox.delete("1.0", "2.0")
            resultsBox.insert(tk.END, result + '\n')
            resultsBox.see(tk.END)

    except Exception as e:
        result = str(e)
        resultsBox.insert(tk.END, result + '\n')
        resultsBox.see(tk.END)


window = tk.Tk()
window.configure(bg=variables.windowBackGroundColor)
window.title("UL Database")
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()

windowWidth = int(screenWidth * variables.windowSizeConverter)
windowHeight = int(screenHeight * variables.windowSizeConverter)
center_x = int(screenWidth / 2 - windowWidth / 2)
center_y = int(screenHeight / 2 - windowHeight / 2)
window.geometry(f'{windowWidth}x{windowHeight}+{center_x}+{center_y}')

commandBox = tk.Text(window)
commandBox.place(x=int(variables.commandBoxPlaceX * variables.windowSizeConverter),
                 width=int(variables.commandBoxWidth * variables.windowSizeConverter),
                 y=int(variables.commandBoxPlaceY * variables.windowSizeConverter),
                 height=int(variables.commandBoxHeight * variables.windowSizeConverter))
commandBox.configure(bg=variables.boxBackGroundColor, fg=variables.boxTextColor)
commandBox.bind('<Return>', execute)

resultsBox = tk.Text(window)
resultsBox.place(x=int(variables.resultsBoxPlaceX * variables.windowSizeConverter),
                 width=int(variables.resultsBoxWidth * variables.windowSizeConverter),
                 y=int((variables.commandBoxPlaceY + variables.commandBoxHeight +
                        variables.commandAndResultsBoxOffset) * variables.windowSizeConverter),
                 height=int(variables.resultsBoxHeight * variables.windowSizeConverter))
resultsBox.configure(bg=variables.boxBackGroundColor, fg=variables.boxTextColor)

window.mainloop()
