# Code Review 05/10/23

## Dependencies

- Add django_filters to requirements.txt

# Pre-commit

- Use pre-commit to check code syntax before commiting your work

# Git

- Add .gitignore file to do not push .vscode (specific for each dev) on the repository
- Please be explicit in your commit message, you can follow this convention: you can use those prefix fix,feat,chore,docs, etc.
https://github.com/commitizen/cz-cli
- This tool allows to enforce the commit message


## General

[ ] Clean unused imports (use black library to clean your code, isort to resort imports)

https://github.com/psf/black

[ ] Imports should be ordered as followed

- Python builtin imports
- (Empty line)
- Python third party imports
- (Empty line)
- Python local project imports

[ ] Delete unused comments

[ ] Use ModelViewSet when you can for example PostViewSet

[ ] No print in production code if you want to setuo logs use django loggers

https://docs.djangoproject.com/en/4.2/topics/logging/#examples

[ ] Only add trailing slash if the route contains other routes or actions

https://stackoverflow.com/questions/61547014/restful-uri-trailing-slash-or-no-trailing-slash

[ ] Fix pylint erros and pass the pylint code check

[ ] The general rule is to add docstrings for classes and methods
You can use the following format:

[ ] I would rename auth to users (up to you to make the change if your think it adds value else no worries)

[ ] Where are you tests? :)

Please add tests for each layer:
- Models
- Serializers
- Views

[ ] I would put the routes for posts and auth to empty
It looks a bit strange to have something like /posts/v1/posts
I would prefer /v1/posts/

[ ] Please use environment variables for the email credentials in settings

[ ] Looks a bit strange to have post in models.py when there is a specific folder called posts in the same folder

https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html
# What has been reviewed

[X] api/posts/views.py
[X] api/posts/serializers.py
[X] api/posts/views.py
[X] api/admin.py
[X] api/models.py
[X] api/tests.py
[X] api/urls.py
[X] auth/views.py
[X] auth/urls.py
[X] auth/serializers.py
[X] ihlserver/media
[X] ihlserver/settings/base.py
[X] ihlserver/settings/developer.py
[X] ihlserver/settings/production.py
