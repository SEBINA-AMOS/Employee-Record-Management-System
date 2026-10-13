/**
 * Smooth Cursor Component
 * Inspired by React Bits Pro (Smooth, springy trailing cursor with interactive states)
 * Adds an ultra-fluid glowing cursor trail across the entire website
 */
(function () {
  function initSmoothCursor() {
    // Only on pointer devices (not pure touch)
    if (window.matchMedia('(pointer: coarse)').matches) return;

    var dot = document.createElement('div');
    dot.className = 'smooth-cursor-dot';

    var ring = document.createElement('div');
    ring.className = 'smooth-cursor-ring';

    var trailCount = 6;
    var trailDots = [];
    for (var i = 0; i < trailCount; i++) {
      var t = document.createElement('div');
      t.className = 'smooth-cursor-trail';
      document.body.appendChild(t);
      trailDots.push({ el: t, x: -100, y: -100 });
    }

    document.body.appendChild(dot);
    document.body.appendChild(ring);

    var mouse = { x: -100, y: -100 };
    var dotPos = { x: -100, y: -100 };
    var ringPos = { x: -100, y: -100 };
    var isHovering = false;
    var isClicking = false;
    var isVisible = false;

    window.addEventListener('mousemove', function (e) {
      mouse.x = e.clientX;
      mouse.y = e.clientY;
      if (!isVisible) {
        isVisible = true;
        dot.style.opacity = '1';
        ring.style.opacity = '1';
        trailDots.forEach(function (d) { d.el.style.opacity = '0.4'; });
      }
    });

    window.addEventListener('mousedown', function () {
      isClicking = true;
      ring.classList.add('cursor-clicking');
    });

    window.addEventListener('mouseup', function () {
      isClicking = false;
      ring.classList.remove('cursor-clicking');
    });

    window.addEventListener('mouseleave', function () {
      isVisible = false;
      dot.style.opacity = '0';
      ring.style.opacity = '0';
      trailDots.forEach(function (d) { d.el.style.opacity = '0'; });
    });

    // Detect hover over clickable elements
    function updateHoverState(e) {
      var target = e.target;
      var clickable = target.closest('a, button, input, select, textarea, .btn, .card, [role="button"]');
      if (clickable) {
        isHovering = true;
        ring.classList.add('cursor-hovering');
      } else {
        isHovering = false;
        ring.classList.remove('cursor-hovering');
      }
    }
    window.addEventListener('mouseover', updateHoverState);

    function render() {
      requestAnimationFrame(render);

      // Fast spring for center dot
      dotPos.x += (mouse.x - dotPos.x) * 0.45;
      dotPos.y += (mouse.y - dotPos.y) * 0.45;
      dot.style.transform = 'translate3d(' + dotPos.x + 'px, ' + dotPos.y + 'px, 0)';

      // Elastic spring for outer ring
      ringPos.x += (mouse.x - ringPos.x) * 0.16;
      ringPos.y += (mouse.y - ringPos.y) * 0.16;
      ring.style.transform = 'translate3d(' + ringPos.x + 'px, ' + ringPos.y + 'px, 0)';

      // Springy ribbon trail dots
      var prevX = dotPos.x;
      var prevY = dotPos.y;
      for (var i = 0; i < trailDots.length; i++) {
        var t = trailDots[i];
        t.x += (prevX - t.x) * (0.35 - i * 0.04);
        t.y += (prevY - t.y) * (0.35 - i * 0.04);
        var scale = Math.max(0.2, (1 - (i / trailCount) * 0.8));
        t.el.style.transform = 'translate3d(' + t.x + 'px, ' + t.y + 'px, 0) scale(' + scale + ')';
        prevX = t.x;
        prevY = t.y;
      }
    }

    render();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initSmoothCursor);
  } else {
    initSmoothCursor();
  }
})();
