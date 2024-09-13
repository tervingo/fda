// smooth-scroll.js
document.addEventListener('DOMContentLoaded', function() {
    const headerHeight = document.querySelector('header#banner').offsetHeight;

    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();

            const targetId = this.getAttribute('href');
            const target = document.querySelector(targetId);
            
            if (target) {
                const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - headerHeight;

                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });

                // Optionally update URL
                history.pushState(null, '', targetId);
            }
        });
    });
});