import re
import os
import sys
from typing import Union, List
from bole.config import CascadingConfig, CascadingConfigDictionary, config_file_parser
from yapenv.consts import YAPENV_CONFIG_FILES
from yapenv.utils import resolve_path


REQUIREMENTS_COLLECTION_NAME = "requirements"


class YAPENVConfigRequirement(CascadingConfigDictionary):
    @property
    def package(self) -> str:
        """The name of the package to require"""
        return self.get("package", None)

    @package.setter
    def package(self, val: str):
        self["package"] = val

    @property
    def import_path(self) -> str:
        """A path to a requirements file to import (relative to config root)"""
        return self.get("import", None)

    @classmethod
    def parse(cls, val: Union[str, dict, List[dict]]):
        if isinstance(val, str):
            val = {"package": val}
        return super().parse(val)

    @classmethod
    def unique(cls, requirements: List[Union["YAPENVConfigRequirement", dict]]):
        """Removes duplicate requirements and validates a requirement list."""
        requirements = [YAPENVConfigRequirement.parse(r) for r in requirements]
        requirements.reverse()
        cleaned = []
        matched = set()
        for r in requirements:
            if r.import_path is not None:
                pkg_name = "import: " + r.import_path
            else:
                pkg_name = re.match(r"^[\w._-]+", r.package.strip())
                if pkg_name is None:
                    pkg_name = r.package
                else:
                    pkg_name = pkg_name[0]
            if pkg_name in matched:
                continue
            matched.add(pkg_name)
            cleaned.append(r)

        cleaned.reverse()

        return cleaned


class YAPENVConfig(CascadingConfig):
    RESOLVE_PATH_KEYS = [
        "pip_config_path",
        "env_file",
    ]
    """A collection of configuration keys to resolve as paths. The resolve will be called relative
    to the location of the config file.
    """

    @property
    def env_file(self) -> str:
        return self.get("env_file", ".env")

    @property
    def pip_install_args(self) -> List[str]:
        return self.get("pip_install_args", [])

    @property
    def virtualenv_args(self) -> List[str]:
        return self.get("virtualenv_args", [])

    @property
    def venv_directory(self) -> str:
        """The path of the virtual env directory"""
        return self.get("venv_directory", ".venv")

    @property
    def venv_path(self) -> str:
        """The path to the virtual environment"""
        if os.path.isabs(self.venv_directory):
            return self.venv_directory
        return os.path.abspath(os.path.join(self.source_directory, self.venv_directory))

    @property
    def venv_local_folder_path(self) -> str:
        """The path to the virtual environment"""
        return os.path.join(os.path.join(self.venv_path, "local"))

    @property
    def pip_config_path(self) -> str:
        return self.get("pip_config_path", None)

    @property
    def python_version(self) -> str:
        return self.get(
            "python_version", f"{sys.version_info.major}.{sys.version_info.minor}"
        )

    @python_version.setter
    def python_version(self, val: str):
        self["python_version"] = val

    @property
    def python_executable(self) -> str:
        """The path to the python executable to use"""
        return self.get("python_executable", None)

    @property
    def requirements(self) -> List[YAPENVConfigRequirement]:
        """A list of pip requirements"""
        self[REQUIREMENTS_COLLECTION_NAME] = YAPENVConfigRequirement.parse_list(
            self.get(REQUIREMENTS_COLLECTION_NAME, [])
        )
        return self[REQUIREMENTS_COLLECTION_NAME]

    def has_virtual_environment(self) -> dict:
        """True if a virtual environment exists"""
        return os.path.isdir(self.venv_path)

    def resolve_from_venv_directory(self, *parts: List[str]):
        """Resolve path with the virtual env directory as root path"""
        return resolve_path(
            *parts,
            root_directory=self.venv_local_folder_path
            if os.path.exists(
                self.venv_local_folder_path
            )  # Case where local path exists
            else self.venv_path,
        )

    def resolve_from_venv_bin_directory(self, *parts: List[str]):
        """Resolves a script from the bin directory"""
        possible_bin_folders = ["bin", "Scripts"]
        bin_fldr = None
        for fldr in possible_bin_folders:
            if os.path.exists(self.resolve_from_venv_directory(fldr)):
                bin_fldr = fldr
                break
        assert bin_fldr is not None, FileNotFoundError(
            f"Bin folder was not found (searched for {possible_bin_folders})"
        )
        return self.resolve_from_venv_directory(bin_fldr, *parts)

    def resolve_from_source_directory(self, *parts: List[str]):
        """Resolve path with the source directory as root path"""
        return resolve_path(*parts, root_directory=self.source_directory)

    def initialize(self, environment: str = None):
        super().initialize(environment)

        for key in self.RESOLVE_PATH_KEYS:
            if isinstance(self.get(key, None), str):
                self[key] = self.resolve_from_source_directory(self[key])

        # Resolve the requirement for absolute imports. This is to allow
        # requirements to have the proper relative path to the source.
        for requirement in self.requirements:
            if requirement.import_path is not None:
                requirement["import"] = self.resolve_from_source_directory(
                    requirement.import_path
                )

    def load_requirements(self):
        """Resolves and loads the internal requirement imports and cleans up the requirements list"""
        if len(self.requirements) == 0:
            return []

        resolved_requirements = []
        for req in self.requirements:
            if req.import_path is not None:
                abs_import_path = os.path.abspath(
                    self.resolve_from_source_directory(req.import_path)
                )

                if os.path.isfile(abs_import_path):
                    with open(abs_import_path, "r", encoding="utf-8") as req_file:
                        requirements_raw = req_file.read()

                    # Clean comments
                    requirements_raw = re.sub(r"[#].*", "", requirements_raw)
                    for req_as_str in requirements_raw.split("\n"):
                        req_as_str = req_as_str.strip()
                        if len(req_as_str) == 0:
                            continue
                        resolved_requirements.append(
                            YAPENVConfigRequirement.parse(req_as_str)
                        )

            elif req.package is not None:
                resolved_requirements.append(req)

        self[REQUIREMENTS_COLLECTION_NAME] = resolved_requirements
        self.clean_requirements()

    def load_virtualenv(self):
        """Loads the virtual environment into python (using activate.py)."""
        import importlib.util

        import_path = self.resolve_from_venv_bin_directory("activate_this.py")
        assert os.path.isfile(import_path), (
            "Virtual env not found or virtualenv invalid @ " + self.venv_path
        )
        spec = importlib.util.spec_from_file_location(
            re.sub(r"[^\w]+", "_", import_path), import_path
        )
        foo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(foo)

    def clean_requirements(self):
        """Clean the requirement list for all environments and remove duplicates"""
        requirement_configs = [self, *self.environments.values()]

        # Resolve to relative the base path keys
        for key in self.RESOLVE_PATH_KEYS:
            if isinstance(self.get(key, None), str):
                self[key] = os.path.relpath(self[key], self.source_directory)

        # First resolve to relative
        req_config: YAPENVConfig = None
        for req_config in requirement_configs:
            if REQUIREMENTS_COLLECTION_NAME in req_config:
                for requirement in req_config.requirements:
                    if requirement.import_path is not None and os.path.isabs(
                        requirement.import_path
                    ):
                        requirement["import"] = os.path.relpath(
                            requirement.import_path, self.source_directory
                        )

        # Now remove duplicates
        for req_config in requirement_configs:
            if REQUIREMENTS_COLLECTION_NAME in req_config:
                req_config[
                    REQUIREMENTS_COLLECTION_NAME
                ] = YAPENVConfigRequirement.unique(req_config.requirements)

    @classmethod
    def load(
        cls,
        src: str,
        environment: str = None,
        max_inherit_depth: int = -1,
        load_imports: bool = True,
        search_paths: List[str] = YAPENV_CONFIG_FILES,
        parse_config=config_file_parser,
        clean_requirements: bool = True,
    ):
        max_inherit_depth = max_inherit_depth if max_inherit_depth is not None else -1
        config = super().load(
            src,
            environment,
            max_inherit_depth,
            load_imports,
            search_paths,
            parse_config,
        )

        if clean_requirements:
            config.clean_requirements()

        return config
