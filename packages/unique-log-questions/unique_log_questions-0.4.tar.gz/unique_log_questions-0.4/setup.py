# from setuptools import setup, find_packages

# setup(
#     name='unique-log-questions',
#     version='0.3',
#     packages=find_packages(),
#     include_package_data=True,
#     install_requires=[
        
#     ],
#     package_data={
#         'app1': ['*.py','templates/*'],  # Include all Python files in question_answer_db
#     },
#     classifiers=[
#         'Framework :: Django',
#         'Programming Language :: Python :: 3',
#         'License :: OSI Approved :: MIT License',
#         'Operating System :: OS Independent',
#     ],
# )





from setuptools import setup, find_packages
import os

with open("README.md", "r") as fh:
    long_description = fh.read()
def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append((path, [os.path.join(path, filename)]))
    return paths

setup(
    name='unique-log-questions',
    version='0.4',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # List your dependencies here
    ],
    entry_points={
        'console_scripts': [
            'manage.py = chatbot.manage:main',
            'configure-aws = chatbot.scripts.configure_aws:main',
            'readme = chatbot.scripts.readme:main',
        ],
    },
    package_data={
        'app1': ['static/*', 'templates/*', ],
    },
    # data_files=[
    #     ('', ['README.md', 'manage.py', 'requirements.txt', 'static/*']),
    # ],
    # data_files = package_files('static') + [('', ['README.md', 'manage.py', 'requirements.txt'])],
    
    author='Swati Saini',
    author_email='swati@mixorg.com',
    description='A Django app for chatbot functionality.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/saini2001/chatbot_code',
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python :: 3.11',
    ],
)
