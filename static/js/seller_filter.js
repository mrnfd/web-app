// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    
    function registerSearchButtonHandler(){
        // Register event handler for search button
        const searchButton = document.getElementById('apply-filters')
        // when clicked retrive filtered content
        searchButton.addEventListener('click', async function(){
            const searchFilter = document.getElementById('search-value').value;

            const sellerPlaceholder = document.getElementById('sellers-listed')
            const url = new URL(window.location.href);
            url.search = ''; 
            
            // Smiða url bara þeir filterar sem voru include-aðir
            
            url.searchParams.append('search_filter', searchFilter || '');

            const response = await fetch(url);

            if (response.ok){

                // display filtered content
                const json = await response.json();
                if (json.sellers && Array.isArray(json.sellers)) {
                    const selleres = json.sellers.map(seller => `
                        
                        <div class="seller-card">
                            <img src="/static/${ seller.profile_image_url }" alt="Seller image">
                            <p class="seller-name">${seller.name}, ${seller.seller_type}<br /> </p>
                            {% if seller.address}
                                <p class="seller-name">${seller.name}, ${seller.seller_type}<br /></p> 
                            {% endif %}
                            <a href="/sellers/${seller.id}/"> See more </a>
                        </div>
                        
                    `);
                    
                    // Update the content with the filtered properties
                    sellerPlaceholder.innerHTML = selleres.join('');
                    
                } else {
                    console.error('No sellers match filter:', json);
                    propertyPlaceholder.innerHTML = '<p> No seller found matching your search.</p>';
                } 
            }
        });

    }
    registerSearchButtonHandler();
    
});

