from setuptools import setup
from os import path


DIR = path.dirname(path.abspath(__file__))
VIT_VERSION = open(path.join(DIR, 'vit', 'VERSION')).read().strip()
INSTALL_PACKAGES = open(path.join(DIR, 'requirements.txt')).read().splitlines()

with open(path.join(DIR, 'README.md')) as f:
    README = f.read()

setup(
    name='vit',
    packages=['vit', 'vit.formatter', 'vit.theme'],
    description="Visual Interactive Taskwarrior full-screen terminal interface",
    long_description=README,
    long_description_content_type='text/markdown',
    install_requires=INSTALL_PACKAGES,
    version=VIT_VERSION,
    url='https://github.com/scottkosty/vit',
    author='Chad Phillips',
    author_email='chad@apartmentlines.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Programming Language :: Python',
        'Natural Language :: English',
        'Topic :: Text Processing :: General',
    ],
    keywords=[
        'taskwarrior',
        'console',
        'tui',
        'text-user-interface',
    ],
    tests_require=[
    ],
    entry_points = {
        'console_scripts': [
            'vit=vit.command_line:main',
        ],
    },
    include_package_data=True,
    python_requires='>=2.7',
    zip_safe=False
)