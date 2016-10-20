###general website updating procedure###

1.  update local repo

2.  add pages/posts, make changes to theme, etc.

3.  run `pelican content` from the main repo directory

    +  to test changes, enter the output directory, run `python -m SimpleHTTPServer`, and go to "localhost:8000" in a browser
    
4.  to upload your changes to the website, the output directory

5.  you are now in a new git repo, so run `git commit` and `git push` as usual.

6.  now, `cd ..` to the main repo, and commit and push your changes here as well
        
7.  to publish, log into the website EC2 instance, navigate to /var/www/html (which is a clone of the output repo) and run `git pull`.

###for more extensive updates###

1.  create new branch in local main repo, and local output repo.

2.  switch to these branches, and do all the work there. merge when finished.