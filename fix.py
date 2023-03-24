import os


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
                with open(os.path.join(dir_path, filename), 'r') as f:
                    content = f.read()
                    if '```' not in content or '算法复杂度' not in content or '$' in content:
                        print(os.path.join(dir_path, filename))


if __name__ == '__main__':
    find_incomplete_files('.')
