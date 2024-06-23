# What's new?

## Version 1.0

The 1.0 release has focused on:
- simplicity of use, especially for simple courses: tutorial, more automation and dashboards,
- backward incompatible changes to better support the best practices,
- backward incompatible changes that helped improve the code quality,
- quality of the code.

In particular:
- the minimal supported Python version is now 3.8,
- black formatting has been applied.

Users are strongly advised not to upgrade to version 1.0 during teaching sessions.

### New features

- Add `quickstart` and `deploy` utilities to ease course creation and deployment (see the
  [quickstart tutorial](quickstart_tutorial)).
- Fix and generalize the instructor dashboard to make it work with any course, including
  courses not using Jupyter notebooks and nbgrader.
- Generalize assignment generation to simple courses.

### Documentation

- Add installation instructions.
- Update tutorials, in particular about [creating and deploying a course](quickstart_tutorial).
- Update and improve docstrings.
- Add developer's guide.

### Backward incompatibilities

- Change default values in `course.py`:

  - `group_submission` is now set to `True`, submissions are grouped by course and session,
    in `https://<forge>//<student>-travo/<course>/<session>/<assignment>` rather than
    `https://<forge>/<student>/<course>-<session>-<assignment>`;
  - `student_dir` is now set to `./`.
- Rename `assignment` attributes and parameters to `assignment_name`.
- Rename `personal_repo` attributes and parameters to `submission`.
- `GitLab.get_user()` throws an exception is called without the `username` parameter.
- Refactor `Course.collect()` collecting student submissions.

### Bug fixes

- Fix name incompatibilities with gitlab and FQDN standards.
- Better interactions with Instructor and student dashboards.
- Fix `Projet.get_creator()` where the current user was returned, rather than the
  student having submitted.

### Command line

- Add `--version` option to the command line.
- Fix boolean options in command line.

### Test infrastructure

- Improve the usability of the test gitlab instance.
- Improve test coverage.
- Allow all the tests to be run locally.

### Translations

- Switch to `i18nice` for localization.
- Improve dashboard translations.
