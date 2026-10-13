/**
 * Spectral Drape Component
 * Inspired by React Bits Pro (3D Glowing Drape of Dots Folding in Space)
 * Pure Three.js / WebGL implementation with interactive mouse physics and shader-like depth glow
 */
(function () {
  function initSpectralDrape() {
    // Look for existing container or automatically create one if missing
    var container = document.getElementById('spectral-drape-canvas');
    if (!container) {
      container = document.createElement('div');
      container.id = 'spectral-drape-canvas';
      document.body.insertBefore(container, document.body.firstChild);
    }

    // Load Three.js if not already present
    if (typeof THREE === 'undefined') {
      var script = document.createElement('script');
      script.src = 'https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js';
      script.onload = function () {
        setupScene(container);
      };
      document.head.appendChild(script);
    } else {
      setupScene(container);
    }
  }

  function setupScene(container) {
    if (container.dataset.initialized === 'true') return;
    container.dataset.initialized = 'true';

    var scene = new THREE.Scene();
    scene.fog = new THREE.FogExp2(0x070b14, 0.0016);

    var width = window.innerWidth;
    var height = window.innerHeight;

    var camera = new THREE.PerspectiveCamera(65, width / height, 1, 3000);
    camera.position.set(0, 140, 460);
    camera.lookAt(0, 0, 0);

    var renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.setSize(width, height);
    renderer.setClearColor(0x070b14, 1);
    container.appendChild(renderer.domElement);

    // Grid of dots forming the flexible cloth/drape
    var cols = 140;
    var rows = 90;
    var numParticles = cols * rows;

    var geometry = new THREE.BufferGeometry();
    var positions = new Float32Array(numParticles * 3);
    var colors = new Float32Array(numParticles * 3);
    var initialPositions = new Float32Array(numParticles * 3);

    var spacingX = 14;
    var spacingZ = 12;
    var startX = -(cols * spacingX) / 2;
    var startZ = -(rows * spacingZ) / 2;

    // Palette: Spectral neon colors (electric violet, cyan, azure, magenta, emerald)
    var c1 = new THREE.Color(0x6366f1); // Indigo
    var c2 = new THREE.Color(0x38bdf8); // Sky Cyan
    var c3 = new THREE.Color(0xd946ef); // Fuchsia / Magenta
    var c4 = new THREE.Color(0x10b981); // Emerald Green accent

    var idx = 0;
    for (var r = 0; r < rows; r++) {
      for (var c = 0; c < cols; c++) {
        var x = startX + c * spacingX;
        var y = 0;
        var z = startZ + r * spacingZ;

        positions[idx * 3] = x;
        positions[idx * 3 + 1] = y;
        positions[idx * 3 + 2] = z;

        initialPositions[idx * 3] = x;
        initialPositions[idx * 3 + 1] = y;
        initialPositions[idx * 3 + 2] = z;

        // Spectral gradient along the drape folds
        var u = c / cols;
        var v = r / rows;
        var mixedColor = new THREE.Color();

        if (u < 0.5) {
          mixedColor.lerpColors(c1, c2, u * 2);
        } else {
          mixedColor.lerpColors(c2, c3, (u - 0.5) * 2);
        }

        // Add depth variations
        mixedColor.lerp(c4, Math.sin(v * Math.PI) * 0.2);

        colors[idx * 3] = mixedColor.r;
        colors[idx * 3 + 1] = mixedColor.g;
        colors[idx * 3 + 2] = mixedColor.b;

        idx++;
      }
    }

    geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
    geometry.setAttribute('color', new THREE.BufferAttribute(colors, 3));

    // Circular glowing particle texture
    var canvasTexture = document.createElement('canvas');
    canvasTexture.width = 64;
    canvasTexture.height = 64;
    var ctx = canvasTexture.getContext('2d');
    var gradient = ctx.createRadialGradient(32, 32, 0, 32, 32, 32);
    gradient.addColorStop(0, 'rgba(255, 255, 255, 1)');
    gradient.addColorStop(0.2, 'rgba(220, 240, 255, 0.9)');
    gradient.addColorStop(0.6, 'rgba(99, 102, 241, 0.4)');
    gradient.addColorStop(1, 'rgba(0, 0, 0, 0)');
    ctx.fillStyle = gradient;
    ctx.fillRect(0, 0, 64, 64);

    var particleMap = new THREE.CanvasTexture(canvasTexture);

    var material = new THREE.PointsMaterial({
      size: 5.5,
      map: particleMap,
      vertexColors: true,
      transparent: true,
      opacity: 0.88,
      blending: THREE.AdditiveBlending,
      depthWrite: false
    });

    var particleSystem = new THREE.Points(geometry, material);
    particleSystem.rotation.x = -0.35;
    particleSystem.rotation.z = -0.15;
    scene.add(particleSystem);

    // Mouse interaction
    var mouse = { x: 0, y: 0, targetX: 0, targetY: 0 };
    window.addEventListener('mousemove', function (e) {
      mouse.targetX = (e.clientX - window.innerWidth / 2) * 0.15;
      mouse.targetY = (e.clientY - window.innerHeight / 2) * 0.15;
    });

    // Resize handler
    window.addEventListener('resize', function () {
      var w = window.innerWidth;
      var h = window.innerHeight;
      camera.aspect = w / h;
      camera.updateProjectionMatrix();
      renderer.setSize(w, h);
    });

    // Animation loop: Wave & drape folding physics
    var clock = new THREE.Clock();

    function animate() {
      requestAnimationFrame(animate);

      var elapsed = clock.getElapsedTime() * 0.85;

      // Smooth mouse follow
      mouse.x += (mouse.targetX - mouse.x) * 0.04;
      mouse.y += (mouse.targetY - mouse.y) * 0.04;

      camera.position.x = mouse.x * 0.4;
      camera.position.y = 140 - mouse.y * 0.3;
      camera.lookAt(0, 0, 0);

      var posAttr = geometry.attributes.position;
      var array = posAttr.array;

      for (var i = 0; i < numParticles; i++) {
        var ix = i * 3;
        var origX = initialPositions[ix];
        var origZ = initialPositions[ix + 2];

        // 3D drape folding math
        var wave1 = Math.sin(origX * 0.005 + elapsed * 1.8) * 45;
        var wave2 = Math.cos(origZ * 0.006 + elapsed * 1.4) * 35;
        var foldDrape = Math.sin((origX + origZ) * 0.004 + elapsed * 1.1) * 30;
        var microRipples = Math.sin(origX * 0.02 + elapsed * 3.0) * Math.cos(origZ * 0.02) * 8;

        // Cloth droop hanging in space
        var droop = -Math.cos(origX * 0.002) * 20;

        array[ix + 1] = wave1 + wave2 + foldDrape + microRipples + droop;
      }

      posAttr.needsUpdate = true;
      renderer.render(scene, camera);
    }

    animate();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initSpectralDrape);
  } else {
    initSpectralDrape();
  }
})();
