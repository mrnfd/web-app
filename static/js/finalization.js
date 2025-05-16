document.addEventListener('DOMContentLoaded', function() {
        const ChangeContactInfoBtn = document.querySelector(".back-contact-info-button");
        console.log("THIS WAS RUNN")
        if (ChangeContactInfoBtn) {
            console.log("THIS WAS RUNN")
            ChangeContactInfoBtn.addEventListener('click', function() {
                const offerID = this.getAttribute('data-id');

                window.location.href = `/transaction/${offerID}/finalization`;

            });
        }

    })

function showPaymentFields(method) {
    // Hide all
    document.getElementById('credit-fields').style.display = 'none';
    document.getElementById('mortgage-fields').style.display = 'none';
    document.getElementById('bank-fields').style.display = 'none';

    // Show the selected one
    if (method === 'credit') {
      document.getElementById('credit-fields').style.display = 'block';
    } else if (method === 'mortgage') {
      document.getElementById('mortgage-fields').style.display = 'block';
    } else if (method === 'bank') {
      document.getElementById('bank-fields').style.display = 'block';
    }
  }

