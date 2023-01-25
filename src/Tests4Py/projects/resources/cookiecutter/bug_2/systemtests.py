from abc import ABC

from Tests4Py.tests.diversity import Systemtests


class DefaultTests(ABC, Systemtests):
    def __init__(self, passing: bool = False):
        Systemtests.__init__(self, passing=passing)

    @staticmethod
    def _default_config(
        full_name='"Marius Smytzek"',
        email='"mariussmtzek@cispa.de"',
        github_username='"smythi93"',
        project_name='"Test4Py Project"',
        repo_name='"t4p"',
        project_short_description='"The t4p project"',
        release_date='"2022-12-25"',
        year='"2022"',
        version='"0.1"',
    ):
        return (
            f'{{"full_name":{full_name},'
            f'"email":{email},'
            f'"github_username":{github_username},'
            f'"project_name":{project_name},'
            f'"repo_name":{repo_name},'
            f'"project_short_description":{project_short_description},'
            f'"release_date":{release_date}'
            f'"year":{year},'
            f'"version":{version}}}'
        )


class TestsFailing(DefaultTests):
    def __init__(self):
        super().__init__(passing=False)

    def test_diversity_1(self):
        return f"{self._default_config()}\npre:pre1\npre:pre2"

    def test_diversity_2(self):
        return f"{self._default_config()}\npost:post1\npost:post2"

    def test_diversity_3(self):
        return f"{self._default_config()}\npre:pre1\npost:post2\npre:pre2"

    def test_diversity_4(self):
        return f"{self._default_config()}\npost:post1\npost:post2\npre:pre1"

    def test_diversity_5(self):
        return f"{self._default_config()}\npre:pre1\npost:post1\npre:pre2\npost:post2"

    def test_diversity_6(self):
        return f"{self._default_config()}\npre:pre1\npre:pre2\npre:pre3"

    def test_diversity_7(self):
        return f"{self._default_config()}\npost:post1\npost:post2\npost:post3"

    def test_diversity_8(self):
        full_name = '["Marius Smytzek","Martin Eberlein"]'
        return f"{self._default_config(full_name=full_name)}\npost:post1\npost:post2"

    def test_diversity_9(self):
        full_name = '["Marius Smytzek","Martin Eberlein"]'
        return f"{self._default_config(full_name=full_name)}\npre:pre1\npre:pre2"

    def test_diversity_10(self):
        return f"{self._default_config()}\npre:This is a more complex example of a pre hook_ Will this work\npre:pre2"


class TestsPassing(DefaultTests):
    def __init__(self):
        super().__init__(passing=False)

    def test_diversity_1(self):
        return f"{self._default_config()}\npre:pre1"

    def test_diversity_2(self):
        return f"{self._default_config()}\npost:post1"

    def test_diversity_3(self):
        return f"{self._default_config()}\npre:pre1\npost:post1"

    def test_diversity_4(self):
        return f"{self._default_config()}\npost:post1\npre:pre1"

    def test_diversity_5(self):
        return f"{self._default_config()}\n"

    def test_diversity_6(self):
        full_name = '["Marius Smytzek","Martin Eberlein"]'
        return f"{self._default_config(full_name=full_name)}\npre:pre1"

    def test_diversity_7(self):
        full_name = '["Marius Smytzek","Martin Eberlein"]'
        return f"{self._default_config(full_name=full_name)}\npre:pre1\npost:post1"

    def test_diversity_8(self):
        full_name = '["Marius Smytzek","Martin Eberlein"]'
        return f"{self._default_config(full_name=full_name)}\npost:post1"

    def test_diversity_9(self):
        full_name = '["Marius Smytzek","Martin Eberlein"]'
        return f"{self._default_config(full_name=full_name)}\n"

    def test_diversity_10(self):
        return f"{self._default_config()}\npre:This is a more complex example of a pre hook_ Will this work"
