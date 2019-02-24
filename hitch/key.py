from commandlib import CommandError, Command, python, python_bin
from hitchrun import DIR, expected
import build


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


