// Run code after the DOM is fully loaded
document.addEventListener('DOMContentLoaded', function() {
    
    function registerSearchButtonHandler(){
        // Attach click event to the "apply filters" button
        const searchButton = document.getElementById('apply-filters')
        searchButton.addEventListener('click', async function(){
            // Get filter values from the inputs
            const searchFilter = document.getElementById('search-value').value;
            const minPrice = document.getElementById('min-price-input').value;
            const maxPrice = document.getElementById('max-price-input').value;
            const propertyType = document.getElementById('property-filter').value;
            const moreFilter = document.getElementById('more-filter').value;
            const sortBy = document.getElementById('sort-button').value;

            const propertyPlaceholder = document.getElementById('properties-listed')
            const url = new URL(window.location.href);
            url.search = '';  // clear existing query parameters
            
             // Append only active filters to the URL
            url.searchParams.append('search_filter', searchFilter || '');
            url.searchParams.append('min_price', minPrice || '');
            url.searchParams.append('max_price', maxPrice || '');
            url.searchParams.append('type', propertyType || '');
            url.searchParams.append('more', moreFilter || '');
            url.searchParams.append('sort', sortBy || '');

            // Fetch filtered properties from the server specifically as AJAX
            
            const response = await fetch(url, {
                headers: {
                    'X-Requested-With': 'XMLHttpRequest' 
                }
            });

            if (response.ok){
                const json = await response.json();
                if (json.propertys && Array.isArray(json.propertys)) {
                    // Build HTML for each property and update the page
                    const properties = json.propertys.map(property => {
                        let statusclass = "status available";
                        
                        switch (property.status) {
                            case 'AVAILABLE': 
                                statusclass = "status available";
                                break;
                            case 'PENDING':
                                statusclass = "status pending";
                                break;
                            case 'SOLD':
                                statusclass = "status sold";
                                break;
                        }
                        return`
                        <a href="/catalogue/${property.id}">
                            <div class="property-card">
                                <img src="/static/${ property.thumbnail }" alt="Property image">
                                <div class="property-info">
                                    <p class="property-address">${property.street} ${property.number}, ${property.type}</p>
                                    <p class="property-address">Price: $${property.price}</p>
                                    <p><strong>Listing status: </strong> <span class="${statusclass}">${property.status}</span></p>
                                    <div class="rooms-seller">
                                        <span><strong>Rooms:</strong> ${property.numb_of_rooms}</span>
                                        <span><strong>Seller:</strong> ${property.seller}</span>
                                    </div>
                                </div>
                            </div>
                        </a>
                    `});

                    propertyPlaceholder.innerHTML = properties.join('');
                    
                } else {
                    // Handle case where no properties match filters
                    console.error('No properties match filter:', json);
                    propertyPlaceholder.innerHTML = '<p> No properties found matching your filters.</p>';
                } 
            }
        });

    }
    registerSearchButtonHandler();

    // Trigger filter application when sort option changes
    const sortSelect = document.getElementById('sort-button');
    if (sortSelect) {
        sortSelect.addEventListener('change', function () {
            document.getElementById('apply-filters').click();
        });
    }
    
    const urlParams = new URLSearchParams(window.location.search);
    const searchValue = urlParams.get('search_filter');
    
    if (searchValue) {
      const input = document.getElementById('search-value');
      if (input) input.value = searchValue;

      const button = document.getElementById('apply-filters');
      if (button) button.click();
    }
});


