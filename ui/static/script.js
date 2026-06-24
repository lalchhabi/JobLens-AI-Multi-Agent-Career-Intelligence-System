console.log("🔥 STREAMING SCRIPT LOADED");
document.addEventListener("DOMContentLoaded", function () {

    const btn = document.getElementById("analyzeBtn");
    const resumeInput = document.getElementById("resume");
    const jobInput = document.getElementById("jobDescription");
    const resultDiv = document.getElementById("result");

    // =============================
    // UI HELPERS (NEW)
    // =============================

    function showToast(message, color = "#333") {
        const toast = document.createElement("div");

        toast.innerText = message;
        toast.style.position = "fixed";
        toast.style.bottom = "20px";
        toast.style.right = "20px";
        toast.style.background = color;
        toast.style.color = "white";
        toast.style.padding = "10px 15px";
        toast.style.borderRadius = "8px";
        toast.style.zIndex = 9999;
        toast.style.fontSize = "14px";
        toast.style.boxShadow = "0 4px 10px rgba(0,0,0,0.2)";

        document.body.appendChild(toast);

        setTimeout(() => {
            toast.remove();
        }, 2500);
    }

    function setLoading(isLoading) {
        if (isLoading) {
            btn.innerText = "⏳ Analyzing...";
            btn.disabled = true;
            btn.style.opacity = "0.7";
        } else {
            btn.innerText = "🚀 Analyze Career Fit";
            btn.disabled = false;
            btn.style.opacity = "1";
        }
    }

    // =============================
    // EVENT LISTENERS
    // =============================

    btn.addEventListener("click", async function () {

        // Validation
        if (!resumeInput.files[0]) {
            showToast("Please upload resume", "#e74c3c");
            return;
        }

        if (!jobInput.value.trim()) {
            showToast("Please enter job description", "#e74c3c");
            return;
        }

        // Loading state
        setLoading(true);
        resultDiv.innerHTML = "<p>⏳ Analyzing your profile...</p>";

        try {
            const formData = new FormData();
            formData.append("resume", resumeInput.files[0]);
            formData.append("job_description", jobInput.value);

            const response = await fetch("/analyze-stream", {
                method: "POST",
                body: formData
            });

            // STREAM READER
            const reader = response.body.getReader();
            const decoder = new TextDecoder();

            let buffer = "";

            // hold partial results
            let partialData = {
                resume_analysis: null,
                gap_analysis: null,
                interview_analysis: null,
                learning_roadmap: null,
                market_analysis: null
            };

            resultDiv.innerHTML = `
                <div id="streamContainer" class="result-container">
                    <p>⏳ Starting streaming analysis...</p>
                </div>
            `;

            const streamContainer = document.getElementById("streamContainer");

            while (true) {
                const { value, done } = await reader.read();
                if (done) break;

                buffer += decoder.decode(value, { stream: true });

                const chunks = buffer.split("\n\n");
                buffer = chunks.pop(); // keep incomplete chunk

                for (const chunk of chunks) {
                    if (!chunk.startsWith("data: ")) continue;

                    const jsonStr = chunk.replace("data: ", "");
                    const event = JSON.parse(jsonStr);
                    console.log("EVENT RECEIVED:", event);
                    console.log("TYPE =", event.type);
                    console.log("DATA =", event.data);
                    if (event.error){
                        showToast(event.error, "#e74c3c");
                        resultDiv.innerHTML += `
                            <div class="card">
                                <h3>❌ AI service is busy right now.
                                Please try again in a few minutes.
                                </h3>
                                <p>${event.error}</p>
                            </div>
                        `;

                        setLoading(false);

                        return;
                    }

                    console.log("Stream event:", event);

                    // detect which node finished
                    if (event.type === "error") {

                        showToast(event.data, "#e74c3c");

                        resultDiv.innerHTML += `
                            <div class="card">
                                <h3>❌ Analysis Failed</h3>
                                <p>${event.data}</p>
                            </div>
                        `;

                        setLoading(false);
                        return;
                    }

                    const key = event.type;
                    partialData[key] = event.data;

                    if (key) {
                        partialData[key] = event.data;
                    }

                    const map = {
                        resume: "Resume Analysis",
                        job: "Job Analysis",
                        gap: "Gap Analysis",
                        interview: "Interview Questions",
                        roadmap: "Learning Roadmap",
                        market_analysis: "Market Insights"
                    };
                    const uiKey = map[event.type];
                    showToast(`${uiKey} completed ✔`, "#3498db");

                    // live UI update
                    streamContainer.innerHTML = `
                        ${partialData.resume_analysis 
                            ? renderResume(partialData.resume_analysis) 
                            : "<p>🧠 Resume analysis running...</p>"}

                        ${partialData.gap_analysis 
                            ? renderGap(partialData.gap_analysis)
                            : "<p>📊 Gap analysis running...</p>"}

                        ${partialData.interview_analysis 
                            ? renderInterview(partialData.interview_analysis)
                            : "<p>🎯 Interview questions generating...</p>"}

                        ${partialData.learning_roadmap 
                            ? renderRoadmap(partialData.learning_roadmap) 
                            : "<p>📚 Roadmap generating...</p>"}

                        ${partialData.market_analysis 
                            ? renderMarket(partialData.market_analysis) 
                            : "<p>📚 Market Analysis running...</p>"}
                    `;
                }
            }

            // final toast when stream ends
            showToast("Analysis completed successfully ✔", "#2ecc71");

        } catch (error) {
            console.error(error);
            showToast("Analysis failed ❌", "#e74c3c");
            resultDiv.innerHTML = "<p style='color:red'>Error occurred during analysis</p>";
        }

        setLoading(false);
    });

    // =============================
    // FILE UPLOAD NOTIFICATION (NEW)
    // =============================
    resumeInput.addEventListener("change", function () {
        if (this.files.length > 0) {
            showToast(`Resume uploaded: ${this.files[0].name}`, "#2ecc71");
        }
    });

    jobInput.addEventListener("input", function () {
        if (jobInput.value.trim().length > 20) {
            showToast("Job description added ✔", "#2ecc71");
        }
    });

    // =============================
    // RESULT RENDERING (YOUR EXISTING LOGIC - IMPROVED ONLY SLIGHTLY)
    // =============================

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

    function renderMarket(market_analysis) {
        console.log("Market Object = ", market_analysis);
    if (!market_analysis) return "";

    return `
    <div class="card">
        <h2>🌍 Market Insights</h2>

        <h4>Similar Roles</h4>
        <ul>
            ${(market_analysis.similar_roles || []).map(r => `<li>${r}</li>`).join("")}
        </ul>

        <h4>Alternative Roles</h4>
        <ul>
            ${(market_analysis.alternative_roles || []).map(r => `<li>${r}</li>`).join("")}
        </ul>

        <h4>Trending Skills</h4>
        <div class="tags">
            ${(market_analysis.trending_skills || []).map(s => `<span class="tag">${s}</span>`).join("")}
        </div>

        <h4>Recommended Jobs</h4>
        <ul>
            ${(market_analysis.recommended_jobs || []).map(job => `
                <li>
                    <strong>${job.title}</strong>
                    ${job.company}
                    (${job.location})
                </li>
            `).join("")}
        </ul>

        <p>
            <strong>Summary:</strong>
            ${market_analysis.market_summary || ""}
        </p>
    </div>
    `;
}

});