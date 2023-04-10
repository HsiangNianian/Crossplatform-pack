from setuptools import setup, find_packages

setup(
    name="Crossplatform-pack",
    version="0.1.0",
    description="Crossplatform-pack",
    url="https://github.com/HsiangNianian/Crossplatform-pack",
    packages=find_packages(include=["app", "app.*"]),
    entry_points={"console_scripts": ["Crossplatform-pack=app.main:main"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
