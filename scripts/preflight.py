#!/usr/bin/env python3
"""
Preflight validation for ChittyOS bundle exports.
Verifies configuration, credentials, and readiness before export.
"""
import argparse
import os
import sys
from pathlib import Path

import yaml


def parse_args():
    p = argparse.ArgumentParser(description="Preflight checks for bundle export")
    p.add_argument("--config", default="chittyos-export.yaml", help="Path to export config YAML")
    p.add_argument("--bundle", help="Specific bundle to check (optional)")
    return p.parse_args()


def load_yaml_config(path: str) -> dict:
    """Load and parse YAML configuration file."""
    try:
        with open(path, "r") as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        print(f"❌ Config file not found: {path}", file=sys.stderr)
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"❌ Invalid YAML in {path}: {e}", file=sys.stderr)
        sys.exit(1)


def check_notion_token() -> bool:
    """Verify NOTION_TOKEN environment variable is set."""
    token = os.getenv("NOTION_TOKEN")
    if not token:
        print("❌ NOTION_TOKEN environment variable not set", file=sys.stderr)
        return False
    if len(token) < 20:
        print("⚠️  NOTION_TOKEN appears too short (< 20 chars)", file=sys.stderr)
        return False
    print("✅ NOTION_TOKEN is set")
    return True


def check_bundle_config(cfg: dict, bundle_key: str = None) -> bool:
    """Validate bundle configuration structure."""
    bundles = cfg.get("export_bundles", {})
    if not bundles:
        print("❌ No 'export_bundles' section in config", file=sys.stderr)
        return False

    keys_to_check = [bundle_key] if bundle_key else list(bundles.keys())
    all_valid = True

    for key in keys_to_check:
        if key not in bundles:
            print(f"❌ Bundle '{key}' not found in config", file=sys.stderr)
            all_valid = False
            continue

        bundle = bundles[key]
        print(f"\n📦 Checking bundle: {key}")

        # Check required fields
        if "name" not in bundle:
            print(f"  ❌ Missing 'name' field", file=sys.stderr)
            all_valid = False
        else:
            print(f"  ✅ Name: {bundle['name']}")

        if "schema_version" not in bundle:
            print(f"  ❌ Missing 'schema_version' field", file=sys.stderr)
            all_valid = False
        else:
            print(f"  ✅ Schema version: {bundle['schema_version']}")

        # Check databases
        databases = bundle.get("databases", [])
        if not databases:
            print(f"  ❌ No databases configured", file=sys.stderr)
            all_valid = False
        else:
            print(f"  ✅ {len(databases)} database(s) configured")

            # Check for TODO URLs
            todo_count = 0
            for db in databases:
                db_key = db.get("key", "unknown")
                notion_url = db.get("notion_url", "")
                if notion_url.startswith("TODO:"):
                    print(f"    ⚠️  Database '{db_key}' has placeholder URL: {notion_url}", file=sys.stderr)
                    todo_count += 1
                else:
                    print(f"    ✅ Database '{db_key}' URL configured")

            if todo_count > 0:
                print(f"  ⚠️  {todo_count} database(s) have TODO URLs (won't export)", file=sys.stderr)

    return all_valid


def check_output_directories(cfg: dict) -> bool:
    """Verify output directories can be created."""
    defaults = cfg.get("defaults", {})
    output_root = defaults.get("output_root", "packages")

    if not Path(output_root).exists():
        print(f"ℹ️  Output directory '{output_root}' doesn't exist yet (will be created)")
    else:
        print(f"✅ Output directory '{output_root}' exists")

    # Check write permissions
    try:
        test_path = Path(output_root)
        test_path.mkdir(parents=True, exist_ok=True)
        test_file = test_path / ".preflight_test"
        test_file.write_text("test")
        test_file.unlink()
        print(f"✅ Write permissions verified for '{output_root}'")
        return True
    except Exception as e:
        print(f"❌ Cannot write to '{output_root}': {e}", file=sys.stderr)
        return False


def main():
    args = parse_args()

    print("🔍 ChittyOS Bundle Export Preflight Check\n")
    print(f"Config: {args.config}")
    if args.bundle:
        print(f"Bundle: {args.bundle}")
    print()

    # Load config
    cfg = load_yaml_config(args.config)

    # Run checks
    checks_passed = True
    checks_passed &= check_notion_token()
    checks_passed &= check_bundle_config(cfg, args.bundle)
    checks_passed &= check_output_directories(cfg)

    print("\n" + "=" * 50)
    if checks_passed:
        print("✅ All preflight checks passed!")
        print("Ready to export bundles.")
        sys.exit(0)
    else:
        print("❌ Some preflight checks failed")
        print("Please fix the issues above before exporting.")
        sys.exit(1)


if __name__ == "__main__":
    main()
