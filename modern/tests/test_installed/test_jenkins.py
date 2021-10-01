import pytest


@pytest.mark.service('jenkins')
class TestJenkinsAgent:

    def test_java(self, container):
        out, err = container.exec(['java', '-version'])
        first_line = out.splitlines()[0]
        # Check Java, up to minor version
        assert 'openjdk version "1.8' in first_line.strip(), f"out: '{out}' err: '{err}'"

    def test_entrypoint(self, container):
        out, err = container.exec(['/opt/entrypoint.sh'])
        # It shows help (missing arguments), but we know it works
        assert 'java -jar agent.jar [options...] <secret key> <agent name>' in out, f"out: '{out}' err: '{err}'"
