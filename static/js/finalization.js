document.addEventListener('DOMContentLoaded', function() {
        // Select the button to change contact info, if it exists
        const ChangeContactInfoBtn = document.querySelector(".back-contact-info-button");

        if (ChangeContactInfoBtn) {
            // Add click event to redirect to finalization page with the offer ID
            ChangeContactInfoBtn.addEventListener('click', function() {
                const offerID = this.getAttribute('data-id');
                window.location.href = `/transaction/${offerID}/finalization`;

            });
        }

    })

function showPaymentFields(method) {
    // Hide all payment method fields
    document.getElementById('credit-fields').style.display = 'none';
    document.getElementById('mortgage-fields').style.display = 'none';
    document.getElementById('bank-fields').style.display = 'none';

    // Show the fields for the selected payment method
    if (method === 'credit') {
      document.getElementById('credit-fields').style.display = 'block';
    } else if (method === 'mortgage') {
      document.getElementById('mortgage-fields').style.display = 'block';
    } else if (method === 'bank') {
      document.getElementById('bank-fields').style.display = 'block';
    }
  }

