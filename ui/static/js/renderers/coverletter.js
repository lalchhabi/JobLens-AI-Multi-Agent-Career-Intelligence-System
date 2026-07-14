function renderCoverLetter(data) {

    if (!data) return "";

    return `
    <div class="card">

        <h2>📨 Application Assistant</h2>

        <h3 class="content-title">📄 Cover Letter</h3>

        <div class="letter-box">
            ${data.full_cover_letter}
        </div>

        <button
            class="copy-btn"
            onclick="copyText(\`${data.full_cover_letter}\`)">

            📋 Copy Cover Letter

        </button>

        <hr class="divider">

        <h3 class="content-title">📧 Application Email</h3>

        <div class="letter-box">
            ${data.application_email}
        </div>

        <button
            class="copy-btn"
            onclick="copyText(\`${data.application_email}\`)">

            📋 Copy Email

        </button>

        <hr class="divider">

        <h3 class="content-title">💼 LinkedIn Message</h3>

        <div class="letter-box">
            ${data.linkedin_message}
        </div>

        <button
            class="copy-btn"
            onclick="copyText(\`${data.linkedin_message}\`)">

            📋 Copy LinkedIn Message

        </button>

    </div>
    `;
}