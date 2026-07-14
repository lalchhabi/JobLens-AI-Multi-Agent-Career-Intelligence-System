function renderInterview(interview) {

    if (!interview) return "";

    return `
    <div class="card">

        <h2>🎯 Interview Questions</h2>

        <h4>Technical</h4>

        <ul>
            ${interview.technical_questions
                .map(q => `<li>${q}</li>`)
                .join("")}
        </ul>

        <h4>Behavioral</h4>

        <ul>
            ${interview.behavioral_questions
                .map(q => `<li>${q}</li>`)
                .join("")}
        </ul>

        <h4>Project Based</h4>

        <ul>
            ${interview.project_based_questions
                .map(q => `<li>${q}</li>`)
                .join("")}
        </ul>

    </div>
    `;
}