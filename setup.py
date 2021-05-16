import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
        name='d578uv-k0hax',
        version='0.1.20210516.2',
        author='Michael Englehorn',
        author_email='michael+pypi@englehorn.com',
        description='Python library to simulate a AnyTone AT-D578UV-III hand mic',
        long_description=long_description,
        long_description_content_type='text/markdown',
        url="https://github.com/K0HAX/py-at-d578-microphone",
        project_urls={
            "Bug Tracker": "https://github.com/K0HAX/py-at-d578-microphone/issues",
            },
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
            "Operating System :: OS Independent",
            ],
        package_dir={"": "src"},
        packages=setuptools.find_packages(where="src"),
        python_requires=">=3.6",
        install_requires=['pyserial'],
        )

