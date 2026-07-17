function renderRoadmap(roadmap) {

    if (!roadmap) return "";

    const items = (list) =>
        (list || [])
            .map(item => `<li>${escapeHtml(item)}</li>`)
            .join("");

    return `
    <div class="card">

        <h2>Learning roadmap</h2>

        <h4>Week 1</h4>

        <ul>
            ${items(roadmap.first_week)}
        </ul>

        <h4>Week 2</h4>

        <ul>
            ${items(roadmap.second_week)}
        </ul>

        <h4>Projects</h4>

        <ul>
            ${items(roadmap.projects)}
        </ul>

        <h4>Resources</h4>

        <ul>
            ${items(roadmap.resources)}
        </ul>

    </div>
    `;
}
