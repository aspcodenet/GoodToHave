import setuptools

# with open("README.md", "r", encoding="utf-8") as fh:
#     long_description = fh.read()
long_description = "na"

setuptools.setup(
    name='goodtohave',
    version='0.0.4',
    author='Stefan Holmberg',
    author_email='stefan.holmberg@systementor.se',
    description='Good to have things',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/aspcodenet/goodtohave',
    project_urls = {
        "Bug Tracker": "https://github.com/aspcodenet/goodtohave/issues"
    },
    license='MIT',
    packages=['goodtohave'],
    install_requires=['requests']
)