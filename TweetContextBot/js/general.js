/**
 * 
 * Loads Buttons onto each tweet
 * 
 * Note: Since Twitter loads content dynamically after the page loads, this pattern detects DOM subtree pattern changes
 * and triggers an event
 */
MutationObserver = window.MutationObserver || window.WebKitMutationObserver;

var observer = new MutationObserver(function(mutations, observer) {
    var tweets_bars = document.getElementsByClassName('r-1mdbhws');

    //Check if content has loaded
    if (tweets_bars.length != 0) {

        //Loop through tweet
        for (let bar of tweets_bars) {

            //Check if the button has already been appended to the tweet
            if (bar.getElementsByClassName('context-button').length > 0) continue;
            
            let container = document.createElement("div");
            container.className = "container-button css-1dbjc4n r-1mlwlqe r-18u37iz r-18kxxzh r-1h0z5md";
            container.addEventListener('click', function() {
                return getContent(container, event);
            });

            let content = document.createElement("span");
            content.innerHTML = "Get Background";
            content.className = "context-button css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0";
            
            container.appendChild(content);
            bar.appendChild(container);
        } 
    }
});
observer.observe(document, { subtree: true, attributes: true });

async function getContent(calling_container, e) {
    e.preventDefault(); 
    e.stopPropagation();

    var tweet_dom = calling_container.parentNode.parentNode.parentNode.childNodes[1].childNodes[0];
    var text = tweet_dom.innerText;

    const response = await fetch('http://localhost:5000/findContext', {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(text)
    })
    console.log(response.json())
}
