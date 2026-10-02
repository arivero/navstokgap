/* Schematic drawing coordinates only: no physical simulation or proof calculation. */
(() => {
  "use strict";
  const slider = document.getElementById("refinement-level");
  if (!slider) return;
  const levels = [2, 4, 8, 16, 32];
  const svgNS = "http://www.w3.org/2000/svg";
  const steps = document.getElementById("motion-steps");
  const defect = document.getElementById("motion-defect");
  const marks = document.getElementById("motion-marks");
  const grid = document.getElementById("field-grid");
  const cell = document.getElementById("field-cell");
  const button = document.getElementById("refine-step");
  function draw() {
    const level = Number(slider.value);
    const n = levels[level];
    const points = [];
    const dots = document.createDocumentFragment();
    const lines = [];
    for (let i = 0; i <= n; i++) {
      const t = i / n;
      const x = 42 + 440 * t;
      const y = 42 + 224 * t * t;
      points.push(x + "," + y);
      const circle = document.createElementNS(svgNS, "circle");
      circle.setAttribute("cx", x);
      circle.setAttribute("cy", y);
      circle.setAttribute("r", n > 16 ? "2.5" : "4");
      dots.appendChild(circle);
      const gx = 70 + 400 * t;
      const gy = 36 + 224 * t;
      lines.push("M" + gx + " 36V260M70 " + gy + "H470");
    }
    steps.setAttribute("points", points.join(" "));
    defect.setAttribute("d", "M" + points.join("L") + "Q262 42 42 42Z");
    marks.replaceChildren(dots);
    const path = document.createElementNS(svgNS, "path");
    path.setAttribute("d", lines.join(""));
    grid.replaceChildren(path);
    cell.setAttribute("width", 400 / n);
    cell.setAttribute("height", 224 / n);
    document.getElementById("field-callout").setAttribute("d",
      "M" + (270 + 200 / n) + " " + (148 + 112 / n) + "L326 284");
    document.getElementById("division-count").textContent = n + " divisions";
    slider.setAttribute("aria-valuetext", n + " divisions");
    button.textContent = level === levels.length - 1 ? "Start again ↺" : "Refine once +";
  }
  slider.addEventListener("input", draw);
  button.addEventListener("click", () => {
    slider.value = (Number(slider.value) + 1) % levels.length;
    draw();
  });
  draw();
  document.getElementById("refinement-controls").hidden = false;
})();
