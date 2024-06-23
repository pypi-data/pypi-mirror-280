import os.path
import pkg_resources
import typing
import yaml  # type: ignore
import i18n  # type: ignore


class MyLoader(i18n.loaders.YamlLoader):
    loader = yaml.FullLoader


i18n.register_loader(MyLoader, ["yml", "yaml"])
i18n.set("enable_memoization", True)
i18n.set("fallback", "en")
i18n.load_path.append(pkg_resources.resource_filename(__name__, "/locale"))
i18n.set("locale", os.environ.get("LANG", "en")[:2])


def _(key: str, **kwargs: typing.Any) -> str:
    """Return the i18n translation for this key

    Examples:

        >>> from travo.i18n import _

        >>> i18n.set('locale', 'en')
        >>> _('hi')
        'Hello'
        >>> _('help', script='foo')
        "Type 'foo' for help"

        >>> i18n.set('locale', 'fr')
        >>> _('hi')
        'Bonjour'
        >>> _('help', script='foo')
        "Tapez «foo» pour de l'aide"
    """
    return typing.cast(str, i18n.t(f"travo.{key}", **kwargs))
