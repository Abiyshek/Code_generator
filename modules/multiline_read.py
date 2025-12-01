def read_multiline_input():
    print("Paste your code now. Press ENTER on an empty line to finish.")
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)
    return "\n".join(lines)


