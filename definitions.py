def help_me():
    help_text = "\n"
    for internalCommand in CommandDictionary:
        help_text += internalCommand + "\n"
    return help_text


def clear():
    return "clear"


def exit_app():
    return "exit"


def a1():
    return "a1"


# command list, use # if not in use

CommandDictionary = {
    "h": help_me,
    "c": clear,
    "e": exit_app,
    "1": a1,
    "2": a1,
    "3": a1,
    "4": a1,
    "5": a1,
    "6": a1,
}

# defaultCommandList = [
#     "[h]elp - display list of usable commands",
#     "[c]lear - clean all windows",
#     "[e]xit - close app"]
