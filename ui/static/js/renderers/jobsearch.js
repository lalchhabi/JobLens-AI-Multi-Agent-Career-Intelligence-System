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