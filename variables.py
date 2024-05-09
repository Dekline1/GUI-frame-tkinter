# by_script settable parameters & options (no parameters validation)
windowSizeConverter = 0.8  # default value = 0.8, min rational value is 0.4
fontSize = 14  # default value = 14 for bold, and 13 for normal. Non scalable

# all bellowed values is compared with windowSizeConverter in script

resultBoxLength = 15  # default value = 15 (experimental value, not real amount of lines)

defaultUnknownCommandLine1 = "Unknown command: "
defaultUnknownCommandLine2 = ", type: [h]elp"


labelCommandBoxWidth = 350  # default value = 350
labelCommandBoxHeight = 80  # default value = 80
labelCommandBoxPlaceX = 50  # default value = 50
labelCommandBoxPlaceY = 50  # default value = 50

labelResultsBoxWidth = 350  # default value = 350
labelResultsBoxHeight = 80  # default value = 008
# labelResultsBoxPlaceX # auto adjusted in script
labelResultsBoxPlaceY = 50  # default value = 50


commandBoxWidth = 700  # default value = 700
commandBoxHeight = 80  # default value = 400
commandBoxPlaceX = 50  # default value = 50
# commandBoxPlaceY # auto adjusted in script

commandAndResultsBoxOffset = 50  # default value = 50

resultsBoxWidth = 1050  # default value = 700
resultsBoxHeight = 800  # default value = 400
# resultsBoxPlaceX  # auto adjusted in script
resultsBoxPlaceY = 50  # default value = 50


windowBackGroundColor = "#1e1f22"
boxBackGroundColor = "#2b2d30"
boxTextColor = "#bcbec4"

# command list, use # if not in use

defaultCommandList = [
    "[h]elp - display list of usable Commands",
    "[c]lear - clean all windows",
    "[e]xit - close app"]

# add own commands here
userCommandList = [
    "a[1] - aaaaaaaaaa",
    "a[2] - aaaaaaaaaa",
    "a[3] - aaaaaaaaaa",
    'a[4] - aaaaaaaaaa']
