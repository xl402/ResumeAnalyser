import os

import pytest


@pytest.fixture
def resource_dir():
    repo_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(repo_path, 'resources')


@pytest.fixture
def example_resume_path(resource_dir):
    path = os.path.join(resource_dir, 'example_resume.pdf')
    return path
