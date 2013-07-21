fasttransfer
============

A multithreaded/multiprocessed uploader from traditional filesystems to Objects Storage. Without the need for a database!

=====
Install
=====
Install requirements.txt  
Install celery/rabbit  
Make sure Rabbit and Celery (below in Startup) are on.  
Make sure you copy fasttransfer.conf to ~/.fasttransfer.conf

======
Startup
======

Start up the 2 queues. "celery" is the default and is used for job submission. "files" is used for processing filecontainers. You need as many processors as possible for "files", as that will be the primary way to distribute the load. "celery" queue is mostly just used to start up a few jobs at a time. "celery" jobs will spawn thousands of "files" jobs.  

Think about it this way, if you have a directory of millions of files and sub-dirs, and you point the crawler at it, that goes into the queue as a single "celery" job. That job, while running, will spawn many more "files" jobs.

```
PYTHONPATH=$PYTHONPATH:/Users/dbernick/git/fasttransfer/src celery worker -A FastTransfer.tasks -c 1 -E -l info -Q celery
PYTHONPATH=$PYTHONPATH:/Users/dbernick/git/fasttransfer/src celery worker -A FastTransfer.tasks -c 4 -E -l info -Q files
```