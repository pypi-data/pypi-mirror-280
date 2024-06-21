from setuptools import setup, find_packages


with open( "README.md", encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

# you need to change all these
VERSION = '0.1'
DESCRIPTION = 'Decorator for Fast Generation of Function Input Output Components'
LONG_DESCRIPTION = 'A function decorator that generates corresponding input and output components with Tkinter based on the number of arguments and return values of the function.'

setup(
    name="defgui",
    version=VERSION,
    author="davidho",
    author_email="",
    url="https://github.com/davidho123/defgui",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'gui', 'defgui','function','tkinter'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
    ]
)
