from setuptools import setup, find_packages

setup(
    name='jafri-chromedriver-installer',
    version='0.1.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'update-chromedriver=jafri_chromedriver_installer.installer:update_chromedriver',
        ],
    },
    author='Musharraf Jafri',
    author_email='musharrafsoft@gmail.com',
    description='A package to automatically update Chromedriver to match the installed Chrome version.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/musharrafjafri/jafri-chromedriver-installer',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
