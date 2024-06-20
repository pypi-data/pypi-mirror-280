import setuptools

setuptools.setup(
    name='carcraft_ads_downloader',
    version='1.0.0',
    author='Artyom Suhov',
    author_email='rock4ts@gmail.com',
    description='',
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        'certifi==2024.6.2',
        'elasticsearch7==7.17.9',
        'python-dotenv==1.0.1',
        'urllib3==1.26.18',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.12',
)
