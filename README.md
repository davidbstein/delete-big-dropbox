# Delete a big Dropbox Folder

Sometime you create an enourmous Dropbox folder and get in a bad state.
 - you can't sync it because it's too big. 
 - you can't delete it on the website because there are too many files.

This little script will fix that issue.


## Setup

You'll need an API key - you can get it [here](https://dropbox.github.io/dropbox-api-v2-explorer/#files_delete_v2) (click the `get token` button)


## Run Script

__THIS WILL DELETE EVERYTHING IN THAT FOLDER AND IS NOT UNDOABLE__
(well, it's kind undoable but you'll probably need to email drobox support so it'll take several days)

run the script by running the following two commands and then following the instructions.

```
    pip install dropbox
    python delete_folder.py /path/to/folder
```

