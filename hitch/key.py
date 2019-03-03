from commandlib import CommandError, Command, python, python_bin
from hitchstory import HitchStoryException, StoryCollection
from hitchrun import DIR, expected
from pathquery import pathquery
import engine
import build


def _exercisebook(rewrite=False):
    return StoryCollection(
        pathquery(DIR.project / "exercises").ext("story"), engine.Engine(DIR, rewrite=rewrite)
    )



@expected(CommandError)
def postgres():
    """
    Run python 3 code with the hk virtualenv.
    """
    db_service = build.pgdata(DIR).server()
    db_service.start()
    psql = db_service.psql(
        "-U", "myuser", "-p", "15432", "-d", "mydb",
    ).with_env(PG_PASSWORD="mypassword")
    assert "London" in psql(
        "-c", "select name from cities where location = 'GB';"
    ).output()
    db_service.stop()


@expected(HitchStoryException)
def exercise(*keywords):
    """
    Run exercise matching keywords.
    """
    _exercisebook().shortcut(*keywords).play()



@expected(HitchStoryException)
def rewrite(*keywords):
    """
    Run exercise in rewrite mode (for building exercises).
    """
    _exercisebook(rewrite=True).shortcut(*keywords).play()
