from setuptools import setup, find_packages

setup(
    name="myapp",
    version="0.1.0",
    description="My Awesome App",
    url="https://github.com/yourusername/myapp",
    packages=find_packages(),
    entry_points={"console_scripts": ["myapp=app.main:main"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
