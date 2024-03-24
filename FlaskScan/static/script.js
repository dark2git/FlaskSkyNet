let currentLanguage = 'en'; // english is default

function checkDevices() {
    // show loader
    document.querySelector('.loader').style.display = 'flex';

    // clear previous res
    document.getElementById('deviceStatus').innerHTML = '';

    // hide rescan 
    document.getElementById('rescan').style.display = 'none';

    fetch('/check_devices')
        .then(response => response.text())
        .then(data => {
            const statuses = data.split('<br>'); 
            const deviceStatusElement = document.getElementById('deviceStatus');

            statuses.forEach(status => {
                const statusElement = document.createElement('div'); // create div
                statusElement.innerHTML = status; // set status
                if (status.includes('online')) {
                    statusElement.classList.add('online'); // add class 'online'
                } else if (status.includes('offline')) {
                    statusElement.classList.add('offline'); // add class 'offline'
                }
                deviceStatusElement.appendChild(statusElement);
            });

            // hide loader when its done
            document.querySelector('.loader').style.display = 'none';

            // show rescan btn
            document.getElementById('rescan').style.display = 'flex';
        })
        .catch(error => console.log(error));
}

// hide rescan btn
document.getElementById('rescan').style.display = 'none';

function changeLanguage(language) {
    currentLanguage = language; // change language
    let button = document.querySelector('.original-button');
    if (language === 'uk') {
        button.textContent = "Сканувати";
        document.getElementById('output').textContent = "Результати"; // change to "Результати"
    } else if (language === 'pl') {
        button.textContent = "Skanować";
        document.getElementById('output').textContent = "Wyniki"; // change to "Wyniki"
    } else if (language === 'en') {
        button.textContent = "Scan";
        document.getElementById('output').textContent = "Results"; // change to "Results"
    }
}

// add scroll to sections
function scrollToSection(sectionId) {
    var section = document.getElementById(sectionId);
    section.scrollIntoView({ behavior: 'smooth' });
}