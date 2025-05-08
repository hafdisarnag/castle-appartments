document.addEventListener("DOMContentLoaded", function () {
    const searchButton = document.getElementById("search-button");
    const propertiesPlaceholder = document.getElementById("property-placeholder");

    async function runFilterSearch() {
        const address = document.getElementById("search-value").value;
        const postal = document.getElementById("postal").value;
        const minPrice = document.getElementById("minPrice").value;
        const maxPrice = document.getElementById("maxPrice").value;
        const type = document.getElementById("type").value;
        const rooms = document.getElementById("rooms").value;
        const sort = document.getElementById("sort").value;

        const params = new URLSearchParams();
        if (address) params.append("search_filter", address);
        if (postal) params.append("postal", postal);
        if (minPrice) params.append("min_price", minPrice);
        if (maxPrice) params.append("max_price", maxPrice);
        if (type) params.append("type", type);
        if (rooms) params.append("rooms", rooms);
        if (sort) params.append("sort", sort);

        const response = await fetch(`?${params.toString()}`);
        if (!response.ok) return;

        const json = await response.json();
        const properties = json.data.map(property => `
            <div class="property-item">
                <div class="property-image" style="background-image: url(${property.image})">
                    <div class="property-type">${property.type}</div>
                </div>
                <div class="property-info">
                    <h3>${property.address}</h3>
                    <div class="zip-city">${property.zip} ${property.city}</div>
                </div>
                <div class="line"></div>
                <div class="property-details">
                    <div class="property-detail">📐 ${property.size} m²</div>
                    <div class="property-detail">🛏 ${property.rooms}</div>
                    <div class="property-detail">🛁 ${property.bathrooms}</div>
                    <div class="property-detail">🛌 ${property.bedrooms}</div>
                </div>
                <div class="property-price">
                    <div>${property.price} kr.</div>
                    <a href="${property.id}">See more</a>
                </div>
            </div>
        `);
        propertiesPlaceholder.innerHTML = properties.join('');
    }

    if (searchButton) {
        searchButton.addEventListener("click", runFilterSearch);
    }
});
