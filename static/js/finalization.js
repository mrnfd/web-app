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