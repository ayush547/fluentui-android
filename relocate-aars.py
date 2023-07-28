import os
import shutil

# This is a util function that moves all the output .aar into a new directory called aar_files.
# To be used for testing purposes only.


def group_aars(directory, extension):
    # Make output directory if it doesn't exist. (not tracked by git)
    dst_directory = os.path.join(directory, 'aar_files')
    if not os.path.exists(dst_directory):
        os.makedirs(dst_directory)

    for root, dirs, files in os.walk(directory):
        for file in files:
            # out.aar is an intermediate file and not required.
            if file.endswith(extension) and file != 'out.aar':
                src_path = os.path.join(root, file)
                dst_path = os.path.join(directory, 'aar_files', file)
                shutil.move(src_path, dst_path)
                # Debug print statement -
                # print('Moved {} to {}'.format(src_path, dst_path))
                print('implementation files (\'{}\')'
                      .format(os.path.abspath(dst_path)).replace('\\', '/'))


group_aars('.', 'aar')
