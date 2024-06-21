import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="is3_analyse",
    version="0.5",
    author="Zhiheng Ning",
    author_email="",
    description="is3 python server",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ZhihengNing/Python-server",
    packages=setuptools.find_packages(),
    install_requires=['Flask==3.0.3', 'numpy==1.26.4'],
    entry_points={
        'console_scripts': [
            'is3_analyse=is3_analyse:main'
        ],
    },
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
