// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    
    function registerSearchButtonHandler(){
        
        const searchButton = document.getElementById('apply-filters')
        
        searchButton.addEventListener('click', async function(){
            const searchFilter = document.getElementById('search-value').value;
            const sortBy = document.getElementById('status-filter').value;

            const offerPlaceholder = document.getElementById('offer-listed')
            const url = new URL(window.location.href);
            url.search = ''; 
            
            // Construct URL only with included filters
            url.searchParams.append('search_filter', searchFilter || '');
            url.searchParams.append('sort', sortBy || '');

            const response = await fetch(url);

            if (response.ok){
                
                const json = await response.json();
                if (json.offers && Array.isArray(json.offers)) {
                    const offerers = json.offers.map(offer => {
                        
                        let statusClass = 'pending';
                        let statusText = offer.status;

                        switch(offer.status) {
                            case 'REJECTED':
                                statusClass = 'rejected';
                                break;
                            case 'ACCEPTED':
                                statusClass = 'accepted';
                                break;
                            case 'CONTINGENT':
                                statusClass = 'contingent';
                                break;
                            default:
                                statusClass = 'pending';
                        }

                        return `
                        <div class="property-card">
                            <div class="property-content">
                                <img src="/static/${offer.thumbnail}" alt="Property image">
                                <div class="property-details">
                                    <a href="/catalogue/${offer.listing_id}"> 
                                        <strong>${offer.street} ${offer.house_numb}, ${offer.zip} ${offer.city}, ${offer.type}</strong>
                                    </a>

                                    <p>Date of submission: ${offer.submission_date}</p>
                                    <p>Expiration date: ${offer.expiration_date}</p>
                                    <p>Seller: ${offer.seller}</p>
                                    <p>Purchase offer price: ${offer.price}$</p>

                                    <p>Status: <span class="status ${statusClass}">${statusText}</span></p>
                                </div>
                            </div>

                            <div class="buttons">
                                <button type="button" id="cancel-btn">Delete offer</button>
                                <button type="button">Resubmit offer</button>
                                <button type="button" onclick="redirectToFinalize()">Finalize offer</button>
                            </div>
                        </div>
                    `});
                    
                    // Update the content with the filtered properties
                    offerPlaceholder.innerHTML = offerers.join('');
                    
                } else {
                    console.error('No offers match filter:', json);
                    offerPlaceholder.innerHTML = '<p>No offers found matching your filters.</p>';
                } 
            }
        });
    }
    registerSearchButtonHandler();

    const sortSelect = document.getElementById('status-filter');
    if (sortSelect) {
        sortSelect.addEventListener('change', function () {
            document.getElementById('apply-filters').click();
        });
    }
});