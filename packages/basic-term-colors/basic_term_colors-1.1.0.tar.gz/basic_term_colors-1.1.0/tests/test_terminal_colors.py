import pytest
from src.terminal_colors import TerminalColors
import os


@pytest.mark.parametrize(
    "method, level, message, formatting, should_print, expected_output",
    [
        (TerminalColors.error, "ERROR", "This Is An Error", TerminalColors.RED + TerminalColors.BOLD, True,
         f"{TerminalColors.RED + TerminalColors.BOLD}ERROR: This Is An Error{TerminalColors.RESET}\n"),
        (TerminalColors.error, "ERROR", "This Is An Error Message", TerminalColors.RED + TerminalColors.BOLD, False,
         f"{TerminalColors.RED + TerminalColors.BOLD}ERROR: This Is An Error Message{TerminalColors.RESET}"),
        (TerminalColors.error, "ERROR", "This Is An Error Message", TerminalColors.LIGHT_RED + TerminalColors.ITALIC,
         True,
         f"{TerminalColors.LIGHT_RED + TerminalColors.ITALIC}ERROR: This Is An Error Message{TerminalColors.RESET}\n"),
        (TerminalColors.warning, "WARNING", "This Is A Warning Message", TerminalColors.YELLOW + TerminalColors.BOLD,
         True,
         f"{TerminalColors.YELLOW + TerminalColors.BOLD}WARNING: This Is A Warning Message{TerminalColors.RESET}\n"),
        (TerminalColors.warning, "WARNING", "This Is A Warning Message", TerminalColors.YELLOW + TerminalColors.BOLD,
         False,
         f"{TerminalColors.YELLOW + TerminalColors.BOLD}WARNING: This Is A Warning Message{TerminalColors.RESET}"),
        (TerminalColors.warning, "WARNING", "This Is A Warning Message",
         TerminalColors.LIGHT_YELLOW + TerminalColors.ITALIC, True,
         f"{TerminalColors.LIGHT_YELLOW + TerminalColors.ITALIC}WARNING: This Is A Warning Message{TerminalColors.RESET}\n"),
        (TerminalColors.success, "SUCCESS", "This Is A Success Message",
         TerminalColors.LIGHT_GREEN + TerminalColors.BOLD, True,
         f"{TerminalColors.LIGHT_GREEN + TerminalColors.BOLD}SUCCESS: This Is A Success Message{TerminalColors.RESET}\n"),
        (TerminalColors.success, "SUCCESS", "This Is A Success Message",
         TerminalColors.LIGHT_GREEN + TerminalColors.BOLD, False,
         f"{TerminalColors.LIGHT_GREEN + TerminalColors.BOLD}SUCCESS: This Is A Success Message{TerminalColors.RESET}"),
        (TerminalColors.success, "SUCCESS", "This Is A Success Message",
         TerminalColors.LIGHT_GREEN + TerminalColors.ITALIC, True,
         f"{TerminalColors.LIGHT_GREEN + TerminalColors.ITALIC}SUCCESS: This Is A Success Message{TerminalColors.RESET}\n"),
        (TerminalColors.info, "INFO", "This Is An Info Message", TerminalColors.LIGHT_GRAY + TerminalColors.BOLD, True,
         f"{TerminalColors.LIGHT_GRAY + TerminalColors.BOLD}INFO: This Is An Info Message{TerminalColors.RESET}\n"),
        (TerminalColors.info, "INFO", "This Is An Info Message", TerminalColors.LIGHT_GRAY + TerminalColors.BOLD, False,
         f"{TerminalColors.LIGHT_GRAY + TerminalColors.BOLD}INFO: This Is An Info Message{TerminalColors.RESET}"),
        (TerminalColors.info, "INFO", "This Is An Info Message", TerminalColors.BLUE + TerminalColors.ITALIC, True,
         f"{TerminalColors.BLUE + TerminalColors.ITALIC}INFO: This Is An Info Message{TerminalColors.RESET}\n")
    ]
)
def test_terminal_colors(method, level, message, formatting, should_print, expected_output, capsys):
    if should_print:
        method(message, formatting=formatting, should_print=should_print)
        captured = capsys.readouterr()
        assert captured.out == expected_output
    else:
        formatted_message = method(message, formatting=formatting, should_print=should_print)
        assert formatted_message == expected_output
