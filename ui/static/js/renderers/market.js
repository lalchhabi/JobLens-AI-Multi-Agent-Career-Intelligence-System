function formatPostedDate(dateString) {

    if (!dateString) return "Unknown";

    const date = new Date(dateString);

    return date.toLocaleDateString("en-GB", {
        day: "numeric",
        month: "short",
        year: "numeric"
    });

}

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

                            <div class="job-item">
                                Posted • ${formatPostedDate(job.created)}
                            </div>

                            ${
                                job.salary_min || job.salary_max
                                    ? `
                                        <div class="job-item">
                                            💰 ${job.salary_min ?? "?"}
                                            ${
                                                job.salary_max
                                                    ? " - " + job.salary_max
                                                    : ""
                                            }
                                        </div>
                                    `
                                    : ""
                            }

                        </div>
                        <p class="job-description">
                            ${
                                job.job_description.length > 180
                                    ? text(job.job_description.slice(0, 180)) + "..."
                                    : text(job.job_description)
                            }
                        </p>

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

                <div class="job-search-panel">

                    <div class="search-title">

                        🔍 Search Live Jobs

                    </div>

                    <div class="search-subtitle">

                        Find current openings from different countries.

                    </div>

                    <div class="job-search-controls">

                        <div class="search-field">

                            <label for="countrySelect">
                                Country
                            </label>

                            <select id="countrySelect">

                                <option value="au" selected>Australia</option>
                                <option value="at">Austria</option>
                                <option value="be">Belgium</option>
                                <option value="br">Brazil</option>
                                <option value="ca">Canada</option>
                                <option value="fr">France</option>
                                <option value="de">Germany</option>
                                <option value="in">India</option>
                                <option value="it">Italy</option>
                                <option value="mx">Mexico</option>
                                <option value="nl">Netherlands</option>
                                <option value="nz">New Zealand</option>
                                <option value="pl">Poland</option>
                                <option value="sg">Singapore</option>
                                <option value="za">South Africa</option>
                                <option value="es">Spain</option>
                                <option value="ch">Switzerland</option>
                                <option value="gb">United Kingdom</option>
                                <option value="us">United States</option>

                            </select>

                        </div>

                        <button
                            id="searchJobsBtn"
                            class="job-search-btn">

                            Search Jobs

                        </button>

                    </div>

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
    
    const countryName =
        document.getElementById("countrySelect")
            .options[
                document.getElementById("countrySelect").selectedIndex
            ].text;

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
            <div class="spinner"></div>
            Searching live jobs...
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

            const error = await response.json();

            throw new Error(error.detail);

        }

        const jobs = await response.json();

        const jobsContainer = document.getElementById("jobsContainer");

        if (!jobs || jobs.length === 0) {
            jobsContainer.innerHTML = `
                <div class="empty-card">
                    <h4>No jobs found</h4>
                    <p>No matching jobs were found for <strong>${countryName}</strong>.</p>
                    <p>Try another country.</p>
                </div>
            `;
            return;
        }

        jobsContainer.innerHTML = renderJobs(jobs);

    }
    catch (err) {

        console.error(err);

        jobsContainer.innerHTML = `
            <div class="empty-card">
                ${err.message}
            </div>
        `;

    }

});
