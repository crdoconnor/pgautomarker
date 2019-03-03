from hitchstory import StoryCollection, BaseEngine, exceptions, validate, no_stacktrace_for
from hitchstory import GivenDefinition, GivenProperty, Failure
from strictyaml import Str
from templex import Templex
import build


class Engine(BaseEngine):
    given_definition = GivenDefinition(
        exercise=GivenProperty(Str()),
    )

    def __init__(self, paths, rewrite):
        self._path = paths
        self._rewrite = rewrite

    def set_up(self):
        self._db_service = build.pgdata(self._path).server()
        self._db_service.start()
        self._psql = self._db_service.psql(
            "-U", "myuser", "-p", "15432", "-d", "mydb",
        ).with_env(PG_PASSWORD="mypassword")

    @no_stacktrace_for(AssertionError)
    def sql(self, expected_result):
        exercise_file = self._path.project / self.given['exercise']
        assert exercise_file.exists(), "{} doesn't exist.".format(self.given['exercise'])
        actual_result = self._psql("-f", self._path.project / self.given['exercise']).output()

        if actual_result != expected_result:
            try:
                Templex(expected_result).assert_match(actual_result)
            except AssertionError:
                if self._rewrite:
                    self.current_step.update(expected_result=actual_result)
                else:
                    raise

    def tear_down(self):
        if hasattr(self, '_db_service'):
            self._db_service.stop()
