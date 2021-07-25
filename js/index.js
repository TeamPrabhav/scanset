function w3_open() {
  document.getElementById("main").style.marginLeft = "25%";
  document.getElementsByClassName("w3-sidenav")[0].style.width = "25%";
  document.getElementsByClassName("w3-sidenav")[0].style.display = "block";
  document.getElementsByClassName("w3-opennav")[0].style.display = 'none';
}
function w3_close() {
  document.getElementById("main").style.marginLeft = "0%";
  document.getElementsByClassName("w3-sidenav")[0].style.display = "none";
  document.getElementsByClassName("w3-opennav")[0].style.display = "inline-block";
}

// openTab('Home')
function openTab(tabName, element) {
    var i;
    var x = document.getElementsByClassName("tabs");
    var y = document.getElementsByClassName("tablink");
    for (i = 0; i < x.length; i++) {
       x[i].style.display = "none";  
       if (y[i].classList.contains('w3-amber'))
       y[i].classList.remove("w3-amber");  
    }
    document.getElementById(tabName).style.display = "block";  
    element.classList.add("w3-amber");
}

// $(document).ready(function() {
//     $('#dataTable').DataTable();
// });

$(function () {
    $('#dataTable').DataTable({
      "pageLength": 5,
      "paging": true,
      "lengthChange": false,
      "searching": false,
      "ordering": true,
      "info": true,
    //   "autoWidth": false,
      "order": [[1, 'asc']]
      });
  });


//   ajax call
// $(function () {
//     $('#dataTable').DataTable({
//         "ajax": {
//             "url": "#", /*Data source*/
//             "dataSrc": "data", /*object that holds the data*/
//         },
//         columns: [
//             { data: 'id' },
//             { data: 'name' },
//             { data: 'year' },
//             { data: 'color' },
//             { data: 'pantone_value' }
//         ],
//         "columnDefs": [{ /* default values for columns */
//             "defaultContent": "-",
//             "targets": "_all"
//         }],
//     });
// }); 

// var ctx = document.getElementById('myChart'); // node
// var ctx = document.getElementById('myChart').getContext('2d'); // 2d context
// var ctx = $('#myChart'); // jQuery instance
// var ctx = 'myChart'; // element id
// var xyValues = [
//   {x:50, y:7},
//   {x:60, y:8},
//   {x:70, y:8},
//   {x:80, y:9},
//   {x:90, y:9},
//   {x:100, y:9},
//   {x:110, y:10},
//   {x:120, y:11},
//   {x:130, y:14},
//   {x:140, y:14},
//   {x:150, y:15}
// ];

// var myChart = new Chart(ctx, {
//   type: "scatter",
//   data: {
//     datasets: [{
//       pointRadius: 4,
//       pointBackgroundColor: "rgba(0,0,255,1)",
//       data: xyValues
//     }]
//   },
//   options:{ legend: {display: false},
//   scales: {
//     xAxes: [{ticks: {min: 40, max:160}}],
//     yAxes: [{ticks: {min: 6, max:16}}],
//   }}
// });

// Load google charts
// google.charts.load('current', {'packages':['corechart']});
// google.charts.setOnLoadCallback(drawChart);

// // Draw the chart and set the chart values
// function drawChart() {
//   var data = google.visualization.arrayToDataTable([
//   ['Task', 'Hours per Day'],
//   ['Work', 8],
//   ['Friends', 2],
//   ['Eat', 2],
//   ['TV', 2],
//   ['Gym', 2],
//   ['Sleep', 8]
// ]);

//   // Optional; add a title and set the width and height of the chart
//   var options = {'title':'My Average Day', 'width':550, 'height':400};

//   // Display the chart inside the <div> element with id="piechart"
//   var chart = new google.visualization.PieChart(document.getElementById('piechart'));
//   chart.draw(data, options);
// }


// var xValues = ["Italy", "France", "Spain", "USA", "Argentina"];
// var yValues = [55, 49, 44, 24, 15];
// var barColors = [
//   "#b91d47",
//   "#00aba9",
//   "#2b5797",
//   "#e8c3b9",
//   "#1e7145"
// ];

// new Chart("myChart", {
//   type: "pie",
//   data: {
//     labels: xValues,
//     datasets: [{
//       backgroundColor: barColors,
//       data: yValues
//     }]
//   },
//   options: {
//     title: {
//       display: true,
//       text: "World Wide Wine Production 2018"
//     }
//   }
// });