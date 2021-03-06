function graphTest() {
  // Reset the graph
  $('#graph').remove();
  $('#container').append('<canvas id="graph" data-url="/draw-graph/"></canvas>');

  var $graph = $("#graph");

  var fromDatetime = $("#fromDatetime").val();
  var toDatetime = $("#toDatetime").val();

  $.ajax({
    url: $graph.data("url"),
    type: "GET",
    data: {
    "fromDatetime": fromDatetime,
    "toDatetime": toDatetime
    },
    success: function graphTest(response) {

      var ctx = document.getElementById('graph').getContext('2d');

      new Chart(ctx, {
        type: 'line',
        data: {
          labels: response.labels,
          datasets: [{
            label: 'Population',
            backgroundColor: 'blue',
            data: response.data
          }]
        },
        options: {
          responsive: true,
          legend: {
            position: 'top',
          },
          title: {
            display: true,
            text: 'Population Bar Chart'
          }
        }
      });

    }
  });
};

$(function initGraph() {
  graphTest();
});
