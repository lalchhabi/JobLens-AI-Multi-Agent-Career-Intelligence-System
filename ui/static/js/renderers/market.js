function renderMarket(market) {

    if (!market) return "";

    const items = (list) =>
        (list || [])
            .map(item => `<li>${escapeHtml(item)}</li>`)
            .join("");

    return `
    <div class="card">

        <h2>Market insights</h2>

        <h4>Similar Roles</h4>

        <ul>
            ${items(market.similar_roles)}
        </ul>

        <h4>Alternative Roles</h4>

        <ul>
            ${items(market.alternative_roles)}
        </ul>

        <h4>Trending Skills</h4>

        <div class="tags">

            ${(market.trending_skills || [])
                .map(s => `<span class="tag">${escapeHtml(s)}</span>`)
                .join("")}

        </div>

        <p>

            <strong>Summary:</strong>

            ${text(market.market_summary, "No summary available.")}

        </p>

    </div>
    `;
}
