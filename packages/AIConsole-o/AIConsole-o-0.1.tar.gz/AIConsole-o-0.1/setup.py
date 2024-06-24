from setuptools import setup, find_packages

setup(
    name='AIConsole-o',
    version='0.1',
    description='An AI-powered assistant for command-line operations, networking configurations, and file system management, and more...',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Houssam El Khesassi',
    author_email='elkhesassi@gmail.com',
    url='https://github.com/houssam-nxy/Aiconsole-o',
    packages=find_packages(include=['app', 'app.*']),
    install_requires=[
        'google-generativeai',
        'python-dotenv',
        'colorama',
    ],
    entry_points={
        'console_scripts': [
            'aiconsole=app.main:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6', 
)
