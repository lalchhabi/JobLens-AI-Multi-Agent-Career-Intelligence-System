function renderResume(resume) {

    if (!resume) return "";

    return `
    <div class="card">

        <h2>Resume</h2>

        <h4>Candidate</h4>

        <p><strong>Name:</strong> ${text(resume.name)}</p>

        <p><strong>Email:</strong> ${text(resume.email)}</p>


        <h4>Experience</h4>

        ${(resume.experience || []).map(exp => `

        <div class="experience-item">

            <h4>${text(exp.role)}</h4>

            <p>
                <strong>${text(exp.company)}</strong>
            </p>

            <small>${text(exp.duration, "Duration not listed")}</small>

            <ul>

                ${(exp.responsibilities || [])
                    .slice(0,3)
                    .map(item => `<li>${escapeHtml(item)}</li>`)
                    .join("")}

            </ul>

        </div>

        `).join("")}


        <h4>Skills</h4>

        <div class="tags">

            ${(resume.skills || []).map(skill => `
                <span class="tag">${escapeHtml(skill)}</span>
            `).join("")}

        </div>


        <h4>Projects</h4>

        ${(resume.projects || []).map(project => `

            <div class="project-item">

                <h4>${text(project.name)}</h4>

                    <p>

                        ${text(project.description, "No description provided")}

                    </p>

            </div>

        `).join("")}


        <h4>Education</h4>

        ${(resume.education || []).map(item => `

            <div class="education-item">

                <h4>${text(item.institution)}</h4>

                <small>
                    ${text(item.degree, "Degree not listed")}
                    ·
                    ${text(item.year, "Year not listed")}
                </small>

            </div>

        `).join("")}

    </div>
    `;
}
