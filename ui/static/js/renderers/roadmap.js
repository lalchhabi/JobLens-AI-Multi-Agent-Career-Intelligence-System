function renderRoadmap(roadmap) {

    if (!roadmap) return "";

    return `
    <div class="card">

        <h2>📚 Learning Roadmap</h2>

        <h4>Week 1</h4>

        <ul>
            ${roadmap.first_week
                .map(d => `<li>${d}</li>`)
                .join("")}
        </ul>

        <h4>Week 2</h4>

        <ul>
            ${roadmap.second_week
                .map(d => `<li>${d}</li>`)
                .join("")}
        </ul>

        <h4>Projects</h4>

        <ul>
            ${roadmap.projects
                .map(p => `<li>${p}</li>`)
                .join("")}
        </ul>

    </div>
    `;
}