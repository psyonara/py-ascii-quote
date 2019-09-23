def split_into_lines(text, line_length):
    words = text.split(" ")
    lines = []

    current_line = ""
    for word in words:
        if len(word) > line_length:
            print(f"Word '{word}' was too long.")
            continue
        chars_left = line_length - len(current_line)
        if len(f"{word} ") > chars_left:
            lines.append(current_line.ljust(line_length))
            current_line = ""

        current_line += f"{word} "

    if current_line:
        lines.append(current_line.ljust(line_length))

    return lines


def generate_quote(quote, author, add_sh_echo=False):
    if len(author) > 25:
        return "Author name too long."

    quote_lines = split_into_lines(quote, 27)

    character_line = f"- {author} ".rjust(27)

    scroll_strings = []
    scroll_strings.append("")
    scroll_strings.append(" _________________________________")
    scroll_strings.append(" /  \                             \.")
    scroll_strings.append(f" |   | {quote_lines[0]}|.")
    if len(quote_lines) > 1:
        scroll_strings.append(f"  \__| {quote_lines[1]}|.")
    else:
        scroll_strings.append("  \__|                            |.")
    if len(quote_lines) > 2:
        for line in quote_lines[2:]:
            scroll_strings.append(f"     | {line}|.")
    scroll_strings.append(f"     | {character_line}|.")
    scroll_strings.append("     |   _________________________|___")
    scroll_strings.append("     |  /                            /.")
    scroll_strings.append("     \_/____________________________/.")
    scroll_strings.append("")

    for string in scroll_strings:
        if add_sh_echo is True:
            print(f"echo \"{string}\"")
        else:
            print(string)


if __name__ == "__main__":
    quote = input("Please enter your quote: ")
    author = input("Please enter the author of the quote: ")
    add_sh_echo = input("Add 'echo' for shell script? (y/n)")
    generate_quote(quote, author, add_sh_echo.lower() == "y")

