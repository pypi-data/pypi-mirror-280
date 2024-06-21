from setuptools import setup, find_packages

VERSION = '0.0.3' 
DESCRIPTION = 'Generic email and text messaging package'
LONG_DESCRIPTION = 'Python package for delivering email and text. the sender needs the right email and associated permissions setup to use this'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="txtmsg_rshweet", 
        version=VERSION,
        author="Robert Bunnell",
        author_email="<rshweet@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'first package', 'txtmsg', 'email'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)
