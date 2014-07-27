The Quest For Subcommands (Part II)
===================================

:category: Programming
:tags: bash, tools
:lang: en
:date: 2014-07-27

This is the second part of a little story about my personal quest to find a solution to my subcommand needs. Please read `Part I`_ if you haven't done so already. If you think you might have such needs, if you are not sure if you do, or if you are simply curious, please read on.

.. _Part I: {filename}/articles/2013/11/the-quest-for-subcommands-part-i.rst

After my unsuccessful experience with the promising but otherwise complex SM, I just switched back to my self crafted launcher and used it for months. But then one day, a link on `Hacker News`_ took me to `a post in the 37 Signals (now Basecamp) blog`__ where they talked about a little tool they use to aggregate a collection of scripts as subcommands of a main launcher. They called it **sub**, and it looked exactly like what I had been looking for.

.. _Hacker News: https://news.ycombinator.com/
__ http://signalvnoise.com/posts/3264-automating-with-convention-introducing-sub

Sub's usage is quite simple. One only needs to clone a repository, run a script that will rename the launcher (originally called sub) to whatever you want, and then you only have to put your commands under the ``libexec`` directory. They call this bundle *a sub*. Of course, Sub comes with completion for the name of all your commands, but you can even get completion for your subcommands easily: If you have a comment in the script that says “*Provide foo completions*”, where *foo* is your sub's name, sub will run your subcommand with the ``--complete`` flag when it is finding completions, and will take anything it writes to standard output as the completions for that command. So, for example, if *foo* has a command that can take flags ``-a`` and ``-b``, you can get completion for those with:

.. code:: bash

    # Provide foo completions
    if [[ $1 == '--complete' ]]; then
        echo -a -b
    fi


It cannot get any simpler. Sub also has a killer feature that I really loved: You can have special subcommands that were run directly in the shell you used to invoke them, so you could have a subcommand to, for instance, *cd* into a particular directory. This worked because, as part of its initialisation, Sub was setting up a shell function with your sub's name, so when you call your sub, you are actually running this shell function. This shell function then checked if the subcommand you wanted to run was one of these special shell commands, and in that case, it ``eval``'ed the output of it, otherwise it simply ran the command. Brilliant idea!

So I started porting everything to Sub, and I was happy for a short while. But then I realised that one main command with some subcommands was not enough to cover all my needs. Some commands asked for several levels of subcommands. Particularly, at work, I wanted to have **one single command** to aggregate all of my little utility scripts, and there were many, all related to different things, I wanted to use some namespacing.

I wanted to run something like:

.. code::

    $ w test runall
    $ w test new
    $ w db wipe
    $ w db check

Or even more levels. Not surprisingly, someone else had had that need too, so there was already a pull request in the repository that added support for *sub-sub-commands*. I gave it a try but was not convinced with the results, so since it was a simple shell script, I tried to implement the feature myself. I shared my findings with the author of that pull request, but did not send my own because I thought it would have been poor *netiquette* to do so.

But what happened was that the code got ugly fast. This use case by far exceeded the complexity that you want a shell script to handle. Also, while writing that enhancement, I thought of several others, so I decided to write the whole thing in Python.

And I did, a somewhat straight translation from shell script to python, not particularly idiomatic, but at least functional. I started using that version extensively. I keep it in the ``python`` branch of `my fork of sub on github`__. You can use it today the same way you can use Sub, plus you get the sub-sub-commands support.

__ https://github.com/jdevera/sub/tree/python

However, the story does not end here. Once I finished a working version of my Python port, I started to use it extensively and created a number of subs. Then I realised that, whenever I found a bug in the launcher, I had to copy the fix to all the subs I had created. So I ended up linking all the launchers to one single location, but this was rather *hackish*, since I had to remember to do that every time I cloned a new sub. I was not too happy with this. I realised that it was a far more solid approach to have the subs contain the commands, but not the launcher itself. The launcher code should be in a library, and the actual launcher script for the sub would only have to use the library. Then I would only have to update the library and the fixed bug would be gone from all of my subs.

In the third part of this series I will cover briefly the new project I created to solve this issue and to go wild with many other ideas I had about sub commands. Until then, enjoy your sub-sub-sub-sub... commands.
