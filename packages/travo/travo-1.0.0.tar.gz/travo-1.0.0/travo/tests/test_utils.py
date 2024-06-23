import os
import subprocess
import pytest

from travo.utils import git_get_origin


def test_get_origin_error(tmp_path: str) -> None:
    os.chdir(tmp_path)
    with pytest.raises(RuntimeError, match="fatal: not a git repository"):
        os.environ["LANG"] = "en_US.UTF-8"
        # The directory is not a git repository
        git_get_origin()

    subprocess.run(["git", "init", "--quiet"], cwd=tmp_path)
    with pytest.raises(RuntimeError, match="error: No such remote 'origin'"):
        os.environ["LANG"] = "en_US.UTF-8"
        # The remote origin is not defined
        git_get_origin()
