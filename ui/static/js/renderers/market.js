function renderJobs(jobs) {

        if (!jobs || jobs.length === 0) {

            return `
                <div class="empty-card">
                    No matching jobs found.
                </div>
            `;

        }

        return `
            <div class="jobs-list">

                ${jobs.map(job => `

                    <div class="job-card">

                        <div class="job-header">

                            <h3>${text(job.title)}</h3>

                        </div>

                        <div class="job-meta">

                            <div class="job-item">
                                🏢 ${text(job.company)}
                            </div>

                            <div class="job-item">
                                📍 ${text(job.location)}
                            </div>

                            ${job.salary
                                ? `
                                    <div class="job-item">
                                        💰 ${escapeHtml(job.salary)}
                                    </div>
                                `
                                : ""
                            }

                        </div>

                        <div class="job-footer">

                            <a
                                href="${escapeHtml(job.apply_url)}"
                                target="_blank"
                                rel="noopener noreferrer"
                                class="job-apply-btn">

                                Apply Job →

                            </a>

                        </div>

                    </div>

                `).join("")}

            </div>
        `;

    };




function renderMarket(market) {

    if (!market) return "";

    // ----------------------------------------
    // Helpers
    // ----------------------------------------

    const renderTags = (list) => {

        if (!list || list.length === 0) {
            return `<p class="empty-text">No data available.</p>`;
        }

        return `
            <div class="tags">
                ${list.map(item => `
                    <span class="tag">
                        ${escapeHtml(item)}
                    </span>
                `).join("")}
            </div>
        `;
    };

    // ----------------------------------------
    // UI
    // ----------------------------------------

    return `

        <div class="card market-card">

            <h2>Market Insights</h2>

            <div class="market-section">

                <h3>Similar Roles</h3>

                ${renderTags(market.similar_roles)}

            </div>

            <div class="market-section">

                <h3>Alternative Roles</h3>

                ${renderTags(market.alternative_roles)}

            </div>

            <div class="market-section">

                <h3>Trending Skills</h3>

                ${renderTags(market.trending_skills)}

            </div>

            <div class="section-divider"></div>

            <div class="market-section">

                <h3>Live Job Search</h3>

                <div class="job-search-controls">

                    <select
                        id="countrySelect"
                        class="job-country-select">

                        <option value="au">Australia</option>
                        <option value="ca">Canada</option>
                        <option value="gb">United Kingdom</option>
                        <option value="us">United States</option>
                        <option value="sg">Singapore</option>
                        <option value="nz">New Zealand</option>
                        <option value="in">India</option>

                    </select>

                    <button
                        id="searchJobsBtn"
                        class="job-apply-btn"
                        type="button">

                        Search Jobs

                    </button>

                </div>
  
                <div id="jobsContainer" class="jobs-container">

                    <div class="empty-card">

                        Select a country and click
                        <strong>Search Jobs</strong>.

                    </div>

                </div>

            </div>

        </div>

    `;

}

window.renderJobs = renderJobs;

// =====================================
// LIVE JOB SEARCH
// =====================================

document.addEventListener("click", async (event) => {

    if (event.target.id !== "searchJobsBtn")
        return;

    const country =
        document.getElementById("countrySelect").value;

    // Current target role from analysis
    const role = state.job_analysis?.title;

    if (!role) {

        showToast("Job title not available.", "danger");

        return;

    }

    const jobsContainer =
        document.getElementById("jobsContainer");

    jobsContainer.innerHTML = `
        <div class="empty-card">
            Searching jobs...
        </div>
    `;

    try {

        const response = await fetch("/search-jobs", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({

                role: role,
                country: country

            })

        });

        if (!response.ok) {

            throw new Error("Failed to search jobs.");

        }

        const jobs = await response.json();

        jobsContainer.innerHTML = renderJobs(jobs);

    }
    catch (err) {

        console.error(err);

        jobsContainer.innerHTML = `
            <div class="empty-card">
                Unable to load jobs.
            </div>
        `;

    }

});
