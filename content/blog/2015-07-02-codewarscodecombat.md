Title: learn to code with codewars.com and codecombat.com
Date: 2015-07-02 11:30
Tags: coding, teaching, review
Slug: 2015-07-02-codewarscodecombat
Authors: JENS Horst 
Summary: <div style="float: left; padding:5px"><img src="http://spielend-programmieren.at/blog/images/20150702_codecombat.png" width="100" alt="logo"></div>A quick look into two interesting, open-source aware websites to learn and train coding skills: codecombat.com and codewars.com<div style="clear:both;"></div>

# learn to code
<small><a href="http://goo.gl/4lnyTe">This article</a> was first published on the "<a href="http://spielend-programmieren.at/blog">open everything" blog</a> of Horst JENS. Shortlink: http://goo.gl/4lnyTe</small>

I recently  [stumbled](https://www.reddit.com/r/Python/comments/3bgjud/you_sit_down_with_your_machine_and_a_person_who/csmd4yz) upon two different websites offering the possibility to learn and train coding skills:

 * [CodeCombat](http://codecombat.com)
 * [CodeWars](http://codewars.com)
 
 
Both websites use a free software philosophy (all code examples [free licensed](http://www.gnu.org/licenses/license-list.en.html) or on [github](https://github.com/codecombat)) and offer to train different computer programming languages. I tested both systems with the programming language [Python](http://python.org) and some of my [students](http://spielend-programmieren.at): 

# CodeCombat

<div align="center">
<dl style="background-color: #dddddd;">
<br>
<dt>
<a href="http://codecombat.com"><img border="0" src="http://spielend-programmieren.at/blog/images/20150702_codecombat.png" width="800"></a>
</dt>
<dd>Artwork of the <a href="http://codecombat.com">CodeCombat</a> start page</dd>
</dl>
</div>

CodeCombat focus on [gameification](https://en.wikipedia.org/wiki/Gamification) and is suitable for a younger audience. If you like RPG games with cartoon fantasy graphics, you will like it. The concept of code combat build up from older learn-to-code systems such as [Rurple](https://en.wikipedia.org/wiki/RUR-PLE), [Karel](https://en.wikipedia.org/wiki/Karel_(programming_language)) and other programming enviroments. The screen is splitted into a coding editor (right half) and a labyrinth or level on the left half. Placed inside the labyrinth is a (beautiful painted) avatar, to be controlled by the player using a restricted set of commands, like `self.moveDown()`, `self.moveRight()`, `self.attack(self.findNearestEnemy())` etc. Those commands have to be typed correctly in the code editor to control the avatar. Incorrect programs with logical faults (like commanding the avatar to run against a wall) will let the avatar loose hitpoints and die, like in a computer game. 
 
The student/player has in each level a task to complete, usually to collect gems with the avatar, defeat monsters and move to the exit of a level. Gradually, the player is introduced into new commands, like loops, conditionals and variables. Diamonds collected in a level can be invested between levels in better armor, weapons and programming commands (cleverly symbolized as spellbooks and magic devices) to master the increasingly more tricky tasks in the higher levels.


<div align="center">
<dl style="background-color: #dddddd;">
<br>
<dt>
<a href="https://en.wikipedia.org/wiki/RUR-PLE#/media/File:RUR-PLE-Python_Learning_Environment.png"><img border="0" src="http://spielend-programmieren.at/blog/images/20150702_rurple.png" width="800"></a>
</dt>
<dd><a href="http://rur-ple.sourceforge.net/">Rurple</a>, one of many code-learing enviroments</dd>
</dl>
</div>

Code Combat begins with a slow learning curve, suitable for children who never had coding experience before. As the player makes progress and solves more and more levels, the tasks involve more complex programming concepts. Most important, the levels itself become more complex due to more possible interaction with the objects in the game world: fences can be buid, fire traps can be set, enemys can be lured into minefields, special weapons allow special attacks with a cooldown timer etc. 

Not only are the levels designed beautifully, the riddles in the higher levels of Code Combat are complex enough to fascinate gamers as well as coders.

## licenses

The code of CodeCombat itself can be found on github under the free [MIT license](https://en.wikipedia.org/wiki/MIT_License). All the art assets (sprites, backgrounds, sound effects etc.) can also be found on github and are published under a [creative commons CC-By 4.0](https://creativecommons.org/licenses/by/4.0/) license. This allows easy use of the game artwork for projects of students.

## business model

On the [code combat legal page](http://codecombat.com/legal) the licenses and attributing are explained in more detail. CodeCombat reserve the right to publish levels for code combat created and uploaded with the code-combat level editor under a non-free license.

The business model (as it is visible now) consist of "nudging" parents and teachers into a 9.99$/month subscription to gain access to video tutorials, more levels and more (virtual) diamonds. 

While the in-build advertising/nudging to subscribe may be slightly irritating for some players, it is a legal way to build an business ecosystem around an free/libre/open source core. 

As the complete Codecombat source code is on Github, [forkers](https://en.wikipedia.org/wiki/Fork_(software_development)) should be able to create their own code-combat system with a different (or no) business models attached to it.

## user participation

CodeCombat seeks the participation of users for level-design, coding, translation and other task. I look especially forward into community-created content of teachers and educators, like lesson plans or best-practice guidebooks of how to integrate codecombat sessions into computer science courses.

<div align="center">
<dl style="background-color: #dddddd;">
<br>
<dt>
<a href="http://codecombat.com/contribute"><img border="0" src="http://spielend-programmieren.at/blog/images/20150702_codecombatcontribute.png" width="800"></a>
</dt>
<dd>Participating is possible in many ways at <a href="http://codecombat.com/contribute">CodeCombat</a></dd>
</dl>
</div>


## teaching experience 

My own experience of using CodeCombat for students in my [programming courses](http://spielend-programmieren.at) was pleasant:

Testing with german-speaking, 11-year old students with little english skill, CodeCombat was a crowd-pleaser and often attracted older students willing "to help" and, more so, "to look" at the nice animated combat scenes. Students were able to figure out most of the tasks for themselves with little or no assistance from a teacher, at least for the first levels.

Depending on the level, a student is sometimes not allowed to edit existing code, sometime he must edit existing code, and sometimes the task description is hidden in the code comments. On higher levels (second game world) better english skills are necessary and teacher assistance is more often required. 

The gameification works very well, especially younger students loved to spend much time pondering how to invest hard-earned virtual diamonds best into virtual goods, and were very pleased to be able to buy superior virtual armor and weapons.

## critique 
I do not have much to critisize:

 * [Pythonic](http://docs.python-guide.org/en/latest/writing/style/) non-python: CodeCombat students learn a lot of commands making only sense inside the CodeCombat world. While this is fine for the game world, some "structural" commands like `loop:` also exist only inside CodeCombat and not in the (selected) programming language python. I wonder why not instead the correct python command (`while True:`) was used.

 * [Forced Object orientation](https://en.wikipedia.org/wiki/Object-oriented_programming): CodeCombat introduce commands like `self.moveDown()` instead `moveDown()` at the beginning, indicating that the avatar is an instance of an avatar class. While i like the concept of "do it right from the start, explain it later" i wonder if it is really necessary to force object-oriented concepts into students right from the start, when the necessary teaching (loops, conditionals, variables) could be as well teached without object-orientation paradigma. I guess it makes sense this way to enable CodeCombat the use of different programing languages, like Java. 

<hr>

# CodeWars

[CodeWars](http://codewars.com) is a more serious, less child-appealing website than CodeCombat and aims at a older, more experienced audience. A student is not guided throug lessons, but instead confronted with programming tasks, not unlike the homework assignements of a typical computer science class:

## Kata

Each programming task, in reference to japanese martial art called [kata](https://en.wikipedia.org/wiki/Kata), includes a short task description, a set of input data and the desired output data. The student is tasked to write a function in his preferred programming language to transform the given input into the desired outuput. This is all done with the online, in-build programming editor. 

The student is also tasked with [writing his own tests](https://en.wikipedia.org/wiki/Test-driven_development) and the outcome of the tests (passed or failed) gives clues if the code is ready to submit to the public. 

To make the katas more difficult (and realistic?) the given set of input-output data in the task descriptoin is only a subset of the data used to test a kata before submitting it to the public. 

The user can run his function against his own test with a button or can press "submit" to test his function against the bigger, hidden dataset. Only if all tests are passed can the function be uploaded to and inspected by the public.

This is a very revealing moment: even for a seemingly simple and straith-forward problem exist countless different solutions. Solutions can be upvoted as "best practice" so that the swarm intelligence of all coders sort the most acceptable solution to the top. It is also possible to vote a solution as "clever".

Included is an in-build web forum were solutions of a kata can be discussed.

There is not much gameification in Codewars, but solving katas will slowly raise the rank of a student, as do other activities, such as submitting your own katas.

<div align="center">
<dl style="background-color: #dddddd;">
<br>
<dt>
<a href="http://www.codewars.com/kata/simple-pig-latin/python"><img border="0" src="http://spielend-programmieren.at/blog/images/20150702_codewars.png" width="800"></a>
</dt>
<dd>From the pythonic verbose to the perl-like on-liner: There exist many different solutions for a <a href="http://www.codewars.com/kata/simple-pig-latin/python">pig latin kata</a></dd>
</dl>
</div>


## Kumite

A step up from katas are [kumites](https://en.wikipedia.org/wiki/Kumite), more complex coding problems were other coders are invited to refactor code and provide solutions.

## teaching experience

While i personally like CodeWars a lot, i found it less ideal suited for teaching python (tested with 14-year old students, german-speakers, some python practice, average knowledge of english). In contrast to CodeCombat, the teaching must happen before CodeWars is used, or a student must have the skill and self-discipline to learn necessary coding skills by other ways and test those skills using CodeWars. 

The biggest problem were understanding the task description and understanding how to use write tests. Simply put, most tests use the assert.equal statement:

`Test.assert_equals(function_name('input data'),'desired output data')`

Sadly this line was not present in the test area in all katas, additionally confusing students.

However, Codewars offers huge learning opportunities by looking at (and discussing) the solutions of others. It is also a good tool to tackle katas already solved in a preferred programming language with a different, new programming language.

Finally, Codewars is good suited to introduce the concept of [pair programming](https://en.wikipedia.org/wiki/Pair_programming) via coding dojos: Two students have to solve a kata togehter, one doing the thinking (navigator) while the other does the typing (driver). After a given time interval or after at least one test is passed, a new student becomes driver and the former driver becomes navigator.  

## participation and license

Users in Codewars are encouraged to particpate. Ability to discuss, share and fork katas and kumites is in-build. As stated in the [Codwars terms page](http://www.codewars.com/about/terms-of-service), all uploaded code is licensed under the [FreeBSD 2-Clause License](http://opensource.org/licenses/BSD-2-Clause) 

## critique

I have nothing at all to critisize about CodeWars. I just wonder about CodeWars business model. As it looks now and according to the Codewars site itself, there seem to be none. I guess the site could become useful as a recruiting tool for IT-Jobs. Hopefully the site will attract enough donations from thankful Computer science teachers finally getting rid of the need to create and score homework.


<hr>

  * This article was republished on July 30, 2015 at [OpenSource.com](http://opensource.com/education/15/7/codewars-codecombat-review), thanks to [Jen Wike Huger](https://twitter.com/JenWike).
  * This article was republished on October 29, 2015 at [internationalopenmagazine](http://internationalopenmagazine.org)




# advertisement (google adsense)

<hr style="height: 3px;">

<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- intopenmag-unten -->
<ins class="adsbygoogle"
     style="display:inline-block;width:728px;height:90px"
     data-ad-client="ca-pub-3535173094498375"
     data-ad-slot="7210184316"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>


