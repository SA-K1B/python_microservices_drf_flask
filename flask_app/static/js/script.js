function fetchMealData() {
    // Fetching the data from the DRF API (your Django view)
    fetch(`http://127.0.0.1:5000/searched/list`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok: ' + response.statusText);
            }
            return response.json(); // Parse JSON response
        })
        .then(data => {
            // Get the 'meal-info' div
            const mealInfoDiv = document.getElementById('meal-info');
            
            // Clear any existing content in the 'meal-info' div
            mealInfoDiv.innerHTML = '';

            // Loop through all meals in the response and display them in Bootstrap cards
            data.meals.forEach(meal => {
                mealInfoDiv.innerHTML += `
                    <div class="card">
                        <img src="${meal.image}" class="card-img-top" alt="${meal.name}">
                        <div class="card-body">
                            <h5 class="card-title">${meal.name}</h5>
                            <p class="card-text">Category: ${meal.category}<br>Area: ${meal.area}</p>
                        </div>
                    </div>
                `;
            });
        })
        .catch(error => console.error('Error fetching data:', error));
}
window.onload = fetchMealData;