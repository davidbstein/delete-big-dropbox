import dropbox


def delete_folder(path, dbx=dbx):
    print("deleting {}".format(path))
    try:
        dbx.files_delete_v2(path)
    except dropbox.exceptions.ApiError as e:
        if type(e.error) is dropbox.files.DeleteError:
            print("too many files! Moving down a level.")
            content = dbx.files_list_folder(path)
            for file in content.entries:
                delete_folder(file.path_lower)
        else:
            raise(e)


if __name__ == '__main__':
    import sys
    dbx = dropbox.Dropbox(rawinput("input your API key: "))
    delete_folder(sys.argv[1], dbx)
