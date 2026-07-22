function renderMarket(market) {

    if (!market) return "";
    console.log("Market Object:", market);

    console.log("Live Jobs:", market.live_jobs);

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

    const renderJobs = (jobs) => {

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

                <h3>
                    Latest Jobs (${market.live_jobs?.length || 0})
                </h3>

                ${renderJobs(market.live_jobs)}

            </div>

        </div>

    `;

}