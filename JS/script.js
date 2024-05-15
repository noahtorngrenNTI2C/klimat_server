const btn = document.querySelector("button");

function random(number) {
  return Math.floor(Math.random() * (number + 1));
}

btn.addEventListener("click", () => {
  const rndCol = `rgb(${random(255)} ${random(255)} ${random(255)})`;
  document.body.style.backgroundColor = rndCol;
});

function temperatur_read(){
  fetch('/tempRead')
    .then(response => response.text())
    .then(data => {
      document.getElementById('temperatur').textContent = data;
    })
}

function humidity_read(){
  fetch('/humRead')
    .then(response => response.text())
    .then(data => {
      document.getElementById('humidity').textContent = data;
    })
}

function rain_read(){
  fetch('rainRead')
    .then(response => response.text())
    .then(data => {
      document.getElementById('rain').textContent = data;
    })
}

