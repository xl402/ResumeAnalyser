import os

import pytest


repo_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESOURCE_DIR = os.path.join(repo_path, 'resources')


@pytest.fixture
def example_resume_path():
    path = os.path.join(RESOURCE_DIR, 'example_resume.pdf')
    return path
