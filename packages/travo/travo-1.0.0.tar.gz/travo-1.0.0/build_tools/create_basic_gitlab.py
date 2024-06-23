import os
import gitlab
from gitlab.v4.objects import User, Group, Project
import requests
from urllib.parse import urljoin

from typing import (
    Dict,
    Any,
)


def create_user(user_data: Dict[str, Any]) -> User:
    try:
        return gl.users.create(user_data)
    except gitlab.exceptions.GitlabCreateError as e:
        print(f"user {user_data['username']} already defined: {e.error_message}")
        return gl.users.list(username=user_data["username"])[0]


def create_group_or_subgroup(group_data: Dict[str, Any]) -> Group:
    try:
        return gl.groups.create(group_data)
    except gitlab.exceptions.GitlabCreateError as e:
        print(f"group {group_data['name']} already defined: {e.error_message}")
        return [gr for gr in gl.groups.list() if gr.name == group_data["name"]][0]


def create_user_project(user: User, project_data: Dict[str, Any]) -> Project:
    try:
        user.projects.create(project_data)
    except gitlab.exceptions.GitlabCreateError as e:
        print(f"project {project_data['name']} already defined: {e.error_message}")

    return [pr for pr in gl.projects.list() if pr.name == project_data["name"]][0]


if "GITLAB_HOST" in os.environ and "GITLAB_80_TCP_PORT" in os.environ:
    gitlab_url = (
        f"http://{os.environ['GITLAB_HOST']}:{os.environ['GITLAB_80_TCP_PORT']}"
    )
else:
    gitlab_url = "http://gitlab"

# Password authentification is no longer supported by python-gitlab
# https://python-gitlab.readthedocs.io/en/stable/api-usage.html#note-on-password-authentication # noqa: E501
data = {"grant_type": "password", "username": "root", "password": "dr0w554p!&ew=]gdS"}
resp = requests.post(urljoin(gitlab_url, "oauth/token"), data=data)
resp_data = resp.json()
gitlab_oauth_token = resp_data["access_token"]

# login
gl = gitlab.Gitlab(gitlab_url, oauth_token=gitlab_oauth_token)

# create users
user_data = {
    "username": "travo-test-etu",
    "email": "travo@gmail.com",
    "name": "Étudiant de test pour travo",
    "password": "aqwzsx(t1",
    "can_create_group": "True",
}

user = create_user(user_data)

other_user_data = {
    "username": "blondin_al",
    "email": "blondin_al@blondin_al.fr",
    "name": "Utilisateur de test pour travo",
    "password": "aqwzsx(t2",
}

other_user = create_user(other_user_data)

# create user projects and groups
project_data = {"name": "nom-valide", "visibility": "private"}

create_user_project(user, project_data)

project_data = {
    "name": "Fork-de-travo-test-etu-du-projet-Exemple-projet-CICD",
    "visibility": "private",
}

create_user_project(user, project_data)

group_data = {"name": "group1", "path": "group1"}

group = create_group_or_subgroup(group_data)

try:
    group.members.create(
        {"user_id": user.id, "access_level": gitlab.const.AccessLevel.DEVELOPER}
    )
except gitlab.exceptions.GitlabCreateError as e:
    print(f"member already exists: {e.error_message}")

subgroup_data = {"name": "subgroup", "path": "subgroup", "parent_id": group.id}

subgroup = create_group_or_subgroup(subgroup_data)

grouppublic_data = {
    "name": "Groupe public test",
    "path": "groupe-public-test",
    "visibility": "public",
}

grouppublic = create_group_or_subgroup(grouppublic_data)

admin_user = gl.users.list(username="root")[0]
project_data = {
    "name": "Projet public",
    "visibility": "public",
    "namespace_id": grouppublic.id,
}

project = create_user_project(admin_user, project_data)

# create commits
# See https://docs.gitlab.com/ce/api/commits.html#create-a-commit-with-multiple-files-and-actions # noqa: E501
# for actions detail
data = {
    "branch": "master",
    "commit_message": "blah blah blah",
    "author_name": user.name,
    "author_email": user.email,
    "actions": [
        {
            "action": "create",
            "file_path": "README.md",
            "content": "This is a README.",
        },
    ],
}

try:
    project.commits.create(data)
except gitlab.exceptions.GitlabCreateError as e:
    print(f"file already committed: {e.error_message}")


# general settings for project export and import
settings = gl.settings.get()
settings.max_import_size = 50
settings.import_sources = ["git", "gitlab_project"]
settings.save()
