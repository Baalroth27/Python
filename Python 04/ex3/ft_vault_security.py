def secure_archive(
        filename: str,
        action: str = 'r',
        content: str | None = None,
        ) -> tuple[bool, str]:
    if action == 'r':
        try:
            with open(filename, "r") as f:
                return (True, f.read())
        except (OSError, UnicodeDecodeError) as e:
            return (False, str(e))
    elif action == 'w':
        if content is None:
            return (False, 'No content to write has been provided.')
        try:
            with open(filename, "w") as f:
                f.write(content)
                return (True, 'Content successfully written to file')
        except OSError as e:
            return (False, str(e))
    else:
        return (False, f"Invalid action '{action}'")


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")
    print('')
    print("Using 'secure_archive' to read from nonexistent file:")
    print(f"{secure_archive('/not/existing/file')}")
    print('')
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(f"{secure_archive('/etc/master.passwd')}")
    print('')
    print("Using 'secure_archive' to read from a regular file:")
    result = secure_archive('ancient.fragment.txt')
    new_content = result[1]
    print(f"{result}")
    print('')
    print("Using 'secure_archive' to write previous content to a new file:")
    print(f"{secure_archive('new_file', 'w', new_content)}")
