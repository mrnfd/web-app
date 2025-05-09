// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    function registerSearchButtonHandler(){
        // Register event handler for search button
        const searchButton = document.getElementById('apply-filters')
        // when clicked retrive filtered content
        searchButton.addEventListener('click', async function(){
            const searchFilter = document.getElementById('search-value').value;
            const minPrice = document.getElementById('min-price-input').value;
            const maxPrice = document.getElementById('max-price-input').value;
            const propertyType = document.getElementById('property-filter').value;
            const moreFilter = document.getElementById('more-filter').value;

            const propertyPlaceholder = document.getElementById('properties-listed')
            const url = new URL(window.location.href);
            url.search = ''; 
            
            // Smiða url bara þeir filterar sem voru include-aðir
            //if (searchFilter) url.searchParams.append('search_filter', searchFilter);
            //if (minPrice) url.searchParams.append('min_price', minPrice);
            //if (maxPrice) url.searchParams.append('max_price', maxPrice);
            //if (propertyType) url.searchParams.append('type', propertyType);
            //if (moreFilter) url.searchParams.append('more', moreFilter);
            url.searchParams.append('search_filter', searchFilter || '');
            url.searchParams.append('min_price', minPrice || '');
            url.searchParams.append('max_price', maxPrice || '');
            url.searchParams.append('type', propertyType || '');
            url.searchParams.append('more', moreFilter || '');

            const response = await fetch(url);

            if (response.ok){

                // display filtered content
                const json = await response.json();
                if (json.propertys && Array.isArray(json.propertys)) {
                    const properties = json.propertys.map(property => `
                        <a href="/listing/${property.id}">
                            <div class="property-card">
                                <img src="https://via.placeholder.com/300x200" alt="Property image">
                                <div class="property-info">
                                    <p class="property-address">${property.street} ${property.number}, ${property.type}</p>
                                    <p class="property-address">${property.price}</p>
                                    <div class="rooms-seller">
                                        <span><strong>Rooms:</strong> ${property.numb_of_rooms}</span>
                                        <span><strong>Seller:</strong> ${property.seller_id}</span>
                                    </div>
                                </div>
                            </div>
                        </a>
                    `);
                    
                    // Update the content with the filtered properties
                    propertyPlaceholder.innerHTML = properties.join('');
                    
                } else {
                    console.error('No properties match filter:', json);
                    propertyPlaceholder.innerHTML = '<p> No properties found matching your filters.</p>';
                } 
            }
        });

    }
    registerSearchButtonHandler();
});