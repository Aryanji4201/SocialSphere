document.addEventListener("DOMContentLoaded", () => {

    document.querySelectorAll(".like-btn").forEach(button => {

        button.addEventListener("click", async function (e) {

            e.preventDefault();

            const postId = this.dataset.post;

            const response = await fetch(`/api/like/${postId}`, {

                method: "POST"

            });

            const data = await response.json();

            this.innerHTML =
                `<i class="bi bi-heart-fill text-danger"></i> ${data.likes}`;

        });

    });

});