/* ═══════════════════════════════════════════
   DEXMULTICHAIN — PREMIUM INTERACTIONS
   ═══════════════════════════════════════════ */

(function() {
  'use strict';

  // ── PARTICLE SYSTEM ──
  const canvas = document.getElementById('particleCanvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  let particles = [];
  let mouse = { x: -1000, y: -1000 };
  let animFrame;

  function resize() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  }
  resize();
  window.addEventListener('resize', resize);

  class Particle {
    constructor() {
      this.reset();
    }

    reset() {
      this.x = Math.random() * canvas.width;
      this.y = Math.random() * canvas.height;
      this.size = Math.random() * 1.5 + 0.5;
      this.speedX = (Math.random() - 0.5) * 0.3;
      this.speedY = (Math.random() - 0.5) * 0.3;
      this.opacity = Math.random() * 0.5 + 0.1;
      this.life = Math.random();
      this.decay = Math.random() * 0.005 + 0.002;
    }

    update() {
      this.x += this.speedX;
      this.y += this.speedY;
      this.life -= this.decay;

      // Mouse repulsion
      const dx = this.x - mouse.x;
      const dy = this.y - mouse.y;
      const dist = Math.sqrt(dx * dx + dy * dy);
      if (dist < 120) {
        const force = (120 - dist) / 120;
        this.x += dx * force * 0.02;
        this.y += dy * force * 0.02;
      }

      if (this.life <= 0 || this.x < -10 || this.x > canvas.width + 10 || this.y < -10 || this.y > canvas.height + 10) {
        this.reset();
      }
    }

    draw() {
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(124, 92, 252, ${this.opacity * this.life})`;
      ctx.fill();
    }
  }

  // Initialize particles
  const particleCount = Math.min(80, Math.floor(window.innerWidth / 20));
  for (let i = 0; i < particleCount; i++) {
    particles.push(new Particle());
  }

  // Draw connections
  function drawConnections() {
    for (let i = 0; i < particles.length; i++) {
      for (let j = i + 1; j < particles.length; j++) {
        const dx = particles[i].x - particles[j].x;
        const dy = particles[i].y - particles[j].y;
        const dist = Math.sqrt(dx * dx + dy * dy);

        if (dist < 120) {
          const opacity = (1 - dist / 120) * 0.08;
          ctx.beginPath();
          ctx.moveTo(particles[i].x, particles[i].y);
          ctx.lineTo(particles[j].x, particles[j].y);
          ctx.strokeStyle = `rgba(124, 92, 252, ${opacity})`;
          ctx.lineWidth = 0.5;
          ctx.stroke();
        }
      }
    }
  }

  function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    drawConnections();

    for (const p of particles) {
      p.update();
      p.draw();
    }

    animFrame = requestAnimationFrame(animate);
  }
  animate();

  // Mouse tracking
  document.addEventListener('mousemove', (e) => {
    mouse.x = e.clientX;
    mouse.y = e.clientY;
  });

  // ── INTERSECTION OBSERVER (Reveal on scroll) ──
  const revealElements = document.querySelectorAll('.reveal');

  if ('IntersectionObserver' in window) {
    const revealObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const delay = parseInt(entry.target.dataset.delay) || 0;
          setTimeout(() => {
            entry.target.classList.add('visible');
          }, delay);
          revealObserver.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.1,
      rootMargin: '0px 0px -50px 0px'
    });

    revealElements.forEach(el => revealObserver.observe(el));
  } else {
    // Fallback
    revealElements.forEach(el => el.classList.add('visible'));
  }

  // ── NAVBAR SCROLL EFFECT ──
  const navbar = document.querySelector('.navbar');
  let lastScroll = 0;

  window.addEventListener('scroll', () => {
    const scrollY = window.scrollY;

    if (scrollY > 50) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }

    lastScroll = scrollY;
  }, { passive: true });

  // ── COUNTER ANIMATION ──
  const counterElements = document.querySelectorAll('[data-count]');

  if ('IntersectionObserver' in window) {
    const counterObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const el = entry.target;
          const target = parseInt(el.dataset.count);
          const duration = 2000;
          const start = performance.now();

          function updateCounter(now) {
            const elapsed = now - start;
            const progress = Math.min(elapsed / duration, 1);
            const eased = 1 - Math.pow(1 - progress, 3);
            const current = Math.floor(eased * target);
            el.textContent = current.toLocaleString();

            if (progress < 1) {
              requestAnimationFrame(updateCounter);
            } else {
              el.textContent = target.toLocaleString();
            }
          }

          requestAnimationFrame(updateCounter);
          counterObserver.unobserve(el);
        }
      });
    }, { threshold: 0.5 });

    counterElements.forEach(el => counterObserver.observe(el));
  }

  // ── SMOOTH PARALLAX FOR MESH ORBS ──
  const orbs = document.querySelectorAll('.mesh-orb');

  document.addEventListener('mousemove', (e) => {
    const x = (e.clientX / window.innerWidth - 0.5) * 2;
    const y = (e.clientY / window.innerHeight - 0.5) * 2;

    orbs.forEach((orb, i) => {
      const speed = (i + 1) * 15;
      orb.style.transform = `translate(${x * speed}px, ${y * speed}px)`;
    });
  });

  // ── MOBILE MENU ──
  const mobileBtn = document.getElementById('mobileMenuBtn');
  const mobileMenu = document.getElementById('mobileMenu');

  if (mobileBtn && mobileMenu) {
    mobileBtn.addEventListener('click', () => {
      mobileBtn.classList.toggle('active');
      mobileMenu.classList.toggle('open');
    });

    mobileMenu.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        mobileBtn.classList.remove('active');
        mobileMenu.classList.remove('open');
      });
    });
  }

  // ── SCROLL PROGRESS INDICATOR ──
  const scrollProgress = document.createElement('div');
  scrollProgress.style.cssText = `
    position: fixed;
    top: 0; left: 0;
    height: 2px;
    background: linear-gradient(90deg, var(--accent), var(--accent2), var(--green));
    z-index: 9999;
    transition: width 0.1s linear;
    width: 0%;
  `;
  document.body.appendChild(scrollProgress);

  window.addEventListener('scroll', () => {
    const scrollTop = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const progress = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
    scrollProgress.style.width = progress + '%';
  }, { passive: true });

  // ── KEYBOARD SHORTCUTS ──
  document.addEventListener('keydown', (e) => {
    // Ctrl+K or Cmd+K to focus search (on scanner page)
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
      e.preventDefault();
      const searchInput = document.getElementById('caInput');
      if (searchInput) searchInput.focus();
    }
  });

  // ── PERFORMANCE: Pause particles when tab hidden ──
  document.addEventListener('visibilitychange', () => {
    if (document.hidden) {
      cancelAnimationFrame(animFrame);
    } else {
      animate();
    }
  });

})();
