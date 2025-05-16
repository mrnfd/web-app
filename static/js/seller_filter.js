// Run after the DOM is fully loaded
document.addEventListener('DOMContentLoaded', function() {
    
    function registerSearchButtonHandler(){
        const searchButton = document.getElementById('apply-filters')

        // When the search button is clicked, fetch filtered sellers
        searchButton.addEventListener('click', async function(){
            const searchFilter = document.getElementById('search-value').value;

            const sellerPlaceholder = document.getElementById('sellers-listed')
            const url = new URL(window.location.href);
            url.search = '';  // Clear existing query parameters
            
            // Append search filter parameter if present
            url.searchParams.append('search_filter', searchFilter || '');

            const response = await fetch(url);

            if (response.ok){
                const json = await response.json();
                if (json.sellers && Array.isArray(json.sellers)) {
                    // Build HTML for each seller
                    const selleres = json.sellers.map(seller => {

                        let agencyInfo = '';

                        switch(seller.seller_type) {
                            case 'Agency':
                                agencyInfo = `<p class="seller-address">${seller.city}, ${seller.street} ${seller.house_numb} <br /></p>`;
                                break;
                            default:
                                agencyInfo = '';
                        }
                        return`
                        <div class="seller-card">
                            <div class="seller-img">
                                <img src="/static/${ seller.profile_image_url }" alt="Seller image">
                            </div>
                            <div class="seller-info">
                                <p class="seller-name">${seller.name}</p>
                                <p class="seller-type">${seller.seller_type}</p>
                                ${agencyInfo}
                                <a href="/sellers/${seller.id}/"> See more </a>
                            </div>
                        </div>
                        
                    `});
                    
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

