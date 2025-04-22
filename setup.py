from setuptools import setup, find_packages

setup(
    name="vidot",
    version="1.0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "vidot=xdot.__main__:main",
        ]
    },
    include_package_data=True,
    python_requires=">=3.6",
    description="Fork of xdot with clickable URL and editor support",
    author="Aliqyan",
)
