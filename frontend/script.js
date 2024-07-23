document.getElementById('increment-btn').addEventListener('click', function() {
    fetch('http://localhost:5555/counter/increment', { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            document.getElementById('counter').innerText = data.counter;
        });
});

function updateCounter() {
    fetch('http://localhost:5555/counter')
        .then(response => response.json())
        .then(data => {
            console.log(data);
            document.getElementById('counter').innerText = data.counter;
        });
}

updateCounter();
