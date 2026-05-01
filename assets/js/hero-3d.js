
(function () {
  "use strict";

  const canvases = Array.from(document.querySelectorAll(".axiona-3d-canvas"));
  if (!canvases.length) return;

  const prefersReduced = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function createShader(gl, type, source) {
    const shader = gl.createShader(type);
    gl.shaderSource(shader, source);
    gl.compileShader(shader);
    if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) {
      throw new Error(gl.getShaderInfoLog(shader) || "Shader compile failed");
    }
    return shader;
  }

  function createProgram(gl, vs, fs) {
    const program = gl.createProgram();
    gl.attachShader(program, createShader(gl, gl.VERTEX_SHADER, vs));
    gl.attachShader(program, createShader(gl, gl.FRAGMENT_SHADER, fs));
    gl.linkProgram(program);
    if (!gl.getProgramParameter(program, gl.LINK_STATUS)) {
      throw new Error(gl.getProgramInfoLog(program) || "Program link failed");
    }
    return program;
  }

  function mat4Identity() {
    return [1,0,0,0, 0,1,0,0, 0,0,1,0, 0,0,0,1];
  }

  function mat4Multiply(a, b) {
    const out = new Array(16);
    for (let r = 0; r < 4; r++) {
      for (let c = 0; c < 4; c++) {
        out[c * 4 + r] =
          a[0 * 4 + r] * b[c * 4 + 0] +
          a[1 * 4 + r] * b[c * 4 + 1] +
          a[2 * 4 + r] * b[c * 4 + 2] +
          a[3 * 4 + r] * b[c * 4 + 3];
      }
    }
    return out;
  }

  function mat4Perspective(fovy, aspect, near, far) {
    const f = 1 / Math.tan(fovy / 2);
    const nf = 1 / (near - far);
    return [f/aspect,0,0,0, 0,f,0,0, 0,0,(far+near)*nf,-1, 0,0,(2*far*near)*nf,0];
  }

  function mat4Translate(tx, ty, tz) {
    return [1,0,0,0, 0,1,0,0, 0,0,1,0, tx,ty,tz,1];
  }

  function mat4RotateX(a) {
    const c = Math.cos(a), s = Math.sin(a);
    return [1,0,0,0, 0,c,s,0, 0,-s,c,0, 0,0,0,1];
  }

  function mat4RotateY(a) {
    const c = Math.cos(a), s = Math.sin(a);
    return [c,0,-s,0, 0,1,0,0, s,0,c,0, 0,0,0,1];
  }

  function mat4RotateZ(a) {
    const c = Math.cos(a), s = Math.sin(a);
    return [c,s,0,0, -s,c,0,0, 0,0,1,0, 0,0,0,1];
  }

  function init(canvas) {
    const gl = canvas.getContext("webgl", { antialias: true, alpha: true, powerPreference: "high-performance" });
    if (!gl) {
      canvas.classList.add("webgl-unavailable");
      return;
    }

    const vsColor = `
      attribute vec3 aPosition;
      attribute vec3 aColor;
      uniform mat4 uMVP;
      uniform float uPointSize;
      varying vec3 vColor;
      void main() {
        gl_Position = uMVP * vec4(aPosition, 1.0);
        gl_PointSize = uPointSize;
        vColor = aColor;
      }
    `;
    const fsColor = `
      precision mediump float;
      varying vec3 vColor;
      uniform float uAlpha;
      void main() {
        vec2 c = gl_PointCoord - vec2(0.5);
        float d = dot(c, c);
        if (gl_PointSize > 2.0 && d > 0.25) discard;
        gl_FragColor = vec4(vColor, uAlpha);
      }
    `;
    const vsTex = `
      attribute vec3 aPosition;
      attribute vec2 aUV;
      uniform mat4 uMVP;
      varying vec2 vUV;
      void main() {
        gl_Position = uMVP * vec4(aPosition, 1.0);
        vUV = aUV;
      }
    `;
    const fsTex = `
      precision mediump float;
      varying vec2 vUV;
      uniform sampler2D uTexture;
      uniform float uAlpha;
      void main() {
        vec4 tex = texture2D(uTexture, vUV);
        gl_FragColor = vec4(tex.rgb, tex.a * uAlpha);
      }
    `;

    const colorProgram = createProgram(gl, vsColor, fsColor);
    const texProgram = createProgram(gl, vsTex, fsTex);

    const positions = [
      // front
      -0.7,-0.7, 0.7,   0.7,-0.7, 0.7,   0.7, 0.7, 0.7,
      -0.7,-0.7, 0.7,   0.7, 0.7, 0.7,  -0.7, 0.7, 0.7,
      // back
      -0.7,-0.7,-0.7,  -0.7, 0.7,-0.7,   0.7, 0.7,-0.7,
      -0.7,-0.7,-0.7,   0.7, 0.7,-0.7,   0.7,-0.7,-0.7,
      // left
      -0.7,-0.7,-0.7,  -0.7,-0.7, 0.7,  -0.7, 0.7, 0.7,
      -0.7,-0.7,-0.7,  -0.7, 0.7, 0.7,  -0.7, 0.7,-0.7,
      // right
       0.7,-0.7,-0.7,   0.7, 0.7,-0.7,   0.7, 0.7, 0.7,
       0.7,-0.7,-0.7,   0.7, 0.7, 0.7,   0.7,-0.7, 0.7,
      // top
      -0.7, 0.7,-0.7,  -0.7, 0.7, 0.7,   0.7, 0.7, 0.7,
      -0.7, 0.7,-0.7,   0.7, 0.7, 0.7,   0.7, 0.7,-0.7,
      // bottom
      -0.7,-0.7,-0.7,   0.7,-0.7,-0.7,   0.7,-0.7, 0.7,
      -0.7,-0.7,-0.7,   0.7,-0.7, 0.7,  -0.7,-0.7, 0.7
    ];

    const colors = [];
    for (let i = 0; i < positions.length / 3; i++) {
      const face = Math.floor(i / 6);
      const palette = [
        [0.09, 0.85, 0.95],
        [0.10, 0.35, 0.46],
        [0.08, 0.75, 0.70],
        [0.15, 0.88, 0.54],
        [0.45, 0.95, 1.00],
        [0.04, 0.18, 0.24]
      ][face];
      colors.push(...palette);
    }

    function makeRing(radius, plane, color) {
      const arr = [];
      const segments = 144;
      for (let i = 0; i <= segments; i++) {
        const a = i / segments * Math.PI * 2;
        const x = Math.cos(a) * radius;
        const y = Math.sin(a) * radius;
        if (plane === "xy") arr.push(x, y, 0, ...color);
        if (plane === "xz") arr.push(x, 0, y, ...color);
        if (plane === "yz") arr.push(0, x, y, ...color);
      }
      return new Float32Array(arr);
    }

    function makeNodes() {
      const arr = [];
      const nodes = [
        [-1.35, .38, .28, 0.09, .85, .95],
        [ 1.32,-.22,-.18, 0.15, .88, .54],
        [.44, 1.12,.28, 0.45, .95, 1.00],
        [-.46,-1.08,-.36, 0.09, .85, .95],
        [.92,.68,-.62, 0.15, .88, .54],
        [-.96,-.68,.58, 0.45, .95, 1.00]
      ];
      nodes.forEach(n => arr.push(...n));
      return new Float32Array(arr);
    }

    const posBuffer = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, posBuffer);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(positions), gl.STATIC_DRAW);

    const colorBuffer = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, colorBuffer);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(colors), gl.STATIC_DRAW);

    const ringBuffers = [
      makeRing(1.34, "xy", [0.09, .85, .95]),
      makeRing(1.55, "xz", [0.15, .88, .54]),
      makeRing(1.76, "yz", [0.45, .95, 1.0])
    ].map(data => {
      const b = gl.createBuffer();
      gl.bindBuffer(gl.ARRAY_BUFFER, b);
      gl.bufferData(gl.ARRAY_BUFFER, data, gl.STATIC_DRAW);
      return { buffer: b, count: data.length / 6 };
    });

    const nodeData = makeNodes();
    const nodeBuffer = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, nodeBuffer);
    gl.bufferData(gl.ARRAY_BUFFER, nodeData, gl.STATIC_DRAW);

    const plane = new Float32Array([
      -0.43,-0.43,0.73, 0,1,
       0.43,-0.43,0.73, 1,1,
       0.43, 0.43,0.73, 1,0,
      -0.43,-0.43,0.73, 0,1,
       0.43, 0.43,0.73, 1,0,
      -0.43, 0.43,0.73, 0,0
    ]);
    const planeBuffer = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, planeBuffer);
    gl.bufferData(gl.ARRAY_BUFFER, plane, gl.STATIC_DRAW);

    const texture = gl.createTexture();
    gl.bindTexture(gl.TEXTURE_2D, texture);
    gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, 1, 1, 0, gl.RGBA, gl.UNSIGNED_BYTE, new Uint8Array([7, 16, 24, 255]));
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
    const image = new Image();
    image.onload = function () {
      gl.bindTexture(gl.TEXTURE_2D, texture);
      gl.pixelStorei(gl.UNPACK_PREMULTIPLY_ALPHA_WEBGL, true);
      gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, image);
    };
    image.src = canvas.dataset.icon || "assets/brand/r41/axiona-header-icon.png";

    let pointerX = 0;
    let pointerY = 0;
    const wrap = canvas.closest(".real-3d-panel") || canvas;
    wrap.addEventListener("pointermove", function (ev) {
      const rect = wrap.getBoundingClientRect();
      pointerX = ((ev.clientX - rect.left) / rect.width - 0.5) * 0.35;
      pointerY = ((ev.clientY - rect.top) / rect.height - 0.5) * 0.22;
    }, { passive: true });
    wrap.addEventListener("pointerleave", function () {
      pointerX = 0;
      pointerY = 0;
    }, { passive: true });

    function resize() {
      const dpr = Math.min(window.devicePixelRatio || 1, 2);
      const rect = canvas.getBoundingClientRect();
      const width = Math.max(320, Math.floor(rect.width * dpr));
      const height = Math.max(260, Math.floor(rect.height * dpr));
      if (canvas.width !== width || canvas.height !== height) {
        canvas.width = width;
        canvas.height = height;
      }
      gl.viewport(0, 0, canvas.width, canvas.height);
    }

    function bindColorAttributes(stride) {
      const aPosition = gl.getAttribLocation(colorProgram, "aPosition");
      const aColor = gl.getAttribLocation(colorProgram, "aColor");
      gl.enableVertexAttribArray(aPosition);
      gl.enableVertexAttribArray(aColor);
      gl.vertexAttribPointer(aPosition, 3, gl.FLOAT, false, stride, 0);
      gl.vertexAttribPointer(aColor, 3, gl.FLOAT, false, stride, 12);
    }

    function draw(now) {
      resize();
      const time = prefersReduced ? 0.8 : now * 0.001;
      gl.clearColor(0, 0, 0, 0);
      gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);
      gl.enable(gl.DEPTH_TEST);
      gl.enable(gl.BLEND);
      gl.blendFunc(gl.SRC_ALPHA, gl.ONE_MINUS_SRC_ALPHA);

      const aspect = canvas.width / canvas.height;
      const proj = mat4Perspective(Math.PI / 4.2, aspect, 0.1, 50);
      const view = mat4Translate(0, 0, -5.2);
      let model = mat4Identity();
      model = mat4Multiply(model, mat4RotateX(-0.34 + pointerY));
      model = mat4Multiply(model, mat4RotateY(time * 0.42 + pointerX));
      model = mat4Multiply(model, mat4RotateZ(Math.sin(time * 0.33) * 0.05));
      const mvp = mat4Multiply(proj, mat4Multiply(view, model));

      gl.useProgram(colorProgram);
      gl.uniformMatrix4fv(gl.getUniformLocation(colorProgram, "uMVP"), false, new Float32Array(mvp));

      gl.bindBuffer(gl.ARRAY_BUFFER, posBuffer);
      const aPosition = gl.getAttribLocation(colorProgram, "aPosition");
      gl.enableVertexAttribArray(aPosition);
      gl.vertexAttribPointer(aPosition, 3, gl.FLOAT, false, 0, 0);
      gl.bindBuffer(gl.ARRAY_BUFFER, colorBuffer);
      const aColor = gl.getAttribLocation(colorProgram, "aColor");
      gl.enableVertexAttribArray(aColor);
      gl.vertexAttribPointer(aColor, 3, gl.FLOAT, false, 0, 0);
      gl.uniform1f(gl.getUniformLocation(colorProgram, "uAlpha"), 0.26);
      gl.uniform1f(gl.getUniformLocation(colorProgram, "uPointSize"), 1.0);
      gl.drawArrays(gl.TRIANGLES, 0, positions.length / 3);

      gl.lineWidth(1);
      ringBuffers.forEach((r, idx) => {
        let ringModel = mat4Multiply(model, mat4RotateZ(time * (0.18 + idx * 0.05)));
        const ringMVP = mat4Multiply(proj, mat4Multiply(view, ringModel));
        gl.uniformMatrix4fv(gl.getUniformLocation(colorProgram, "uMVP"), false, new Float32Array(ringMVP));
        gl.bindBuffer(gl.ARRAY_BUFFER, r.buffer);
        bindColorAttributes(24);
        gl.uniform1f(gl.getUniformLocation(colorProgram, "uAlpha"), 0.36 - idx * 0.05);
        gl.uniform1f(gl.getUniformLocation(colorProgram, "uPointSize"), 1.0);
        gl.drawArrays(gl.LINE_STRIP, 0, r.count);
      });

      gl.uniformMatrix4fv(gl.getUniformLocation(colorProgram, "uMVP"), false, new Float32Array(mvp));
      gl.bindBuffer(gl.ARRAY_BUFFER, nodeBuffer);
      bindColorAttributes(24);
      gl.uniform1f(gl.getUniformLocation(colorProgram, "uAlpha"), 0.92);
      gl.uniform1f(gl.getUniformLocation(colorProgram, "uPointSize"), Math.max(5, canvas.width / 90));
      gl.drawArrays(gl.POINTS, 0, nodeData.length / 6);

      gl.useProgram(texProgram);
      gl.uniformMatrix4fv(gl.getUniformLocation(texProgram, "uMVP"), false, new Float32Array(mvp));
      gl.uniform1f(gl.getUniformLocation(texProgram, "uAlpha"), 0.96);
      gl.activeTexture(gl.TEXTURE0);
      gl.bindTexture(gl.TEXTURE_2D, texture);
      gl.uniform1i(gl.getUniformLocation(texProgram, "uTexture"), 0);
      gl.bindBuffer(gl.ARRAY_BUFFER, planeBuffer);
      const tPos = gl.getAttribLocation(texProgram, "aPosition");
      const tUV = gl.getAttribLocation(texProgram, "aUV");
      gl.enableVertexAttribArray(tPos);
      gl.enableVertexAttribArray(tUV);
      gl.vertexAttribPointer(tPos, 3, gl.FLOAT, false, 20, 0);
      gl.vertexAttribPointer(tUV, 2, gl.FLOAT, false, 20, 12);
      gl.drawArrays(gl.TRIANGLES, 0, 6);

      if (!prefersReduced) requestAnimationFrame(draw);
    }

    requestAnimationFrame(draw);
  }

  canvases.forEach(function (canvas) {
    try {
      init(canvas);
      canvas.classList.add("webgl-active");
    } catch (error) {
      canvas.classList.add("webgl-unavailable");
      console.warn("AXIONA 3D fallback:", error);
    }
  });
})();
