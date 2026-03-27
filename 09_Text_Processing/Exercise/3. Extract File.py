def solve():
    path = input()
    parts = path.replace("\\", "/").split("/")
    full_name = parts[-1]
    if "." in full_name:
        last_dot_index = full_name.rfind(".")
        file_name = full_name[:last_dot_index]
        extension = full_name[last_dot_index + 1:]
    else:
        file_name = full_name
        extension = ""

    print(f"File name: {file_name}")
    print(f"File extension: {extension}")

if __name__ == "__main__":
    solve()
