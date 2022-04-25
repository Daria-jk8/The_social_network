
ACTION PLAN:

DJANGO_start
# architecture and filenames
--> ci.yml                   # check code quality

-Pipfile                     #
Pipfiles contain information for the dependencies of the project, and supersedes the requirements.txt file used in most Python projects. You should add a Pipfile in the Git repository letting users who clone the repository know the only thing required would be installing Pipenv in the machine and typing pipenv install. Pipenv is a reference implementation for using Pipfile.

-Pipfile.lock                # for computer
-README.md                   # document