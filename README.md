# delete-big-dropbox

Sometimes you can't sync a folder because it's too big. Sometimes you can't delete on the website because there are too many files.

You'll need an API key - you can get it [here](https://dropbox.github.io/dropbox-api-v2-explorer/#files_delete_v2) (click the `get token` button)

run the script by running

```
    pip install dropbox
    python delete_folder.py /path/to/folder
```

__THIS WILL DELETE EVERYTHING IN THAT FOLDER AND IS NOT UNDOABLE__
