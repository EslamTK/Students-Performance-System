//getting data from hidden input field
var my_data = document.getElementById("myVar").value;
//formating data to valid json format
my_data = my_data.slice(10, my_data.length, my_data);
my_data = my_data.replace('>', '');
my_data = my_data.replace(/'/g, '"');
my_data = JSON.parse(my_data);

window.onload = drawChart(my_data, true);

var selectedDep = "";
var selectedYear = "";
$('#year-selector').change(function () {

    selectedYear = $('#year-selector option:selected').val();
    send_request();
});
$('#department-selector').change(function () {

    selectedDep = $('#department-selector option:selected').val();
    send_request();
});

function send_request() {
    'use strict';
    var depId = 'department_id=' + selectedDep + '';
    var cYear = '&year=' + selectedYear + '';
    var baseUrl = request_url + '?';
    var aUrl = baseUrl + depId + cYear;
    $.ajax({
        url: aUrl,
        dataType: "json",
        type: 'GET',
        contentType: 'application/json',
        success: function (data) {
            drawChart(data.result);
        }
    });
}


function drawChart(data, isNew) {
    'use strict';

    var label_data = [];
    var rates = [];
    for (var i = 0; i < data.length; i++) {
        label_data.push(data[i].review_item__name);
        rates.push(data[i].rate__avg);
    }


    var lineChartData = {
        labels: label_data,
        datasets: [{
            label: 'Rate',
            backgroundColor: 'rgba(151,187,205,0.2)',
            borderColor: 'rgba(151,187,205,1)',
            pointBackgroundColor: 'rgba(151,187,205,1)',
            pointBorderColor: '#fff',
            data: rates
        }]
    };

    if (isNew) {
        var ctx = document.getElementById('canvas-1');
        window.chart = new Chart(ctx, {
            type: 'bar',
            data: lineChartData,
            options: {
                responsive: true,
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }]
                }
            }
        });
    }
    else {
        window.chart.data = lineChartData;
        window.chart.update();
    }


}