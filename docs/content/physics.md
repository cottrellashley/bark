---
title: "Physics Simulations"
description: "Interactive physics simulations and visualizations"
---

# Physics Simulations

This page contains interactive physics simulations built with HTML5 Canvas and JavaScript.

## Particle in a Box (2D)

This simulation demonstrates a quantum mechanical particle confined to a 2D box. The particle bounces elastically off the walls, maintaining constant kinetic energy.

<div id="particle-sim" style="text-align: center; margin: 2rem 0;">
  <canvas id="canvas" width="600" height="400" style="border: 2px solid #333; background: #000;"></canvas>
  <div style="margin-top: 1rem;">
    <button onclick="resetSimulation()" style="padding: 0.5rem 1rem; margin: 0.25rem; background: #007acc; color: white; border: none; border-radius: 4px; cursor: pointer;">Reset</button>
    <button onclick="togglePause()" style="padding: 0.5rem 1rem; margin: 0.25rem; background: #28a745; color: white; border: none; border-radius: 4px; cursor: pointer;">Pause/Resume</button>
    <button onclick="addParticle()" style="padding: 0.5rem 1rem; margin: 0.25rem; background: #ffc107; color: black; border: none; border-radius: 4px; cursor: pointer;">Add Particle</button>
  </div>
  <div id="info" style="margin-top: 1rem; font-family: monospace; font-size: 0.9rem; color: #666;">
    Particles: <span id="particleCount">1</span> | 
    Speed: <span id="speed">2.0</span> px/frame
  </div>
</div>

<script>
// Canvas setup
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
let particles = [];
let isPaused = false;
let animationId;

// Particle class
class Particle {
  constructor(x, y, vx, vy, radius = 8, color = null) {
    this.x = x || Math.random() * (canvas.width - 20) + 10;
    this.y = y || Math.random() * (canvas.height - 20) + 10;
    this.vx = vx || (Math.random() - 0.5) * 4;
    this.vy = vy || (Math.random() - 0.5) * 4;
    this.radius = radius;
    this.color = color || this.generateColor();
    this.trail = [];
    this.maxTrailLength = 50;
  }

  generateColor() {
    const hue = Math.random() * 360;
    return `hsl(${hue}, 70%, 60%)`;
  }

  update() {
    // Store current position for trail
    this.trail.push({ x: this.x, y: this.y });
    if (this.trail.length > this.maxTrailLength) {
      this.trail.shift();
    }

    // Update position
    this.x += this.vx;
    this.y += this.vy;

    // Bounce off walls (elastic collision)
    if (this.x <= this.radius || this.x >= canvas.width - this.radius) {
      this.vx = -this.vx;
      this.x = Math.max(this.radius, Math.min(canvas.width - this.radius, this.x));
    }
    if (this.y <= this.radius || this.y >= canvas.height - this.radius) {
      this.vy = -this.vy;
      this.y = Math.max(this.radius, Math.min(canvas.height - this.radius, this.y));
    }
  }

  draw() {
    // Draw trail
    if (this.trail.length > 1) {
      ctx.strokeStyle = this.color;
      ctx.lineWidth = 2;
      ctx.globalAlpha = 0.3;
      ctx.beginPath();
      ctx.moveTo(this.trail[0].x, this.trail[0].y);
      for (let i = 1; i < this.trail.length; i++) {
        const alpha = i / this.trail.length * 0.3;
        ctx.globalAlpha = alpha;
        ctx.lineTo(this.trail[i].x, this.trail[i].y);
      }
      ctx.stroke();
      ctx.globalAlpha = 1.0;
    }

    // Draw particle
    ctx.beginPath();
    ctx.arc(this.x, this.y, this.radius, 0, 2 * Math.PI);
    ctx.fillStyle = this.color;
    ctx.fill();
    ctx.strokeStyle = '#fff';
    ctx.lineWidth = 1;
    ctx.stroke();

    // Draw velocity vector
    ctx.strokeStyle = this.color;
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(this.x, this.y);
    ctx.lineTo(this.x + this.vx * 10, this.y + this.vy * 10);
    ctx.stroke();
  }
}

// Initialize simulation
function initSimulation() {
  particles = [new Particle()];
  updateInfo();
}

// Animation loop
function animate() {
  if (!isPaused) {
    // Clear canvas with fade effect
    ctx.fillStyle = 'rgba(0, 0, 0, 0.1)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // Update and draw particles
    particles.forEach(particle => {
      particle.update();
      particle.draw();
    });

    // Draw box boundaries
    ctx.strokeStyle = '#333';
    ctx.lineWidth = 2;
    ctx.strokeRect(0, 0, canvas.width, canvas.height);
  }
  
  animationId = requestAnimationFrame(animate);
}

// Control functions
function resetSimulation() {
  particles = [new Particle()];
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  updateInfo();
}

function togglePause() {
  isPaused = !isPaused;
}

function addParticle() {
  if (particles.length < 10) {
    particles.push(new Particle());
    updateInfo();
  }
}

function updateInfo() {
  document.getElementById('particleCount').textContent = particles.length;
  if (particles.length > 0) {
    const avgSpeed = particles.reduce((sum, p) => sum + Math.sqrt(p.vx * p.vx + p.vy * p.vy), 0) / particles.length;
    document.getElementById('speed').textContent = avgSpeed.toFixed(1);
  }
}

// Start simulation
initSimulation();
animate();

// Handle canvas clicks to add particles
canvas.addEventListener('click', (e) => {
  if (particles.length < 10) {
    const rect = canvas.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    particles.push(new Particle(x, y));
    updateInfo();
  }
});
</script>

## Simulation Features

- **Elastic Collisions**: Particles bounce off walls with perfect energy conservation
- **Particle Trails**: Visual trails show the path history of each particle
- **Velocity Vectors**: Lines extending from particles show their velocity direction
- **Interactive Controls**: Reset, pause/resume, and add particles
- **Click to Add**: Click anywhere on the canvas to add a new particle (max 10)

## Physics Concepts

This simulation demonstrates several key physics principles:

### Conservation of Energy
The total kinetic energy of the system remains constant as particles bounce elastically off the walls.

### Quantum Mechanics Analogy
While this is a classical simulation, it represents the concept of a "particle in a box" - a fundamental quantum mechanical system where a particle is confined to a region of space.

### Wave-Particle Behavior
The trail visualization helps illustrate how particle motion can create wave-like patterns over time, especially with multiple particles interacting with the boundaries.

---

*Try clicking on the simulation canvas to add more particles and observe how they interact with the boundaries and each other!*