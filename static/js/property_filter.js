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
                displayProperties(json.html);
            }

    }

    function displayProperties(propertiesHTML) {
        propertiesPlaceholder.innerHTML = propertiesHTML;
        if (typeof initializeFavorites === 'function') {
            initializeFavorites();
    }
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

            await runFilterSearch();
        });
    }

});
