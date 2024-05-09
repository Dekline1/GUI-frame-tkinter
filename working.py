#
    try:
        command = commandBox.get("1.0", "end-1c").strip()
        commandBox.delete("1.0", tk.END)

        if command:
            result = command_list(command)
            current_content = resultsBox.get("1.0", tk.END).splitlines()

            if len(current_content) >= int(variables.resultBoxLength * variables.windowSizeConverter):
                # resultsBox.insert(tk.END, str(resultsBox.place))
                resultsBox.delete("1.0", "2.0")
            resultsBox.insert(tk.END, result)
            resultsBox.insert(tk.END, '\n')
            resultsBox.see(tk.END)
#


def OPERATION_clear():
    resultsBox.delete("1.0", tk.END)


def OPERATION_exit_app():
    window.destroy()