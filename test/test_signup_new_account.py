__author__ = 'Nataly'


def test_signup_nem_account(app):
    username = "user1"
    password = "test"
    app.james.ensure_user_exists(username, password)
