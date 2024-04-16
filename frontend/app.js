async function fetchJobVacancies() {
    try {
        const response = await fetch('https://job-api-cv1f.onrender.com/data/');
        if (!response.ok) {
            throw new Error('Failed to fetch job vacancies');
        }
        const vacancies = await response.json();
        displayVacancies(vacancies);
    } catch (error) {
        console.error('Error fetching job vacancies:', error.message);
    }
}

async function searchVacancies() {
    const searchInputCompany = document.getElementById('search-input-company').value;
    const searchInputPosition = document.getElementById('search-input-position').value;

    // Construct the base URL
    let url = 'https://job-api-cv1f.onrender.com/data/?';

    // Add company parameter if it's provided
    if (searchInputCompany) {
        url += `company=${encodeURIComponent(searchInputCompany)}&`;
    }

    // Add position parameter if it's provided
    if (searchInputPosition) {
        url += `position=${encodeURIComponent(searchInputPosition)}`;
    }

    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error('Failed to fetch job vacancies');
        }
        const vacancies = await response.json();
        displayVacancies(vacancies);
    } catch (error) {
        console.error('Error fetching job vacancies:', error.message);
    }
}

document.getElementById('search-button').addEventListener('click', searchVacancies);

window.onload = function () {
    fetchJobVacancies();
    toggleMode(); // Initially toggle mode to set the default mode
};

// Function to toggle between light and dark modes
function toggleMode() {
    const body = document.body;
    body.classList.toggle('light-mode'); // Toggle light mode
    body.classList.toggle('dark-mode'); // Toggle dark mode
}

// Event listener for mode toggle button
document.getElementById('toggle-mode-button').addEventListener('click', toggleMode);
