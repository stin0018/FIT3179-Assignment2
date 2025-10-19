var vg_1 = "src/map.vg.json";       // Global map
var vg_2 = "src/uk.map.vg.json";    // UK map
var vg_3 = "src/top.10.lad.density.json";
var vg_4 = "src/subject.json";
var vg_5 = "src/top.10.museum.barchart.json";
var vg_6 = "src/acquisition_over_time.json";
// var vg_6 = "top.15.object.type.json";
// var vg_7 = "top.15.cultures.json";


vegaEmbed("#museum_map", vg_1)
  .then(function(result) {
    console.log("Global map successfully loaded!");
  })
  .catch(console.error);

vegaEmbed("#uk_map", vg_2)
  .then(function(result) {
    console.log("UK map successfully loaded!");
  })
  .catch(console.error);

  vegaEmbed("#density", vg_3)
  .then(function(result) {
    console.log("UK map successfully loaded!");
  })
  .catch(console.error);

  vegaEmbed("#subject", vg_4)
  .then(function(result) {
    console.log("UK map successfully loaded!");
  })
  .catch(console.error);


  vegaEmbed("#top_10", vg_5)
  .then(function(result) {
    console.log("UK map successfully loaded!");
  })
  .catch(console.error);

  vegaEmbed("#object_type", vg_6)
  .then(function(result) {
    console.log("UK map successfully loaded!");
  })
  .catch(console.error);

  // vegaEmbed("#culture", vg_7)
  // .then(function(result) {
  //   console.log("UK map successfully loaded!");
  // })
  // .catch(console.error);
