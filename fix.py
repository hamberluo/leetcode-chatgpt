import os
import re


def find_files(root_dir):
    for dir_path, dir_names, file_names in os.walk(root_dir):
        for filename in file_names:
            name_without_ext, ext = os.path.splitext(filename)
            if ext == '.md' and name_without_ext.isdigit():
                new_filename = name_without_ext.zfill(4) + ext
                os.rename(os.path.join(dir_path, filename), os.path.join(dir_path, new_filename))


def find_incomplete_files(root_dir):
    for dir_path, dir_names, file_names in os.walk(root_dir):
        for filename in file_names:
            name_without_ext, ext = os.path.splitext(filename)
            if ext == '.md' and name_without_ext.isdigit():
                file_path = os.path.join(dir_path, filename)
                with open(file_path, 'r') as f:
                    content = f.read()
                    if '```' not in content or '算法复杂度' not in content or '$' in content:
                        print(os.path.join(dir_path, filename))


def find_code_block(root_dir):
    for file_name in os.listdir(root_dir):
        if os.path.isdir(os.path.join(root_dir, file_name)):
            lang = file_name
            dir_path = os.path.join(root_dir, file_name)
            for filename in os.listdir(dir_path):
                fix_code_block(lang, os.path.join(dir_path, filename))
        else:
            lang = os.path.basename(root_dir)
            fix_code_block(lang, os.path.join(root_dir, file_name))


def fix_code_block(lang, file_path):
    name_without_ext, ext = os.path.splitext(os.path.basename(file_path))
    if ext != '.md' or not name_without_ext.isdigit():
        return

    with open(file_path, 'r') as fr:
        content = fr.read()

        pattern = r'```\n([\s\S]+?)\n```'
        matches = re.findall(pattern, content)

        for match in matches:
            code = match
            new_code_block = f'```{lang}\n{code}\n```'
            content = content.replace(f'```\n{code}\n```', new_code_block)

        if matches:
            with open(file_path, 'w') as fw:
                fw.write(content)
                print(f'Fix {file_path}')


if __name__ == '__main__':
    find_code_block('.')
    find_incomplete_files('.')
