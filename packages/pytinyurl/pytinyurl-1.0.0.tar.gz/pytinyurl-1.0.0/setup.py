from setuptools import setup

setup(
    name='pytinyurl',
    version='1.0.0',
    py_modules=['pytinyurl'],
    entry_points={
        'console_scripts': [
            'pytinyurl = pytinyurl:main',
        ],
    },
    author='Avinion',
    author_email='shizofrin@gmail.com',
    url='https://x.com/Lanaev0li',
    description='An interactive script to shorten URLs using TinyURL',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
