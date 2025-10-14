document.addEventListener("DOMContentLoaded", function() {
	const scroller = document.querySelector('.scroller-inner');
	if (!scroller) return;

	// Duplicate the content for seamless looping
	scroller.innerHTML += scroller.innerHTML;

	// Get the pixel width of the first set of cards
	const originalCards = Array.from(scroller.children).slice(0, scroller.children.length / 2);
	let firstSetWidth = 0;
	originalCards.forEach(card => {
		firstSetWidth += card.offsetWidth;
	});
	// Add gaps between cards
	const cardGap = parseInt(getComputedStyle(document.documentElement).getPropertyValue('--card-gap'));
	firstSetWidth += cardGap * (originalCards.length - 1);
	scroller.style.width = (firstSetWidth * 2) + "px";

	// Speed in px/sec, adjustable via CSS variable --scroller-speed (seconds for full scroll)
	const speed = firstSetWidth / parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--scroller-speed'));
	let pos = 0;
	let lastTimestamp = null;
	let paused = false;
	let animationFrameId;

	function step(timestamp) {
		if (paused) {
			animationFrameId = requestAnimationFrame(step);
			return;
		}
		if (!lastTimestamp) lastTimestamp = timestamp;
		const elapsed = (timestamp - lastTimestamp) / 1000; // seconds
		lastTimestamp = timestamp;
		pos -= speed * elapsed;
		if (Math.abs(pos) >= firstSetWidth) {
			pos += firstSetWidth;
		}
		scroller.style.transform = `translateX(${pos}px)`;
		animationFrameId = requestAnimationFrame(step);
	}

	// Pause/resume logic
	const scrollerContainer = document.querySelector('.scroller');
	if (scrollerContainer) {
		scrollerContainer.addEventListener('mouseenter', function() {
			paused = true;
		});
		scrollerContainer.addEventListener('mouseleave', function() {
			paused = false;
			lastTimestamp = null;
		});
		scrollerContainer.addEventListener('focusin', function() {
			paused = true;
		});
		scrollerContainer.addEventListener('focusout', function() {
			paused = false;
			lastTimestamp = null;
		});
	}

	animationFrameId = requestAnimationFrame(step);
});
