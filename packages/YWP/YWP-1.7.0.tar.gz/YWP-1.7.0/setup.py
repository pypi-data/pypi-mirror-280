from setuptools import setup, find_packages

setup(
    name='YWP',
    version='1.7.0',
    packages=find_packages(),
    install_requires=[
        "dill",
        "flask",
        "flask-cors",
        "gtts",
        "joblib",
        "moviepy",
        "nltk",
        "pyaudio",
        "pygame",
        "selenium",
        "setuptools",
        "sounddevice",
        "SpeechRecognition",
        "tensorflow",
        "tflearn",
        "twine",
        "wheel",
        "pycryptodome"
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.6',
    description='This is a library to simplify the Python language for beginners while adding some features that are not found in other libraries',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Wanted Products (YWP)',
    author_email='pbstzidr@ywp.freewebhostmost.com',
)
