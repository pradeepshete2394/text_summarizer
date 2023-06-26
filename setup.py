import setuptools 
with open ("README.md","r",encoding="utf-8") as f:
    long_description = f.read()

__version__ ="0.0.0"
REPO_NAME = "text_summarizer"
AUTHOR_USER_NAME="PRADEEP"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "pradeepshete001@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for nlp app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pradeepshete001/textSummarizer",
    project_url={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",},
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src"))