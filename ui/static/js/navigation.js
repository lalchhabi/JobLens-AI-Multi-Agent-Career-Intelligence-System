const tabs = [
    {
        id: "resume",
        title: "📄 Resume",
        key: "resume_analysis",
        renderer: renderResume
    },
    {
        id: "gap",
        title: "📊 Gap Analysis",
        key: "gap_analysis",
        renderer: renderGap
    },
    {
        id: "interview",
        title: "🎯 Interview",
        key: "interview_analysis",
        renderer: renderInterview
    },
    {
        id: "roadmap",
        title: "📚 Roadmap",
        key: "learning_roadmap",
        renderer: renderRoadmap
    },
    {
        id: "market",
        title: "🌍 Market",
        key: "market_analysis",
        renderer: renderMarket
    },
    {
        id: "cover",
        title: "✉️ Cover Letter",
        key: "cover_letter",
        renderer: renderCoverLetter
    }
];

function renderNavigation(stateData = state) {

    const result = document.getElementById("result");

    const sidebar = tabs.map(tab => {

        const active =
            state.activePage === tab.id ? "active" : "";

        return `
            <button
                class="nav-btn ${active}"
                data-tab="${tab.id}">
                ${tab.title}
            </button>
        `;

    }).join("");

    result.innerHTML = `
        <div class="result-layout">

            <aside class="result-sidebar">

                ${sidebar}

            </aside>

            <section
                id="resultContent"
                class="result-content">

                ${renderCurrentTab(stateData)}

            </section>

        </div>
    `;

    document
        .querySelectorAll(".nav-btn")
        .forEach(button => {

            button.addEventListener("click", () => {

                state.activePage =
                    button.dataset.tab;

                renderNavigation(state);

            });

        });

}

function renderCurrentTab(data) {

    const tab = tabs.find(
        t => t.id === state.activePage
    );

    if (!tab) {

        return `
            <div class="card">

                <h2>Page not found</h2>

            </div>
        `;

    }

    const value = data[tab.key];

    if (!value) {

        return `
            <div class="card">

                <h2>${tab.title}</h2>

                <p>⏳ Waiting for this analysis...</p>

            </div>
        `;

    }

    return tab.renderer(value);

}

// Make available globally
window.renderNavigation = renderNavigation;