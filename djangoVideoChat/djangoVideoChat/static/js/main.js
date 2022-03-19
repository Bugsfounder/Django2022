console.log("Hello JavaScript");

let labelUsername = document.getElementById('label-username');
let usernameInput = document.getElementById('username');
let btnJoin = document.getElementById("btn-join");

let username;

btnJoin.addEventListener('click', (e) => {
    username = usernameInput.value;

    console.log("username: ", username);

    if (username === "") {
        return;
    }
    usernameInput.value = ''
    usernameInput.disabled = true;
    usernameInput.style.visibility = 'hidden';

    btnJoin.disabled = true;
    btnJoin.style.visibility = 'hidden';

    labelUsername.innerText = username;

    let loc = window.location;
    let wsStart = "ws://";

    if (loc.protocol == 'https') {
        wsStart = 'wss://';
    }
});