###general website updating procedure###

1.  update local repo

2.  add pages/posts, make changes to theme, etc.

3.  run `pelican content` from the main repo directory

    +  to test changes, enter the output directory, run `python -m SimpleHTTPServer`, and go to "localhost:8000" in a browser
    
4.  to upload your changes to the website, first make sure you are in the output directory

5.  then run the s3cmd sync command. make sure to use one of the following commands:

    +  if you have only added content (not removed any files), you can use
    
            s3cmd.py sync ./ s3://legiongis.com --acl-public
    
    +  but if you have removed files in the local repo, and want them to also be removed from the bucket, you must use
    
            s3cmd.py sync ./ s3://legiongis.com --acl-public --delete-removed --exclude "downloads/*" --exclude "safe/*"

        the `--delete-removed` flag will remove files from the bucket that are not in the local directory, but _both_ of the `--exclude` flags are **crucial**, because we have zip files, html files, pdf slideshows, etc. in the bucket (in the "downloads" and "safe" folders) which would be deleted from the bucket without the explicit `--exclude` flags.