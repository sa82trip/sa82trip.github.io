+++
title = "Get latest log file from remote server by using script languages"
author = ["langEx"]
date = 2022-05-20T00:26:00+09:00
draft = true
+++

## Preface {#preface}

The first thing that I usually do when I face an error or issue raised as an bug I usually check the log.
For checking log, I need to go to remote server to open and look throuhg the log for finding error message.
It was okay for the first few months but moving around directories and checking files on the remote server is pretty slow.
It was challenge for me to endure that laggy movements whenever I need to check the logs.
So I decided I need to make something for making my life easier than before.


## Steps {#steps}

At first I thought I could make make one very simple program with shell script.
So I just began write down code to make my program :)
I created a shell script file like this

```sh
$langEx vim get_log_from_remote.sh
```

and I added this code into get\_log\_from\_remote.sh file

```sh
#!/bin/sh
scp langEx@some_remote_server:/vol1/program1/logs/awesome.log ~/latest.log
```

This progam was working fine, however, it was not what I wanted because I need to input my password for access remote server.

So I tried to find a way to get automation for input my password for access.
