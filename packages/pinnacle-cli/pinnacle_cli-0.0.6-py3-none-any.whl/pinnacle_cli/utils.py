import dotenv
import os
import zipfile
import sys
import subprocess
from pinnacle_cli.constants import env_path

IGNORED_FILES = [".git", ".gitignore", ".env.example", ".DS_Store"]
IGNORED_DIRS = [
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    "dist",
    "build",
    ".metadata",
]


def write_or_update_pinnacle_env(key: str, value: str):
    dotenv.set_key(env_path, key, value)


def create_dependency_zip(requirements_file_path, output_dir):
    print(f"Creating dependencies zip file at {output_dir}/dependencies")
    # Creates a zip file with the dependencies by using the pip install -r requirements.txt command
    if not os.path.isfile(requirements_file_path):
        print(f"No requirements.txt found at {requirements_file_path}. Ignoring.")
        return False

    subprocess.check_call(
        [
            sys.executable,
            "-m",
            "pip",
            "install",
            "--prefer-binary",
            "-r",
            requirements_file_path,
            "-t",
            f"{output_dir}/dependencies",
            "--upgrade",
            "--no-cache-dir",
            "--platform",
            "manylinux2014_x86_64",
            "--no-deps",
        ]
    )

    print(f"Dependencies installed successfully at {output_dir}/dependencies")
    return True


def zip_lambda_function(
    source_dir, zip_file, dependencies_dir, contains_dependencies=False
):
    with zipfile.ZipFile(zip_file, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(source_dir):
            # Ensure that the virtual environment is not included in the zip file
            if "pyvenv.cfg" in files:
                continue
            for file in files:
                if file in IGNORED_FILES:
                    continue

                file_path = os.path.join(root, file)
                relative_path = (
                    "./pinnacle/" if file != ".env" else "./"
                ) + os.path.relpath(file_path, source_dir)
                zf.write(file_path, relative_path)

            # Remove directories that contain a virtual environment
            dirs[:] = [
                d
                for d in dirs
                if "pyvenv.cfg" not in os.listdir(os.path.join(root, d))
                and d not in IGNORED_DIRS
            ]

        if contains_dependencies:
            for root, dirs, files in os.walk(dependencies_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    zf.write(file_path, os.path.relpath(file_path, dependencies_dir))


def attach_dist_files(dist_dir, zip_file):
    # This function is used to attach the files in ./dist_files to the zip file that will be deployed to AWS Lambda.
    with zipfile.ZipFile(zip_file, "a", zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(dist_dir):
            for file in files:
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, dist_dir)
                zf.write(file_path, relative_path)
