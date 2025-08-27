// script.js

document.addEventListener('DOMContentLoaded', () => {
    const tripsContainer = document.getElementById('trips-container');
    const addTripForm = document.getElementById('add-trip-form');
    const getStartedButton = document.getElementById('get-started');

    let trips = [];

    // Function to display trips
    function displayTrips() {
        tripsContainer.innerHTML = ''; // Clear existing trips
        trips.forEach((trip, index) => {
            const tripCard = document.createElement('div');
            tripCard.classList.add('trip-card');

            const img = document.createElement('img');
            img.src = trip.image || 'assets/productImage.jpg'; // Use a default image if none provided
            img.alt = trip.title;

            const h3 = document.createElement('h3');
            h3.textContent = trip.title;

            const destination = document.createElement('p');
            destination.textContent = `Destination: ${trip.destination}`;

            const date = document.createElement('p');
            date.textContent = `Date: ${trip.date}`;

            const description = document.createElement('p');
            description.textContent = trip.description;

            tripCard.appendChild(img);
            tripCard.appendChild(h3);
            tripCard.appendChild(destination);
            tripCard.appendChild(date);
            tripCard.appendChild(description);

            tripsContainer.appendChild(tripCard);
        });
    }

    // Function to handle form submission
    addTripForm.addEventListener('submit', (e) => {
        e.preventDefault();

        const title = document.getElementById('trip-title').value;
        const destination = document.getElementById('trip-destination').value;
        const date = document.getElementById('trip-date').value;
        const description = document.getElementById('trip-description').value;
        const image = document.getElementById('trip-image').value;

        const newTrip = {
            title: title,
            destination: destination,
            date: date,
            description: description,
            image: image
        };

        trips.push(newTrip);
        displayTrips();

        // Clear the form
        addTripForm.reset();
    });

    // Initial display of trips (if any)
    displayTrips();

    // Smooth scrolling for navigation
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();

            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // "Get Started" button functionality
    getStartedButton.addEventListener('click', () => {
        document.getElementById('add-trip').scrollIntoView({
            behavior: 'smooth'
        });
    });
});