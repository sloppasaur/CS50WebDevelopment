// utilize local storage to accumulate counter
if (!localStorage.getItem('counter')) {
    localStorage.setItem('counter', 0);
}

function count() {
    let counter = localStorage.getItem('counter');  // grabs key for counter from the local storage
    counter++;
    document.querySelector('h1').innerHTML = counter;
    localStorage.setItem('counter', counter);       // sets the item counter to counter

}

document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('h1').innerHTML = localStorage.getItem('counter'); // refreshes the output on the page to local storage
    document.querySelector('button').onclick = count;

    // setInterval(count, 1000);
})