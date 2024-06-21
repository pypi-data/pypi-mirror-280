"""Synchronizes requirements and hatch pyproject."""

import logging

import subprocess
import sys
from pathlib import Path

import click
import requests
import tomlkit
import tomlkit.container


def get_latest_version(package_name):
    """Gets the latest version of the specified package from PyPI.

    Args:
        package_name (str): The name of the package to fetch the latest version for.

    Returns:
        str or None: The latest version of the package, or None if not found or on error.
    """
    try:
        response = requests.get(f"https://pypi.org/pypi/{package_name}/json")
        response.raise_for_status()  # Raises stored HTTPError, if one occurred.
        data = response.json()
        releases = data.get("releases", {})
        if releases:
            filtered_versions = [version for version in releases if all(part.isdigit() for part in version.split("."))]
            sorted_versions = sorted(filtered_versions, key=lambda x: tuple(map(int, x.split("."))), reverse=True)
            return sorted_versions[0] if sorted_versions else None
    except Exception:
        logging.warning(f"Failed to fetch the latest version of {package_name}.")
    return None


def modify_requirements(package_name, package_version=None, action="install") -> None:
    """Modify the requirements.txt file to install or uninstall a package.

    Args:
        package_name (str): The name of the package to install or uninstall.
        package_version (str, optional): The version of the package to install. Defaults to None.
        action (str): The action to perform, either 'install' or 'uninstall'.

    Raises:
        FileNotFoundError: If the requirements.txt file does not exist when attempting to read.
    """
    try:
        with open("requirements.txt") as f:
            lines = f.readlines()
    except FileNotFoundError:
        logging.warning("requirements.txt file not found, creating a new file.")
        lines = []

    # Filter out comments and empty lines
    lines = [line.strip() for line in lines if line.strip() and not line.strip().startswith("#")]

    # Extract the base package name and optional extras
    base_package_name, *extras = package_name.split("[")
    extras_str = "[" + ",".join(extras) if extras else ""
    package_line = next((line for line in lines if base_package_name == line.split("[")[0].split("==")[0]), None)

    if action == "install" and package_version:
        new_line = f"{base_package_name}{extras_str}=={package_version}"
        if package_line:
            # Replace the line with the same base package name
            lines = [line if base_package_name != line.split("[")[0].split("==")[0] else new_line for line in lines]
        else:
            lines.append(new_line)

    elif action == "uninstall":
        # Remove lines with the same base package name
        lines = [line for line in lines if base_package_name != line.split("[")[0].split("==")[0]]

    # Ensure each line ends with a newline character
    lines = [line + "\n" for line in lines]

    with open("requirements.txt", "w") as f:
        f.writelines(lines)


def format_pyproject_toml(pyproject: tomlkit.TOMLDocument) -> str:
    """Formats the pyproject.toml content to be written back to the file.

    Args:
        pyproject (dict): The modified pyproject content.

    Returns:
        str: The formatted pyproject.toml content.
    """
    content = tomlkit.dumps(pyproject)
    lines = content.splitlines()
    
    
    # lines = [line[:88].removesuffix(',').removeprefix(',') + ", \n" + line[88:].removeprefix(',').removesuffix(',') + "," if len(line) > 88 and not line.startswith('[') and not line.startswith('[') else line for line in lines]
    return "\n".join(lines)

def write_pyproject_toml(pyproject: tomlkit.TOMLDocument, filepath="pyproject.toml") -> None:
    """Writes the modified content back to the pyproject.toml file. Splits lines at 88 characters with comma delimiters.

    Args:
        pyproject (dict): The modified pyproject content.
        filepath (str, optional): The path to the pyproject.toml file. Defaults to "pyproject.toml".
    """
    with Path(filepath).open("w") as f:
        for line in format_pyproject_toml(pyproject).splitlines():
            f.write(line + "\n")

def modify_dependencies(dependencies, package_version_str, action):
    """Modify the dependencies list for installing or uninstalling a package.

    Args:
        dependencies (list): List of current dependencies.
        package_version_str (str): Package with version string.
        action (str): Action to perform, either 'install' or 'uninstall'.

    Returns:
        list: Modified list of dependencies.
    """
    if action == "install" and package_version_str not in dependencies:
        dependencies.append(package_version_str)
    elif action == "uninstall" and package_version_str in dependencies:
        dependencies.remove(package_version_str)
    return dependencies


def modify_optional_dependencies(optional_dependencies: dict, package_version_str, action, dependency_group):
    """Modify the optional dependencies for installing or uninstalling a package.

    Args:
        optional_dependencies (dict): Dictionary of optional dependencies groups.
        package_version_str (str): Package with version string.
        action (str): Action to perform, either 'install' or 'uninstall'.
        dependency_group (str): The group of optional dependencies to modify.

    Returns:
        dict: Modified dictionary of optional dependencies.
    """
    group_dependencies = optional_dependencies.get(dependency_group, [])
    all_group = optional_dependencies.setdefault("all", [])

    if action == "install":
        if package_version_str not in group_dependencies:
            group_dependencies.append(package_version_str)
        if package_version_str not in all_group:
            all_group.append(package_version_str)
    elif action == "uninstall":
        if package_version_str in group_dependencies:
            group_dependencies.remove(package_version_str)
        if package_version_str in all_group:
            all_group.remove(package_version_str)

    optional_dependencies[dependency_group] = group_dependencies
    optional_dependencies["all"] = all_group
    return optional_dependencies


def modify_pyproject_toml(
    package_name,
    package_version="",
    action="install",
    hatch_env=None,
    dependency_group="dependencies",
) -> None:
    """Modify the pyproject.toml file to update dependencies based on action.

    Args:
        package_name (str): The name of the package to install or uninstall.
        package_version (str, optional): The version of the package. Defaults to "".
        action (str): The action to perform, either 'install' or 'uninstall'.
        hatch_env (str, optional): The Hatch environment to use. Defaults to None.
        dependency_group (str, optional): The group of dependencies to modify. Defaults to "dependencies".
    """
    is_optional = dependency_group != "dependencies"
    pyproject: tomlkit.TOMLDocument = tomlkit.parse(Path("pyproject.toml").read_text()) 
    logging.debug(f"pyproject: {pyproject}, package_name: {package_name}, package_version: {package_version}, action: {action}, hatch_env: {hatch_env}, dependency_group: {dependency_group}")

    package_version_str = f"{package_name}{('==' + package_version) if package_version else ''}"
    is_hatch_env =  hatch_env and  "tool" in pyproject and "hatch" in pyproject["tool"] and hatch_env in pyproject["tool"]["hatch"]["envs"]
    
    if is_optional:
        optional_dependencies = pyproject.get("project", {}).get("optional-dependencies", {})
        pyproject["project"].setdefault("optional-dependencies",modify_optional_dependencies(
            optional_dependencies,
            package_version_str,
            action,
            dependency_group,
        ))
    elif is_hatch_env:
        dependencies = pyproject["tool"]["hatch"]["envs"][hatch_env].get("dependencies", tomlkit.array())
    else:
        dependencies = pyproject.get("project", {}).get("dependencies", tomlkit.array())
        pyproject["project"].setdefault("dependencies", modify_dependencies(dependencies, package_version_str, action))
        optional_dependencies = pyproject.get("project", {}).get("optional-dependencies", {})
        pyproject["project"].setdefault("optional-dependencies",
                                        modify_optional_dependencies(
                                            optional_dependencies, package_version_str, action, dependency_group))
    write_pyproject_toml(pyproject)



@click.group(invoke_without_command=True)
@click.pass_context
@click.option("--hatch-env", default=None, help="Specify the Hatch environment to use")
@click.option("--verbose", is_flag=True, help="Enable verbose output")
def cli(ctx, hatch_env, verbose):
    """Main CLI entry point. If no subcommand is provided, it shows the dependencies.

    Args:
        ctx (click.Context): Click context object.
        hatch_env (str, optional): The Hatch environment to use. Defaults to "default".
    """
    logging.basicConfig(level=logging.DEBUG, force=True) if verbose else None
    if ctx.invoked_subcommand is None:
        show_command(hatch_env)



def get_pip_freeze():
    """Get the list of installed packages as a set.

    Returns:
        set: Set of installed packages with their versions.
    """
    result = subprocess.run([sys.executable, "-m", "pip", "freeze"], stdout=subprocess.PIPE, check=False)
    return set(result.stdout.decode().splitlines())




@cli.command("install")
@click.argument("packages", nargs=-1)
@click.option(
    "-r", "--requirements", type=click.Path(exists=True), help="Install packages from the given requirements file",
)
@click.option("-U", "--upgrade", is_flag=True, help="Upgrade the package(s)")
@click.option("-e", "--editable", is_flag=True, help="Install a package in editable mode")
@click.option("--hatch-env", default=None, help="Specify the Hatch environment to use")
@click.option("-g", "--dependency-group", default="dependencies", help="Specify the dependency group to use")
def install_command(packages, requirements, upgrade, editable, hatch_env, dependency_group) -> None:
    """Install packages and update requirements.txt and pyproject.toml accordingly.

    Args:
        packages (tuple): Packages to install.
        requirements (str, optional): Path to requirements file. If provided, install packages from this file.
        upgrade (bool, optional): Whether to upgrade the packages. Defaults to False.
        editable (bool, optional): Whether to install a package in editable mode. Defaults to False.
        hatch_env (str, optional): The Hatch environment to use. Defaults to "default".
        dependency_group (str, optional): The dependency group to use. Defaults to "dependencies".
    """
    try:
        if requirements:
            with open(requirements) as f:
                packages = [line.strip() for line in f if line.strip() and not line.startswith("#")]

        initial_packages = get_pip_freeze()

        for package in packages:
            package_install_cmd = [sys.executable, "-m", "pip", "install"]
            if editable:
                package_install_cmd.append("-e")
            if upgrade:
                package_install_cmd.append("-U")
            package_install_cmd.append(package)
            subprocess.check_call(package_install_cmd)

            # Determine the newly installed package by comparing pip freeze output
            final_packages = get_pip_freeze()
            new_packages = final_packages - initial_packages
            if new_packages:
                for new_package in new_packages:
                    package_name_maybe_version = new_package.split("==")
                    package_name = package_name_maybe_version[0]
                    package_version = package_name_maybe_version[1] if len(package_name_maybe_version) > 1 else get_latest_version(package_name)
                    
                    modify_requirements(package_name,package_version, action="install")
                    modify_pyproject_toml(package_name, package_version, hatch_env=hatch_env, action="install", dependency_group=dependency_group)
            else:
                package_name_maybe_version = package.split("==")
                package_name = package_name_maybe_version[0]
                package_version = package_name_maybe_version[1] if len(package_name_maybe_version) > 1 else get_latest_version(package_name)
                
                modify_pyproject_toml(package_name,package_version, action="install", hatch_env=hatch_env,dependency_group=dependency_group)
                modify_requirements(package_name,package_version, action="install")
    except subprocess.CalledProcessError as e:
        click.echo(f"Error: Failed to install {package}.", err=True)
        click.echo(f"Reason: {e}", err=True)
        sys.exit(e.returncode)


@cli.command("format")
def format_command() -> None:
    """Format the pyproject.toml file to split lines at 88 characters."""
    try:
        pyproject = tomlkit.parse(Path("pyproject.toml").read_text())
        write_pyproject_toml(pyproject)
    except Exception as e:
        click.echo(f"Error: Failed to format pyproject.toml.", err=True)
        click.echo(f"Reason: {e}", err=True)
        sys.exit(1)

def is_package_in_requirements(package_name) -> bool:
    """Check if a package is listed in the requirements.txt file.

    Args:
        package_name (str): The name of the package.

    Returns:
        bool: True if the package is listed in requirements.txt, False otherwise.
    """

    Path("requirements.txt").touch()
    
    return any(line.strip().startswith(package_name) for line in Path("requirements.txt").read_text().splitlines())


def is_package_in_pyproject(package_name, hatch_env=None, dependency_group="dependencies") -> bool:
    """Check if a package is listed in the pyproject.toml file for a given Hatch environment.

    Args:
        package_name (str): The name of the package.
        hatch_env (str): The Hatch environment to check in. Defaults to "default".

    Returns:
        bool: True if the package is listed in pyproject.toml, False otherwise.
    """
    if not Path("pyproject.toml").exists():
        return False
    with open("pyproject.toml") as f:
        content = f.read()
        pyproject = tomlkit.parse(content)
    if dependency_group == "dependencies" and not hatch_env:
        deps = pyproject["project"]["dependencies"]
    elif "tool" in pyproject and "hatch" in pyproject["tool"]:
        deps = pyproject["tool"]["hatch"]["envs"][hatch_env].get("dependencies", [])
    else:
     deps = pyproject.get("project", {}).get("optional-dependencies", {}).get(dependency_group, [])
     deps += pyproject.get("project", {}).get("optional-dependencies", {}).get("all", [])
     
    return any(package_name in dep for dep in deps)


@cli.command("uninstall")
@click.argument("packages", nargs=-1)
@click.option("--hatch-env", default=None, help="Specify the Hatch environment to use")
def uninstall_command(packages, hatch_env) -> None:
    """Uninstall packages and update requirements.txt and pyproject.toml accordingly.

    Args:
        packages (tuple): Packages to uninstall.
        hatch_env (str, optional): The Hatch environment to use. Defaults to "default".
    """
    for package in packages:
        package_name = package.split("==")[0].split("[")[0]  # Handle extras
        in_requirements = is_package_in_requirements(package_name)
        in_pyproject = is_package_in_pyproject(package_name, hatch_env)

        if not in_requirements and not in_pyproject:
            click.echo(f"Package '{package_name}' is not listed in requirements.txt or pyproject.toml, skipping.")
            continue

        try:
            subprocess.check_call([sys.executable, "-m", "pip", "uninstall", package_name, "-y"])
            modify_requirements(package_name, action="uninstall")
            modify_pyproject_toml(package_name, action="uninstall", hatch_env=hatch_env)
            click.echo(f"Successfully uninstalled {package_name}")
        except subprocess.CalledProcessError as e:
            click.echo(f"Error: Failed to uninstall {package_name}.", err=True)
            click.echo(f"Reason: {e}", err=True)
            sys.exit(e.returncode)
        except Exception as e:
            click.echo(f"Unexpected error occurred while trying to uninstall {package_name}:", err=True)
            click.echo(f"{e}", err=True)
            sys.exit(1)


@cli.command("show")
@click.option("--hatch-env", default="default", help="Specify the Hatch environment to use")
def show_command(hatch_env) -> None:
    """Show the dependencies from the pyproject.toml file.

    Args:
        hatch_env (str, optional): The Hatch environment to use. Defaults to "default".
    """
    try:
        with open("pyproject.toml") as f:
            content = f.read()
            pyproject = tomlkit.parse(content)

        # Determine if we are using Hatch or defaulting to project dependencies
        if "tool" in pyproject and "hatch" in pyproject["tool"]:
            dependencies = pyproject["tool"]["hatch"]["envs"][hatch_env]["dependencies"]
        else:
            dependencies = pyproject.get("project", {}).get("dependencies", [])

        for _dep in dependencies:
            pass
    except FileNotFoundError:
        pass
    except Exception:
        pass



