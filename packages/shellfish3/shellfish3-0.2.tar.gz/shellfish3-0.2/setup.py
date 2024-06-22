from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='shellfish3',
    version='0.2',
    author='AppSecGroup',
    description='Shellfish testing library',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/appsecgroup/shellfish3',
    license='MIT',
    include_package_data=True,
    packages=find_packages(include=[
        "shellfish3", "shellfish3.*"
    ]),
    package_data={
        '': ['*']
    },
    install_requires=['requests'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License"
    ]
)
