document.addEventListener('DOMContentLoaded', function() { 

    // Tab functionality 

    const tabs = document.querySelectorAll('.tab'); 

    tabs.forEach(tab => { 

        tab.addEventListener('click', function() { 

            tabs.forEach(t => t.classList.remove('active')); 

            this.classList.add('active'); 

        }); 

    }); 

 

    // Search functionality 

    const searchInput = document.querySelector('.search-input'); 

    if (searchInput) { 

        searchInput.addEventListener('input', function(e) { 

            const searchTerm = e.target.value.toLowerCase(); 

            const cards = document.querySelectorAll('.card'); 

             

            cards.forEach(card => { 

                const title = card.querySelector('.card-title')?.textContent.toLowerCase() || ''; 

                const description = card.querySelector('.card-description')?.textContent.toLowerCase() || ''; 

                 

                if (title.includes(searchTerm) || description.includes(searchTerm)) { 

                    card.style.display = 'flex'; 

                } else { 

                    card.style.display = 'none'; 

                } 

            }); 

        }); 

    } 

 

    // Card hover effects 

    const cards = document.querySelectorAll('.card'); 

    cards.forEach(card => { 

        card.addEventListener('mouseenter', function() { 

            this.style.transition = 'all 0.3s ease'; 

        }); 

    }); 

 

    // Progress bar animation for explorer cards 

    const progressBars = document.querySelectorAll('.progress-bar'); 

    progressBars.forEach((bar, index) => { 

        setTimeout(() => { 

            bar.style.transition = 'width 1s ease-out'; 

        }, index * 100); 

    }); 

 

    // Smooth scroll behavior 

    document.querySelectorAll('a[href^="#"]').forEach(anchor => { 

        anchor.addEventListener('click', function (e) { 

            e.preventDefault(); 

            const target = document.querySelector(this.getAttribute('href')); 

            if (target) { 

                target.scrollIntoView({ 

                    behavior: 'smooth', 

                    block: 'start' 

                }); 

            } 

        }); 

    }); 

 

    // Copilot button removed; no-op

 

    // Card click navigation + analytics
    const homeCards = document.querySelectorAll('.home-card');
    homeCards.forEach(card => {
        card.addEventListener('click', function(e) {
            const title = this.querySelector('.card-title')?.textContent;
            const href = this.getAttribute('data-href');
            console.log(`Card clicked: ${title}`);
            // Add analytics tracking here
            if (href) window.location.href = href;
        });
    });

}); 

 

// Utility function for debouncing 

function debounce(func, wait) { 

    let timeout; 

    return function executedFunction(...args) { 

        const later = () => { 

            clearTimeout(timeout); 

            func(...args); 

        }; 

        clearTimeout(timeout); 

        timeout = setTimeout(later, wait); 

    }; 

} 

 



const debouncedSearch = debounce((searchTerm) => { 

    console.log('Searching for:', searchTerm); 



}, 300); 


function gotoSection(url) {
    if (!url) return;
    window.location.href = url;
}