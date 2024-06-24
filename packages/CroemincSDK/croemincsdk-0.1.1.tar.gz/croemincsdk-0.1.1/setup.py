from setuptools import setup, find_packages

setup(
    name="CroemincSDK",
    version="0.1.1",
    author="Muhammad Umer farooq",
    author_email="support@croeminc.com",
    description="This SDK provides an organized way to connect and consume Croeminc payment gateway, card storage, and customer management service",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://dev.azure.com/croeminc/NeoGateway/_git/NeoGateway.SDK.Python.Package",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'jsonpickle>=3.2.1',
        'requests>=2.32.3'
    ]
)