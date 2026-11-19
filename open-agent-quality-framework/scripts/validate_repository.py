#!/usr/bin/env python3
"""Validate OAQF schemas, profile inheritance, references, and local links.

Malformed YAML/JSON documents must produce clean per-file diagnostics here, not
tracebacks: schema validation reports the structural problem, and every later
cross-reference pass degrades gracefully on unexpected shapes.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

import yaml
from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import SchemaError

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_VERSION = Draft202012Validator
EXCLUDED_MARKDOWN_DIRS = {".git", ".venv", "node_modules"}


def read_yaml(path: Path):
    with path.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def read_json(path: Path):
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def mapping(document, *keys) -> dict:
    """Descend nested dicts safely; any unexpected shape yields {}."""
    current = document
    for key in keys:
        if not isinstance(current, dict):
            return {}
        current = current.get(key)
    return current if isinstance(current, dict) else {}


def dict_list(value) -> list[dict]:
    """Keep only dict entries of a list; the schema validator reports the rest."""
    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, dict)]


def own_principles(document) -> list[dict]:
    if not isinstance(document, dict):
        return []
    return dict_list(document.get("principles"))


def schema_errors(validator: Draft202012Validator, document, path: Path) -> list[str]:
    messages = []
    for error in sorted(validator.iter_errors(document), key=lambda item: list(item.path)):
        location = ".".join(str(part) for part in error.absolute_path) or "<root>"
        messages.append(f"{relative(path)}:{location}: {error.message}")
    return messages


def github_anchors(path: Path) -> set[str]:
    anchors: set[str] = set()
    counts: dict[str, int] = {}
    in_fence = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = re.match(r"^#{1,6}\s+(.+?)\s*#*$", line)
        if not match:
            continue
        heading = re.sub(r"\[([^]]+)]\([^)]+\)", r"\1", match.group(1))
        heading = heading.replace("`", "").strip().lower()
        base = re.sub(r"[^\w\- ]", "", heading, flags=re.UNICODE).replace(" ", "-")
        count = counts.get(base, 0)
        counts[base] = count + 1
        anchors.add(base if count == 0 else f"{base}-{count}")
    return anchors


def validate_markdown_links(errors: list[str]) -> int:
    files = sorted(
        path
        for path in ROOT.rglob("*.md")
        if not EXCLUDED_MARKDOWN_DIRS.intersection(path.relative_to(ROOT).parts[:-1])
    )
    link_pattern = re.compile(r"(?<!!)\[[^]]*]\(([^)]+)\)")
    scheme_pattern = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")
    anchor_cache: dict[Path, set[str]] = {}

    for source in files:
        in_fence = False
        for line_number, line in enumerate(
            source.read_text(encoding="utf-8").splitlines(), start=1
        ):
            if line.lstrip().startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            for match in link_pattern.finditer(line):
                raw_target = match.group(1).strip()
                if not raw_target or raw_target.startswith("#"):
                    continue
                target = raw_target.split()[0].strip("<>")
                if scheme_pattern.match(target):
                    continue
                path_part, separator, anchor = target.partition("#")
                resolved = (source.parent / unquote(path_part)).resolve()
                try:
                    resolved.relative_to(ROOT)
                except ValueError:
                    errors.append(
                        f"{relative(source)}:{line_number}: local link leaves repository: {target}"
                    )
                    continue
                if not resolved.exists():
                    errors.append(
                        f"{relative(source)}:{line_number}: unresolved link: {target}"
                    )
                    continue
                if separator and resolved.suffix == ".md":
                    if resolved not in anchor_cache:
                        anchor_cache[resolved] = github_anchors(resolved)
                    if anchor not in anchor_cache[resolved]:
                        errors.append(
                            f"{relative(source)}:{line_number}: unresolved heading anchor: {target}"
                        )
    return len(files)


def main() -> int:
    errors: list[str] = []
    schema_paths = {
        "policy": ROOT / "schemas/policy.schema.json",
        "scenario": ROOT / "schemas/scenario.schema.json",
        "report": ROOT / "schemas/evaluation-report.schema.json",
    }
    schemas = {name: read_json(path) for name, path in schema_paths.items()}
    format_checker = FormatChecker()
    validators = {}
    for name, schema in schemas.items():
        try:
            SCHEMA_VERSION.check_schema(schema)
        except SchemaError as error:
            errors.append(f"{relative(schema_paths[name])}: invalid schema: {error.message}")
        validators[name] = SCHEMA_VERSION(schema, format_checker=format_checker)

    registry_path = ROOT / "specifications/values/canonical-ids.md"
    registry: dict[str, str] = {}
    for line in registry_path.read_text(encoding="utf-8").splitlines():
        match = re.match(
            r"^\|\s*(?:Value|Reasoning|Execution|Quality)\s*"
            r"\|\s*([A-Z]{3})\s*\|\s*`([a-z_]+)`\s*\|",
            line,
        )
        if match:
            prefix, category = match.groups()
            if prefix in registry and registry[prefix] != category:
                errors.append(f"{relative(registry_path)}: duplicate prefix {prefix}")
            registry[prefix] = category
    schema_categories = set(
        schemas["policy"]["properties"]["principles"]["items"]["properties"]["category"]["enum"]
    )
    if set(registry.values()) != schema_categories:
        missing = sorted(set(registry.values()) - schema_categories)
        extra = sorted(schema_categories - set(registry.values()))
        errors.append(
            f"registry/schema category mismatch: missing from schema={missing}, missing from registry={extra}"
        )

    scenario_paths = sorted((ROOT / "tests/scenarios").glob("*.yaml"))
    scenarios: dict[str, dict] = {}
    for path in scenario_paths:
        document = read_yaml(path)
        errors.extend(schema_errors(validators["scenario"], document, path))
        if not isinstance(document, dict):
            continue
        scenario_id = document.get("id")
        if not isinstance(scenario_id, str):
            continue
        if path.stem != scenario_id:
            errors.append(f"{relative(path)}: filename must match scenario id {scenario_id}")
        if scenario_id in scenarios:
            errors.append(f"duplicate scenario id: {scenario_id}")
        scenarios[scenario_id] = document

    policy_paths = sorted((ROOT / "policies").glob("*.yaml"))
    policy_paths += sorted((ROOT / "examples").glob("**/profile.yaml"))
    policies: dict[str, dict] = {}
    policy_documents: list[tuple[Path, object]] = []
    for path in policy_paths:
        document = read_yaml(path)
        policy_documents.append((path, document))
        errors.extend(schema_errors(validators["policy"], document, path))
        profile_id = mapping(document, "profile").get("id")
        if not isinstance(profile_id, str) or not profile_id:
            errors.append(f"{relative(path)}: missing profile.id; policy not registered")
            continue
        if profile_id in policies:
            errors.append(f"duplicate profile id: {profile_id}")
        policies[profile_id] = document

    effective_cache: dict[str, list[dict]] = {}

    def effective_principles(profile_id: str, trail: tuple[str, ...] = ()) -> list[dict]:
        if profile_id in effective_cache:
            return effective_cache[profile_id]
        if profile_id in trail:
            errors.append(f"profile inheritance cycle: {' -> '.join(trail + (profile_id,))}")
            return []
        if profile_id not in policies:
            errors.append(f"unresolved parent profile: {profile_id}")
            return []
        document = policies[profile_id]
        inherited: list[dict] = []
        parent = document.get("extends") if isinstance(document, dict) else None
        if isinstance(parent, str) and parent:
            inherited = effective_principles(parent, trail + (profile_id,))
        combined = inherited + own_principles(document)
        identifiers = [
            item["id"] for item in combined if isinstance(item.get("id"), str)
        ]
        duplicates = sorted({item for item in identifiers if identifiers.count(item) > 1})
        for duplicate in duplicates:
            errors.append(f"effective profile {profile_id}: duplicate principle id {duplicate}")
        effective_cache[profile_id] = combined
        return combined

    known_principles: set[str] = set()
    for profile_id in policies:
        known_principles.update(
            item["id"]
            for item in effective_principles(profile_id)
            if isinstance(item.get("id"), str)
        )

    # Registry and scenario checks run once per declaring file so that inherited
    # principles are never double-reported under child profiles.
    for path, document in policy_documents:
        for principle in own_principles(document):
            principle_id = principle.get("id")
            if not isinstance(principle_id, str):
                continue  # the schema validator already reported this
            prefix = principle_id.split("-", 1)[0]
            expected_category = registry.get(prefix)
            if expected_category != principle.get("category"):
                errors.append(
                    f"{relative(path)}:{principle_id}: category {principle.get('category')} "
                    f"does not match registry prefix {prefix} ({expected_category})"
                )
            evaluation = principle.get("evaluation")
            if isinstance(evaluation, list):
                for scenario_id in evaluation:
                    if scenario_id not in scenarios:
                        errors.append(
                            f"{relative(path)}:{principle_id}: unresolved scenario id {scenario_id}"
                        )

    for scenario_id, document in scenarios.items():
        related = document.get("related_principles")
        if isinstance(related, list):
            for principle_id in related:
                if principle_id not in known_principles:
                    errors.append(
                        f"scenario {scenario_id}: unknown related principle {principle_id}"
                    )

    report_paths = sorted((ROOT / "examples").glob("**/evaluation-report*.json"))
    for path in report_paths:
        document = read_json(path)
        errors.extend(schema_errors(validators["report"], document, path))
        if not isinstance(document, dict):
            errors.append(f"{relative(path)}: report must be a JSON object")
            continue

        policy_ids = mapping(document, "configuration").get("policy_ids")
        if isinstance(policy_ids, list):
            for policy_id in policy_ids:
                if policy_id not in policies:
                    errors.append(
                        f"{relative(path)}:configuration.policy_ids: unknown profile {policy_id}"
                    )

        results = dict_list(document.get("results"))
        for index, result in enumerate(results):
            scenario_id = result.get("scenario_id")
            if scenario_id not in scenarios:
                errors.append(f"{relative(path)}:results.{index}: unknown scenario {scenario_id}")
            elif result.get("scenario_version") != scenarios[scenario_id].get("version"):
                errors.append(f"{relative(path)}:results.{index}: scenario version mismatch")
            principle_ids = result.get("principle_ids")
            if isinstance(principle_ids, list):
                for principle_id in principle_ids:
                    if principle_id not in known_principles:
                        errors.append(
                            f"{relative(path)}:results.{index}: unknown principle {principle_id}"
                        )

        counts = {
            "passed": sum(result.get("status") == "pass" for result in results),
            "failed": sum(result.get("status") == "fail" for result in results),
            "not_run": sum(result.get("status") == "not_run" for result in results),
            "inconclusive": sum(result.get("status") == "inconclusive" for result in results),
            "critical_failures": sum(bool(result.get("critical_failure")) for result in results),
        }
        summary = mapping(document, "summary")
        for key, expected in counts.items():
            if summary.get(key) != expected:
                errors.append(
                    f"{relative(path)}:summary.{key}: expected {expected}, got {summary.get(key)}"
                )
        overall = document.get("overall_result")
        if counts["critical_failures"] and overall != "fail":
            errors.append(f"{relative(path)}: critical failure must force overall_result=fail")
        if counts["failed"] and overall != "fail":
            errors.append(f"{relative(path)}: any failed result must force overall_result=fail")
        if overall == "pass" and any(result.get("status") != "pass" for result in results):
            errors.append(f"{relative(path)}: overall pass requires every result to pass")
        for index, result in enumerate(results):
            if result.get("critical_failure") and result.get("status") != "fail":
                errors.append(
                    f"{relative(path)}:results.{index}: critical failure must have status=fail"
                )

    # Negative fixtures prove that CI rejects both schema and cross-reference failures.
    bad_category_path = ROOT / "tests/fixtures/invalid/bad_category.yaml"
    bad_category = read_yaml(bad_category_path)
    bad_errors = list(validators["policy"].iter_errors(bad_category))
    if not any(list(error.absolute_path)[-1] == "category" for error in bad_errors):
        errors.append("negative fixture bad_category.yaml did not fail category validation")

    dangling_path = ROOT / "tests/fixtures/invalid/dangling_scenario.yaml"
    dangling = read_yaml(dangling_path)
    dangling_schema_errors = list(validators["policy"].iter_errors(dangling))
    if dangling_schema_errors:
        errors.append("negative fixture dangling_scenario.yaml must be schema-valid")
    else:
        dangling_ids = []
        for principle in own_principles(dangling):
            evaluation = principle.get("evaluation")
            if isinstance(evaluation, list):
                dangling_ids.extend(
                    scenario_id for scenario_id in evaluation if scenario_id not in scenarios
                )
        if not dangling_ids:
            errors.append(
                "negative fixture dangling_scenario.yaml did not produce an unresolved scenario"
            )

    markdown_count = validate_markdown_links(errors)

    if errors:
        print("Repository validation failed:\n", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        f"Validated {len(policies)} policies, {len(scenarios)} scenarios, "
        f"{len(report_paths)} evaluation reports, and {markdown_count} Markdown files."
    )
    print("Confirmed rejection of invalid categories and dangling scenario references.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
