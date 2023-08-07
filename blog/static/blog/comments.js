const pre = document.querySelector('pre');

function likeHandler(event) {
	event.preventDefault();

  // Get the element that was clicked on. It's the event
  // currentTarget property.
  const element = event.currentTarget;
  // This is an <a> tag and has a readable href property

  // Print out the result
  pre.textContent = 'PLEASE REFRESH THE PAGE TO SEE UPDATED LIKES AND DISLIKES.' + '\n';

  fetch(url=element.href, {
    method: 'POST',
    // Set the CSRF token header
    headers: { 'X-CSRFToken': csrftoken },
  });

}

// Select multiple classes: both like & dislike buttons
document.querySelectorAll('.like, .dislike')
	.forEach(function (link) {
		link.addEventListener('click', likeHandler);
	});