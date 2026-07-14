function renderResume(resume) {

    return `
    <div class="card">

        <h2>📄 Resume Analysis</h2>

        <h3>👤 Candidate Information</h3>

        <p><strong>Name:</strong> ${resume.name}</p>

        <p><strong>Email:</strong> ${resume.email}</p>


        <h3>💼 Experience</h3>

        ${(resume.experience || []).map(exp => `

        <div class="experience-item">

            <h4>${exp.role}</h4>

            <p>
                <strong>${exp.company}</strong>
            </p>

            <small>${exp.duration}</small>

            <ul>

                ${(exp.responsibilities || [])
                    .slice(0,3)
                    .map(item => `<li>${item}</li>`)
                    .join("")}

            </ul>

        </div>

        `).join("")}


        <h3>🛠 Skills</h3>

        <div class="tags">

            ${(resume.skills || []).map(skill => `
                <span class="tag">${skill}</span>
            `).join("")}

        </div>


        <h3>🚀 Featured Projects</h3>

        ${(resume.projects || []).map(project => `

            <div class="project-item">

                <h4>${project.name}</h4>

                    <p>

                        ${project.description}

                    </p>

            </div>

        `).join("")}

    </div>
    `;
}