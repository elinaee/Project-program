from distutils.core import setup

import py2exe, glob

setup(
    # this is the file that is run when you start the game from the command line.
    console=["main.py"],
    # data files - these are the non-python files, like images and sounds
    data_files=[
        ("sounds", glob.glob("sounds\\*.ogg") + glob.glob("sounds\\*.wav")),
        ("img", glob.glob("img\\*.gif") + glob.glob("img\\*.png")),
        ("", ["settings.json"]),
    ],
)
