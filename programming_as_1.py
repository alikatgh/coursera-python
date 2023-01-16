def read_file(file_name):
    try:
        with open(file_name) as f:
            contents = f.read()
            print(contents)
            return contents
    except:
        raise NotImplementedError()


def read_file_into_list(file_name):
    try:
        with open(file_name) as f:
            return f.readlines()
    except:
        raise NotImplementedError()


def write_first_line_to_file(file_contents, output_filename):
    try:
        first_line = file_contents.split('\n')[0]
        with open(output_filename, 'w') as f:
            f.write(first_line)
        return
    except:
        raise NotImplementedError()


def read_even_numbered_lines(file_name):
    try:
        with open(file_name, 'r') as f:
            lines_list = f.readlines()
            even_lines = []
            for idx, line in enumerate(lines_list):
                if (idx + 1) % 2 == 0:
                    even_lines.append(line)
            return even_lines
    except:
        raise NotImplementedError()


def read_file_in_reverse(file_name):
    try:
        with open(file_name) as f:
            return f.readlines()[::-1]
    except:
        raise NotImplementedError()


def main():
    file_contents = read_file("sampletext.txt")
    print(read_file_into_list("sampletext.txt"))
    write_first_line_to_file(file_contents, "online.txt")
    print(read_even_numbered_lines("sampletext.txt"))
    print(read_file_in_reverse("sampletext.txt"))


if __name__ == "__main__":
    main()
