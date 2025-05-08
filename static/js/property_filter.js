document.addEventListener("DOMContentLoaded", function () {
    function registerSearchButtonHandler() {
        const searchButton = document.getElementById("search-icon");
        searchButton.addEventListener("click", async function () {
            const searchValueElement = document.getElementById("search-value");
            const propertiesPlaceholder = document.getElementById("property-placeholder");
            const value = searchValueElement.value;

            const response = await fetch(`?search_filter=${value}`);

            if (response.ok) {
                const json = await response.json();
                const properties = json.data.map(property => `
                        <div class="property-item">
                            <span class="heart-icon">🖤</span>
                            <div class="property-image" style="background-image: url(${ property.image })">
                                <div class="property-type">${ property.type }</div>
                            </div>
                            <div class="property-info">
                                <h3>${ property.address }</h3>
                                <div class="zip-city">${ property.zip } ${ property.city }</div>
                            </div>
                            <div class="line"></div>
                            <div class="property-details">
                                <div class="property-detail">📐 ${ property.size } m²</div>
                                <div class="property-detail">🛏 ${ property.rooms}</div>
                                <div class="property-detail">🛁 ${ property.bathrooms }</div>
                                <div class="property-detail">🛌 ${ property.bedrooms}}</div>
                            </div>
                            <div class="property-price">
                                <div>${ property.price} kr.</div>
                                <a href="${property.id}">See more</a>
                            </div>
                        </div>
                        
                    </div>`);
                propertiesPlaceholder.innerHTML = properties.join('');

            }
        })

    }
    registerSearchButtonHandler();
});