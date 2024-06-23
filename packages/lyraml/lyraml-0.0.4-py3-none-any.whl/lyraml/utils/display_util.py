import sys

def clear_line():
    """
    Clears the current console line using a carriage return and space padding.
    Adjust the padding length if needed to cover longer lines.
    """
    # Move the cursor back to the beginning of the line
    sys.stdout.write('\r')
    # Overwrite the line with spaces
    sys.stdout.write(' ' * 80)  # Assuming 80 characters is the width of your console
    # Move the cursor back to the beginning again
    sys.stdout.write('\r')

def green_check():
    """
    Prints a green check mark in the console.
    """
    # ANSI escape code for green text
    green_color = '\033[92m'
    # Unicode character for check mark
    check_mark = '\u2714'

    # Print the check mark in green
    return green_color + check_mark

def red_check():
    # ANSI escape code for red text
    red_color = '\033[91m'
    # ANSI escape code to reset color to default
    reset_color = '\033[0m'
    # Unicode character for "X"
    x_mark = '\u2716'

    # Print the "X" in red
    return red_color + x_mark

def reset_color():
    reset_color = '\033[0m'
    return reset_color