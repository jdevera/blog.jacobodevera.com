The Code Function
=================

:category: Programming
:tags: bash, tools
:lang: en
:date: 2013-11-21

I use a somewhat customised shell environment, with lots of aliases, functions,
scripts, etc. I use those as commands without actually stopping to think what
they really are.

But sometimes, I need to know. I used to do ``which <program>`` and then open
the response in a pager or editor, but that can be misleading, since a function
with the same name might exist and will take precedence over a script.

I put an end to that by writing the **code** function:

.. code:: bash

    function code() 
    { 
        local type=$(builtin type -t $1);
        case $type in 
            alias)
                echo "$1 is an alias";
                builtin alias $1 | sed 's/^[^=]\+=//'
            ;;
            function)
                echo "$1 is a function";
                builtin declare -f $1;
            ;;
            builtin | keyword)
                echo "$1 is a shell $type";
                builtin help $1
            ;;
            file)
                local path=$(which $1);
                if head -1 $path | grep -q "^#!"; then
                    echo "$1 is a script at $path";
                    cat $path;
                else
                    echo "$1 is a binary at $path";
                fi
            ;;
            *)
                echo "I don't know what $1 is";
                return 1
            ;;
        esac
    }

It simply finds the type of executable *thing* that the shell will use and
tries to describe it in its output:

- For an **alias**, it prints its definition
- For a **function**, it prints its code
- For a **shell builtin**, it prints its help text
- For a **script**, it prints the source
- For a **binary executable** file, it prints nothing.

So now I can happily do something like this::

    $ code cp
    cp is an alias
    'rsync -avz'

    $ code code abspath
    abspath is a script at /home/jdevera/other/run/bin/abspath
    #!/usr/bin/python
    import os.path
    import sys

    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        print os.path.abspath(sys.argv[1])
    else:
        sys.exit(1)

I can even run ``code code``! :)

