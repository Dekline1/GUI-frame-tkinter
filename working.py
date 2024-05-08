#
resultsBox = tk.Text(window,
                     width=int(variables.resultsBoxWidth * variables.windowSizeConverter),
                     height=int(variables.resultsBoxHeight * variables.windowSizeConverter))
resultsBox.configure(bg=variables.boxBackGroundColor, fg=variables.boxTextColor)
resultsBox.place(x=variables.resultsBoxPlaceX * variables.windowSizeConverter,
                 y=(variables.commandBoxPlaceY + variables.commandBoxHeight*15 + variables.commandAndResultsBoxOffset)
                   * variables.windowSizeConverter)
#



#
commandBox = tk.Text(window, width=int(variables.commandBoxWidth * variables.windowSizeConverter),
                     height=int(variables.commandBoxHeight * variables.windowSizeConverter))
commandBox.place(x=variables.commandBoxPlaceX * variables.windowSizeConverter,
                 y=variables.commandBoxPlaceY * variables.windowSizeConverter)
commandBox.configure(bg=variables.boxBackGroundColor, fg=variables.boxTextColor)
commandBox.bind('<Return>', execute)
#