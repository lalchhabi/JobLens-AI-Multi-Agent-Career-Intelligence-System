function renderJob(job) {

    if (!job) return "";

    return `
    <div class="card">

        <h2>Job requirements</h2>

        <h4>Role</h4>

        <p><strong>Title:</strong> ${text(job.title)}</p>

        <p><strong>Company:</strong> ${text(job.company)}</p>

        <p>
            <strong>Experience level:</strong>
            ${text(job.experience_level, "Not specified")}
        </p>


        <h4>Required Skills</h4>

        <div class="tags">

            ${(job.required_skills || [])
                .map(s => `<span class="tag">${escapeHtml(s)}</span>`)
                .join("")}

        </div>


        <h4>Preferred Skills</h4>

        <div class="tags blue">

            ${(job.preferred_skills || [])
                .map(s => `<span class="tag">${escapeHtml(s)}</span>`)
                .join("")}

        </div>


        <h4>Responsibilities</h4>

        <ul>
            ${(job.responsibilities || [])
                .map(r => `<li>${escapeHtml(r)}</li>`)
                .join("")}
        </ul>

    </div>
    `;
}
