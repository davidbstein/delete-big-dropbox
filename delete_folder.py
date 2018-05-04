import dropbox

USAGE = """
delete_folder

usage:
    python delete_folder.py <folder path> [<API key>]
"""

def delete_folder(path, dbx):
    print("deleting {}".format(path))
    try:
        dbx.files_delete_v2(path)
    except dropbox.exceptions.ApiError as e:
        if type(e.error) is dropbox.files.DeleteError:
            print("too many files! Moving down a level from {}".format(path))
            content = dbx.files_list_folder(path)
            print("found {} files in {}".format(len(content.entries), path))
            for file in content.entries:
                delete_folder(file.path_lower, dbx)
        else:
            raise(e)

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        dbx = dropbox.Dropbox(input("input your API key: "))
        delete_folder(sys.argv[1], dbx)
    elif len(sys.argv) == 1:
        delete_folder(sys.argv[1], sys.argv[2])
    else:
        print(USAGE)
