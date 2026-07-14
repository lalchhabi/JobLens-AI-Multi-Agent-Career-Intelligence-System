function renderGap(gap) {

    if (!gap) return "";

    return `
    <div class="card">

        <h2>📊 Gap Analysis</h2>

        <div class="score-box">

            <h3>
                Match Score:
                ${gap.match_score.overall_score}%
            </h3>

            <div class="progress">

                <div
                    class="bar"
                    style="width:${gap.match_score.overall_score}%">

                </div>

            </div>

            <p>
                <strong>Required Skills:</strong>
                ${gap.match_score.required_skill_score}%
            </p>

            <p>
                <strong>Preferred Skills:</strong>
                ${gap.match_score.preferred_skill_score}%
            </p>

        </div>

        <h4>Matched Required Skills</h4>

        <div class="tags green">
            ${(gap.matched_required_skills || [])
                .map(s => `<span class="tag">${s}</span>`)
                .join("")}
        </div>

        <h4>Missing Required Skills</h4>

        <div class="tags red">
            ${(gap.missing_required_skills || [])
                .map(s => `<span class="tag">${s}</span>`)
                .join("")}
        </div>

        <h4>Matched Preferred Skills</h4>

        <div class="tags blue">
            ${(gap.matched_preferred_skills || [])
                .map(s => `<span class="tag">${s}</span>`)
                .join("")}
        </div>

        <h4>Learning Recommendations</h4>

        <ul>
            ${(gap.learning_recommendation || [])
                .map(r => `<li>${r}</li>`)
                .join("")}
        </ul>

    </div>
    `;
}