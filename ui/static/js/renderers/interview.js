function renderInterview(interview) {

    if (!interview) return "";

    const questions = (list) =>
        (list || [])
            .map(q => `<li>${escapeHtml(q)}</li>`)
            .join("");

    return `
    <div class="card">

        <h2>Interview questions</h2>

        <h4>Technical</h4>

        <ul>
            ${questions(interview.technical_questions)}
        </ul>

        <h4>Behavioral</h4>

        <ul>
            ${questions(interview.behavioral_questions)}
        </ul>

        <h4>Project Based</h4>

        <ul>
            ${questions(interview.project_based_questions)}
        </ul>

    </div>
    `;
}
