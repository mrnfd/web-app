document.querySelector(".registration-form").addEventListener("submit", function(event) {
        const pw = document.getElementById("user_pw").value;
        const confirmPw = document.getElementById("confirm_pw").value;

        // Prevent form submission if passwords don't match
        if (pw !== confirmPw) {
            event.preventDefault();
            alert("Passwords do not match!");
        }
    });