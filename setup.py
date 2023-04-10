from setuptools import setup, find_packages

setup(
    name="Crossplatform-pack",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # dependencies go here
    ],
    entry_points={
        "console_scripts": [
            "myapp = app.main:main"
        ]
    },
    license="MIT",
    long_description=open("Crossplatform-pack/app/README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/HsiangNianian/Crossplatform-pack",
    author="HsiangNianian",
    author_email="your.email@example.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
