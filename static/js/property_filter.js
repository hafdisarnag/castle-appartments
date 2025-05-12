document.addEventListener("DOMContentLoaded", function () {
    const searchButton = document.getElementById("search-button");
    const clearButton = document.getElementById("clear-button");
    const propertiesPlaceholder = document.getElementById("property-placeholder");

    async function runFilterSearch() {
        const params = new URLSearchParams();

        const address = document.getElementById("search-value").value;
        const postal = document.getElementById("postal").value;
        const minPrice = document.getElementById("minPrice").value;
        const maxPrice = document.getElementById("maxPrice").value;
        const type = document.getElementById("type").value;
        const rooms = document.getElementById("rooms").value;
        const sort = document.getElementById("sort").value;

        if (address) params.append("search_filter", address);
        if (postal) params.append("postal", postal);
        if (minPrice) params.append("min_price", minPrice);
        if (maxPrice) params.append("max_price", maxPrice);
        if (type) params.append("type", type);
        if (rooms) params.append("rooms", rooms);
        if (sort) params.append("sort", sort);

        const response = await fetch(`?${params.toString()}`);
        if (response.ok) {
            const json = await response.json();
            displayProperties(json.data);
        }
    }

    function displayProperties(properties) {
        if (properties.length === 0) {
            propertiesPlaceholder.innerHTML = `<div>No properties found.</div>`;
            return;
        }

        const items = properties.map(property => `
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
        propertiesPlaceholder.innerHTML = items.join('');
    }

    if (searchButton) {
        searchButton.addEventListener("click", runFilterSearch);
    }

    if (clearButton) {
        clearButton.addEventListener("click", async () => {
            document.getElementById("postal").value = "";
            document.getElementById("minPrice").value = "";
            document.getElementById("maxPrice").value = "";
            document.getElementById("type").value = "";
            document.getElementById("rooms").value = "";
            document.getElementById("search-value").value = "";
            document.getElementById("sort").value = "Price: low to high";

            // Call the same search function to reload all properties
            await runFilterSearch();
        });
    }

    // Optionally trigger initial search on page load if needed:
    // runFilterSearch();
});
