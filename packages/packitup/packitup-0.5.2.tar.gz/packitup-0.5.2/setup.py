from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="packitup",
    version="0.5.2",
    author="James Fincher",
    author_email="jamesfincher@example.com",
    description="A tool to generate project structure and contents as Markdown",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jamesfincher/packitup",
    packages=find_packages(),
    install_requires=[
        "pyperclip",
        "colorama",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Documentation",
        "Topic :: Utilities",
    ],
    python_requires=">=3",
    entry_points={
        "console_scripts": [
            "packitup=packitup.packitup:main",
        ],
    },
)