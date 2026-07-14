document.addEventListener("DOMContentLoaded", () => {

    const btn = document.getElementById("analyzeBtn");
    const resumeInput = document.getElementById("resume");
    const jobInput = document.getElementById("jobDescription");

    // Resume upload notification
    resumeInput.addEventListener("change", () => {

        if (resumeInput.files.length > 0) {
            showToast(
                `Resume uploaded: ${resumeInput.files[0].name}`,
                "#2ecc71"
            );
        }

    });

    // Job description notification
    jobInput.addEventListener("input", () => {

        if (jobInput.value.trim().length > 20) {
            showToast("Job description added ✔", "#2ecc71");
        }

    });

    btn.addEventListener("click", async () => {

        // =============================
        // Validation
        // =============================

        if (!resumeInput.files[0]) {

            showToast("Please upload resume", "#e74c3c");
            return;

        }

        if (!jobInput.value.trim()) {

            showToast("Please enter job description", "#e74c3c");
            return;

        }

        // =============================
        // Reset State
        // =============================

        state.resume_analysis = null;
        state.gap_analysis = null;
        state.interview_analysis = null;
        state.learning_roadmap = null;
        state.market_analysis = null;
        state.cover_letter = null;
        state.error = null;
        state.loading = true;

        setLoading(true);

        const formData = new FormData();

        formData.append("resume", resumeInput.files[0]);
        formData.append("job_description", jobInput.value);

        try {

            await startStreaming(formData, {

                onEvent(event) {

                    state[event.type] = event.data;

                    renderNavigation(state);

                },

                onError(error) {

                    state.error = error;
                    showToast(error, "#e74c3c");

                },

                onComplete() {

                    state.loading = false;

                    setLoading(false);

                    showToast(
                        "Analysis completed ✔",
                        "#2ecc71"
                    );

                }

            });

        }
        catch (err) {

            console.error(err);

            state.loading = false;

            setLoading(false);

            showToast(
                "Analysis failed",
                "#e74c3c"
            );

        }

    });

});