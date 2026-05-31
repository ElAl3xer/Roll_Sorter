from setuptools import setup

APP = ['ClipsSorter.py']
OPTIONS = {
    'packages': ['librosa', 'moviepy', 'numpy'],
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
