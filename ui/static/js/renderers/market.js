function renderMarket(market) {

    if (!market) return "";

    return `
    <div class="card">

        <h2>🌍 Market Insights</h2>

        <h4>Similar Roles</h4>

        <ul>
            ${(market.similar_roles || [])
                .map(r => `<li>${r}</li>`)
                .join("")}
        </ul>

        <h4>Alternative Roles</h4>

        <ul>
            ${(market.alternative_roles || [])
                .map(r => `<li>${r}</li>`)
                .join("")}
        </ul>

        <h4>Trending Skills</h4>

        <div class="tags">

            ${(market.trending_skills || [])
                .map(s => `<span class="tag">${s}</span>`)
                .join("")}

        </div>

        <p>

            <strong>Summary:</strong>

            ${market.market_summary}

        </p>

    </div>
    `;
}