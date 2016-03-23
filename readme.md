###general website updating procedure###

1.  update local repo

2.  add pages/posts, make changes to theme, etc.

3.  run `pelican content` from the main repo directory

    +  to test changes, enter the output directory, run `python -m SimpleHTTPServer`, and go to "localhost:8000" in a browser
    
4.  to upload your changes to the website, first make sure you are in the output directory

5.  then run the s3cmd sync command. make sure to use the following:

        s3cmd.py sync ./ s3://legiongis.com --acl-public
    
    _**OR**_
    
        s3cmd.py sync ./ s3://legiongis.com --acl-public --delete-removed --exclude "downloads/*" --exclude "safe/*"

    Use the first if you have only added new content to the website, and the second if you have removed any files (such as an image, or a post/post). The `--delete-removed` flag will remove files from the bucket that are not in the local directory, and both of the `--exclude` flags are **crucial**, because we have zip files, html files, pdf slideshows, etc. which sit in the "downloads" and "safe" directories on the bucket (because they do not need to exist within this repo or the "output" directory) and would be deleted from the bucket without the `--exclude` flags.