document.addEventListener("DOMContentLoaded", function () {

    const btn = document.getElementById("analyzeBtn");

    const resumeInput = document.getElementById("resume");
    const jobInput = document.getElementById("jobDescription");
    const resultBox = document.getElementById("result");

    if (!btn) {
        console.error("Analyze button not found in DOM");
        return;
    }

    btn.addEventListener("click", async function () {

        const resume = resumeInput.files[0];
        const job = jobInput.value;

        if (!resume || !job) {
            alert("Please upload resume and enter job description");
            return;
        }

        let formData = new FormData();
        formData.append("resume", resume);
        formData.append("job_description", job);

        resultBox.innerText = "Analyzing...";

        try {
            let response = await fetch("/analyze", {
                method: "POST",
                body: formData
            });

            let data = await response.json();

            resultBox.innerText = JSON.stringify(data, null, 2);

        } catch (err) {
            console.error(err);
            resultBox.innerText = "Error occurred while analyzing";
        }
    });

});