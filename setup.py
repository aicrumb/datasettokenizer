import setuptools

setuptools.setup(
    name='datasettokenizer',
    version='0.0.1',
    author='aicrumb',
    author_email='aicrumbmail@gmail.com',
    description='one function to tokenize a huggingface dataset that isnt streamed',
    long_description='i was bored of writing the code myself every time lol',
    long_description_content_type="text/markdown",
    url='https://github.com/aicrumb/tokenizer',
    project_urls = {
        "Bug Tracker": "https://github.com/aicrumb/tokenizer/issues"
    },
    license='GNU GPLv3',
    packages=['datasettokenizer'],
    install_requires=['tqdm'],
)