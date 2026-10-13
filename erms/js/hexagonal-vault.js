/**
 * Hexagonal Vault Component
 * Inspired by React Bits Pro (Hexagonal Grid lit by soft glowing light following the cursor)
 * Canvas 2D + interactive math for high performance and smooth animation
 */
(function () {
  function initHexVault() {
    var container = document.getElementById('hexagonal-vault-canvas');
    if (!container) return;

    var canvas = document.createElement('canvas');
    canvas.style.position = 'absolute';
    canvas.style.top = '0';
    canvas.style.left = '0';
    canvas.style.width = '100%';
    canvas.style.height = '100%';
    canvas.style.pointerEvents = 'none';
    container.appendChild(canvas);

    var ctx = canvas.getContext('2d');
    var dpr = Math.min(window.devicePixelRatio || 1, 2);

    var width, height;
    var mouse = { x: -1000, y: -1000, targetX: -1000, targetY: -1000, active: false };

    // Hexagon sizing
    var radius = 34; // hex outer radius
    var hexHeight = radius * 2;
    var hexWidth = Math.sqrt(3) * radius;
    var vertDist = hexHeight * 0.75;
    var horizDist = hexWidth;

    function resize() {
      width = window.innerWidth;
      height = window.innerHeight;
      canvas.width = width * dpr;
      canvas.height = height * dpr;
      ctx.scale(dpr, dpr);
    }
    window.addEventListener('resize', resize);
    resize();

    window.addEventListener('mousemove', function (e) {
      mouse.targetX = e.clientX;
      mouse.targetY = e.clientY;
      mouse.active = true;
    });

    window.addEventListener('mouseleave', function () {
      mouse.active = false;
    });

    function drawHexagon(cx, cy, r) {
      ctx.beginPath();
      for (var i = 0; i < 6; i++) {
        var angle = (Math.PI / 3) * i - Math.PI / 6;
        var x = cx + r * Math.cos(angle);
        var y = cy + r * Math.sin(angle);
        if (i === 0) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
      }
      ctx.closePath();
    }

    var time = 0;

    function animate() {
      requestAnimationFrame(animate);
      time += 0.02;

      // Smooth mouse easing
      if (mouse.active) {
        mouse.x += (mouse.targetX - mouse.x) * 0.1;
        mouse.y += (mouse.targetY - mouse.y) * 0.1;
      } else {
        // Subtle ambient wandering light when idle
        mouse.x = width / 2 + Math.cos(time * 0.5) * (width * 0.25);
        mouse.y = height / 2 + Math.sin(time * 0.4) * (height * 0.2);
      }

      ctx.clearRect(0, 0, width, height);

      // Deep dark futuristic background
      ctx.fillStyle = '#070b14';
      ctx.fillRect(0, 0, width, height);

      // Ambient radial background glow behind mouse
      var ambientGlow = ctx.createRadialGradient(
        mouse.x, mouse.y, 10,
        mouse.x, mouse.y, 450
      );
      ambientGlow.addColorStop(0, 'rgba(56, 189, 248, 0.15)');
      ambientGlow.addColorStop(0.4, 'rgba(99, 102, 241, 0.08)');
      ambientGlow.addColorStop(1, 'rgba(7, 11, 20, 0)');
      ctx.fillStyle = ambientGlow;
      ctx.fillRect(0, 0, width, height);

      var cols = Math.ceil(width / horizDist) + 2;
      var rows = Math.ceil(height / vertDist) + 2;

      var glowRadius = 260; // Light radius around cursor

      for (var r = -1; r < rows; r++) {
        for (var c = -1; c < cols; c++) {
          var cx = c * horizDist + ((r % 2 === 0) ? 0 : horizDist / 2);
          var cy = r * vertDist;

          var dx = cx - mouse.x;
          var dy = cy - mouse.y;
          var dist = Math.sqrt(dx * dx + dy * dy);

          var intensity = Math.max(0, 1 - dist / glowRadius);
          intensity = Math.pow(intensity, 1.8); // sharper falloff

          // Dynamic breathing wave
          var wave = Math.sin(time + cx * 0.005 + cy * 0.005) * 0.03;
          var baseAlpha = 0.07 + Math.max(0, wave);

          var totalAlpha = Math.min(1, baseAlpha + intensity * 0.85);

          if (intensity > 0.01) {
            // Hexagon fill glow
            ctx.fillStyle = 'rgba(56, 189, 248, ' + (intensity * 0.12) + ')';
            drawHexagon(cx, cy, radius - 2);
            ctx.fill();

            // Inner center light pulse dot
            ctx.beginPath();
            ctx.arc(cx, cy, 2 + intensity * 2.5, 0, Math.PI * 2);
            ctx.fillStyle = 'rgba(129, 140, 248, ' + (intensity * 0.9) + ')';
            ctx.fill();
          }

          // Hexagon stroke
          ctx.lineWidth = intensity > 0.05 ? 1.5 : 1;
          if (intensity > 0.2) {
            ctx.strokeStyle = 'rgba(56, 189, 248, ' + totalAlpha + ')';
          } else if (intensity > 0.02) {
            ctx.strokeStyle = 'rgba(99, 102, 241, ' + totalAlpha + ')';
          } else {
            ctx.strokeStyle = 'rgba(255, 255, 255, ' + baseAlpha + ')';
          }

          drawHexagon(cx, cy, radius - 2);
          ctx.stroke();
        }
      }
    }

    animate();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initHexVault);
  } else {
    initHexVault();
  }
})();
