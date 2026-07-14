// =====================================
// TOAST NOTIFICATION
// =====================================

function showToast(message, color = "#333") {

    const toast = document.createElement("div");

    toast.innerText = message;

    toast.style.position = "fixed";
    toast.style.bottom = "20px";
    toast.style.right = "20px";
    toast.style.background = color;
    toast.style.color = "#fff";
    toast.style.padding = "12px 18px";
    toast.style.borderRadius = "10px";
    toast.style.fontSize = "14px";
    toast.style.boxShadow = "0 8px 25px rgba(0,0,0,.15)";
    toast.style.zIndex = "9999";
    toast.style.opacity = "0";
    toast.style.transition = "opacity .25s ease";

    document.body.appendChild(toast);

    requestAnimationFrame(() => {
        toast.style.opacity = "1";
    });

    setTimeout(() => {

        toast.style.opacity = "0";

        setTimeout(() => {
            toast.remove();
        }, 300);

    }, 2500);
}


// =====================================
// COPY TO CLIPBOARD
// =====================================

async function copyText(text) {

    try {

        await navigator.clipboard.writeText(text);

        showToast("Copied successfully ✔", "#2ecc71");

    }
    catch (err) {

        console.error(err);

        showToast("Failed to copy", "#e74c3c");

    }

}


// Make available for inline onclick handlers
window.copyText = copyText;


// =====================================
// BUTTON LOADING
// =====================================

function setLoading(isLoading) {

    const btn = document.getElementById("analyzeBtn");

    if (!btn) return;

    if (isLoading) {

        btn.innerHTML = "⏳ Analyzing...";
        btn.disabled = true;
        btn.style.opacity = "0.7";
        btn.style.cursor = "not-allowed";

    } else {

        btn.innerHTML = "🚀 Analyze Career Fit";
        btn.disabled = false;
        btn.style.opacity = "1";
        btn.style.cursor = "pointer";

    }

}


// =====================================
// EMPTY STATE
// =====================================

function showEmptyState(container) {

    container.innerHTML = `
        <div class="empty-state">
            <h3>🧠 JobLens AI</h3>
            <p>
                Upload your resume and job description to begin
                your AI career analysis.
            </p>
        </div>
    `;

}


// =====================================
// STREAM START
// =====================================

function showStreaming(container) {

    container.innerHTML = `
        <div class="card">
            <h3>⏳ Starting AI Analysis...</h3>
            <p>
                Please wait while JobLens AI analyzes your
                resume and the job description.
            </p>
        </div>
    `;

}


// =====================================
// ERROR STATE
// =====================================

function showError(container, message) {

    container.innerHTML = `
        <div class="card">
            <h2>❌ Analysis Failed</h2>
            <p>${message}</p>
        </div>
    `;

}