The Quest For Subcommands (Part I)
==================================

:category: Programming
:tags: bash, tools
:lang: en
:date: 2013-11-24


This is the first part of a little story about my personal quest to find a
solution to my subcommand needs. If you think you might have such needs, if you
are not sure if you do, or if you are simply curious, please read on.

Where I work, we develop a product that is based on several subsystems, written
in various languages and with different degrees of autonomy. In order to
provide an homogeneous development environment, we use a *chrooted* sandbox that
tries to imitate the actual environment where out software will run. We also
have access to some actual hardware boxes for testing our full images or the
actual network communication between boxes, and so on.

This basically means that in my daily work, in order to test stuff, I have to
run a thousand commands, all of them written in different times, by different
people, without conventions, sometimes without documentation, sometimes even
written in Perl (I know!).

This was giving me headaches, so I started to write little command wrappers
grouped by topic. I wrote them as shell functions, since some of them would
require changing the current directory on the running shell. One of these
wrappers, for example one called ``foo``, would look like this:


.. code:: bash

    # Check if the given name can be executed as a command
    has_dep()
    {
        [[ -z $1 ]] && return 1
        type -t "$1" > /dev/null
    }

    # A light launcher for all things 'foo-'
    foo()
    {
        local subcommand="$1"
        shift
        command="foo-$subcommand"
        if has_dep "$command" ; then
            $command "$@"
        else
            echo "Command 'foo $subcommand' not found"
            has_dep foo-help && foo-help
        fi
    }


With this simple structure, I can then have a collection of programs, scripts,
functions, aliases, whatever, as long as its name starts with ``foo-``, that
can be launched with this ``foo`` wrapper/launcher. It will call ``foo-help``
if it exists in cases where the entered subcommand does not exists.

For this to be usable for me at all, I had to set up shell completion for it.
This is how:

.. code:: bash

    __complete_foo()
    {
        compgen -c foo- | sed 's/^foo-//' | grep "^$2.*"
    }

    complete -C __complete_foo -o default foo


This is more than enough for a simple need, but after I had created four or
five of those, with a number of subcommands each, my environment ended up being
polluted with lots of those subcommands in the PATH.

Also, the ``help`` command for each one needs to be maintained in sync with
available subcommands manually and, even worse, shell completion works only up
to the second token (the subcommand).

More problems appeared when I started playing a bit with the `Fish shell`__,
but I found myself extremely unproductive without all my bash functions and
wrapper/launchers, so I started trying to port them. It was a pain, and it was
not worth it, since I might choose to change shells again the week after.

__ Fish_

And so I started to look for some way to organise scripts in a hierarchy of sub
commands, with these requirements:

- Multiple levels of subcommands, so that I could put everything under a huge
  **master command** called perhaps *work*.

- An easy way to keep documentation and inline help synchronised with the
  changes in the commands.

- Some easy way to provide shell completion, all the way in.

- Ideally, that I could have the subcommands outside the PATH, to keep the
  environment clean.

So, for a while, all I found was SM_. It seems like a great project, and I
started trying to implement my needs with it, I got a lot of help from the
maintainers. BUT it was simply too much. I could not understand exactly how it
worked and at some point I got stuck getting the most basic bits to behave as
expected, so I temporarily gave up and continued using my simple wrappers and
trying to port them to Fish.

But hope was not lost, and, in fact,  I found another tool that, while simple
enough to be understood in a short session of "just looking at the code", it
provided most of my requirements. But that, I'll leave for **part II**.

.. _SM: https://smf.sh
.. _Fish: http://fishshell.com/

