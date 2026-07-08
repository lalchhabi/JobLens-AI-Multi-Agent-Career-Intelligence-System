"""
Utility functions for normalizing job skills before they are sent to the LLM or the module that converts compound skills into individual skills so the LLM can perform more accurate semantic matching.
"""

from __future__ import annotations

import re


def normalize_skills(skills: list[str]) -> list[str]:
    """
    Utility functions for normalizing job skills before they are sent to the LLM or the module that converts compound skills into individual skills so the LLM can perform more accurate semantic matching.
    """

    normalized = []

    for skill in skills:

        if not skill:
            continue

        # Split by common separators
        parts = re.split(
            r"\s+or\s+|\s*&\s*|\/|,",
            skill,
            flags=re.IGNORECASE,
        )

        for part in parts:
            part = part.strip()

            if part:
                normalized.append(part)

    # Remove duplicates while preserving order
    seen = set()
    unique = []

    for skill in normalized:
        key = skill.lower()

        if key not in seen:
            seen.add(key)
            unique.append(skill)

    return unique