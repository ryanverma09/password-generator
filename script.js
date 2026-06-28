const BACKEND_URL = "https://password-generator-dfv9.onrender.com";

function handleButtonClick(event) {
    const clickedButtonID = event.target.id;
    const newPasswordSection = document.getElementById("new_password_section");
    const recallPasswordSection = document.getElementById("recall_password_section");
    const savedPasswordSection = document.getElementById("saved_passwords");
    const backButtonSection = document.getElementById("back-button-section");
    const landingMenuButton = document.getElementById("landing_menu");

    if (clickedButtonID === "new-password") {
        newPasswordSection.style.display = "flex";
        recallPasswordSection.style.display = "none";
        savedPasswordSection.style.display = "none";
        backButtonSection.style.display = "flex";
        landingMenuButton.style.display = "none";
    }
    else if (clickedButtonID === "recall-password") {
        newPasswordSection.style.display = "none";
        recallPasswordSection.style.display = "flex";
        savedPasswordSection.style.display = "none";
        backButtonSection.style.display = "flex";
        landingMenuButton.style.display = "none";
    }
    else if (clickedButtonID === "saved-password") {
        newPasswordSection.style.display = "none";
        recallPasswordSection.style.display = "none";
        savedPasswordSection.style.display = "flex";
        backButtonSection.style.display = "flex";
        landingMenuButton.style.display = "none";
    }
    else if (clickedButtonID === "back-button") {
        newPasswordSection.style.display = "none";
        recallPasswordSection.style.display = "none";
        savedPasswordSection.style.display = "none";
        backButtonSection.style.display = "none";
        landingMenuButton.style.display = "flex";
    }
}

// Create password form
const createForm = document.getElementById('create-password-form');
createForm.addEventListener('submit', async function(event) {
    event.preventDefault();
    const called_length = document.getElementById("password_len").value;
    const called_name = document.getElementById("web_name").value;

    try {
        const response = await fetch(`${BACKEND_URL}/create-password?site_input=${called_name}&pass_len=${called_length}`, { method: "POST" });
        const data = await response.json();
        document.getElementById("success_message").innerHTML = data.generated;
        createForm.reset();
    } catch (err) {
        console.error('API error:', err);
        document.getElementById("success_message").innerHTML = "Something went wrong. Please try again.";
    }
});

// Recall password form
const recallForm = document.getElementById('recall-password-form');
recallForm.addEventListener('submit', async function(event) {
    event.preventDefault();
    const called_website = document.getElementById("recalled_website").value;

    try {
        const response = await fetch(`${BACKEND_URL}/fetch-password?website_name=${called_website}`);
        const data = await response.json();
        const w = String(data.website_name).toWellFormed();
        const formattedWebsite = w.charAt(0).toUpperCase() + w.slice(1);
        document.getElementById("fetched_password").innerHTML = `${formattedWebsite} : ${data.decryped}`;
        recallForm.reset();
    } catch (err) {
        console.error('API error:', err);
        document.getElementById("fetched_password").innerHTML = "Something went wrong. Please try again.";
    }
});

// Load saved websites on page load
const websites_contain = document.getElementById('stored_websites');
fetch(`${BACKEND_URL}/password-library`)
    .then(response => response.json())
    .then(data => {
        const websites = data.websites;
        for (const website of websites) {
            if(website.length != 0) {
                // Handle empty website names if necessary
                const h5_website = document.createElement("h5");
                h5_website.textContent = website;
                websites_contain.appendChild(h5_website);
            }
        }
    })
    .catch(err => {
        console.error('Failed to load password library:', err);
        websites_contain.innerHTML = "<p>Could not load saved websites.</p>";
    });