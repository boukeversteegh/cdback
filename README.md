cd/back
======

Trace back your steps in the commandline. Wraps system `cd` and adds a `back` command.
Similar to `cd -` but supporting multiple steps.

```bash
~$ cd /home
/home$ cd admin
/home/admin$ cd docs
/home/admin/docs$ back
/home/admin$ back
/home$ back
/$ back
~$ 
```

Installing
==========

```bash
# Clone the repository into any directory
cd ~/somedir
git clone http://github.com/boukeversteegh/cdback

echo "export CDBACK=~/somedir" >> ~/.bash_profile
echo "source ~/somedir/cdback/cdback.sh" >> ~/.bash_profile
```

Open a new shell or terminal window to start using cd/back.
