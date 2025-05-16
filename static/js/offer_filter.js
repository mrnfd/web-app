document.addEventListener('DOMContentLoaded', function () {
    // Initialize event handlers
    registerSearchButtonHandler();
    bindFinalizeOfferButtons();

    // Redirect helper functions
    function redirectToDelete(offerID) {
        window.location.href = `/offers/delete_offer/${offerID}`;

    }
    function redirectToUpdate(offerID) {
        window.location.href = `/offers/update_offer/${offerID}`;

    }

     // Trigger filter application when status filter changes
    const sortSelect = document.getElementById('status-filter');
    if (sortSelect) {
        sortSelect.addEventListener('change', function () {
            document.getElementById('apply-filters').click();
        });
    }

    // Register the search/filter button click event
    function registerSearchButtonHandler() {
        const searchButton = document.getElementById('apply-filters');

        searchButton.addEventListener('click', async function () {
            const searchFilter = document.getElementById('search-value').value;
            const sortBy = document.getElementById('status-filter').value;

            const offerPlaceholder = document.getElementById('offer-listed');
            const url = new URL(window.location.href);
            url.search = '';  // Clear existing query parameters

            // Append active filters to URL
            url.searchParams.append('search_filter', searchFilter || '');
            url.searchParams.append('sort', sortBy || '');

            const response = await fetch(url);

            if (response.ok) {
                const json = await response.json();
                if (json.offers && Array.isArray(json.offers)) {
                    // Build the HTML for each offer
                    const offerers = json.offers.map(offer => {
                        let statusClass = 'pending';

                        switch (offer.status) {
                            case 'REJECTED': statusClass = 'rejected'; break;
                            case 'ACCEPTED': statusClass = 'accepted'; break;
                            case 'CONTINGENT': statusClass = 'contingent'; break;
                        }

                        return `
                        <div class="property-card">
                            <div class="property-content">
                                <img src="/static/${offer.thumbnail}" alt="Property image">
                                <div class="property-details">
                                    <a href="/catalogue/${offer.listing_id}">
                                        <strong>${offer.street} ${offer.housenumber || ''}, ${offer.zip} ${offer.city}, ${offer.type}</strong>
                                    </a>
                                    <p>Date of submission: ${offer.submission_date}</p>
                                    <p>Expiration date: ${offer.expiration_date}</p>
                                    <p>Seller: ${offer.seller}</p>
                                    <p>Purchase offer price: ${offer.price}$</p>
                                    <p>Status: <span class="status ${statusClass}">${offer.status}</span></p>
                                </div>
                            </div>
                            <div class="buttons">
                                <button data-id1 = "${offer.id}" type="button" class="delete-offer-button" >Delete offer</button>
                                
                                
                                ${offer.button}
                            </div>
                        </div>`;
                    });

                     // Update page with offers
                    offerPlaceholder.innerHTML = offerers.join('');
                    // Re-bind buttons added dynamically
                    bindFinalizeOfferButtons(); 
                } else {
                    offerPlaceholder.innerHTML = '<p>No offers found matching your filters.</p>';
                }
            }
        });
    }

    // Attach click handlers to dynamic buttons for finalize, delete, and edit
    function bindFinalizeOfferButtons() {
        document.querySelectorAll(".finalize-offer-button").forEach(button => {
            button.addEventListener('click', function () {
                const offerID = this.getAttribute('data-id');
                window.location.href = `/transaction/${offerID}/finalization`;
            });
        });
        document.querySelectorAll(".delete-offer-button").forEach(button => {
            button.addEventListener('click', function () {
                const offerID = this.getAttribute('data-id1');
                window.location.href = `/offers/delete_offer/${offerID}`;
            });
        });
        document.querySelectorAll(".edit-offer-button").forEach(button => {
            button.addEventListener('click', function () {
                const offerID = this.getAttribute('data-id2');
                window.location.href = `/offers/update_offer/${offerID}`;
            });
        });
    }
});