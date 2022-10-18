# 0x14. JavaScript - Web scraping
`Scripting` `API` `JavaScript`

|By: Guillaume, CTO at Holberton School|
|:--|
|Weight: 1|
|Project will start Oct 18, 2022 6:00 AM, must end by Oct 19, 2022 6:00 AM|
|will be released at Oct 18, 2022 12:00 PM|
|An auto review will be launched at the deadline|

# Resources
**Read or watch:**

- [Working with JSON data](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON)
- [The workflow of accessing the attributes of a simply-created JSON object by Jimmy Tran from Cohort 1 - San Francisco](https://medium.com/@vietkieutie/the-workflow-of-accessing-the-attributes-of-a-simply-created-json-object-82a5b33e2319)
- [request module](https://github.com/request/request)
- [Modern JS](https://github.com/mbeaudru/modern-js-cheatsheet)

# Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General
- Why JavaScript programming is amazing
- How to manipulate JSON data
- How to use request and fetch API
- How to read and write a file using fs module
- Copyright - Plagiarism
- You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
- You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
- You are not allowed to publish any content of this project.
- Any form of plagiarism is strictly forbidden and will result in removal from the program.

# Requirements
## General
- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 14.04 LTS using node (version 10.14.x)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/node
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should be semistandard compliant. Rules of Standard + semicolons on top. Also as reference: AirBnB style
- All your files must be executable
- The length of your files will be tested using wc
- You are not allowed to use var

# More Info
Install Node 10
```
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```
Install semi-standard
- [Documentation](https://github.com/standard/semistandard)
```
$ sudo npm install semistandard --global
```
Install request module and use it
- [Documentation](https://github.com/request/request)
```
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```

**Notes**: Request module has been deprecated since February 2020 - the team is considering alternative to replace this module - however, it’s a really simple and powerful module for practicing web-scraping in JavaScript (and still used a lot in the industry).
