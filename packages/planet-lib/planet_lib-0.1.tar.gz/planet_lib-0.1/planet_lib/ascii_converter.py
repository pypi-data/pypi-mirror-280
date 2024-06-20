import pyfiglet

def ascii(text):
    """
    Transform a text to ASCII art.

    Args:
        text (str): Text to ASCII

    Returns:
        None
    """
    ascii_art = pyfiglet.figlet_format(text)
    print(ascii_art)