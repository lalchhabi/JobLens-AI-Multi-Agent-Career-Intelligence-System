function renderCoverLetter(data) {

    if (!data) return "";

    // Each block renders its text once, escaped, and the copy button
    // points at it by id. The delegated handler in ui.js reads the text
    // back off the DOM, so generated content never has to survive being
    // embedded in an inline onclick attribute.
    const block = (id, heading, body, copyLabel) => `

        <h3 class="content-title">${heading}</h3>

        <div class="letter-box" id="${id}">${escapeHtml(body)}</div>

        <button
            class="copy-btn"
            type="button"
            data-copy-from="${id}">

            ${copyLabel}

        </button>
    `;

    return `
    <div class="card">

        <h2>Application materials</h2>

        ${block(
            "coverLetterText",
            "Cover letter",
            data.full_cover_letter,
            "Copy"
        )}

        <hr class="divider">

        ${block(
            "applicationEmailText",
            "Application email",
            data.application_email,
            "Copy"
        )}

        <hr class="divider">

        ${block(
            "linkedinMessageText",
            "LinkedIn message",
            data.linkedin_message,
            "Copy"
        )}

    </div>
    `;
}
