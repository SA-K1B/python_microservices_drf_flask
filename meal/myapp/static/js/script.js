function fetchMealData() {
    const categoryName = document.getElementById('categoryName').value;
    
    // Fetching the data from the DRF API (your Django view)
    fetch(`http://127.0.0.1:8080/${categoryName}`)
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
                        <img src="${meal.strMealThumb}" class="card-img-top" alt="${meal.strMeal}">
                        <div class="card-body">
                            <h5 class="card-title">${meal.strMeal}</h5>
                            <p class="card-text">Category: ${meal.strCategory}<br>Area: ${meal.strArea}</p>
                        </div>
                    </div>
                `;
            });
        })
        .catch(error => console.error('Error fetching data:', error));
}