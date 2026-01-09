import argparse
import os


def get_arguments():
    parser = argparse.ArgumentParser(description="File Organizer CLI")

    parser.add_argument(
        "--path",
        type=str,
        required=True,
        help="Path of the folder to organize"
    )

    return parser.parse_args()


def main():
    args = get_arguments()
    folder_path = args.path

    if not os.path.exists(folder_path):
        print("Error: Path does not exist")
        return

    if not os.path.isdir(folder_path):
        print("Error: Path is not a directory")
        return

    files = os.listdir(folder_path)

    if not files:
        print("Folder is empty")
        return

    print("Scanning folder:", folder_path)

    for file_name in files:
        full_path = os.path.join(folder_path, file_name)

        if os.path.isfile(full_path):
            print("File:", file_name)


if __name__ == "__main__":
    main()

