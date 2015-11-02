# project site: http://internationalopenmagazine.org

This [Github Repo](https://github.com/horstjens/internationalopenmagazine) has all the source files, articles, necessary scripts and themes to make a local copy of The [internationl open magazine](http://internationalopenmagazine.org)

The reason for this Github repository is to allow readers to modify, fork, write and submit articles for the [international open magazine](http://internationalopenmagazine.org)



## commiting articles

please do the following, either via git commands or via this webinterface:

  * (fork the repo locally) or use the github web interface
  * create a new file inside the `content/blog` folder and name it `YYYY-MM-DD-cool_name_for-article.md`
    * write your article inside this file. See [template.md](template.md). Use the [Markdown](https://guides.github.com/features/mastering-markdown/) Syntax. You can use `html` directly inside Markdown.
  * _**only** if necessary_: put additional material like images, audio files, pdf's etc. inside an new subfolder of `images`
    * create a folder with the same name as your file, but without the `.md` inside the images folder: `YYYY-MM-DD-cool_name_for-article`
    * put all extra materials into this folder
    * from within your `.md` file, reference to the extra material via `[myimage](images/YYYY-MM-DD-cool_name_for-article/myimage.jpg)`
  * send an pull request



## detailed instruction of how to setup local fork
  * see [localinstall.md](localinstall.md)
