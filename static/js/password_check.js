document.querySelector(".registration-form").addEventListener("submit", function(event) {
        const pw = document.getElementById("user_pw").value;
        const confirmPw = document.getElementById("confirm_pw").value;

        if (pw !== confirmPw) {
            event.preventDefault();
            alert("Passwords do not match!");
        }
    });