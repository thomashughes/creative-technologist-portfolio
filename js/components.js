// ===================
// COMPONENTS.JS - Loads shared partials
// ===================

// Determine base path based on current location
function getBasePath() {
    const path = window.location.pathname;
    if (path.includes('/projects/')) {
        return '..';
    }
    return '.';
}

const basePath = getBasePath();

// Load Navigation
const navPlaceholder = document.getElementById('nav-placeholder');
if (navPlaceholder) {
    fetch(`${basePath}/partials/nav.html`)
        .then(response => {
            if (!response.ok) throw new Error('Nav not found');
            return response.text();
        })
        .then(html => {
            navPlaceholder.innerHTML = html;
            initNavHovers();
        })
        .catch(err => {
            console.error('Error loading nav:', err);
            // Fallback inline nav
            navPlaceholder.innerHTML = `
                <nav class="nav">
                    <div class="nav-logo"><a href="${basePath}/index.html">TH</a></div>
                    <div class="nav-links">
                        <a href="${basePath}/index.html#work">WORK</a>
                        <a href="${basePath}/index.html#about">ABOUT</a>
                        <a href="${basePath}/projects/creative-experiments.html">EXPERIMENTS</a>
                        <a href="${basePath}/index.html#contact">CONTACT</a>
                    </div>
                </nav>
            `;
        });
}

// Load Footer
const footerPlaceholder = document.getElementById('footer-placeholder');
if (footerPlaceholder) {
    fetch(`${basePath}/partials/footer.html`)
        .then(response => {
            if (!response.ok) throw new Error('Footer not found');
            return response.text();
        })
        .then(html => {
            footerPlaceholder.innerHTML = html;
        })
        .catch(err => {
            console.error('Error loading footer:', err);
            // Fallback inline footer
            footerPlaceholder.innerHTML = `
                <footer class="footer">
                    <div class="footer-left">© 2026 THOMAS HUGHES</div>
                    <div class="footer-center">TH</div>
                    <div class="footer-right">
                        <a href="https://tag-art.co.uk" class="footer-link" target="_blank">TAG-ART</a>
                    </div>
                </footer>
            `;
        });
}

// Initialize nav hover effects after loading
function initNavHovers() {
    const navLinks = document.querySelectorAll('.nav-links a, .nav-logo a');
    navLinks.forEach(link => {
        link.addEventListener('mouseenter', () => {
            const cursorRing = document.getElementById('cursorRing');
            if (cursorRing) cursorRing.classList.add('hovering');
        });
        link.addEventListener('mouseleave', () => {
            const cursorRing = document.getElementById('cursorRing');
            if (cursorRing) cursorRing.classList.remove('hovering');
        });
    });
}
