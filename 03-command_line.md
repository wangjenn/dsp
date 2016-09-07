# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

- **cd..**: move up one directory
- **mkdir**: make directory 
- **touch**: create a new file inside a working directory 
- **-t**: order files and directories by the time they were last modified 
- **cp**: copy files or directories 
- * : select GROUPS of files 
- **mv**: moving files 
- **rm**: remove files 
- **cat**: outputs the contents of a file to the terminal 
- ** | **: pipeline takes the standard output of the command on the left and pipes it as a standard input to the command on the right
- **grep**: it searches files for lines that match a pattern and returns the results. For it to be case sensitive, use -i. 

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`: list the files and folders you are currently in 
`ls -a`: list files and directories, including those that are hidden   
`ls -l`: lists all contents of a directory in a long format 
`ls -lh`: shows all files in human readable format in a long format  
`ls -lah`: shows all files, including those that are hidden, in human readable format and long format 
`ls -t`: list files and directories by the time they were last modified   
`ls -Glp`: list indictator to directory in a long listing format (don't print group names)  

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

- **C**: displays files in a columnar format 
- **F**: flags filenames 
- **q**: displays all nonprinting characters as ? 
- **x**: displays files as rows across the screen 
- **-1**: displays each entry on a line 

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.
- It is used to build and execute command lines from standard input. More specifically, "xargs" is used to remove long list of file names which were produced by "find" & "grep" commands. It divides the list into into sub-list with acceptable length. 

- **Example**: find . -name "*.sh" | xargs grep "ksh" 
- First, find all files that end in .sh from current directory. Then, find each .sh file that has the word "ksh." 
