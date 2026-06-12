document.getElementById("uploadForm").addEventListener("submit", async function(e) {
    e.preventDefault();

    let resume = document.getElementById("resume").files[0];
    let job = document.getElementById("jobDescription").value;

    let formData = new FormData();
    formData.append("resume", resume);
    formData.append("job_description", job);

    let response = await fetch("/analyze", {
        method: "POST",
        body: formData
    });

    let data = await response.json();
    document.getElementById("result").innerText =
        JSON.stringify(data, null, 2);
});