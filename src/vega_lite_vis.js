// ====== Visualization File Paths ======
var vg_1 = "src/global_museum_density.vg.json";     // Global museum density
var vg_2 = "src/uk_museum_density.vg.json";         // UK museum density map
var vg_3 = "src/uk_museum_population.vg.json";      // UK museum count vs population
var vg_4 = "src/uk_museum_subject.vg.json";         // Museum subjects (lollipop chart)
var vg_5 = "src/top_10_uk_museums.vg.json";         // Top 10 most visited UK museums
var vg_6 = "src/acquisition_over_time.vg.json";     // British Museum acquisitions over time


// ====== Embed Each Visualization ======
vegaEmbed("#museum_map", vg_1)
  .then(function(result) {
    console.log("✅ Global museum density map loaded successfully!");
  })
  .catch(console.error);

vegaEmbed("#uk_map", vg_2)
  .then(function(result) {
    console.log("✅ UK museum density map loaded successfully!");
  })
  .catch(console.error);

vegaEmbed("#population", vg_3)
  .then(function(result) {
    console.log("✅ Museum count vs population scatter plot loaded successfully!");
  })
  .catch(console.error);

vegaEmbed("#subject", vg_4)
  .then(function(result) {
    console.log("✅ UK museum subject distribution chart loaded successfully!");
  })
  .catch(console.error);

vegaEmbed("#top_10", vg_5)
  .then(function(result) {
    console.log("✅ Top 10 most visited UK museums chart loaded successfully!");
  })
  .catch(console.error);

vegaEmbed("#acquisition", vg_6)
  .then(function(result) {
    console.log("✅ British Museum acquisitions over time chart loaded successfully!");
  })
  .catch(console.error);
