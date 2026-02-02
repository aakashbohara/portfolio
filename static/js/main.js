/*
===============================================
PROFESSIONAL PORTFOLIO - JAVASCRIPT
===============================================
*/

document.addEventListener('DOMContentLoaded', function() {

    // ============== NAVBAR SCROLL ==============
    const navbar = document.querySelector('.navbar');
    
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // ============== MOBILE MENU ==============
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const navbarMenu = document.querySelector('.navbar-menu');

    if (mobileMenuBtn && navbarMenu) {
        mobileMenuBtn.addEventListener('click', function() {
            this.classList.toggle('active');
            navbarMenu.classList.toggle('active');
        });

        document.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', () => {
                mobileMenuBtn.classList.remove('active');
                navbarMenu.classList.remove('active');
            });
        });
    }

    // ============== SMOOTH SCROLL ==============
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href !== '#') {
                e.preventDefault();
                const target = document.querySelector(href);
                if (target) {
                    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
            }
        });
    });

    // ============== TYPING EFFECT ==============
    const typingElement = document.querySelector('.typing-text');
    if (typingElement) {
        const texts = JSON.parse(typingElement.dataset.texts || '["Developer", "Designer", "Creator"]');
        let textIndex = 0;
        let charIndex = 0;
        let isDeleting = false;

        function type() {
            const currentText = texts[textIndex];
            
            if (isDeleting) {
                typingElement.textContent = currentText.substring(0, charIndex - 1);
                charIndex--;
            } else {
                typingElement.textContent = currentText.substring(0, charIndex + 1);
                charIndex++;
            }

            if (!isDeleting && charIndex === currentText.length) {
                setTimeout(() => isDeleting = true, 2000);
            } else if (isDeleting && charIndex === 0) {
                isDeleting = false;
                textIndex = (textIndex + 1) % texts.length;
            }

            setTimeout(type, isDeleting ? 50 : 100);
        }
        type();
    }

    // ============== SKILL BARS ANIMATION ==============
    const skillBars = document.querySelectorAll('.skill-progress');
    
    const animateSkills = () => {
        skillBars.forEach(bar => {
            const rect = bar.getBoundingClientRect();
            if (rect.top < window.innerHeight && rect.bottom > 0) {
                bar.style.width = bar.dataset.progress || bar.style.width;
            }
        });
    };

    window.addEventListener('scroll', animateSkills);
    animateSkills();

    // ============== COUNTER ANIMATION ==============
    const counters = document.querySelectorAll('.hero-stat-value, .counter');
    
    const animateCounter = (counter) => {
        const target = parseInt(counter.dataset.target || counter.textContent.replace(/\D/g, ''));
        const suffix = counter.dataset.suffix || '';
        const step = target / 125;
        let current = 0;

        const update = () => {
            current += step;
            if (current < target) {
                counter.textContent = Math.floor(current) + suffix;
                requestAnimationFrame(update);
            } else {
                counter.textContent = target + suffix;
            }
        };
        update();
    };

    const counterObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateCounter(entry.target);
                counterObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    counters.forEach(counter => counterObserver.observe(counter));

    // ============== PROJECT FILTER ==============
    const filterBtns = document.querySelectorAll('.filter-btn');
    const projectCards = document.querySelectorAll('.project-card');

    filterBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            filterBtns.forEach(b => b.classList.remove('active'));
            this.classList.add('active');
            
            const filter = this.dataset.filter;
            
            projectCards.forEach(card => {
                if (filter === 'all' || card.dataset.category === filter) {
                    card.style.display = 'block';
                    card.style.animation = 'fadeIn 0.5s ease';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    });

    // ============== SCROLL ANIMATIONS ==============
    const animateElements = document.querySelectorAll('.skill-card, .project-card, .service-card, .blog-card');
    
    const animateObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
                animateObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

    animateElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        animateObserver.observe(el);
    });

    // ============== BACK TO TOP ==============
    const backToTop = document.createElement('button');
    backToTop.className = 'back-to-top';
    backToTop.innerHTML = '<i class="fas fa-arrow-up"></i>';
    document.body.appendChild(backToTop);

    window.addEventListener('scroll', function() {
        backToTop.classList.toggle('visible', window.scrollY > 500);
    });

    backToTop.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));

    // ============== ALERT AUTO DISMISS ==============
    document.querySelectorAll('.alert').forEach(alert => {
        setTimeout(() => {
            alert.style.opacity = '0';
            setTimeout(() => alert.remove(), 300);
        }, 5000);
    });
});

// Dynamic styles
const style = document.createElement('style');
style.textContent = `
    .back-to-top {
        position: fixed; bottom: 100px; right: 30px;
        width: 50px; height: 50px;
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white; border: none; border-radius: 50%;
        cursor: pointer; opacity: 0; visibility: hidden;
        transition: all 0.3s ease; z-index: 998;
        display: flex; align-items: center; justify-content: center;
        box-shadow: 0 4px 20px rgba(102, 126, 234, 0.4);
    }
    .back-to-top.visible { opacity: 1; visibility: visible; }
    .back-to-top:hover { transform: translateY(-5px); }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
`;
document.head.appendChild(style);
