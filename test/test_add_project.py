__author__ = 'Nataly'
from model.project import Project

def test_add_project(app):
    project = Project("project_name", "description1")
    app.project.add_project(project)
