import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        print("Usage: ft_stream_management.py <file>")
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Accessing file '{args[0]}'")
        content = None
        try:
            f = open(args[0], "r")
            try:
                content = f.read()
                print("---")
                print("")
                print(content)
                print("---")
            except UnicodeDecodeError as e:
                print(f"[STDERR] Error reading file '{args[0]}': {e}",
                      file=sys.stderr)
            finally:
                f.close()
                print(f"File '{args[0]}' closed.")
        except OSError as e:
            print(f"[STDERR] Error opening file '{args[0]}': {e}",
                  file=sys.stderr)
        if content is not None:
            print("")
            transformed = content.replace('\n', '#\n')
            if transformed != '' and not transformed.endswith('\n'):
                transformed += '#'
            print("Transform data:")
            print("---")
            print("")
            print(transformed)
            print("---")
            sys.stdout.write("Enter new file name (or empty): ")
            sys.stdout.flush()
            line = sys.stdin.readline()
            if line and line[-1] == '\n':
                line = line[:-1]
            if line:
                print(f"Saving data to '{line}'")
                try:
                    with open(line, "w") as new_file:
                        new_file.write(transformed)
                    print(f"Data saved in file '{line}'.")
                except OSError as e:
                    print(f"[STDERR] Error opening file '{line}': {e}",
                          file=sys.stderr)
                    print("Data not saved.")
            else:
                print("Not saving data.")
