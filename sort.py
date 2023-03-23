import os


def find_files(root_dir):
    for dir_path, dir_names, file_names in os.walk(root_dir):
        for filename in file_names:
            name_without_ext, ext = os.path.splitext(filename)
            if ext == '.md' and name_without_ext.isdigit():
                new_filename = name_without_ext.zfill(4) + ext
                os.rename(os.path.join(dir_path, filename), os.path.join(dir_path, new_filename))


if __name__ == '__main__':
    find_files('.')
