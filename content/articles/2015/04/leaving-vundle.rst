Leaving Vundle
==============

:category: Programming
:tags: vim, open-source
:lang: en
:date: 2015-04-24

I've been a Vim user for approximately 13 years, and what an editor it is! At
some point I stopped being happy with vanilla Vim with just a couple of
settings in my ``.vimrc`` file and started looking at some plugins to enhance
my editing experience.

This worked out well, but the plugin installation method (unzipping everything
into ``.vim``) was a mess. When Pathogen.vim_ came along it seemed like we were
onto something, it was such a simple and great idea.

.. _Pathogen.vim: https://github.com/tpope/vim-pathogen

Then, in 2011, this commit made its way into my ``dotfiles`` repository::

    commit f694120f093936b693828fb298ea13481a31869c
    Author: Jacobo de Vera
    Date:   Wed Jul 27 02:08:33 2011 +0100

        Vim: Replace plugin submodules with Vundle
        
        Use Gmarik's Vundle to manage vim plugin repositories and stop tracking
        them myself as submodules.
        
        From now on, I will only track plugins that I have written or modified,
        perhaps as a first step before moving them to their own repo if they are
        large enough.

**Vundle!**

Vundle_ brought the twenty first century into the world of installing Vim
plugins. It made our dotfiles better by not having to include all the plugin
code but rather just say what plugin we wanted installed. I got so excited with
Vundle that I started to open issues, pull requests, started to answer users'
questions, etc. At some point, ``gmarik`` granted me commit access to the
repository and, with it, the power to close issues and merge pull requests.  I
thought it was such a great tool that I prepared a presentation_ to tell my
colleagues about how awesome it was.

.. _Vundle: https://github.com/gmarik/Vundle.vim
.. _presentation: http://www.slideshare.net/jacobodevera/vundle-lightning-talk

There was even a time when another contributor was active and testing all sort
of things on Windows. It was a time of fast development, but it did not last
long. He disappeared, and then I could no longer merge non-trivial pull
requests without the risk of breaking Vundle on Windows. I don't use Windows,
I can't troubleshoot it, and the pull requests pile up forever.

Additionally, I also ended up getting frustrated by how slow the installer was,
so I wrote a `script in python`__ that used the Vundle definitions to get a list of
plugins to clone, and then clone in parallel. The results were great, I could
upgrade all my plugins in less than 10 seconds instead of more than a full
minute with Vundle. I however, kept using Vundle because it provided the
declaration and parsing capabilities.

__ https://github.com/jdevera/parallel-vundle-installer

But issues kept being open, Windows users kept getting frustrated, I also kept
getting frustrated for not being able to help them. The authors of pull
requests, or even the users who participated in the discussion for very popular
feature requests kept waiting and sometimes just giving up.

I stopped enjoying spending time working on Vundle, helping people with Vundle,
etc.

I decided to quit it. Go back to being *just another user*.

But just about the same time, I realised that the author of one of my favourite
little tools (fzf_) had his own simple plugin manager for Vim (vim-plug_), and
that coincidentally, one of the Vundle collaborators I had worked with in the
past had apparently moved to this other manager, and actively contributed, and
also that the history of how ``junnegunn`` came about implementing ``vim-plug``
was pretty much the same of why I wrote my parallel-vundle-installer_.

.. _fzf: https://github.com/junegunn/fzf
.. _vim-plug: https://github.com/junegunn/vim-plug
.. _parallel-vundle-installer: https://github.com/jdevera/parallel-vundle-installer

I gave it a try::

    commit c4e863fb0f428be61ab8268cf353fb63393a48be
    Author: Jacobo de Vera
    Date:   Mon Apr 6 21:51:29 2015 +0200

        Vim: Switch from Vundle to Plug to manage plugins
        
        Switch from gmarik/Vundle.vim to junegunn/vim-plug to manage vim
        plugins. Mainly for speed reasons.
        
        In order to do the switch, after getting this commit one should:
        
        - Change all local `Plugin` lines to be `Plug` and adjust the options
        to that of Plug.
        - Run the following commands from within Vim:
        
            :PlugUpgrade
            :PlugInstall
            :PlugUpdate
            :PlugClean

It was completely painless. Updates are fast, I no longer look at the code, I
don't need to, it does everything I need.

Vundle, however, is still widely unmaintained and needs help. There are a ton
of pull request waiting to be assessed, lots of issues, particularly Windows
related, that need to be fixed. Vundle needs help. I'm just sorry I cannot
continue to be there. I've done my 4 years, now I'm moving on, and hope that
some other users get excited enough to help out other users (I'm already seeing
some movement in this direction, which is nice).

But me, well, it's been great, I've had fun. Thanks ``gmarik`` and all other
contributors. I'm moving on.
