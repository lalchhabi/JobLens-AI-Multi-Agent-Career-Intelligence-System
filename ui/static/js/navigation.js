// =====================================
// PIPELINE STAGES
// =====================================

// Mirrors the graph topology in graph/workflow.py:
//
//   parser -> resume -> job -> gap -> ┬-> interview ─┬-> roadmap
//                                     ├-> market  ───┘
//                                     └-> cover_letter
//
// We only ever learn which nodes have *reported*. Everything else is
// derived: a stage is running once all of its dependencies have landed
// and it hasn't itself. Keep `deps` in step with the edges in
// workflow.py or the rail will misreport what's in flight.

const STAGES = [
    { key: "raw_resume",         label: "Parsing resume",        deps: [] },
    { key: "resume_analysis",    label: "Resume profile",        deps: ["raw_resume"] },
    { key: "job_analysis",       label: "Job requirements",      deps: ["resume_analysis"] },
    { key: "gap_analysis",       label: "Skill gap",             deps: ["job_analysis"] },
    { key: "interview_analysis", label: "Interview prep",        deps: ["gap_analysis"] },
    { key: "market_analysis",    label: "Market insights",       deps: ["gap_analysis"] },
    { key: "cover_letter",       label: "Application materials", deps: ["gap_analysis"] },
    { key: "learning_roadmap",   label: "Learning roadmap",      deps: ["interview_analysis", "market_analysis"] }
];


// =====================================
// TABS
// =====================================

const tabs = [
    {
        id: "resume",
        title: "Resume",
        key: "resume_analysis",
        renderer: renderResume
    },
    {
        id: "job",
        title: "Job",
        key: "job_analysis",
        renderer: renderJob
    },
    {
        id: "gap",
        title: "Gap analysis",
        key: "gap_analysis",
        renderer: renderGap
    },
    {
        id: "interview",
        title: "Interview",
        key: "interview_analysis",
        renderer: renderInterview
    },
    {
        id: "roadmap",
        title: "Roadmap",
        key: "learning_roadmap",
        renderer: renderRoadmap
    },
    {
        id: "market",
        title: "Market",
        key: "market_analysis",
        renderer: renderMarket
    },
    {
        id: "cover",
        title: "Application",
        key: "cover_letter",
        renderer: renderCoverLetter
    }
];


// =====================================
// RENDER BOOKKEEPING
// =====================================

// The panel is built once per analysis and patched in place after that.
// Rebuilding it on every SSE event would reset the reader's scroll
// position and selection roughly eight times per run.

let shellMounted = false;
let renderedTab = null;
let renderedPayload = undefined;


function stageStatus(stage, data) {

    if (data[stage.key]) return "done";

    // A failed run leaves everything downstream permanently unreported
    if (data.error) return "stopped";

    const ready = stage.deps.every(dep => data[dep]);

    return ready ? "running" : "pending";

}


function mountShell() {

    const result = document.getElementById("result");

    result.innerHTML = `
        <div id="stageRail" class="stage-rail">

            <div class="stage-rail-head">

                <span
                    class="stage-rail-title"
                    id="stageSummary"
                    role="status"
                    aria-live="polite"></span>

            </div>

            <ol class="stages">

                ${STAGES.map(stage => `
                    <li class="stage is-pending" data-stage="${stage.key}">

                        <span class="stage-dot" aria-hidden="true"></span>

                        <span class="stage-label">${stage.label}</span>

                    </li>
                `).join("")}

            </ol>

        </div>

        <div id="errorSlot"></div>

        <div class="result-layout">

            <aside
                class="result-sidebar"
                id="resultSidebar"
                role="tablist"
                aria-label="Analysis sections">

                ${tabs.map(tab => `
                    <button
                        class="nav-btn"
                        role="tab"
                        type="button"
                        aria-selected="false"
                        data-tab="${tab.id}">

                        <span class="nav-btn-title">${tab.title}</span>

                        <span class="nav-btn-state" aria-hidden="true"></span>

                    </button>
                `).join("")}

            </aside>

            <section
                id="resultContent"
                class="result-content"
                role="tabpanel"></section>

        </div>
    `;

    // Delegated so the listener survives content updates
    document
        .getElementById("resultSidebar")
        .addEventListener("click", (event) => {

            const button = event.target.closest(".nav-btn");

            if (!button) return;

            state.activePage = button.dataset.tab;

            renderNavigation(state);

        });

    shellMounted = true;
    renderedTab = null;
    renderedPayload = undefined;

}


function updateRail(data) {

    let done = 0;

    for (const stage of STAGES) {

        const status = stageStatus(stage, data);

        if (status === "done") done++;

        const element = document.querySelector(
            `[data-stage="${stage.key}"]`
        );

        if (element) element.className = `stage is-${status}`;

    }

    const summary = document.getElementById("stageSummary");

    if (!summary) return;

    if (data.error) {

        summary.textContent =
            `Stopped after ${done} of ${STAGES.length} stages`;

    }
    else if (done === STAGES.length) {

        summary.textContent =
            `Analysis complete · ${STAGES.length} agents finished`;

    }
    else {

        summary.textContent =
            `Analyzing… ${done} of ${STAGES.length} stages complete`;

    }

}


function updateTabs(data) {

    for (const tab of tabs) {

        const button = document.querySelector(
            `.nav-btn[data-tab="${tab.id}"]`
        );

        if (!button) continue;

        const isActive = data.activePage === tab.id;

        button.classList.toggle("active", isActive);
        button.classList.toggle("is-ready", Boolean(data[tab.key]));
        button.setAttribute("aria-selected", String(isActive));

    }

}


function updateError(data) {

    const slot = document.getElementById("errorSlot");

    if (!slot) return;

    // A failure can arrive after some agents have already reported, so
    // show it alongside whatever landed rather than replacing it
    slot.innerHTML = data.error
        ? `
            <div class="card error-card">

                <h2>Analysis failed</h2>

                <p>${escapeHtml(data.error)}</p>

            </div>
        `
        : "";

}


function renderActiveTab(data) {

    const content = document.getElementById("resultContent");

    if (!content) return;

    const tab = tabs.find(t => t.id === data.activePage);

    const payload = tab ? data[tab.key] : null;

    // Skip the rewrite unless this tab's own data changed. Payload
    // identity is a sound check: app.js assigns a fresh object into
    // state only for the key an event carries.
    if (tab && tab.id === renderedTab && payload === renderedPayload) {
        return;
    }

    renderedTab = tab ? tab.id : null;
    renderedPayload = payload;

    if (!tab) {

        content.innerHTML = `
            <div class="card">

                <h2>Page not found</h2>

            </div>
        `;

        return;

    }

    if (!payload) {

        content.innerHTML = `
            <div class="card">

                <h2>${tab.title}</h2>

                <p>Waiting for this agent to report…</p>

            </div>
        `;

        return;

    }

    content.innerHTML = tab.renderer(payload);

}


function renderNavigation(stateData = state) {

    if (!shellMounted) mountShell();

    updateRail(stateData);
    updateTabs(stateData);
    updateError(stateData);
    renderActiveTab(stateData);

}


// Called when a new analysis starts so the next render rebuilds cleanly
function resetResultView() {

    shellMounted = false;
    renderedTab = null;
    renderedPayload = undefined;

}


// Make available globally
window.renderNavigation = renderNavigation;
window.resetResultView = resetResultView;
