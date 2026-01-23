"""
CLI for SkypyDB.

Commands:
- init: generate encryption key + salt and write to .env.local
- dev: start the dashboard for the project database only
"""

from __future__ import annotations

import argparse
import base64
import os
import sys
from typing import Optional

from ..security import EncryptionManager


ENV_FILE_NAME = ".env.local"
DEFAULT_DB_PATH = "./data/skypy.db"
DEFAULT_PORT = 3000


def _write_env_file(
    path: str,
    encryption_key: str,
    salt_b64: str,
    force: bool,
) -> None:
    if os.path.exists(path) and not force:
        print(
            f"[{ENV_FILE_NAME}] already exists. Use --force to overwrite.",
            file=sys.stderr,
        )
        sys.exit(1)

    content = (
        "ENCRYPTION_KEY="
        + encryption_key
        + "\n"
        + "SALT_KEY="
        + salt_b64
        + "\n"
    )
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Created {ENV_FILE_NAME} with ENCRYPTION_KEY and SALT_KEY.")


def cmd_init(args: argparse.Namespace) -> None:
    encryption_key = EncryptionManager.generate_key()
    salt_bytes = EncryptionManager.generate_salt()
    salt_b64 = base64.b64encode(salt_bytes).decode("utf-8")

    env_path = os.path.join(os.getcwd(), ENV_FILE_NAME)
    _write_env_file(env_path, encryption_key, salt_b64, force=args.force)


def cmd_dev(args: argparse.Namespace) -> None:
    if not args.allow_dashboard:
        print("Use --allow-dashboard to start the dashboard.", file=sys.stderr)
        sys.exit(1)

    # Restrict dashboard to the provided project database path.
    os.environ["SKYPYDB_PATH"] = args.path
    os.environ["SKYPYDB_PORT"] = str(args.port)
    os.environ["SKYPYDB_DASHBOARD_FROM_CLI"] = "1"

    try:
        from ..dashboard.dashboard.dashboard import app
    except Exception as exc:
        print(f"Unable to load dashboard app: {exc}", file=sys.stderr)
        sys.exit(1)

    try:
        import uvicorn
    except Exception as exc:
        print(f"Uvicorn is required to run the dashboard: {exc}", file=sys.stderr)
        sys.exit(1)

    print(f"Dashboard is running at http://127.0.0.1:{args.port}")
    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="warning")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="skypydb",
        description="SkypyDB CLI",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser(
        "init",
        help="Generate encryption key and salt into .env.local",
    )
    init_parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing .env.local",
    )
    init_parser.set_defaults(func=cmd_init)

    dev_parser = subparsers.add_parser(
        "dev",
        help="Start the SkypyDB dashboard for the project database only",
    )
    dev_parser.add_argument(
        "--path",
        default=DEFAULT_DB_PATH,
        help=f"Path to the project database (default: [{DEFAULT_DB_PATH}])",
    )
    dev_parser.add_argument(
        "--port",
        type=int,
        default=DEFAULT_PORT,
        help=f"Dashboard port (default: [{DEFAULT_PORT}])",
    )
    dev_parser.add_argument(
        "--allow-dashboard",
        action="store_true",
        help="Required flag to start the dashboard",
    )
    dev_parser.set_defaults(func=cmd_dev)

    return parser


def main(argv: Optional[list[str]] = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
