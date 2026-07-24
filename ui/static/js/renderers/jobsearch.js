// =====================================
// LIVE JOB SEARCH API
// =====================================

async function searchJobs({

    role,
    country = "au"

}) {

    try {

        const response = await fetch("/search-jobs", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({

                role,
                country

            })

        });

        if (!response.ok) {

            throw new Error("Unable to fetch live jobs.");

        }

        return await response.json();

    }
    catch (err) {

        console.error("Job search failed:", err);

        throw err;

    }

}

document.addEventListener("click", async (event) => {

    if (event.target.id !== "searchJobsBtn") return;

    const button = event.target;

    // Disable button while searching
    button.disabled = true;
    button.textContent = "Searching...";

    try {

        const country =
            document.getElementById("countrySelect").value;

        const role = state.job_analysis.title;

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

        const jobs = await response.json();

        document.getElementById("jobsContainer").innerHTML =
            renderJobs(jobs);

    } catch (error) {

        console.error(error);

        document.getElementById("jobsContainer").innerHTML = `
            <div class="empty-card">
                Unable to load jobs.
            </div>
        `;

    } finally {

        // Always restore button
        button.disabled = false;
        button.textContent = "Search Jobs";

    }

});