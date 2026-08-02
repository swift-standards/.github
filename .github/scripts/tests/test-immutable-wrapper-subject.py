#!/usr/bin/env python3
"""Structural controls for the Standards layer wrapper CI subjects."""

from __future__ import annotations

from pathlib import Path
import unittest


ROOT = Path(__file__).parents[3]
WORKFLOWS = (
    ROOT / ".github/workflows/swift-ci.yml",
    ROOT / ".github/workflows/swift-docs.yml",
)
TARGET_REPOSITORY = (
    "target-repo: ${{ github.event_name == 'pull_request' && "
    "github.event.pull_request.head.repo.full_name || github.repository }}"
)
TARGET_REF = (
    "ref: ${{ github.event_name == 'pull_request' && "
    "github.event.pull_request.head.sha || github.sha }}"
)


def findings(source: str) -> list[str]:
    result: list[str] = []
    if TARGET_REPOSITORY not in source:
        result.append("missing immutable PR-head/push repository binding")
    if TARGET_REF not in source:
        result.append("missing immutable PR-head/push SHA binding")
    return result


class ImmutableWrapperSubjectTests(unittest.TestCase):
    def test_every_wrapper_binds_the_immutable_subject(self) -> None:
        for workflow in WORKFLOWS:
            with self.subTest(workflow=workflow.name):
                self.assertEqual(findings(workflow.read_text()), [])

    def test_missing_head_repository_is_detected(self) -> None:
        source = WORKFLOWS[0].read_text().replace(TARGET_REPOSITORY, "")
        self.assertEqual(
            findings(source), ["missing immutable PR-head/push repository binding"]
        )

    def test_missing_head_sha_is_detected(self) -> None:
        source = WORKFLOWS[0].read_text().replace(TARGET_REF, "")
        self.assertEqual(findings(source), ["missing immutable PR-head/push SHA binding"])


if __name__ == "__main__":
    unittest.main()
