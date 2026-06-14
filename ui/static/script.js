document.addEventListener("DOMContentLoaded", () => {
    const analyzeBtn = document.getElementById("analyzeBtn");
    const resultBox = document.getElementById("result");

    if (!analyzeBtn) {
        console.error("Analyze button not found in DOM");
        return;
    }

    analyzeBtn.addEventListener("click", async () => {
        const resume = document.getElementById("resume").files[0];
        const jobDescription = document.getElementById("jobDescription").value;

        if (!resume || !jobDescription) {
            alert("Please upload resume and paste job description");
            return;
        }

        // Show loading state
        resultBox.innerHTML = `<div class="empty-state">⏳ Analyzing your profile...</div>`;

        try {
            const formData = new FormData();
            formData.append("resume", resume);
            formData.append("job_description", jobDescription);

            const response = await fetch("/analyze", {
                method: "POST",
                body: formData
            });

            if (!response.ok) {
                throw new Error("Server error while analyzing data");
            }

            const data = await response.json();

            renderResults(data);

        } catch (error) {
            console.error(error);
            resultBox.innerHTML = `
                <div class="error-box">
                    ❌ Something went wrong while analyzing.
                </div>
            `;
        }
    });

    function renderResults(data) {
        const gap = data.gap_analysis || {};
        const resume = data.resume_analysis || {};
        const interview = data.interview_analysis || {};
        const roadmap = data.learning_roadmap || {};

        resultBox.innerHTML = `
            <div class="dashboard">

                <!-- MATCH SCORE -->
                <div class="card score-card">
                    <h2>🎯 Match Score</h2>
                    <div class="score">${gap.match_score || 0}%</div>
                    <div class="bar">
                        <div class="fill" style="width:${gap.match_score || 0}%"></div>
                    </div>
                </div>

                <!-- RESUME INFO -->
                <div class="card">
                    <h3>👤 Candidate Info</h3>
                    <p><strong>Name:</strong> ${resume.name || "N/A"}</p>
                    <p><strong>Email:</strong> ${resume.email || "N/A"}</p>
                </div>

                <!-- STRONG SKILLS -->
                <div class="card">
                    <h3>💪 Strong Skills</h3>
                    <div class="tags">
                        ${(gap.strong_skills || []).map(skill =>
                            `<span class="tag good">${skill}</span>`
                        ).join("")}
                    </div>
                </div>

                <!-- MISSING SKILLS -->
                <div class="card">
                    <h3>⚠️ Skill Gaps</h3>
                    <div class="tags">
                        ${(gap.missing_skills || []).map(skill =>
                            `<span class="tag bad">${skill}</span>`
                        ).join("")}
                    </div>
                </div>

                <!-- INTERVIEW QUESTIONS -->
                <div class="card">
                    <h3>🧪 Technical Interview Questions</h3>
                    <ol>
                        ${(interview.technical_questions || []).map(q =>
                            `<li>${q}</li>`
                        ).join("")}
                    </ol>
                </div>

                <!-- LEARNING ROADMAP -->
                <div class="card">
                    <h3>🗺 First Week Learning Plan</h3>
                    <ul>
                        ${(roadmap.first_week || []).map(day =>
                            `<li>${day}</li>`
                        ).join("")}
                    </ul>
                </div>

            </div>
        `;
    }
});