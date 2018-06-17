//getting data from hidden input field
var my_data = document.getElementById("myData").value;

//formating data to valid json format
my_data = my_data.slice(10, my_data.length, my_data);
my_data = my_data.replace('>', '');
my_data = my_data.replace(/'/g, '"');
my_data = JSON.parse(my_data);


window.onload = drawChart(my_data, true);

var selectedYear = "";
var selectedDep = "";
var ter_id = "";

window.selected_year = null;
window.selected_dep = null;

$('#year-selector').change(function () {

    selectedYear = $('#year-selector option:selected').val();
    send_request();
});
$('#department-selector').change(function () {

    selectedDep = $('#department-selector option:selected').val();
    send_request();
});

//function applied on change term 
$("input:radio[name=options]").change(function () {

    ter_id = $('input:radio[name=options]:checked').val();
    send_request();
});

function send_request() {
    'use strict';
    var depId = 'department_id=' + selectedDep;
    var yId = '&year_id=' + selectedYear;
    var tId = '&term_id=' + ter_id;
    var bUrl = request_url + '?';
    var aUrl;
    aUrl = bUrl + depId + yId + tId;

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
    console.log(data);

    var label_data = [];
    var success = [];
    var fail = [];


    for (var i = 0; i < data.length; i++) {

        label_data.push(data[i].year);
        success.push(data[i].success);
        fail.push(data[i].fail);
    }
    console.log(success);
    var lineChartData = {
        labels: label_data,
        datasets: [{
            label: 'success',
            backgroundColor: 'rgba(220,220,220,0.2)',
            borderColor: 'rgba(220,220,220,1)',
            pointBackgroundColor: 'rgba(220,220,220,1)',
            pointBorderColor: '#fff',
            data: success
        },
            {
                label: 'Fail',
                backgroundColor: 'rgba(151,187,205,0.2)',
                borderColor: 'rgba(151,187,205,1)',
                pointBackgroundColor: 'rgba(151,187,205,1)',
                pointBorderColor: '#fff',
                data: fail
            }
        ]
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
                            beginAtZero: true,
                            max: 10
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