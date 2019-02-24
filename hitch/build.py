import hitchbuildpg


class DataBuild(hitchbuildpg.DataBuild):
    def __init__(self, dump_sql):
        self._dump_sql = dump_sql

    def run(self):
        self.run_sql_as_root("create user myuser with password 'mypassword';")
        self.run_sql_as_root("create database mydb with owner myuser;")
        self.load_database_dump(
            database="mydb",
            username="myuser",
            password="mypassword",
            filename=self._dump_sql
        )


def pgdata(dirs):
    pgapp = hitchbuildpg.PostgresApp("9.5.12").with_build_path(dirs.share)
    pgdata = hitchbuildpg.PostgresDatafiles(
        "myappdata",
        pgapp,
        DataBuild(dirs.key / "dump.sql"),
    ).with_build_path(dirs.gen)
    pgdata.ensure_built()
    return pgdata
