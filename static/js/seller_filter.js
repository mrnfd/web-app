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

