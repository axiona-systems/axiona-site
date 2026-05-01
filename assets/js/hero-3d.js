
(function () {
  "use strict";

  const canvases = Array.from(document.querySelectorAll(".axiona-3d-canvas"));
  if (!canvases.length) return;

  const reduced = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function shader(gl, type, src) {
    const s = gl.createShader(type);
    gl.shaderSource(s, src);
    gl.compileShader(s);
    if (!gl.getShaderParameter(s, gl.COMPILE_STATUS)) {
      throw new Error(gl.getShaderInfoLog(s) || "shader compile failed");
    }
    return s;
  }

  function program(gl, vs, fs) {
    const p = gl.createProgram();
    gl.attachShader(p, shader(gl, gl.VERTEX_SHADER, vs));
    gl.attachShader(p, shader(gl, gl.FRAGMENT_SHADER, fs));
    gl.linkProgram(p);
    if (!gl.getProgramParameter(p, gl.LINK_STATUS)) {
      throw new Error(gl.getProgramInfoLog(p) || "program link failed");
    }
    return p;
  }

  function perspective(fov, aspect, near, far) {
    const f = 1 / Math.tan(fov / 2);
    const nf = 1 / (near - far);
    return [f/aspect,0,0,0, 0,f,0,0, 0,0,(far+near)*nf,-1, 0,0,(2*far*near)*nf,0];
  }

  function multiply(a, b) {
    const o = new Array(16);
    for (let r = 0; r < 4; r++) {
      for (let c = 0; c < 4; c++) {
        o[c*4+r] = a[0*4+r]*b[c*4+0] + a[1*4+r]*b[c*4+1] + a[2*4+r]*b[c*4+2] + a[3*4+r]*b[c*4+3];
      }
    }
    return o;
  }

  function translate(x,y,z){return [1,0,0,0, 0,1,0,0, 0,0,1,0, x,y,z,1];}
  function rotateX(a){const c=Math.cos(a),s=Math.sin(a);return [1,0,0,0, 0,c,s,0, 0,-s,c,0, 0,0,0,1];}
  function rotateY(a){const c=Math.cos(a),s=Math.sin(a);return [c,0,-s,0, 0,1,0,0, s,0,c,0, 0,0,0,1];}
  function rotateZ(a){const c=Math.cos(a),s=Math.sin(a);return [c,s,0,0, -s,c,0,0, 0,0,1,0, 0,0,0,1];}

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
      void main(){
        gl_Position = uMVP * vec4(aPosition, 1.0);
        gl_PointSize = uPointSize;
        vColor = aColor;
      }
    `;
    const fsColor = `
      precision mediump float;
      varying vec3 vColor;
      uniform float uAlpha;
      uniform float uIsPoint;
      void main(){
        if (uIsPoint > 0.5) {
          vec2 c = gl_PointCoord - vec2(0.5);
          if (dot(c,c) > 0.25) discard;
        }
        gl_FragColor = vec4(vColor, uAlpha);
      }
    `;
    const vsTex = `
      attribute vec3 aPosition;
      attribute vec2 aUV;
      uniform mat4 uMVP;
      varying vec2 vUV;
      void main(){
        gl_Position = uMVP * vec4(aPosition, 1.0);
        vUV = aUV;
      }
    `;
    const fsTex = `
      precision mediump float;
      varying vec2 vUV;
      uniform sampler2D uTexture;
      uniform float uAlpha;
      void main(){
        vec4 t = texture2D(uTexture, vUV);
        gl_FragColor = vec4(t.rgb, t.a * uAlpha);
      }
    `;

    const colorP = program(gl, vsColor, fsColor);
    const texP = program(gl, vsTex, fsTex);

    const cube = new Float32Array([
      -0.74,-0.74, 0.74, 0.09,0.85,0.95,   0.74,-0.74, 0.74, 0.12,0.72,0.75,   0.74, 0.74, 0.74, 0.15,0.88,0.54,
      -0.74,-0.74, 0.74, 0.09,0.85,0.95,   0.74, 0.74, 0.74, 0.15,0.88,0.54,  -0.74, 0.74, 0.74, 0.45,0.95,1.00,
      -0.74,-0.74,-0.74, 0.02,0.12,0.18,  -0.74, 0.74,-0.74, 0.04,0.22,0.27,   0.74, 0.74,-0.74, 0.07,0.30,0.35,
      -0.74,-0.74,-0.74, 0.02,0.12,0.18,   0.74, 0.74,-0.74, 0.07,0.30,0.35,   0.74,-0.74,-0.74, 0.03,0.18,0.22,
      -0.74,-0.74,-0.74, 0.04,0.24,0.28,  -0.74,-0.74, 0.74, 0.09,0.85,0.95,  -0.74, 0.74, 0.74, 0.45,0.95,1.00,
      -0.74,-0.74,-0.74, 0.04,0.24,0.28,  -0.74, 0.74, 0.74, 0.45,0.95,1.00, -0.74, 0.74,-0.74, 0.04,0.22,0.27,
       0.74,-0.74,-0.74, 0.03,0.18,0.22,   0.74, 0.74,-0.74, 0.07,0.30,0.35,   0.74, 0.74, 0.74, 0.15,0.88,0.54,
       0.74,-0.74,-0.74, 0.03,0.18,0.22,   0.74, 0.74, 0.74, 0.15,0.88,0.54,   0.74,-0.74, 0.74, 0.12,0.72,0.75,
      -0.74, 0.74,-0.74, 0.04,0.22,0.27,  -0.74, 0.74, 0.74, 0.45,0.95,1.00,   0.74, 0.74, 0.74, 0.15,0.88,0.54,
      -0.74, 0.74,-0.74, 0.04,0.22,0.27,   0.74, 0.74, 0.74, 0.15,0.88,0.54,   0.74, 0.74,-0.74, 0.07,0.30,0.35,
      -0.74,-0.74,-0.74, 0.02,0.12,0.18,   0.74,-0.74,-0.74, 0.03,0.18,0.22,   0.74,-0.74, 0.74, 0.12,0.72,0.75,
      -0.74,-0.74,-0.74, 0.02,0.12,0.18,   0.74,-0.74, 0.74, 0.12,0.72,0.75,  -0.74,-0.74, 0.74, 0.09,0.85,0.95
    ]);

    function ring(radius, plane, color) {
      const out = [];
      const n = 168;
      for (let i=0;i<=n;i++) {
        const a = (i/n) * Math.PI * 2;
        const x = Math.cos(a) * radius;
        const y = Math.sin(a) * radius;
        if (plane === "xy") out.push(x,y,0,...color);
        if (plane === "xz") out.push(x,0,y,...color);
        if (plane === "yz") out.push(0,x,y,...color);
      }
      return new Float32Array(out);
    }

    const nodes = new Float32Array([
      -1.52,.34,.22, .09,.85,.95,  1.48,-.24,-.14, .15,.88,.54,
      .42,1.26,.26, .45,.95,1.0,  -.38,-1.22,-.32, .09,.85,.95,
      .98,.72,-.56, .15,.88,.54,  -1.02,-.74,.58, .45,.95,1.0
    ]);

    const face = new Float32Array([
      -0.42,-0.42,0.77, 0,1,  0.42,-0.42,0.77, 1,1,  0.42,0.42,0.77, 1,0,
      -0.42,-0.42,0.77, 0,1,  0.42,0.42,0.77, 1,0, -0.42,0.42,0.77, 0,0
    ]);

    function buffer(data) {
      const b = gl.createBuffer();
      gl.bindBuffer(gl.ARRAY_BUFFER, b);
      gl.bufferData(gl.ARRAY_BUFFER, data, gl.STATIC_DRAW);
      return b;
    }

    const cubeB = buffer(cube);
    const ringBs = [
      {b: buffer(ring(1.38,"xy",[.09,.85,.95])), c:169},
      {b: buffer(ring(1.60,"xz",[.15,.88,.54])), c:169},
      {b: buffer(ring(1.82,"yz",[.45,.95,1.0])), c:169}
    ];
    const nodeB = buffer(nodes);
    const faceB = buffer(face);

    const tex = gl.createTexture();
    gl.bindTexture(gl.TEXTURE_2D, tex);
    gl.texImage2D(gl.TEXTURE_2D,0,gl.RGBA,1,1,0,gl.RGBA,gl.UNSIGNED_BYTE,new Uint8Array([7,16,24,255]));
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
    const img = new Image();
    img.onload = function(){
      gl.bindTexture(gl.TEXTURE_2D, tex);
      gl.pixelStorei(gl.UNPACK_PREMULTIPLY_ALPHA_WEBGL, true);
      gl.texImage2D(gl.TEXTURE_2D,0,gl.RGBA,gl.RGBA,gl.UNSIGNED_BYTE,img);
    };
    img.src = canvas.dataset.icon || "assets/brand/r41/axiona-header-icon.png";

    let px = 0, py = 0;
    const panel = canvas.closest(".real-3d-panel") || canvas;
    panel.addEventListener("pointermove", function(e){
      const r = panel.getBoundingClientRect();
      px = ((e.clientX-r.left)/r.width - .5) * .42;
      py = ((e.clientY-r.top)/r.height - .5) * .28;
    }, {passive:true});
    panel.addEventListener("pointerleave", function(){px=0;py=0;}, {passive:true});

    function resize(){
      const dpr = Math.min(window.devicePixelRatio || 1, 2);
      const r = canvas.getBoundingClientRect();
      const w = Math.max(320, Math.floor(r.width * dpr));
      const h = Math.max(260, Math.floor(r.height * dpr));
      if (canvas.width !== w || canvas.height !== h) { canvas.width = w; canvas.height = h; }
      gl.viewport(0,0,canvas.width,canvas.height);
    }

    function attrsColor(){
      const ap = gl.getAttribLocation(colorP,"aPosition");
      const ac = gl.getAttribLocation(colorP,"aColor");
      gl.enableVertexAttribArray(ap);
      gl.enableVertexAttribArray(ac);
      gl.vertexAttribPointer(ap,3,gl.FLOAT,false,24,0);
      gl.vertexAttribPointer(ac,3,gl.FLOAT,false,24,12);
    }

    function render(now){
      resize();
      const t = reduced ? 1.2 : now * 0.001;
      gl.clearColor(0,0,0,0);
      gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);
      gl.enable(gl.DEPTH_TEST);
      gl.enable(gl.BLEND);
      gl.blendFunc(gl.SRC_ALPHA, gl.ONE_MINUS_SRC_ALPHA);

      const proj = perspective(Math.PI/4.1, canvas.width/canvas.height, .1, 50);
      const view = translate(0,0,-5.35);
      let model = rotateX(-.36 + py);
      model = multiply(model, rotateY(t*.42 + px));
      model = multiply(model, rotateZ(Math.sin(t*.34)*.045));
      const mvp = multiply(proj, multiply(view, model));

      gl.useProgram(colorP);
      gl.uniformMatrix4fv(gl.getUniformLocation(colorP,"uMVP"), false, new Float32Array(mvp));
      gl.uniform1f(gl.getUniformLocation(colorP,"uPointSize"), 1);
      gl.uniform1f(gl.getUniformLocation(colorP,"uIsPoint"), 0);
      gl.uniform1f(gl.getUniformLocation(colorP,"uAlpha"), .28);
      gl.bindBuffer(gl.ARRAY_BUFFER, cubeB);
      attrsColor();
      gl.drawArrays(gl.TRIANGLES,0,cube.length/6);

      ringBs.forEach(function(r, i){
        const rm = multiply(model, rotateZ(t*(.18+i*.055)));
        const rmvp = multiply(proj, multiply(view, rm));
        gl.uniformMatrix4fv(gl.getUniformLocation(colorP,"uMVP"), false, new Float32Array(rmvp));
        gl.uniform1f(gl.getUniformLocation(colorP,"uAlpha"), .38 - i*.055);
        gl.uniform1f(gl.getUniformLocation(colorP,"uIsPoint"), 0);
        gl.bindBuffer(gl.ARRAY_BUFFER, r.b);
        attrsColor();
        gl.drawArrays(gl.LINE_STRIP,0,r.c);
      });

      gl.uniformMatrix4fv(gl.getUniformLocation(colorP,"uMVP"), false, new Float32Array(mvp));
      gl.uniform1f(gl.getUniformLocation(colorP,"uAlpha"), .94);
      gl.uniform1f(gl.getUniformLocation(colorP,"uIsPoint"), 1);
      gl.uniform1f(gl.getUniformLocation(colorP,"uPointSize"), Math.max(7, canvas.width/82));
      gl.bindBuffer(gl.ARRAY_BUFFER, nodeB);
      attrsColor();
      gl.drawArrays(gl.POINTS,0,nodes.length/6);

      gl.useProgram(texP);
      gl.uniformMatrix4fv(gl.getUniformLocation(texP,"uMVP"), false, new Float32Array(mvp));
      gl.uniform1f(gl.getUniformLocation(texP,"uAlpha"), .96);
      gl.activeTexture(gl.TEXTURE0);
      gl.bindTexture(gl.TEXTURE_2D, tex);
      gl.uniform1i(gl.getUniformLocation(texP,"uTexture"), 0);
      gl.bindBuffer(gl.ARRAY_BUFFER, faceB);
      const ap = gl.getAttribLocation(texP,"aPosition");
      const au = gl.getAttribLocation(texP,"aUV");
      gl.enableVertexAttribArray(ap);
      gl.enableVertexAttribArray(au);
      gl.vertexAttribPointer(ap,3,gl.FLOAT,false,20,0);
      gl.vertexAttribPointer(au,2,gl.FLOAT,false,20,12);
      gl.drawArrays(gl.TRIANGLES,0,6);

      if (!reduced) requestAnimationFrame(render);
    }

    canvas.classList.add("webgl-active");
    requestAnimationFrame(render);
  }

  canvases.forEach(function(canvas){
    try { init(canvas); }
    catch(e) {
      canvas.classList.add("webgl-unavailable");
      console.warn("AXIONA 3D fallback", e);
    }
  });
})();
