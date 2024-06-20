import os


class TerminalColors:
    """ TerminalColor,
    Modify Terminal Text and Background Color 
     and Formatting

     Returns a string with the ANSI Character Sequence
    """
    os.system("")

    END = '\33[0m'
    RESET = '\33[0m'
    BOLD = '\33[1m'
    ITALIC = '\33[3m'
    URL = '\33[4m'
    SELECTED = '\33[7m'

    BLACK = '\33[30m'
    RED = '\33[31m'
    GREEN = '\33[32m'
    YELLOW = '\33[33m'
    BLUE = '\33[34m'
    VIOLET = '\33[35m'
    TEAL = '\33[36m'
    WHITE = '\33[37m'

    BLACK_BACKGROUND = '\33[40m'
    RED_BACKGROUND = '\33[41m'
    GREEN_BACKGROUND = '\33[42m'
    YELLOW_BACKGROUND = '\33[43m'
    BLUE_BACKGROUND = '\33[44m'
    VIOLET_BACKGROUND = '\33[45m'
    TEAL_BACKGROUND = '\33[46m'
    WHITE_BACKGROUND = '\33[47m'

    GRAY = '\33[90m'
    LIGHT_RED = '\33[91m'
    LIGHT_GREEN = '\33[92m'
    LIGHT_YELLOW = '\33[93m'
    LIGHT_BLUE = '\33[94m'
    LIGHT_VIOLET = '\33[95m'
    LIGHT_TEAL = '\33[96m'
    LIGHT_GRAY = '\33[97m'

    GRAY_BACKGROUND = '\33[100m'
    LIGHT_RED_BACKGROUND = '\33[101m'
    LIGHT_GREEN_BACKGROUND = '\33[102m'
    LIGHT_YELLOW_BACKGROUND = '\33[103m'
    LIGHT_BLUE_BACKGROUND = '\33[104m'
    LIGHT_VIOLET_BACKGROUND = '\33[105m'
    LIGHT_TEAL_BACKGROUND = '\33[106m'
    LIGHT_GRAY_BACKGROUND = '\33[107m'

    @staticmethod
    def format_message(level: str, message: str, formatting: str) -> str:
        """
        Format a message with a given level, message, and formatting.

        :param level: The level of the message (e.g., "ERROR").
        :param message: The message to be formatted.
        :param formatting: The ANSI formatting for the message.
        :return: The formatted message string.
        """
        return f"{formatting}{level}: {message}{TerminalColors.RESET}"

    @staticmethod
    def log_message(level: str, message: str, formatting: str, should_print: bool = True) -> str:
        """
        Log a message with a given level and formatting.

        :param level: The level of the message (e.g., "ERROR").
        :param message: The message to be logged.
        :param formatting: The ANSI formatting for the message.
        :param should_print: Whether to print the message to the terminal.
        :return: The formatted message string.
        """
        formatted_message = TerminalColors.format_message(level, message, formatting)
        if should_print:
            print(formatted_message)
        return formatted_message

    @staticmethod
    def error(message: str, formatting: str = RED + BOLD, should_print: bool = True) -> str:
        """
        Log an error message.

        :param message: The error message to be logged.
        :param formatting: The ANSI formatting for the error message.
        :param should_print: Whether to print the message to the terminal.
        :return: The formatted error message string.
        """
        return TerminalColors.log_message("ERROR", message, formatting, should_print)

    @staticmethod
    def warning(message: str, formatting: str = YELLOW + BOLD, should_print: bool = True) -> str:
        """
        Log a warning message.

        :param message: The warning message to be logged.
        :param formatting: The ANSI formatting for the warning message.
        :param should_print: Whether to print the message to the terminal.
        :return: The formatted warning message string.
        """
        return TerminalColors.log_message("WARNING", message, formatting, should_print)

    @staticmethod
    def success(message: str, formatting: str = LIGHT_GREEN + BOLD, should_print: bool = True) -> str:
        """
        Log a success message.

        :param message: The success message to be logged.
        :param formatting: The ANSI formatting for the success message.
        :param should_print: Whether to print the message to the terminal.
        :return: The formatted success message string.
        """
        return TerminalColors.log_message("SUCCESS", message, formatting, should_print)

    @staticmethod
    def info(message: str, formatting: str = LIGHT_GRAY + BOLD, should_print: bool = True) -> str:
        """
        Log an info message.

        :param message: The info message to be logged.
        :param formatting: The ANSI formatting for the info message.
        :param should_print: Whether to print the message to the terminal.
        :return: The formatted info message string.
        """
        return TerminalColors.log_message("INFO", message, formatting, should_print)


class DisplayColors:
    """
    Helper Functions To Display All Combinations Of
    Colors, Styles, and Backgrounds
    """

    # Required for colors to display properly in Windows terminal
    os.system("")

    def __init__(self):
        self.text_colors = {
            "dark": {
                "BLACK": TerminalColors.BLACK,
                "RED": TerminalColors.RED,
                "GREEN": TerminalColors.GREEN,
                "YELLOW": TerminalColors.YELLOW,
                "BLUE": TerminalColors.BLUE,
                "VIOLET": TerminalColors.VIOLET,
                "TEAL": TerminalColors.TEAL,
                "WHITE": TerminalColors.WHITE,
            },
            "light": {
                "GRAY": TerminalColors.GRAY,
                "LIGHT_RED": TerminalColors.LIGHT_RED,
                "LIGHT_GREEN": TerminalColors.LIGHT_GREEN,
                "LIGHT_YELLOW": TerminalColors.LIGHT_YELLOW,
                "LIGHT_BLUE": TerminalColors.LIGHT_BLUE,
                "LIGHT_VIOLET": TerminalColors.LIGHT_VIOLET,
                "LIGHT_TEAL": TerminalColors.LIGHT_TEAL,
                "LIGHT_GRAY": TerminalColors.LIGHT_GRAY,
            }
        }

        self.text_styles = {
            "END": TerminalColors.END,
            "BOLD": TerminalColors.BOLD,
            "ITALIC": TerminalColors.ITALIC,
            "URL": TerminalColors.URL,
            "SELECTED": TerminalColors.SELECTED,
        }

        self.background_colors = {
            "dark": {
                "BLACK_BACKGROUND": TerminalColors.BLACK_BACKGROUND,
                "RED_BACKGROUND": TerminalColors.RED_BACKGROUND,
                "GREEN_BACKGROUND": TerminalColors.GREEN_BACKGROUND,
                "YELLOW_BACKGROUND": TerminalColors.YELLOW_BACKGROUND,
                "BLUE_BACKGROUND": TerminalColors.BLUE_BACKGROUND,
                "VIOLET_BACKGROUND": TerminalColors.VIOLET_BACKGROUND,
                "TEAL_BACKGROUND": TerminalColors.TEAL_BACKGROUND,
                "WHITE_BACKGROUND": TerminalColors.WHITE_BACKGROUND,
            },
            "light": {
                "GRAY_BACKGROUND": TerminalColors.GRAY_BACKGROUND,
                "LIGHT_RED_BACKGROUND": TerminalColors.LIGHT_RED_BACKGROUND,
                "LIGHT_GREEN_BACKGROUND": TerminalColors.LIGHT_GREEN_BACKGROUND,
                "LIGHT_YELLOW_BACKGROUND": TerminalColors.LIGHT_YELLOW_BACKGROUND,
                "LIGHT_BLUE_BACKGROUND": TerminalColors.LIGHT_BLUE_BACKGROUND,
                "LIGHT_VIOLET_BACKGROUND": TerminalColors.LIGHT_VIOLET_BACKGROUND,
                "LIGHT_TEAL_BACKGROUND": TerminalColors.LIGHT_TEAL_BACKGROUND,
                "LIGHT_GRAY_BACKGROUND": TerminalColors.LIGHT_GRAY_BACKGROUND,
            }
        }

    def show_combinations(self, colors, backgrounds):
        """
        Prints All Colors, Background, and Styles Combinations
        to the Terminal
        """
        for style_name, style in self.text_styles.items():
            for color_name, color in colors.items():
                line = ''
                for bg_name, background in backgrounds.items():
                    text_format = f"{style_name};{color_name};{bg_name}"
                    formatted_text = f"{style}{color}{background}"
                    needed_white_space = 50 - len(text_format)
                    line += f"{formatted_text}{text_format}{' ' * needed_white_space}{TerminalColors.RESET}"
                print(line)
            print('\n')

    def show_dark_colors_and_backgrounds(self):
        """
        Displays all combinations of dark colors and backgrounds with text styles
        """
        self.show_combinations(self.text_colors["dark"], self.background_colors["dark"])

    def show_light_colors_and_backgrounds(self):
        """
        Displays all combinations of light colors and backgrounds with text styles
        """
        self.show_combinations(self.text_colors["light"], self.background_colors["light"])

    def show_all_colors_and_backgrounds(self):
        """
        Displays all combinations of both light and dark colors and backgrounds with text styles
        """
        self.show_combinations(self.text_colors["dark"], self.background_colors["dark"])
        self.show_combinations(self.text_colors["light"], self.background_colors["light"])