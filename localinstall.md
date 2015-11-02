# how to run and test [internationalopenmagazine](http://internationalopenmagazine.org) locally

why to do that:
  * test out the look and feel of your own articles and pages
  * to learn about [pelican](http://docs.getpelican.com/en/3.6.3/index.html), [python](http://python.org), [static website generators](https://wiki.python.org/moin/StaticSiteGenerator)
  * improve the used pelican themes and plugins
  * play-around with your own design ideas
  * help to solve some [issues](https://github.com/horstjens/internationalopenmagazine/issues)
  * get involved into the project 
  * because [@chbw (Christoph B. Wurzinger)](https://github.com/chbw) said so in [#Issue 7](https://github.com/horstjens/internationalopenmagazine/issues/7)
  
## setup for ubuntu mate linux

### preparation 

  * make sure you have an account at http://github.com with verified email address
    * learn about git/github by reading https://help.github.com/articles/fork-a-repo/
  * open nautilus file manager and press F3 to get a two-panel view
  * navigate to the location where you want to have a copy of the project. for me, this was the (already existing) folder `code` inside `home`
  * open terminal with CTRL+ALT+T or with right-click menu inside nautilus 
  * make sure git is installed: `sudo apt-get install git`
  * make sure python is installed: `sudo apt-get install python` (python is pre-installed on ubuntu and most linux distros)
  * make sure terminal shows the content of your `code` folder. if not, run

   cd ~/code
   ls

  * fork the internationalopenmagazine project from github, as described in https://help.github.com/articles/fork-a-repo/ : 
  * navigate to the https://github.com/horstjens/internationalopenmagazine and click on the big **fork** button in the topright corner
  * you have now your own fork on github. copy it to your harddrive:
  * In the right sidebar of your fork's repository page, click the **HTTPS Clone URL** Icon  to copy the clone URL for *your* fork into the clipboard
  * in your terminal, type `git clone` and insert the URL from the clipboard (clicking the mouse middle button). 

    git clone https://github.com/YOUR-GIHUB-USERNAME/internationalopenmagazine
    
  * You now have an new folder `internationalopenmagazine` inside your code folder. change into this folder:
  
    cd internationalopenmagazine
    ls
    
  * all files from github are now on your local harddisk. 

## sync local folder with official repo

  * inside your project folder (`internationalopenmagazine`) type:
     git remote -v
  * you see only two entries, *origin*. type:   
     git remote add upstream https://github.com/horstjens/internationalopenmagazine.git
     git remote -v 
  * you should see now four entries, two *origin* and two *upstream*
  * to learn how to write pull requests and about branches, read:  https://help.github.com/articles/syncing-a-fork
  
## installing pelican and pelican themes

  * make sure you are inside the `internationalopenmagazine` folder
  * install pelican as described here: http://docs.getpelican.com/en/3.6.3/index.html
    * i always use this method:
    
    sudo pip install -e "git+https://github.com/getpelican/pelican.git#egg=pelican"
    sudo pip install Markdown
    sudo pip install typogrify
    
  * check out the installed themes
  
    pelican-themes -l
    
  * (re)install the twitchymagazine theme from folder `mythemes/twitchymagazine` (and make sure any old version of theme is deinstalled first):
  
    sudo pelican-themes -r twitchymagazine
    sudo pelican-themes -i /mythemes/twitchymagazine
    
  * generate the content
  
    pelican content
    
  * done! you can now either manually inspect the files inside the `output` folder or create a local server to view with your browser (recommended):

## start local server

  * open a second (!) Terminal window (CTRL + ALT + T) in your folder `internationlopenmagazine`
  * navigate into the output folder and start local server:
    
    cd output
    python -m pelican.server
    
  * open a browser and surf to: http://localhost:8000/
  * to stop the server, go to the terminal window where you started the browser and press CTRL+C
  
## modify content

  * make changings into the files inside the `content` folder
  * if necessary, adapt the file `pelicanconf.py` inside the project root folder `internationlopenmagazine` 
    * at the moment (31-oct-2015) i run 'python3 horsttagcounter.py' and manually copy the output into pelicanconf.py to get the tags counted correctly
  * if you make changes on the theme, you master either de-install and re-install the theme as described above or:
  * generate a new version using:
  
    pelican content -t mythemes/twitchymagazine/ 
    
  * using the command above, you can try out pelican with other temes without need to globally install them first. (just put them into the mytheme folder).
  * generally repeat those steps:
    * make edits inside the `content` folder or inside `mythemes/twitchymagazine` or in `pelicanconfig.py`
    * save all files and run the local server
    * inspect the results in your browser at http://localhost:8000/
    
## make pull requests

   * if you changed a single file only, you can try to edit it inside the github webpage and hit the green "send pull request" button
   * if you changed several files, read https://help.github.com/articles/using-pull-requests/
   
    
  
      
    
 

