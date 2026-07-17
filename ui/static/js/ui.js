// =====================================
// TEMPLATE HELPERS
// =====================================

// Every renderer builds HTML by interpolating model output into
// template literals, so anything reaching the DOM must go through
// one of these two helpers first.

function escapeHtml(value) {

    if (value === null || value === undefined) return "";

    return String(value)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#39;");

}

// Use for any field the schema marks Optional - without this,
// a missing value interpolates as the literal string "null".
function text(value, fallback = "—") {

    if (
        value === null ||
        value === undefined ||
        String(value).trim() === ""
    ) {
        return fallback;
    }

    return escapeHtml(value);

}

window.escapeHtml = escapeHtml;
window.text = text;


// =====================================
// TOAST NOTIFICATION
// =====================================

const activeToasts = [];

function repositionToasts() {

    let offset = 20;

    for (const toast of activeToasts) {

        toast.style.bottom = `${offset}px`;

        offset += toast.offsetHeight + 10;

    }

}

// tone is semantic ("ok" | "danger" | "neutral"), not a colour -
// the palette lives in toast.css so both themes stay in step.
function showToast(message, tone = "neutral") {

    const toast = document.createElement("div");

    toast.className = `toast toast-${tone}`;

    toast.innerText = message;

    // Announce transient feedback to screen readers
    toast.setAttribute("role", "status");
    toast.setAttribute("aria-live", "polite");

    document.body.appendChild(toast);

    // Stack rather than pile up at an identical position
    activeToasts.push(toast);
    repositionToasts();

    requestAnimationFrame(() => {
        toast.classList.add("is-visible");
    });

    setTimeout(() => {

        toast.classList.remove("is-visible");

        setTimeout(() => {

            toast.remove();

            const index = activeToasts.indexOf(toast);

            if (index > -1) activeToasts.splice(index, 1);

            repositionToasts();

        }, 300);

    }, 2500);
}


// =====================================
// COPY TO CLIPBOARD
// =====================================

async function copyText(text) {

    try {

        await navigator.clipboard.writeText(text);

        showToast("Copied to clipboard", "ok");

    }
    catch (err) {

        console.error(err);

        showToast("Couldn't copy — try selecting the text", "danger");

    }

}


window.copyText = copyText;


// Copy buttons declare [data-copy-from="<element id>"] and the text is
// read back off the DOM, so generated content never has to survive a
// trip through an HTML attribute or a template literal.
// Delegated from document because renderNavigation() replaces the
// results panel wholesale and would discard element-level listeners.
document.addEventListener("click", (event) => {

    const button = event.target.closest("[data-copy-from]");

    if (!button) return;

    const source = document.getElementById(
        button.dataset.copyFrom
    );

    if (!source) {

        showToast("Nothing to copy", "danger");

        return;

    }

    copyText(source.innerText);

});


// =====================================
// BUTTON LOADING
// =====================================

function setLoading(isLoading) {

    const btn = document.getElementById("analyzeBtn");

    if (!btn) return;

    // Disabled styling is handled by .primary-btn:disabled
    btn.textContent = isLoading ? "Analyzing…" : "Analyze";
    btn.disabled = isLoading;

}


// Panel states live in navigation.js, which owns #result:
//   - empty state ships in the template
//   - streaming state is the stage rail, mounted on submit
//   - error state is the banner rendered into #errorSlot