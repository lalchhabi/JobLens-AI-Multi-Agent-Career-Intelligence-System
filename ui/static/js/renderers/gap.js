function renderGap(gap) {

    if (!gap) return "";

    // match_score is Optional in GapSchema, so it can legitimately
    // arrive as null - don't dereference it unguarded
    const score = gap.match_score;

    // The matched/total counts are computed by scoring_engine.py and
    // were never surfaced. Show the ratio behind each percentage, but
    // only when both counts actually arrived.
    const ratio = (matched, total) =>
        Number.isFinite(matched) && Number.isFinite(total)
            ? `<em>${matched}/${total}</em>`
            : "";

    const scoreBox = score
        ? `
        <div class="score-box">

            <div class="score-value">

                <b>${score.overall_score}<span class="score-pct">%</span></b>

                <span class="label">Overall match</span>

            </div>

            <div
                class="progress"
                role="progressbar"
                aria-valuenow="${score.overall_score}"
                aria-valuemin="0"
                aria-valuemax="100"
                aria-label="Overall match score">

                <div
                    class="bar"
                    style="width:${score.overall_score}%">

                </div>

            </div>

            <div class="score-breakdown">

                <div class="score-metric">

                    <span>Required</span>

                    <b>${score.required_skill_score}%
                       ${ratio(score.matched_required, score.total_required)}</b>

                </div>

                <div class="score-metric">

                    <span>Preferred</span>

                    <b>${score.preferred_skill_score}%
                       ${ratio(score.matched_preferred, score.total_preferred)}</b>

                </div>

            </div>

        </div>
        `
        : `
        <div class="score-box">

            <p>Match score unavailable for this analysis.</p>

        </div>
        `;

    const skillTags = (skills) =>
        (skills || [])
            .map(s => `<span class="tag">${escapeHtml(s)}</span>`)
            .join("");

    return `
    <div class="card">

        <h2>Gap analysis</h2>

        ${scoreBox}

        <h4>Matched Required Skills</h4>

        <div class="tags green">
            ${skillTags(gap.matched_required_skills)}
        </div>

        <h4>Missing Required Skills</h4>

        <div class="tags red">
            ${skillTags(gap.missing_required_skills)}
        </div>

        <h4>Matched Preferred Skills</h4>

        <div class="tags blue">
            ${skillTags(gap.matched_preferred_skills)}
        </div>

        <h4>Learning Recommendations</h4>

        <ul>
            ${(gap.learning_recommendation || [])
                .map(r => `<li>${escapeHtml(r)}</li>`)
                .join("")}
        </ul>

    </div>
    `;
}
