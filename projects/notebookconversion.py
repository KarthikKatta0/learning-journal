#!/usr/bin/env python3
from __future__ import annotations

import argparse
import logging
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Iterable


def check_command(name: str) -> bool:
    return shutil.which(name) is not None


def check_python_package(module: str) -> bool:
    try:
        __import__(module)
        return True
    except ImportError:
        return False


def setup_logger(log_file: Path) -> logging.Logger:
    logger = logging.getLogger("nb_batch_convert")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()

    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

    fh = logging.FileHandler(log_file, encoding="utf-8")
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(formatter)
    logger.addHandler(sh)

    return logger


def dependency_report(target: str) -> tuple[bool, list[str]]:
    errors = []

    if not check_python_package("nbconvert"):
        errors.append("Missing Python package: nbconvert. Install with: pip install nbconvert")

    if not check_command("jupyter"):
        errors.append("Missing command: jupyter. Install with: pip install notebook nbconvert")

    if target == "word" and not check_command("pandoc"):
        errors.append("Missing command: pandoc. Install Pandoc and ensure it is on PATH")

    if target == "pdf":
        if not check_command("pandoc"):
            errors.append("Missing command: pandoc. nbconvert PDF workflows commonly require Pandoc")
        latex_found = any(check_command(cmd) for cmd in ["xelatex", "pdflatex", "tectonic"])
        if not latex_found:
            errors.append(
                "Missing LaTeX engine. Install one of: xelatex, pdflatex, or tectonic"
            )

    return (len(errors) == 0, errors)


def find_notebooks(input_dir: Path, recursive: bool) -> Iterable[Path]:
    pattern = "**/*.ipynb" if recursive else "*.ipynb"
    return sorted(input_dir.glob(pattern))


def run_command(cmd: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, capture_output=True, text=True, check=False)


def convert_notebook(notebook: Path, output_dir: Path, target: str, logger: logging.Logger) -> bool:
    fmt = "webpdf" if target == "pdf" else "markdown"
    logger.info("Starting conversion: %s -> %s", notebook.name, target.upper())

    cmd = [
        sys.executable,
        "-m",
        "jupyter",
        "nbconvert",
        "--to",
        fmt,
        str(notebook),
        "--output-dir",
        str(output_dir),
    ]

    result = run_command(cmd)

    if result.returncode != 0:
        logger.error("nbconvert failed for %s", notebook.name)
        if result.stderr.strip():
            logger.error(result.stderr.strip())
        return False

    if target == "pdf":
        logger.info("Converted successfully: %s", notebook.name)
        return True

    md_file = output_dir / f"{notebook.stem}.md"
    docx_file = output_dir / f"{notebook.stem}.docx"

    if not md_file.exists():
        logger.error("Expected markdown output not found: %s", md_file)
        return False

    pandoc_cmd = ["pandoc", str(md_file), "-o", str(docx_file)]
    pandoc_result = run_command(pandoc_cmd)

    if pandoc_result.returncode != 0:
        logger.error("Pandoc failed for %s", notebook.name)
        if pandoc_result.stderr.strip():
            logger.error(pandoc_result.stderr.strip())
        return False

    logger.info("Converted successfully: %s", notebook.name)
    return True


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Batch-convert Jupyter notebooks (.ipynb) to PDF or Word documents."
    )
    parser.add_argument("input_dir", help="Directory containing .ipynb files")
    parser.add_argument(
        "-o", "--output-dir", default="converted_output", help="Directory for converted files and logs"
    )
    parser.add_argument(
        "-f", "--format", choices=["pdf", "word"], required=True, help="Target output format"
    )
    parser.add_argument(
        "-r", "--recursive", action="store_true", help="Search for notebooks recursively"
    )
    args = parser.parse_args()

    input_dir = Path(args.input_dir).expanduser().resolve()
    output_dir = Path(args.output_dir).expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    log_file = output_dir / "conversion.log"
    logger = setup_logger(log_file)

    logger.info("Batch conversion started")
    logger.info("Input directory: %s", input_dir)
    logger.info("Output directory: %s", output_dir)
    logger.info("Target format: %s", args.format.upper())

    if not input_dir.exists() or not input_dir.is_dir():
        logger.error("Input directory does not exist or is not a directory: %s", input_dir)
        return 1

    deps_ok, dep_errors = dependency_report(args.format)
    if not deps_ok:
        logger.error("Dependency check failed")
        for err in dep_errors:
            logger.error(err)
        return 1

    notebooks = list(find_notebooks(input_dir, args.recursive))
    if not notebooks:
        logger.warning("No .ipynb files found in: %s", input_dir)
        return 0

    success_count = 0
    failure_count = 0

    for notebook in notebooks:
        try:
            ok = convert_notebook(notebook, output_dir, args.format, logger)
            if ok:
                success_count += 1
            else:
                failure_count += 1
        except Exception as exc:
            failure_count += 1
            logger.exception("Unexpected error while converting %s: %s", notebook.name, exc)

    logger.info("Batch conversion finished")
    logger.info("Successful conversions: %d", success_count)
    logger.info("Failed conversions: %d", failure_count)

    return 0 if failure_count == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())