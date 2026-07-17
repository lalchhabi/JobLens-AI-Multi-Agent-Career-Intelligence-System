// Keep in sync with validate_pdf() in utils/validators.py
const MAX_RESUME_BYTES = 5 * 1024 * 1024;

document.addEventListener("DOMContentLoaded", () => {

    const btn = document.getElementById("analyzeBtn");
    const resumeInput = document.getElementById("resume");
    const jobInput = document.getElementById("jobDescription");
    const uploadLabel = document.getElementById("uploadLabel");
    const uploadBtn = resumeInput.closest(".upload-btn");

    function resetResumeInput() {

        resumeInput.value = "";

        // Matches the default in index.html
        uploadLabel.innerText = "Choose a file";

        uploadBtn.classList.remove("has-file");

    }

    // Resume selection: validate against the limits the card advertises
    resumeInput.addEventListener("change", () => {

        const file = resumeInput.files[0];

        if (!file) {

            resetResumeInput();

            return;

        }

        if (!file.name.toLowerCase().endsWith(".pdf")) {

            showToast("Only PDF files are supported", "danger");

            resetResumeInput();

            return;

        }

        if (file.size > MAX_RESUME_BYTES) {

            const size = (file.size / 1024 / 1024).toFixed(1);

            showToast(
                `Resume is ${size} MB — the limit is 5 MB`,
                "danger"
            );

            resetResumeInput();

            return;

        }

        // Persistent state, since the toast disappears after 2.5s
        uploadLabel.innerText = file.name;

        uploadBtn.classList.add("has-file");

        showToast(`Resume added: ${file.name}`, "ok");

    });

    // Job description notification: fire once on crossing the threshold,
    // not on every keystroke past it
    let jobToastShown = false;

    jobInput.addEventListener("input", () => {

        const hasContent = jobInput.value.trim().length > 20;

        if (hasContent && !jobToastShown) {

            showToast("Job description added", "ok");

            jobToastShown = true;

        }
        else if (!hasContent) {

            jobToastShown = false;

        }

    });

    btn.addEventListener("click", async () => {

        // =============================
        // Validation
        // =============================

        if (!resumeInput.files[0]) {

            showToast("Add a resume to continue", "danger");
            return;

        }

        if (!jobInput.value.trim()) {

            showToast("Add a job description to continue", "danger");
            return;

        }

        // =============================
        // Reset State
        // =============================

        state.raw_resume = null;
        state.resume_analysis = null;
        state.job_analysis = null;
        state.gap_analysis = null;
        state.interview_analysis = null;
        state.learning_roadmap = null;
        state.market_analysis = null;
        state.cover_letter = null;
        state.error = null;
        state.loading = true;

        setLoading(true);

        // Mount the panel up front so the stage rail is visible from the
        // first second, rather than leaving the user on the empty state
        // until the first node reports
        resetResultView();
        renderNavigation(state);

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

                    // startStreaming() stops on error and never reaches
                    // onComplete, so loading has to be cleared here too
                    state.loading = false;

                    setLoading(false);

                    showToast(error, "danger");

                    renderNavigation(state);

                },

                onComplete() {

                    state.loading = false;

                    setLoading(false);

                    // Don't report success over a failed run
                    if (state.error) return;

                    showToast("Analysis complete", "ok");

                }

            });

        }
        catch (err) {

            console.error(err);

            state.loading = false;

            setLoading(false);

            showToast("Analysis failed", "danger");

        }

    });

});