# Import required libraries
from typing import List
from schemas.match_score_schema import MatchScoreSchema

# Scoring weights
REQUIRED_SKILL_WEIGHT = 0.80
PREFERRED_SKILL_WEIGHT = 0.20


def calculate_match_score(
    matched_required_skills: List[str],
    missing_required_skills: List[str],
    matched_preferred_skills: List[str],
    missing_preferred_skills: List[str],
) -> MatchScoreSchema:
    """
    Calculate a deterministic resume-job match score.

    The overall score is calculated using:
        - Required skills (80%)
        - Preferred skills (20%)

    Args:
        matched_required_skills: Required job skills found in the resume.
        missing_required_skills: Required job skills missing from the resume.
        matched_preferred_skills: Preferred job skills found in the resume.
        missing_preferred_skills: Preferred job skills missing from the resume.

    Returns:
        Dictionary containing overall score and score breakdown.
    """

    # ---------- Required Skills ----------
    total_required = (
        len(matched_required_skills)
        + len(missing_required_skills)
    )

    matched_required_count = len(matched_required_skills)

    required_score = (
        (matched_required_count / total_required) * 100
        if total_required > 0
        else 100
    )

    # ---------- Preferred Skills ----------
    total_preferred = (
        len(matched_preferred_skills)
        + len(missing_preferred_skills)
    )

    matched_preferred_count = len(matched_preferred_skills)

    preferred_score = (
        (matched_preferred_count / total_preferred) * 100
        if total_preferred > 0
        else 100
    )

    # ---------- Overall Score ----------
    overall_score = (
        (required_score * REQUIRED_SKILL_WEIGHT)
        + (preferred_score * PREFERRED_SKILL_WEIGHT)
    )

    return MatchScoreSchema(
        overall_score=round(overall_score),
        required_skill_score=round(required_score),
        preferred_skill_score=round(preferred_score),
        matched_required=matched_required_count,
        total_required=total_required,
        matched_preferred=matched_preferred_count,
        total_preferred=total_preferred,
    )