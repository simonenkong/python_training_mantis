__author__ = 'Nataly'
from model.project import Project

def test_add_project(app):
    project = Project("project_name", "description1")
    old_list = app.project.get_project_list()
    if project in old_list:
        app.project.delete_project(project)
    old_list = app.project.get_project_list()
    app.project.add_project(project)
    new_list = app.project.get_project_list()
    old_list.append(project)
    assert sorted(old_list, key=Project.id_or_max) == sorted(new_list, key=Project.id_or_max)
