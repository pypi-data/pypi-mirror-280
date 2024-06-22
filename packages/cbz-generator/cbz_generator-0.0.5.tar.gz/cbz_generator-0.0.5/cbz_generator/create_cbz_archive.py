import os
import zipfile


def create_cbz_archive(directory_to_archive, output_directory, filename):
    """
    Exports a single directory of images into a CBZ archive with a given filename.

    :param directory_to_archive: full path to the directory containing the images to be archived.
    :param output_directory: full path to the directory to output the CBZ archive to.
    :param filename: File name for the archive. Note: .CBZ will be added at the end and is not required to add manually.
    :return:
    """
    if not os.path.exists(directory_to_archive):
        raise FileNotFoundError(directory_to_archive)

    if not os.path.exists(output_directory):
        raise FileNotFoundError(output_directory)

    # if the file name has any extension other than cbz replace with cbz
    if not filename.endswith('.cbz'):
        filename = filename.split('.')[0] + '.cbz'

    # change to the directory to archive
    os.chdir(directory_to_archive)

    # create a zip file
    with zipfile.ZipFile(os.path.join(output_directory, filename), 'w') as zipf:
        for file in os.listdir():
            if os.path.isfile(file):
                zipf.write(file)


def create_bulk_cbz(directory_of_directories, output_directory):
    """
    Method to allow for bulk processing of many directories into .CBZ archives. File name of the resulting .CBZ archive
    depends on the name of the subdirectory containing the images

    :param directory_of_directories: full path to directory containing subdirectories of images to pack into .CBZ archive.
    :param output_directory: full path to output directory for each subdirectory of images.
    :return: exports CBZ archives into output directory.
    """

    if not os.path.exists(directory_of_directories):
        raise FileNotFoundError(directory_of_directories)

    if not os.path.exists(output_directory):
        raise FileNotFoundError(output_directory)

    for directory in [f.path for f in os.scandir(directory_of_directories) if f.is_dir()]:
        if os.path.basename(directory):
            dir_name = os.path.basename(directory)
            create_cbz_archive(directory, output_directory, dir_name + '.cbz')
