import os
import mimetypes
import pyperclip
import argparse
from datetime import datetime
import shutil
import colorama
from colorama import Fore, Style, Back

SKIP_FOLDERS = [
    'node_modules',
    'venv',
    '.venv',
    'env',
    '.env',
    'pycache',
    'dist',
    'build',
    '.git',
    '.idea',
    '.vscode',
    'vendor',
    'bower_components',
    'jspm_packages',
    'packages'
]

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB
CHUNK_SIZE = 1 * 1024 * 1024  # 1 MB

def is_text_file(file_path):
    mime_type, _ = mimetypes.guess_type(file_path)
    return mime_type and mime_type.startswith('text')

def get_file_content(file_path, output_dir, relative_path, single_file=False):
    file_size = os.path.getsize(file_path)
    if file_size > MAX_FILE_SIZE and not single_file:
        return handle_large_file(file_path, output_dir, relative_path)
    elif is_text_file(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    else:
        return f"[{os.path.splitext(file_path)[1]} file]"

def handle_large_file(file_path, output_dir, relative_path):
    file_name = os.path.basename(file_path)
    parts_dir = os.path.join(output_dir, f"{file_name}_parts")
    os.makedirs(parts_dir, exist_ok=True)
    part_num = 1
    with open(file_path, 'rb') as f:
        while True:
            chunk = f.read(CHUNK_SIZE)
            if not chunk:
                break
            part_file = os.path.join(parts_dir, f"{file_name}.part{part_num}")
            with open(part_file, 'wb') as part:
                part.write(chunk)
            part_num += 1

    return f"[Large file split into {part_num - 1} parts. See {os.path.relpath(parts_dir, output_dir)}]"

def generate_md_content(path, output_dir, indent='', tree_only=False, relative_path='', single_file=False):
    content = []
    for item in sorted(os.listdir(path)):
        if item in SKIP_FOLDERS:
            content.append(f"{indent}- {item}/ (skipped dependency folder)")
            continue
        item_path = os.path.join(path, item)
        item_relative_path = os.path.join(relative_path, item)
        if os.path.isdir(item_path):
            content.append(f"{indent}- {item}/")
            content.extend(generate_md_content(item_path, output_dir, indent + '  ', tree_only, item_relative_path, single_file))
        else:
            content.append(f"{indent}- {item}")
            if not tree_only:
                content.append(f"{indent}  {get_file_content(item_path, output_dir, item_relative_path, single_file)}")
                content.append(f"{indent}  ")
    return content

def list_directory(path):
    print(f"\n{Fore.CYAN}Contents of {Fore.YELLOW}{path}{Fore.RESET}:")
    for item in sorted(os.listdir(path)):
        if os.path.isdir(os.path.join(path, item)):
            print(f"  {Fore.BLUE}📁 {item}/{Fore.RESET}")
        else:
            print(f"  {Fore.GREEN}📄 {item}{Fore.RESET}")
    print()

def print_styled_header(text):
    print(f"\n{Back.CYAN}{Fore.BLACK}{text:^50}{Style.RESET_ALL}")

def print_styled_section(title, content):
    print(f"\n{Fore.CYAN}{title}:")
    for line in content:
        print(f"   {line}")

def make_clickable(path):
    return f"\033]8;;file://{path}\033\\{path}\033]8;;\033\\"

def purge_data():
    home_dir = os.path.expanduser("~")
    home_packitup_dir = os.path.join(home_dir, '.packitup')
    
    if os.path.exists(home_packitup_dir):
        try:
            shutil.rmtree(home_packitup_dir)
            print(f"{Fore.GREEN}✅ Successfully purged all PackItUp data from {home_packitup_dir}")
        except Exception as e:
            print(f"{Fore.RED}❌ Error while purging data: {e}")
    else:
        print(f"{Fore.YELLOW}⚠️ No PackItUp data found to purge.")

    # Also remove any local output directories in the current working directory
    cwd = os.getcwd()
    for item in os.listdir(cwd):
        if os.path.isdir(item) and item.endswith('_structure_'):
            try:
                shutil.rmtree(item)
                print(f"{Fore.GREEN}✅ Removed local output directory: {item}")
            except Exception as e:
                print(f"{Fore.RED}❌ Error while removing {item}: {e}")

def main():
    colorama.init(autoreset=True)  # Initialize colorama with autoreset
    parser = argparse.ArgumentParser(description="Generate project structure and contents as Markdown.")
    parser.add_argument('path', nargs='?', default='.', help="Path to pack (default: current directory)")
    parser.add_argument('-t', '--tree', action='store_true', help="Generate file tree only (no file contents)")
    parser.add_argument('-l', '--list', action='store_true', help="List files and directories in the specified directory")
    parser.add_argument('-s', '--singlefile', action='store_true', help="Ignore file splitting and return as a single file")
    parser.add_argument('-p', '--purge', action='store_true', help="Purge all saved PackItUp data")
    args = parser.parse_args()

    if args.purge:
        purge_data()
        return

    root_dir = os.path.abspath(args.path)

    if args.list:
        list_directory(root_dir)
        return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    root_folder_name = os.path.basename(root_dir)

    # Generate unique filenames and directories
    output_dir = f"{root_folder_name}_structure_{timestamp}"
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f"{root_folder_name}_structure_{timestamp}.md")

    home_dir = os.path.expanduser("~")
    home_packitup_dir = os.path.join(home_dir, '.packitup')
    os.makedirs(home_packitup_dir, exist_ok=True)
    home_output_dir = os.path.join(home_packitup_dir, f"{root_folder_name}_piu_readable_{timestamp}")
    os.makedirs(home_output_dir, exist_ok=True)
    home_output_file = os.path.join(home_output_dir, f"{root_folder_name}_piu_readable_{timestamp}.md")

    content = ["# Project Structure", ""]
    content.extend(generate_md_content(root_dir, output_dir, tree_only=args.tree, single_file=args.singlefile))

    markdown_content = '\n'.join(content)

    # Save to file in output directory
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(markdown_content)

    # Save to file in user's home directory
    with open(home_output_file, 'w', encoding='utf-8') as f:
        f.write(markdown_content)

    if not args.singlefile:
        # Copy large file parts to home directory
        for root, dirs, files in os.walk(output_dir):
            for dir in dirs:
                if dir.endswith('_parts'):
                    src_dir = os.path.join(root, dir)
                    dst_dir = os.path.join(home_output_dir, os.path.relpath(src_dir, output_dir))
                    shutil.copytree(src_dir, dst_dir)

    # Copy to clipboard
    pyperclip.copy(markdown_content)

    # Stylized output
    print_styled_header("PackItUp Completed Successfully!")

    print_styled_section("📁 Output Locations", [
        f"📌 Local: {Fore.YELLOW}{make_clickable(os.path.abspath(output_dir))}",
        f"📌 Home:  {Fore.YELLOW}{make_clickable(home_output_dir)}"
    ])

    print_styled_section("📄 Main Files", [
        f"📌 Local: {Fore.YELLOW}{make_clickable(os.path.abspath(output_file))}",
        f"📌 Home:  {Fore.YELLOW}{make_clickable(home_output_file)}"
    ])

    print_styled_section("ℹ️  Info", [
        f"📋 Markdown content has been copied to clipboard.",
        f"📂 Large files have been split and saved in parts if necessary.",
        f"🗂️  Skipped folders: {', '.join(SKIP_FOLDERS)}"
    ])

if __name__ == "__main__":
    main()
