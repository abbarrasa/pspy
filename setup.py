from setuptools import find_packages, setup


__version__ = '0.0.1'


def get_readme():
    readme = ''
    try:
        import pypandoc
        readme = pypandoc.convert('README.md', 'rst')
    except (ImportError, IOError):
        with open('README.md', 'r') as file_data:
            readme = file_data.read()
    return readme


setup(
    name='pspy',
    version=__version__,
    author='Alberto Buitrago Barrasa',
    author_email='abbarrasa@gmail.com',
    description=('A ISO games manager for PSP.'),
    long_description=get_readme(),
    license='GPLv3',
    keywords=["PSP", "games", "manager", "pspy"],    
    url='https://github.com/abbarrasa/pspy',
    packages=find_packages(),
    package_data={
        'pspy': ['*.txt']
    },
    install_requires=['markdown==2.6.5'],
    classifiers=[
        "Development Status :: 1 - Alpha",
        "License :: OSI Approved :: GNU General Public License v3",
        "Operating System :: POSIX :: Linux",        
        "Programming Language :: Python",
        "Programming Language :: MongoDB",
        "Topic :: Utilities"
    ]
)
