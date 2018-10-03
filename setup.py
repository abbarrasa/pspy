from setuptools import find_packages, setup


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
    name='PSPy',
    version='0.0.1',
    author='Alberto Buitrago Barrasa',
    author_email='abbarrasa@gmail.com',
    description=('A ISO games manager for PSP.'),
    long_description=get_readme(),
    license='BSD',
    keywords='PSP games manager',
    url='https://github.com/abbarrasa/pspy',
    packages=find_packages(),
    package_data={
        'pspy': ['*.txt']
    },
    install_requires=['markdown==2.6.5'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities'
    ]
)
