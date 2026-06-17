document.addEventListener("DOMContentLoaded", function () {

    const btn = document.getElementById("analyzeBtn");
    const resumeInput = document.getElementById("resume");
    const jobInput = document.getElementById("jobDescription");
    const resultDiv = document.getElementById("result");

    btn.addEventListener("click", async function () {

        // Validation
        if (!resumeInput.files[0]) {
            alert("Please upload resume");
            return;
        }

        if (!jobInput.value.trim()) {
            alert("Please enter job description");
            return;
        }

        // Show loading
        resultDiv.innerHTML = "<p>⏳ Analyzing your profile...</p>";

        try {
            const formData = new FormData();
            formData.append("resume", resumeInput.files[0]);
            formData.append("job_description", jobInput.value);

            const response = await fetch("/analyze", {
                method: "POST",
                body: formData
            });

            const data = await response.json();

            renderResults(data);

        } catch (error) {
            console.error(error);
            resultDiv.innerHTML = "<p style='color:red'>Error occurred during analysis</p>";
        }
    });

    function renderResults(data) {

        resultDiv.innerHTML = `
            <div class="result-container">

                ${renderResume(data.resume_analysis)}
                ${renderGap(data.gap_analysis)}
                ${renderInterview(data.interview_analysis)}
                ${renderRoadmap(data.learning_roadmap)}

            </div>
        `;
    }

    function renderResume(resume) {
        return `
        <div class="card">
            <h2>📄 Resume Analysis</h2>
            <p><strong>Name:</strong> ${resume.name}</p>
            <p><strong>Email:</strong> ${resume.email}</p>

            <h4>Skills</h4>
            <div class="tags">
                ${resume.skills.map(skill => `<span class="tag">${skill}</span>`).join("")}
            </div>
        </div>
        `;
    }

    function renderGap(gap) {
        return `
        <div class="card">
            <h2>📊 Gap Analysis</h2>

            <div class="score-box">
                <h3>Match Score: ${gap.match_score}%</h3>
                <div class="progress">
                    <div class="bar" style="width:${gap.match_score}%"></div>
                </div>
            </div>

            <h4>Strong Skills</h4>
            <div class="tags green">
                ${gap.strong_skills.map(s => `<span class="tag">${s}</span>`).join("")}
            </div>

            <h4>Missing Skills</h4>
            <div class="tags red">
                ${gap.missing_skills.map(s => `<span class="tag">${s}</span>`).join("")}
            </div>

            <h4>Recommendations</h4>
            <ul>
                ${gap.learning_recommendation.map(r => `<li>${r}</li>`).join("")}
            </ul>
        </div>
        `;
    }

    function renderInterview(interview) {
        return `
        <div class="card">
            <h2>🎯 Interview Questions</h2>

            <h4>Technical</h4>
            <ul>
                ${interview.technical_questions.map(q => `<li>${q}</li>`).join("")}
            </ul>

            <h4>Behavioral</h4>
            <ul>
                ${interview.behavioral_questions.map(q => `<li>${q}</li>`).join("")}
            </ul>

            <h4>Project Based</h4>
            <ul>
                ${interview.project_based_questions.map(q => `<li>${q}</li>`).join("")}
            </ul>
        </div>
        `;
    }

    function renderRoadmap(roadmap) {
        return `
        <div class="card">
            <h2>📚 Learning Roadmap</h2>

            <h4>Week 1</h4>
            <ul>
                ${roadmap.first_week.map(d => `<li>${d}</li>`).join("")}
            </ul>

            <h4>Week 2</h4>
            <ul>
                ${roadmap.second_week.map(d => `<li>${d}</li>`).join("")}
            </ul>

            <h4>Projects</h4>
            <ul>
                ${roadmap.projects.map(p => `<li>${p}</li>`).join("")}
            </ul>
        </div>
        `;
    }

});