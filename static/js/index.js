document.querySelector("#main-form").addEventListener("submit", async (e) => {
    e.preventDefault();

    let response = await fetch("/attack", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            theme: document.querySelector("#theme").value,
            text: document.querySelector("#text").value,
            email_for_spam: document.querySelector("#email_for_spam").value,
            password: document.querySelector("#password").value,
            email: document.querySelector("#email").value,
            number_of_cycles: document.querySelector("#count").value
        }),
    });
});