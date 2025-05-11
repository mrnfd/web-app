// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    
    function registerSearchButtonHandler(){
        // Register event handler for search button
        const searchButton = document.getElementById('apply-filters')
        // when clicked retrive filtered content
        searchButton.addEventListener('click', async function(){
            const searchFilter = document.getElementById('search-value').value;
            const sortBy = document.getElementById('status-filter').value;

            const propertyPlaceholder = document.getElementById('offer-listed')
            const url = new URL(window.location.href);
            url.search = ''; 
            
            // Smiða url bara þeir filterar sem voru include-aðir
            
            url.searchParams.append('search_filter', searchFilter || '');
            url.searchParams.append('sort', sortBy || '');

            const response = await fetch(url);

            if (response.ok){

                // display filtered content
                const json = await response.json();
                if (json.offers && Array.isArray(json.offers)) {
                    const offerers = json.offers.map(offer => `
                        <div class="property-card">
                            <div class="property-content">
                                 <img src="https://i.pinimg.com/736x/d6/83/a0/d683a0dc882304dd58fa5d7c3038e096.jpg" alt="Property image">
                                <div class="property-details">
                                    <p><strong>Fjallastræti 2, 110 Reykjavík, Single family home</strong></p>
                                    <p><a href="#">Property details</a> </p>
                                    <p>Date of submission: ${offer.submission_date}</p>
                                    <p>Expiration date: ${offer.expiration_date}</p>
                                    <p>Seller: Mia Wong</p>
                                    <p>Purchase offer price: 200,000$</p>
                                    <p>Status: <span class="status pending">Pending</span></p>
                                </div>
                            </div>

                            <div class="buttons">
                                <button type="button" id="cancel-btn">Cancel offer</button>
                                <button type="button">Resubmit offer</button>
                                <button type="button" onclick="redirectToFinalize()">Finalize offer</button>
                            </div>
                        </div>
                    `);
                    
                    // Update the content with the filtered properties
                    propertyPlaceholder.innerHTML = offerers.join('');
                    
                } else {
                    console.error('No offers match filter:', json);
                    propertyPlaceholder.innerHTML = '<p> No offers found matching your filters.</p>';
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

